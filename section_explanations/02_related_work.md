# Related Work — what's been tried before and what's new here

Two streams of prior work matter for this paper.

Stream one is computer vision people trying to read materials off images and video. People have figured out how to label material categories from photos — "this is wood, this is metal" — and they've worked on cloth in particular, since fabrics flutter in informative ways. A specific line of work called "visual vibrometry" looked at video motion to estimate stiffness, but only for relatively simple shapes like fabrics and thin rods, and only as a single number for the whole object. Same uniform material everywhere. That's the limit prior work hit.

Stream two is the engineering world's non-destructive testing community. They have great tools: laser vibrometers that bounce a beam off a structure and measure the wobble, and digital image correlation, which is a precise camera-based technique using carefully prepared surface patterns. These get used to inspect bridges, buildings, materials. They can detect that there's a defect somewhere. They sometimes recover a single overall stiffness number. But they don't generally give you a map of how stiffness varies inside the object.

So here's where this paper plants its flag. Both streams stop at "homogeneous" — one number per object. Nobody has used video to recover a spatially varying interior map: this voxel is stiff, that voxel is soft, this voxel over here is denser than the rest. That last leap is what visual vibration tomography is actually doing.

The word "tomography" in the title is meant the same way as in a medical CT scan. You don't see inside the body directly — you see X-rays passing through from different angles, and a reconstruction algorithm builds the interior from those projections. Same vibe here. You don't see inside the cube; you see how its surface wobbles, and an algorithm rebuilds the interior from that.
