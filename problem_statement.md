# Motivation

In my current workflow, when I'm out walking I collaborate with you over Telegram voice notes. I already have a suite of skills that let me do paper work without ever returning to my desk — paper-download-hack to grab a PDF, paper-reading and highlighting skills to engage with it. All of that flows cleanly from my pocket.

But there's one specific layer inside the paper-reading flow where it falls apart: generating a NotebookLM AUDIO podcast (distinct from NotebookLM video, which is a separate thing). When this need arises mid-walk, the natural move is to delegate it to you. And right now there is no clean way to do that. The motivation for this whole problem is to figure out what that clean delegation should look like.

To see why it's hard, walk through the candidate solutions as a ladder, in order of increasing cleanliness. Each rung fixes the prior rung's problem, and each rung introduces a new problem of its own, until we arrive at one that resolves.

LEVEL 1 is COMPUTER USE — you take my place in front of the NotebookLM browser and click through the UI exactly the way I would. This fails not because you'd be unreliable at it, but because computer use is the wrong mode for a coding agent. Even if you were perfect at clicking buttons, the whole point is that we want clean programmatic interfaces, not UI mimicry.

LEVEL 2 is an MCP built on an UNOFFICIAL NotebookLM SDK or reverse-engineered endpoints. This is a fundamentally different mechanism from Level 1: instead of clicking buttons, you give prompts, and the MCP programmatically creates podcasts (or videos) and downloads them. Cleaner — but it has a new problem. The MCP can fire the creation call, but it doesn't know when the audio is actually ready. To find out, we have to poll a status endpoint or wire up hooks. That's the INFORMATION-EXPERT BOTTLENECK — architecturally dirty.

LEVEL 3 is a direct API call to a service that Google or NotebookLM itself OFFICIALLY exposes — a clean endpoint that takes a podcast-generation request. This sidesteps the unofficial-SDK issue from Level 2. But it brings its own problem. While the audio is being generated, the request is just sitting there — stuck at the "toll booth." The call is fine in principle, but the main session is now blocked waiting on it. That's the SERIALIZATION BOTTLENECK.

LEVEL 4 is the resolution: put the Level-3 API call into a BACKGROUND AGENT. Our main session stays free — we keep doing whatever we're doing. In the background, the agent makes the call, absorbs the wait, lets the podcast generate, and drops the file in a folder when it's done. Twenty minutes later I ask "is the audio ready?" — you check, find it, /upload-and-share it. My phone gets it, I press play, walk on. No clicking, no polling on the main session, no blocking wait.

A note on where we are today: the existing notebooklm-mcp server we have access to is a Level-2 implementation — programmatic, prompt-driven, but built on the unofficial path. The download step is exactly the info-expert bottleneck described above. That's the friction point as it stands today.

# Phase 1 — Does the solution exist?

Vivek fires this off with the `/goal` slash command. It has two parts, and a hard branch in the middle.

**Part 1 — Swarm search.** Use the `swarm` skill to dispatch agents across Google's official documentation, Anthropic's official documentation, Anthropic Claude Code's official documentation, MCP marketplaces, and general online search. The target is either an official Google-exposed MCP for NotebookLM-style podcast generation, OR a podcast-generation API/SDK — Vivek mentioned that "something like" this exists (a service where you POST a prompt and get back a two-host podcast very similar to NotebookLM, but the exact name is half-remembered). The load-bearing channel is Google's official documentation; if it's there, that's the win.

**Branch logic.** If Part 1 returns NOTHING, the `/goal` invocation terminates with a clear "no solution found" verdict and we stop — no point investing further. If Part 1 returns a specific library/product page, proceed to Part 2.

**Part 2 — Niche library deep-dive.** Use the `niche-library-research` skill on whatever Part 1 surfaced. The questions to answer: What are the API/SDK details? Has Google built an MCP on top of it? Has anyone in the community built one we can simply install? Or do we need to build one ourselves? What login credentials are needed, and does Claude already have them?

**Phase 1 output.** A clear one-of-three verdict — (a) official MCP exists, (b) community MCP exists, or (c) nothing exists but we can build something — plus the credential picture.

**Hand-off between phases.** Before Phase 2 starts, if Claude needs credentials it doesn't already have, it will ask Vivek. Vivek will provide. Vivek gives Claude express permission to grab any credentials Claude can grab on its own.

# Phase 2 — Build and use the solution

Phase 2 assumes Phase 1 returned at least something usable.

**Step 1 — Get the MCP in place.** If an official or community MCP already exists, install it. If no MCP exists but an API/SDK is exposed, build a thin MCP on top of it.

**Step 2 — Test 1 (main-session round trip).** Use the `paper-download-hack` skill to download Katie Bowman's "Visual Vibration Tomography" paper. Use the new MCP to generate a podcast from it with a specific prompt. When the audio lands in the folder, use the `/upload-and-share` skill to share it with `vivekjobapp123@gmail.com`. This verifies the MCP works end-to-end in the simplest possible configuration.

**Step 3 — Test 2 (background-agent round trip — the actual target architecture).** Use the `paper-download-hack` skill to download Katie Bowman's "Visual Surface Wave Elastography" paper. Delegate the podcast generation to a BACKGROUND AGENT — the main session keeps moving, the agent absorbs the wait. The podcast generates, lands in the folder. Later, Vivek asks "is the audio ready?" — Claude checks, finds it, and `/upload-and-share`s it. This verifies the full Level-4 architecture from the motivation actually resolves the bottleneck.
