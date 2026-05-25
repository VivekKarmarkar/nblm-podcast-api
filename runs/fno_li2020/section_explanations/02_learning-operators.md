Here's the framing problem.

You're given a pile of examples. Each example is a pair: a starting function and the function it eventually became. Maybe each starting function is an initial heat distribution along a rod, and each ending function is the heat distribution one second later. You have a thousand such pairs.

You want a machine that, given a brand-new starting function it has never seen, predicts what it'll become.

Now — a regular neural network can almost do this, but only if you sample everything onto the same grid. Discretize the input rod into a hundred points, discretize the output rod into a hundred points, feed in the hundred numbers, train the network to spit out the hundred numbers. Done.

The problem with that is the network only knows about hundred-point rods. Show it a thousand-point rod and it panics.

What you really want is something that doesn't care about the grid at all. It just knows the rule that turns starting functions into ending functions. You can ask it for the answer at any resolution you like, any time you like, anywhere you like. The rule lives above all that. The discretization is just a convenience.

That's the idea of learning an operator. An operator is a function whose input is itself a function, and whose output is another function. You're not learning to map a list of numbers to a list of numbers. You're learning to map an entire function to an entire function. It's a level up.

The pitch is that this level-up actually buys you something practical. Train once, use forever. Train on coarse data, evaluate on fine data. Same network, any grid.

The catch is that you can never quite escape having to discretize at some point — computers work with numbers, not functions — but if you set things up carefully, the network's behavior at one discretization is consistent with its behavior at another. Same answer at different grid sizes, give or take a sampling artifact.

That's the framing. The rest of the paper is about how to actually build such a thing.
