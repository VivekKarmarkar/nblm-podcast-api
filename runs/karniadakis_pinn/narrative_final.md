Picture a long iron bar. Maybe a fireplace poker. You stick one end into the coals and you wait. After a minute, the middle is warm. After five, the far end is too hot to hold. Heat moves through metal. Anyone who's ever burned their hand knows it happens.

Here's a less obvious thing. Two hundred years ago, a French mathematician named Joseph Fourier wrote down an equation that describes exactly how that heat creeps along the bar. Not hand-wavy. Precise. If you tell Fourier's equation the temperature at every point along the bar the moment you pull it out of the coals, the equation tells you the temperature at every point at every future moment.

And it's not just heat. There's an equation for how a drum head ripples after you tap it. An equation for how a pollutant smears down a river. An equation for how air flows around the wing of a plane. An equation for how a quantum particle's wave function spreads through space. Each of these is what mathematicians call a partial differential equation, or PDE. Humanity has spent the last three centuries collecting them. We've got a giant pile of these things. Some of the most carefully validated knowledge our species has ever produced.

Now here's the puzzle. Modern machine learning — neural networks, the whole circus — is having an incredible moment. Image recognition, language, genomics. The networks are recognizing your face, transcribing your voice, writing your code.

But you know what they don't usually do? They don't use the equations.

Think about that. We have these centuries-old, hard-won laws describing exactly how physical systems evolve. And we have these brand-new, ravenous neural networks that learn from data. And the two have been living in different rooms.

This paper, published in 2017 by Maziar Raissi, Paris Perdikaris, and George Karniadakis, is about what happens when you put them in the same room.

OK, before we go further, let's pin down the problem. It's specific, and the specificity matters.

Imagine you're an engineer trying to model how heat spreads through a strangely-shaped part inside a jet engine. Or how blood flows through a patient's specific aorta after a stent goes in. Or how a wildfire propagates across a hillside given today's wind. In every one of these, you have an equation describing the physics. Heat diffusion. Fluid flow. Combustion. These are the PDEs. You trust them.

But here's the catch. To actually compute a solution — to get numbers out — you traditionally chop the object into millions of tiny cells, write down the equation for each cell, solve a giant linked system. It's been done this way for fifty years. It works. It's mature. But it's expensive, it needs a supercomputer, it needs careful setup. And if you went and stuck an actual thermometer somewhere, fitting that measurement back in is awkward.

The other route would be a neural network. Train one on a pile of data and let it learn the system. But in a physics problem, you usually don't HAVE a pile of data. You have a handful of measurements. Maybe ten thermometer readings, a hundred pressure sensors, a few drone photos. Vanilla neural networks fall apart with that little to chew on. They're data gluttons. Starve them and they hallucinate.

Two tools and neither one fits. The classical equations need too much computation. The neural networks need too much data.

And here's where the trick comes in.

The authors say, OK, what if we MADE the network respect the equation? When we train it, we don't just say "match my ten thermometer readings" — we ALSO say "and anywhere you don't have a thermometer, you'd better satisfy Fourier's heat equation." The equation becomes part of the loss function the network is trying to minimize.

Hold on. Let me unpack "loss function," because the whole trick lives in there.

Training a neural network is essentially a guessing game. The network spits out a guess. You compare it to the right answer. You measure how wrong the guess is — that measurement is the loss. Then you nudge the network's internal knobs to shrink the loss. Repeat about a billion times and the network gets good. The loss function tells the network what "wrong" means. It's the scoreboard. Whatever you put on the scoreboard, the network optimizes for.

The PINN insight — and PINN stands for physics informed neural network, the term the authors invented — is that you can put the EQUATION on the scoreboard. A wrong answer is one that doesn't match the data, AND one that doesn't satisfy the physics. Optimize against both.

Now you need a way to check, for any guess, whether it satisfies the equation. Fourier's heat equation involves derivatives — how fast temperature is changing in time, how curvy the temperature profile is in space. To check the equation, you compute those derivatives of whatever the network is predicting.

Here's where the second piece of magic comes in. A technique called automatic differentiation has been quietly powering deep learning for years. Neural networks are built out of simple operations — multiplications, additions, sigmoid curves. Each has a known derivative. Chain the operations to form a network, you can chain the derivatives too, automatically, by the chain rule. The upshot is that any neural network can compute the derivatives of its own output, exactly, cheaply, with a slightly modified version of its own forward pass.

So if your network is predicting temperature in a metal bar, it can also compute, on the spot, the rate of change of that temperature in time and space. It can plug those derivatives into Fourier's equation and check whether the equation is satisfied. It can be scored on physical correctness, not just on matching data.

That's the whole engine. Two pieces. Loss function with a physics term. Automatic differentiation to evaluate it. Bolt them together and you've got a network that learns to obey the laws of physics.

OK. Let's see what they did with this. The paper has two real demonstrations, and the second one is the showstopper.

The first demo is on Burgers' equation. Don't let the name throw you. Burgers is a one-dimensional PDE from fluid mechanics that shows up in shock waves, traffic flow, and a bunch of other places where something moves and piles up against itself. Engineers love testing on it because it's NASTY. At low viscosity — the fluid barely resists movement — the solutions develop sharp internal cliffs, near-discontinuities where the value drops off a wall. Classical numerical methods can resolve those cliffs, but only by chopping the domain into incredibly fine cells right around where the cliff is going to be. Tedious.

The authors throw a PINN at it. They give the network a hundred data points — initial conditions plus the values along the edges of the simulation box. Then they pick ten thousand random scattered points throughout the domain and tell the network: at every one of these, check yourself against Burgers' equation.

Then they train. Nine layers deep, twenty neurons per layer. About sixty seconds on a single graphics card. These are called collocation points, by the way — fancy term for "places we forcibly enforce the physics."

What comes out is the full solution, including the nasty cliff, with accuracy a hundred times better than what the same team had achieved with their previous best method. The cliff is right where it should be. The smooth parts are smooth. And critically, the network is now a continuous function — you can ask it for the value at any point in space and time. No mesh. No fine grid. Just a function.

It's worth pausing on what just happened. The classical approach: chop the bar into a million pieces, solve a million tiny problems, glue them together. The PINN approach: ask one network to BE the solution, check that it obeys the equation at ten thousand random spots. Both work. But the PINN version is dramatically smaller, dramatically simpler to implement — the authors inline a tiny TensorFlow snippet, basically two short functions, to make the point — and dramatically more flexible.

The second demo is on the nonlinear Schrödinger equation. Harder. Schrödinger describes quantum mechanical wave functions, plus it shows up in laser optics inside fiber-optic cables. The solutions are complex-valued, and the boundaries are periodic — what flows out one side comes back in the other. Both are headaches for a generic neural network.

The PINN handles them. Same recipe, with two small tweaks: complex values get split into real and imaginary parts, and a term gets added to the loss function that enforces the periodic boundary. The error stays small. The wave function evolves through space and time in a physically correct way.

But the Schrödinger result quietly reveals a problem. The authors needed twenty thousand collocation points to make the network behave properly. Twenty thousand. For a one-dimensional problem.

What happens in two dimensions? You need a square's worth of points. Three dimensions? A cube's worth. The number of points to peppershot through the domain grows exponentially with the dimension of the problem. Physicists have a name for this: the curse of dimensionality. And it threatens to make PINNs unusable for the very problems where they'd be most exciting.

So the authors try a different shape for the network. Don't peppershot collocation points through time. BUILD time-stepping into the architecture.

Here's the idea. There's a family of classical numerical methods called Runge-Kutta schemes. These are old. The workhorses of physics simulation. They take the current state of the system, do a few intermediate calculations called stages, and combine them to advance the system forward by one step in time. A two-stage scheme, a four-stage scheme — most simulations use a handful of stages.

Classical wisdom: you'd love to use Runge-Kutta with lots of stages, because it's more accurate. But it's prohibitively expensive — each step requires solving a coupled system. So in practice, people use a handful and accept the limitations.

The authors' move: in a PINN, the cost doesn't scale badly. So why not crank the stages way up? They build a network with an implicit Runge-Kutta scheme using FIVE HUNDRED stages. To their knowledge, nobody had ever used a scheme like that before. Five hundred. The classical community would consider this insane.

The payoff: the theoretical error of a five-hundred-stage scheme is so absurdly small — something like one followed by ninety-seven zeros below the decimal point — that for all practical purposes, the time-stepping is exact. The only error left is the network's own approximation.

Then they do something that, if you've ever done physics simulation, will make you sit up. They tell the network: take the system from time zero point one to time zero point nine. In ONE STEP. One single time step. A simulation that would normally take thousands of small steps, they do in one.

The error is around eight ten-thousandths. Astonishingly good. They tested on Burgers' again, the same nasty equation with the same cliff, and the network handled the entire evolution in a single leap.

They run the same playbook on another equation, Allen-Cahn, which describes how a uniform mixture of two metals spontaneously separates into distinct domains. Different physics, different nonlinearity. Same result. Sharp internal layers between the two phases, captured from two hundred sparse data points, in a single time step.

So what do you take away from all of this.

There's been this divide for years between two ways of doing science. On one side, classical mathematical physics — equations carefully derived from first principles, solved by engineered numerical methods, working from very little data because the equations carry so much information. On the other side, modern machine learning — neural networks trained on giant datasets, oblivious to physics, but extraordinarily flexible and easy to set up.

This paper says those two worlds don't have to be separate. The equations and the networks can live inside the same loss function. The physics tells the network where to look. The network gives the physics a flexible, mesh-free, continuous, queryable representation. Each side covers the other's weakness.

It's worth being honest about what this paper does NOT claim. The authors are very clear: PINNs are NOT a replacement for classical numerical methods. Those classical methods are fifty years old and battle-tested and they're not going anywhere. The pitch is coexistence, not overthrow.

The paper also flags a real limitation. When the network gives you a prediction, it gives you a number — but no estimate of how confident it is in that number. Gaussian processes, an older statistical technique, naturally produce uncertainty estimates along with their predictions. PINNs as described here don't. The authors call this out as a pressing open question for future work. If you're going to use a PINN to decide whether to land an airplane or operate on a patient, you want to know not just the answer but the confidence in the answer.

But take a step back. The seed planted here turned out to be one of the most influential ideas in scientific computing of the last decade. PINNs have spread across computational fluid dynamics, biomechanics, geophysics, climate modeling, electromagnetics, materials science. The basic recipe — bake the equation into the loss, use automatic differentiation to evaluate it — turned out to generalize way beyond Burgers and Schrödinger.

And here's maybe the deepest thing in the paper. For three hundred years, we've thought of physics equations as things you SOLVE. You have an equation, you have initial conditions, you grind through a procedure, you get a solution. The equation is upstream of the solution.

The PINN flips that. The equation isn't something you solve — it's something you ENFORCE. It's a constraint in the loss function that gets pushed on every training step. The solution emerges from satisfying the constraint. And once you frame it that way, you can do things the procedural approach struggles with — like inferring the equation itself from data, or mixing measurements with physics in arbitrary proportions.

The bar with heat creeping along it. The drum head rippling after you tap it. The air flowing around the wing of a plane. All of those have equations that describe them. All of those have measurements you could take. Until this paper, the equations and the measurements lived in different worlds. After this paper, they live in the same loss function.

That's physics informed deep learning. Old equations, new networks, one loss function, and a future where the two worlds get to talk.
