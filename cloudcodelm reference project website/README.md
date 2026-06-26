# ClaudeCodeLM — reference project website

A self-contained, portable copy of the **ClaudeCodeLM** project-showcase website. Drop this whole folder into another project (e.g. a Vercel-hosted personal site) and point a coding agent at it to port/adapt it.

## What's here

- `index.html` — the entire site in one file. Inline CSS, inline SVG diagrams (architecture + voice-flow), and inline JS for the clickable step details. No build step, no dependencies to install.
- `podcast.mp3` — the embedded audio example (Nakamura–Uhlmann, ElevenLabs Matilda voice, ~16 min). `index.html` references it by relative path (`src="podcast.mp3"`), so keep the two together.
- `README.md` — this file.

## External dependencies (CDN, not bundled)

- **Google Fonts** (`DM Sans`) loaded via `<link>` in the `<head>`. Works online out of the box; self-host the font if you need offline.
- The GitHub footer links to `https://github.com/VivekKarmarkar/nblm-podcast-api`.

## How to run / preview locally

It's a static file — open `index.html` in a browser, or serve the folder:

```
python3 -m http.server 8000
# then visit http://localhost:8000
```

(Browsers may block inline audio over the `file://` protocol; use a local server if the player doesn't load.)

## Structure of the page (sections, top to bottom)

1. **Hero** — title + tagline + targeting tags (orange = field, blue = sector, green = orgs to reach out to).
2. **Audio** — the embedded podcast + metadata.
3. **Introduction** — the walk, the one broken step, the hunt, what got built.
4. **The Abstraction Ladder** — the 5-level escalation; Level 5 (in-house + background agent) is what got built.
5. **Architecture (Post-Pivot)** — the 7-phase background-agent pipeline as an interactive SVG (serpentine flow, parallel per-section swarm, paper-reading hallucination-check stack, MD-store hub).
6. **Design Philosophy** — the voice → spec → `/goal` autonomous pattern.

## Porting notes

- The colour system is a small set of CSS custom utility classes (`.tag-tech-*`, `.tag-domain-*`, `.tag-audience*`, etc.) plus orange `#f97316` / blue `#38bdf8` / green `#4ade80` / amber `#fbbf24` accents on a `#0f1019` background.
- The two diagrams are hand-authored `<svg viewBox="0 0 980 520">` blocks with `data-step` click handlers (`selectStep` / `selectVStep`) — adapt the `stepData` / `vStepData` JS objects to change the per-node detail text.
