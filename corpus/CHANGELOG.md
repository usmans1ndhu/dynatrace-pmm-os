# Corpus Changelog

All approved changes to `corpus/` are logged here, newest first. The
`corpus-refresh` skill appends an entry for every change it writes.

Format per entry:
- **Date** — source(s) that triggered it — file(s) touched — one-line summary.

---

## 2026-09-15 — Two new blog sources added; dt-evals evaluator count resolved

**Sources added to `sources.yaml`** (both tier: primary, cadence: quarterly, last_fetched: 2026-09-15):
- https://www.dynatrace.com/news/blog/evaluate-llm-and-agent-quality-in-dynatrace-ai-observability/ — Kristof Muhi, 2026-06-11. dt-evals: 15 evaluators, offline/online modes, CI gating, alert config, dtctl. Cache: `blog-evaluate-llm-and-agent-quality.txt`.
- https://www.dynatrace.com/news/blog/dynatrace-intelligence-at-the-core-of-autonomous-operations/ — Bernd Greifeneder, 2026-01-28. Deterministic agents, maturity stages, ecosystem integrations, 65% stat. Cache: `blog-dynatrace-intelligence-at-the-core-of-autonomous-operations.txt`.

**Already registered — no change to `sources.yaml`:**
- https://www.dynatrace.com/platform/artificial-intelligence/
- https://docs.dynatrace.com/docs/dynatrace-intelligence
- https://www.dynatrace.com/news/blog/why-ai-agents-need-an-ai-lakehouse-in-the-modern-enterprise/

**`product-truth.md`** (`last_verified` bumped to 2026-09-15):
- dt-evals section expanded: offline/online modes, CI gating, full 15-evaluator list, judge providers, alert config (Slack/email), dtctl CLI.
- Video-transcript evaluator count ⚠ note retired; replaced with resolved note.
- Dynatrace Intelligence section: added deterministic agents (Root Cause, Analytics, Forecasting, Operator), domain-specific agents (mobile crash, security), maturity stages, ecosystem integrations (AWS Kiro, GitHub Copilot, ServiceNow, Azure SRE agent, Atlassian Rovo), 65% stat, Grail petabyte-scale (flagged as conflicting with exabyte-scale in the lakehouse blog).

**`gaps.md`:**
- Video-transcript conflict #1 (evaluator count) resolved: confirmed 15 from written source.
- New positioning conflict #3 added: Grail petabyte vs. exabyte scale discrepancy.

---

## 2026-09-03 — YouTube video sources (official Dynatrace channel only)

- **Sources added to `sources.yaml`** — new `youtube:` section, all `tier: secondary`,
  `cadence: none` (spoken content on published videos; won't change):
  - "How to Run LLM Evaluations with dt-evals │ AI Observability" — Dynatrace,
    https://youtu.be/64WwV4K287g — transcript fetched.
  - "Dynatrace Intelligence: … agentic AI platform | AMA" — Dynatrace,
    https://www.youtube.com/live/Hr7c4DTPDa0 — transcript fetched (~3-min caption gap).
  - "Observability Labs" playlist (180 videos) — catalog pointer only, not transcribed.
- **Removed two non-Dynatrace video sources** (team decision, same day): the two
  "Is It Observable" (Dynatrace DevRel) videos —
  https://www.youtube.com/watch?v=9e2VAKmHft8 ("kagent Explained") and
  https://www.youtube.com/watch?v=g4F-Q5CknDQ ("agent-sandbox & gVisor"). DevRel-channel
  content is not official Dynatrace positioning and must not ground market-facing
  claims. Removed from `sources.yaml`; nothing from them remains in `positioning.md`
  or `product-truth.md`. The "no dedicated AI monitoring product needed"
  counter-narrative section in `positioning.md` and its conflict entry in `gaps.md`
  were deleted with it.
- **`product-truth.md`** — new "From video transcripts (added 2026-09-03)" section:
  dt-evals mechanics/CLI/evaluators/CI-gating/bizevents; Dynatrace Intelligence state
  (operator LLM, MCP-first, remote MCP GA, root-cause agent, agentic workflow templates,
  ServiceNow Now Assist A2A, Dynatrace CLI). Every claim dated + marked as video
  transcript; ⚠ on spoken specifics.
- **`positioning.md`** — new "From video transcripts" section: three phases of AI
  maturity (car analogy), "deliver value in the context of the user", "MCP-first"
  framing, "autonomous cloud" direction. All from the Feb 2026 AMA (official).
- **Resolved: AI Observability vs. Dynatrace Intelligence.** Recorded as a resolution,
  not an open conflict — **two connected pillars on one platform** (Grail, Smartscape,
  Davis): AI Observability observes your AI; Dynatrace Intelligence is Dynatrace's AI
  running your ops. Sourced as a product-architecture point (lakehouse blog + docs +
  platform page); the Feb 2026 AMA is kept as dated supporting evidence.
  `product-truth.md` gains a "How it relates to AI Observability" subsection;
  `gaps.md` moves the item to **Resolved** and drops it from the open-conflicts list;
  `positioning.md` "Open positioning questions" updated.
- **`gaps.md`** — new "Video-transcript conflicts and open items" section: dt-evals
  "14 evaluators" (spoken) vs. shorter docs list; unverified "Opus 4.6" claim; spoken
  proper nouns.

## 2026-08-28 — Competitor research, first pass

- **Sources fetched and cached** (`corpus/.cache/competitor-*.txt`):
  - Datadog — https://www.datadoghq.com/product/llm-observability/ + https://docs.datadoghq.com/llm_observability/
  - New Relic — https://newrelic.com/platform/ai-monitoring
  - Grafana — https://grafana.com/docs/grafana-cloud/monitor-applications/ai-observability/ + Grafana Labs blog (solutions/llm-observability/ 404s)
  - LangSmith — https://www.langchain.com/langsmith
  - Braintrust — https://www.braintrust.dev/
- **Files created:** `corpus/competitors/{datadog,new-relic,grafana,langsmith,braintrust}.md`
  — each with positioning, what they claim to observe, named integrations, public customer
  proof, and a "read vs. Dynatrace" note. Standard YAML header + inline source URLs.
- **`sources.yaml`** — `competitors:` entries updated from placeholders to real URLs, tier,
  cadence (monthly), owner_file, cache filename, `last_fetched: 2026-08-28`, `status: ok`.
- **`gaps.md`** — new "Competitor research — what we could not verify" section (8 open items:
  Datadog product-name shift + metric attribution, New Relic integration list + AI proof,
  Grafana no product page + OpenLIT count, LangSmith deeper case studies, Braintrust
  integration list). "Not yet started" trimmed and a second-pass item added.

## 2026-08-28 — Side-by-side re-fetch: layer framework + integration count

- **Sources re-fetched:** https://www.dynatrace.com/solutions/ai-observability/ and
  https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability. No substantive
  page changes vs. the 2026-08-27 baseline; `.cache/` files unchanged. `last_fetched`
  bumped to 2026-08-28 in `sources.yaml`.
- **`gaps.md`** — new "Resolved" section:
  - Layer framework: the solutions page's **"Seven-Layer Observability Framework"** is
    canonical; the docs page covers the same span informally and does not contradict it.
  - Integration count: **genuinely unresolved** — 6 (solutions) vs. ~12 (docs) vs. ~39
    (Hub), all different scopes. Ruling: do not cite a specific integration number until
    pulled fresh from the Hub and dated.
  - Removed those two items from the "not resolved" list; renumbered the remainder.
- **`product-truth.md`** — updated the two inline notes (seven-layer naming, integration
  count) to point to the resolution. `last_verified` left at 2026-08-27 (only 2 of its 6
  sources were re-checked).

## 2026-08-27 — Initial build

- **Sources fetched and cached** (diff baselines in `corpus/.cache/`):
  - https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability
  - https://www.dynatrace.com/hub/?filter=ai-ml-observability
  - https://www.dynatrace.com/news/blog/why-ai-agents-need-an-ai-lakehouse-in-the-modern-enterprise/
  - https://www.dynatrace.com/news/blog/dynatrace-intends-to-acquire-arize/
  - https://www.dynatrace.com/platform/artificial-intelligence/
  - https://www.dynatrace.com/solutions/ai-observability/
  - https://docs.dynatrace.com/docs/dynatrace-intelligence
  - https://www.dynatrace.com/news/feed/ (RSS baseline for new-source detection)
- **Blocked:** https://community.dynatrace.com/t5/AI/bd-p/AI — Cloudflare challenge; no baseline. Tracked in `gaps.md`.
- **Files created:**
  - `sources.yaml` — source registry with tier / cadence / owner_file / last_fetched, `rss_feeds`, and placeholder `competitors` entries (Datadog, New Relic, Grafana, LangSmith, Braintrust).
  - `positioning.md` — category framing, the pitch, the wedge, messaging pillars.
  - `product-truth.md` — seven-layer framework, capabilities, agentic support, full Hub integration list, the Grail/Smartscape/Davis platform, and the adjacent Dynatrace Intelligence product.
  - `proof-points.md` — TELUS and FreedomPay quotes, Autodesk + analyst quotes (Dynatrace Intelligence), cited survey stats with caveats.
  - `arize.md` — the 2026-08-13 definitive agreement to acquire Arize; Phoenix / Arize AX / OpenInference; stated rationale; open-source commitment; open questions.
  - `gaps.md` — blocked sources, unquantified proof, Arize deal unknowns, five noted positioning conflicts, competitors not yet researched.
  - `CHANGELOG.md` — this file.
- **Registered but not yet fetched** (surfaced from the news RSS feed, cited from summaries only):
  - https://www.dynatrace.com/news/blog/sre-best-practices-platform-engineering-trends/
  - https://www.dynatrace.com/news/blog/how-to-measure-ai-roi-with-business-observability/
