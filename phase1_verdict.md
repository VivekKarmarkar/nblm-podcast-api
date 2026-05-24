# Phase 1 Verdict

**Run date:** 2026-05-23
**Spec source:** `problem_statement.md` (Phase 1)
**Execution:** /goal autonomous swarm — Part 1 (4-channel breadth search) + Part 2 (3-channel niche-library-research deep-dive on the lead candidate).

---

## Headline verdict

**Bucket (b): COMMUNITY MCP EXISTS** — but not for the candidate you'd expect, and with significant nuance.

- **No official Google MCP server** exists for NotebookLM-style podcast generation. Confirmed across MCP marketplaces and Google's published MCP work.
- **An official Google API does exist** — NotebookLM Enterprise's **Audio Overview API** (and the recently deprecated standalone Podcast API). The Audio Overview API is the Level-3-in-the-ladder candidate from the motivation document. But: it is **inaccessible to Vivek's available accounts** (personal Gmail + UIowa institutional both blocked), costs **$1,620/year floor**, and is **functionally incomplete** (no documented poll endpoint, no documented audio-download endpoint — the official API itself requires web-UI fallback for the bottleneck-causing operations).
- **Community MCPs exist** for adjacent services with official, complete APIs — `adamanz/podcast-generator-mcp` (ElevenLabs-based), `elevenlabs/elevenlabs-mcp` (official ElevenLabs), AutoContent API via Zapier MCP. These do NOT use NotebookLM as the generator — they substitute the generator while preserving the two-host conversational output style.
- **The status-quo `notebooklm-mcp`** that Vivek already uses (and a dozen sibling repos) are all reverse-engineered web wrappers stuck at Level 2 of the ladder — swapping among them does not resolve the bottleneck.

**Implication for the ladder:** the user's motivation document treated Level 3 (official Google API) as the assumed-clean foundation for the Level 4 background-agent resolution. Phase 1 reveals that Level 3 is not clean — even when it exists, the official API has the SAME info-expert bottleneck as the unofficial path. This is a substantive finding that changes Phase 2's design space.

---

## Channel reports — Part 1 (breadth)

### Channel 1 — Google official documentation (LOAD-BEARING)
- **Audio Overview API** (NotebookLM Enterprise) — PREVIEW status, active. Endpoint: `https://{LOC}-discoveryengine.googleapis.com/v1alpha/projects/{PROJECT}/locations/{LOC}/notebooks/{NB_ID}/audioOverviews`. Requires NotebookLM Enterprise SKU + GCP project + OAuth via gcloud + IAM role.
- **Podcast API** — DEPRECATED as of **2026-05-22** (literally one day before this Phase 1 run). Google is not allowlisting new customers. This was Vivek's half-remembered name match.
- **No personal-account or API-key path exists.** GCP enterprise tier only.
- **Gemini TTS / Cloud TTS** — not podcast generators, just script readers. Not a match.
- **Google Illuminate** — research-paper-to-podcast tool. No public API. Web-only, waitlisted.

### Channel 2 — Anthropic documentation (sanity check)
- **NOT FOUND.** No Anthropic-built MCP, skill, or plugin for podcast generation in either `anthropics/claude-plugins-official` (203 plugins, none matching) or `anthropics/claude-plugins-community`. Closest audio capability is `save-to-spotify` (single-narrator TTS). Channel ruled out cleanly.

### Channel 3 — MCP marketplaces
- **NotebookLM-flavored MCPs (~12 variants)**: all reverse-engineered consumer-web wrappers using `notebooklm.google.com/_/LabsTailwindUi/data/batchexecute` (the same path the existing `notebooklm-mcp` uses). Same architectural class. Same bottleneck.
- **Non-NotebookLM podcast MCPs with official APIs:**
  - `adamanz/podcast-generator-mcp` — two-host, ElevenLabs TTS + LLM script gen, FastMCP-based
  - `elevenlabs/elevenlabs-mcp` — official ElevenLabs MCP (TTS + Conversational AI primitives, compose flow yourself)
  - AutoContent API MCP via Zapier — wraps `autocontentapi.com`
- **No MCP wrapper exists for the Google Audio Overview API specifically.**

### Channel 4 — General web search
- **Third-party REST APIs offering NotebookLM-style two-host output:**
  - **AutoContent API** (`autocontentapi.com`) — explicitly marketed as "the NotebookLM API." Async REST: POST → poll `/content/Status/{request_id}` → download. API-key auth (email-issued). €24–€166/mo. **Has all the endpoints the Google API lacks.**
  - **Wondercraft Convo Mode** — `POST /v1/podcast/convo-mode/ai-scripted`. X-API-KEY header. Two voice IDs per request.
  - **Jellypod API** — 1–4 hosts, 100+ voices, 30+ languages, async generation.
  - **ElevenLabs GenFM** — native two-host "conversation" mode, ultra-realistic voices, 32 languages. Closest non-Google match to NotebookLM voicing.
- **Open-source projects:**
  - **Podcastfy** (`souzatharsis/podcastfy`, Apache-2.0) — Python lib + CLI + FastAPI deployment. BYO LLM (any of 100+ providers) + TTS (ElevenLabs/Google/Edge). Strongest "drop-in replacement" candidate.
  - **open-notebooklm** family (gabrielchua), **open-notebook** (lfnovo), **open-notebooklm-ollama** (jeffcwolf, local-only).

---

## Lead candidate dossier — Google Audio Overview API (Part 2 deep-dive)

Three parallel agents independently converged on a consistent picture.

### Endpoint surface
- `POST .../notebooks/{NB_ID}/audioOverviews` — create
- `DELETE .../notebooks/{NB_ID}/audioOverviews/default` — delete (note the hardcoded `/default` suffix)
- **No documented GET endpoint.** No LIST endpoint. **No download endpoint.**

### Documented request schema
```json
{
  "sourceIds": [{"id": "SOURCE_ID"}],
  "episodeFocus": "EPISODE_FOCUS",
  "languageCode": "LANGUAGE_CODE"
}
```

### Reality of the request schema
**The API silently rejects every documented field.** Per the maintainer of the only working wrapper (`K-dash/nblm-rs`, the sole Python/Rust client successfully hitting this endpoint): **only `{}` is accepted as the request body**. The docs claim `sourceIds`, `episodeFocus`, and `languageCode` work — runtime returns `"Unknown name"` errors. Voice, language, focus configuration must be done **via the web UI** after creation.

### Async pattern (or lack thereof)
- Create returns synchronously with `status: "AUDIO_OVERVIEW_STATUS_IN_PROGRESS"`.
- No `operations/...` LRO URI.
- No documented GET endpoint to check status.
- **Inferred poll path (medium confidence):** `GET .../notebooks/{NB_ID}/audioOverviews/default` — the singleton-resource convention matches the DELETE path. Surfaced in one paraphrased docs reference but not confirmed via direct REST-reference page (the canonical reference page returns navigation-chrome only on every fetch attempt — a real docs.cloud.google.com platform quirk, not a research gap).
- Per nblm-rs docs verbatim: *"There is no API to retrieve audio overview status. You must check the NotebookLM web UI in your browser to see when audio generation is complete or if it has failed."*
- Only one enum member confirmed in public sources: `AUDIO_OVERVIEW_STATUS_IN_PROGRESS`. Success/failure terminal values are inferred-by-convention only.
- Generation time: 2–5 minutes typically.

### Audio download
- **NOT DOCUMENTED at the REST level.** No `:download?alt=media` endpoint published.
- UI flow only: Studio panel → three-dot menu → Download.
- Format unconfirmed at the API level (UI suggests MP3).

### SDK status
- `google-cloud-discoveryengine` v0.19.0 (released **2026-05-07**, current) — **does not expose audioOverviews**. No `AudioOverviewService` client class in any documented surface.
- The proto file `google.cloud.notebooklm.v1alpha.AudioOverview` **is not in the public `googleapis/googleapis` GitHub repo** (404). Internal-only generation.
- Everyone calling the API in the wild uses **raw REST**.

### Authentication
- OAuth via `gcloud auth print-access-token` (scope: `cloud-platform`).
- IAM permission: `discoveryengine.audioOverviews.create` on the notebook resource.
- Roles: `roles/discoveryengine.notebookLmOwner` ("Cloud NotebookLM Admin") or `roles/discoveryengine.admin`. The deprecated Podcast API's `roles/discoveryengine.podcastApiUser` does NOT apply to AOA.
- Service accounts work; **API keys do not** (Discovery Engine doesn't support them).

### Identity-layer gate
- **Personal Gmail accounts are blocked.** NotebookLM Enterprise requires Cloud Identity, Workforce Identity Federation, or third-party SSO — i.e., a Workspace/Enterprise domain.
- Vivek's `vivekkmk.assistant@gmail.com` (personal Gmail) **cannot create a NotebookLM Enterprise notebook** even with a GCP project and billing.
- Vivek's `vivek-karmarkar@uiowa.edu` (UIowa Workspace) is on a domain that has confirmed institutional blocks on NotebookLM programmatic access (per CLAUDE.md, from a prior consumer-API attempt).

### Cost
- ~$9/license/month, **15-license minimum** → $1,620/year floor.
- Annual commitment discounts available.
- 14-day, 5000-license trial for organizations only (not individuals).
- Audio Overview API is NOT separately billed — covered by seat license.

### Quotas
- 20 audio overviews per user per day.
- 500 notebooks per user.
- 300 sources per notebook.
- 200 MB or 500,000 words per source.

### Ecosystem signal
- Exactly **ONE** wrapper exists using the official endpoint (`K-dash/nblm-rs`, alpha, Rust+Python).
- **ZERO** MCP servers wrap this API.
- **ZERO** Google-published reference architectures for "automated podcast pipeline" on Audio Overview API.
- **ZERO samples in `GoogleCloudPlatform/generative-ai`** for Audio Overview — strong signal that Google itself considers the API too pre-GA to seed reference code.
- A Google Cloud Community author (Sascha Heyer, Medium piece on podcast generation in GCP) explicitly chose to NOT use the official API, hand-rolling instead with Gemini + Google TTS + ElevenLabs.

### Consumer-vs-Enterprise feature gap (interesting context)
The unofficial **consumer** NotebookLM client (`teng-lin/notebooklm-py`, browser-batch-RPC against `notebooklm.google.com`) advertises **richer features than the documented Enterprise API**: 50+ languages, 4 conversation styles (deep-dive, brief, critique, debate), 3 length options, explicit `wait_for_completion` and `download_audio` methods. The Enterprise API's documented request body only exposes `episodeFocus` and `languageCode`. Either (a) Enterprise has more fields in `generationOptions` that aren't documented, or (b) the consumer surface uses an internal richer API that Enterprise simply doesn't expose. Material for Phase 2 design — any MCP wrapper should leave `generationOptions` as a passthrough dict to allow probing.

---

## Credential picture — all viable paths

| Path | Credentials needed | Cost | Status | Bottleneck-resolution? |
|---|---|---|---|---|
| **Google AOA Enterprise API** | Workspace/Enterprise tenant + GCP project + Gemini Enterprise SKU + OAuth (gcloud) + `discoveryengine.notebookLmOwner` role | $1,620/yr floor | **INACCESSIBLE for Vivek's accounts.** Also functionally incomplete (no poll, no download). | No — same bottleneck as L2 |
| **Existing `notebooklm-mcp` (status quo)** | Personal Gmail cookie/session (via `nlm login`) | Free | Already in place. Reverse-engineered web. | No — this IS the bottleneck |
| **AutoContent API** | Email-issued API key (no GCP setup) | €24–166/mo | Available immediately. Has poll + download endpoints. | **Yes** — clean async REST with status + download |
| **Podcastfy (open-source)** | BYO: any LLM key (OpenAI/Anthropic/Google) + TTS key (ElevenLabs/Google/Edge). Vivek already has Anthropic + Google keys. | Variable (per-token cost of underlying LLM + TTS) | Available immediately. Self-hosted. | **Yes** — runs locally, any orchestration model |
| **ElevenLabs MCP (official)** | ElevenLabs API key | Pay-per-use (ElevenLabs character pricing) | Available immediately. Compose two-host flow yourself. | **Yes** — official ElevenLabs API |
| **adamanz/podcast-generator-mcp** | ElevenLabs API key + LLM key | Pay-per-use | Available immediately. FastMCP-based wrapper. | **Yes** — community MCP with official APIs |

---

## Recommendation for Phase 2

The user's motivation document defines success as the Level-4 background-agent architecture working on top of a clean Level-3 official API. Phase 1 reveals:

1. **The Google official API (Audio Overview API) cannot serve as Level 3** for this project. It is inaccessible to Vivek's accounts AND functionally incomplete (no poll/download endpoints, so even users with access fall back to web UI). The dream of "Google's official NotebookLM API as the foundation" is closed for this user.

2. **Viable Level-3 candidates that DO have proper async REST + status + download:**
   - **AutoContent API** — paid, clean, fastest path to a working Phase 2.
   - **Podcastfy + custom MCP wrapper** — open-source, BYO keys, more work but no per-podcast cost beyond LLM/TTS spend.
   - **ElevenLabs GenFM** — best-voiced commercial option.

3. **Status-quo `notebooklm-mcp`** — keeps the bottleneck Vivek is trying to escape; useful only as a fallback if all other paths fail.

**Lead recommendation:** Phase 2 should consider whether the user wants
- (A) **fastest path to working** — adopt AutoContent API + install/use its Zapier MCP, or build a thin MCP if a more direct one isn't suitable. Paid subscription, but the architecture is clean and the asynchronicity is properly modeled in the API.
- (B) **most flexible / self-hosted** — wrap Podcastfy (Python + FastAPI deployable) in a thin MCP. Uses keys Vivek already has. Total control over generation.
- (C) **best voice quality** — adopt ElevenLabs GenFM via the official `elevenlabs/elevenlabs-mcp`, or `adamanz/podcast-generator-mcp` if a richer prompt-driven flow is wanted.

The choice between (A)/(B)/(C) is a Vivek-decision, not a technical one — it depends on willingness to pay vs. willingness to self-host vs. voice-quality priority.

---

## Open questions for the user before Phase 2 kicks off

1. **Which path (A / B / C from above)?** Or some combination (e.g., AutoContent first to ship, then evaluate Podcastfy in parallel).
2. **Willingness to spend ~€24–166/mo on AutoContent API**, if (A) is the choice?
3. **Confirmation that the official Google Audio Overview API is officially off the table** for this project — given the inaccessibility, the enterprise cost floor, and the documented functional gaps. If you want to revisit with a third Google Workspace account (one not blocked by UIowa policies), that's a separate workstream worth flagging.
4. **Should the existing `notebooklm-mcp` be preserved as a Level-2 fallback** for cases where the chosen Phase-2 path can't generate something (e.g., specialized voice not available)? Or should we cut the cord entirely once Phase 2 ships?

---

## Phase 1 termination

Per `problem_statement.md`: Phase 1 outputs a one-of-three verdict + credential picture. Verdict is **(b) community MCP exists**, with the nuance that the most strategically promising paths involve community MCPs wrapping non-NotebookLM generators (AutoContent / ElevenLabs) rather than NotebookLM itself. Credential picture is documented above. Phase 1 complete — ready for user decision before Phase 2 begins.
