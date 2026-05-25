Here's the central trick of the whole paper. Pay attention.

You have a function on your rod. Could be the heat. Could be the velocity. Whatever. You can look at that function in two completely equivalent ways.

Way one is the obvious one: a value at every point along the rod. The straightforward picture.

Way two is the wave decomposition. The same function, rewritten as a sum of pure waves of different wavelengths. A long lazy wave that sweeps across the whole rod. A medium wave that wiggles a few times. A short jittery wave that wiggles a hundred times. Add them all up with the right weights, and you reconstruct the original function exactly. No information lost. Just a different way of writing the same thing.

You can flip back and forth between these two pictures any time you want. It's like switching between looking at a chord on sheet music versus listening to it as individual notes. Same music, different representation.

Here's why that matters. The expensive mixing step — the integral that takes every point on the rod and blends it with every other point — turns out to be wildly simpler in the wave picture. In the obvious picture, you have to do that giant sum-over-everything. In the wave picture, it's just multiplying each wave by its own little weight. Wavelength by wavelength. One multiplication per wave. Done.

That's the magic. A computationally brutal operation in one picture becomes a trivial operation in the other.

So the new layer works like this. Take your function. Flip it into the wave picture. Now you've got, say, a hundred waves with their amplitudes. The layer has learned a little adjustment for each wave — multiply this one by this much, that one by that much. It does that. Then flip back to the obvious picture.

While you're in wave-land, there's a bonus move you can pull. Most of the action in a physical signal lives in the long lazy waves. The short jittery stuff is mostly noise or fine detail you don't need. So before flipping back, throw away the highest-frequency waves entirely. Keep only the first dozen or so. This drops your knob count dramatically without losing much accuracy.

That's why this works on a coarse grid as well as a fine one. The waves you care about — the long lazy ones — are visible at both resolutions. They look the same. The network's job is to adjust the amplitudes of those waves. Whether you sample the result at a hundred points or a thousand, the answer is consistent, because the underlying wave representation is the same.

Train on coarse grids — cheap. Run on fine grids — gives you fine answers anyway, because all you're doing at the end is sampling the same waves at more points. Zero-shot super-resolution. Falls right out.

There's also a small local adjustment alongside the wave layer — a quick per-point tweak that handles things the smooth wave picture misses. Like rough edges at the boundary. With both pieces working together, the layer can handle real-world conditions where the geometry isn't perfectly periodic.

That's the whole architecture. Lift the input. Run it through four of these wave-layers. Project down. Out comes the answer.
