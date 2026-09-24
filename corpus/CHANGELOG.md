# Corpus Changelog

All approved changes to `corpus/` are logged here, newest first. The
`corpus-refresh` skill appends an entry for every change it writes.

Format per entry:
- **Date** — source(s) that triggered it — file(s) touched — one-line summary.

---

## 2026-09-24 — Arize acquisition: secondary source integrated; arize.md, gaps.md, sources.yaml updated

**Source added:** https://www.efficientlyconnected.com/dynatrace-arise-ai-observability-acquisition/ (third-party analysis, tier: secondary, fetched 2026-09-24). Note: article URL has a typo ("arise" vs. "arize") — content refers to Arize correctly.

**`arize.md`** — additions:
- Status note: secondary source uses past-tense "acquires" — may indicate deal closed; NOT confirmed from Dynatrace primary source
- Arize founders named: Aparna Dhinakaran and Jason Lopatecki
- **ADB** added as a fourth Arize asset (purpose-built data store) — secondary source only; not in Dynatrace's primary announcement
- Phoenix adoption: 4,000+ enterprises (secondary source)
- Steve Tack quote: "end-to-end observability that spans both traditional software telemetry and the non-deterministic outputs of AI agents" (secondary source; needs primary-source verification before external use)
- New section: "Market framing from third-party analysis" — ECI Research stats (48.5% compliance priority, 47.2% developer velocity, 52.5% vendor lock-in concern), 12-month integration evaluation window, "operational intelligence platform" framing

**`gaps.md`** — updates:
- "Arize deal — unknown" section updated: deal close flagged as unconfirmed pending Dynatrace primary source; founders and Phoenix stats added; ADB flagged for verification
- "Arize: competitor AND pending acquisition" section updated with 2026-09-24 note: do not use competitive Arize framing in new external content; instructions for what to update if/when close is confirmed from Dynatrace primary source

**`sources.yaml`** — new `third_party:` section added with efficientlyconnected.com entry.

---

## 2026-09-22 — WGU story corrected to right URL; all customer stories expanded to full depth

**Sources:** https://www.dynatrace.com/customers/western-governors-university/ (correct WGU URL). All 12 customer story pages re-fetched for complete content.

**`proof-points.md`** — full rewrite of all customer story sections:
- **WGU**: Replaced incorrect entry (old URL: /wgu/; wrong student count 140,000; wrong quotes). Correct URL: /western-governors-university/. Correct data: 192,000+ students; 20% YoY enrollment growth; 500,000+ degrees. Key metric: 77% faster incident resolution using AWS DevOps Agent (28 min vs. estimated 2 hours). MTTR from days to hours. Spokespeople: Angel Marchena (Director of Technical Operations), Nate Cummings (Senior Director of Infrastructure). Technologies: AWS Lambda, Amazon EKS, AWS DevOps Agent.
- **All other stories expanded**: Added company overview, full problem statement, complete list of Dynatrace solutions implemented with descriptions, how Dynatrace solved it, all quotes with full speaker names and titles, all technologies and integrations. Every story now contains sufficient depth to answer any question about any term mentioned.
- Stories expanded: InPost, CDL, Accenture ALIP, Vitality, FreedomPay, Vodafone, Vestmark, Careem, CIMB Bank, Macquarie Bank, Sicredi.

**`sources.yaml`** — WGU entry updated: URL corrected to /western-governors-university/; last_fetched updated to 2026-09-22; notes updated with correct facts.

---

## 2026-09-17 — Five Autonomous Operations customer stories added (Careem, CIMB, Macquarie, Sicredi, WGU)

**Sources:** dynatrace.com/customers/ Autonomous Operations filter. All five fetched successfully (Macquarie URL resolved as /macquarie-bank/).

**New entries added to `sources.yaml`** under `customers:` (all tier: primary, cadence: quarterly, last_fetched: 2026-09-17):
- Careem, CIMB Bank, Macquarie Bank, Sicredi, WGU

**`proof-points.md`** — new section "Customer proof — Autonomous Operations":
- **Careem**: Strongest quantified proof in section — 65% cost reduction, 84% MTTD reduction (under 2 min), 6x faster root cause, 10,000 engineering hours saved/year, 99.99% availability. Tagged Autonomous Operations + AI Observability.
- **CIMB Bank**: Near-zero critical incidents; availability 0.6→0.95; 90% alert reduction. Tagged Autonomous Operations + AI Observability.
- **Macquarie Bank**: Qualitative; "AI as first responder, human in the loop" framing. Live Debugger + Dynatrace Intelligence. Tagged Autonomous Operations.
- **Sicredi**: 80% faster instrumentation; 67% cognitive load reduction; SLO time 15min→3min. Tagged AI Observability.
- **WGU**: Qualitative; proactive detection, uninterrupted availability. Only education sector story in corpus. Tagged Autonomous Operations.

---

## 2026-09-16 — FY27 Integrated Campaign Messaging v3.0 (14 pages) read and integrated

**Source added to `sources.yaml`** — new entry under `internal:` (tier: internal, v3.0, last updated 2026-07-07, status: work in progress, in review; owners: Kristi Beard, Ashley Adams, Greg Findlen, Mrudula Bangera; 14 pages).

**`positioning.md`** (`last_verified` → 2026-09-16) — major update. New section "Official FY27 campaign messaging":
- Official tagline: "Powered by AI. Built for AI."
- Official positioning statement (verbatim)
- Short description + elevator pitches (platform-level, Built for AI, Powered by AI)
- Campaign value proposition (5 bullets)
- Why Dynatrace Intelligence can act with confidence (4 differentiators: grounded/guardrails/full-stack/closed-loop)
- Closed-loop operational model for AI workloads
- Creative hooks per use case
- Customer value propositions (for sales conversations)
- Market opportunity questions
- Competitive framing: Fiddler, Arize, Langfuse as point solutions; Datadog+Grafana named targets; generic AIOps framing
- Partner alignment: Microsoft (Azure + Sentinel + GitHub), Google Cloud, AWS
- Persona targeting with new AI-native job titles

**`proof-points.md`** — stats table updated:
- 51% stat: source confirmed as "Pulse of Agentic AI Report 2026" (messaging doc v3.0)
- Added: 95% of AI initiatives deliver zero ROI (MIT, "The GenAI Divide," June 2025)
- Added: Global AI market $189B (2023) → $4.8T (2033)

**`product-truth.md`** — new "AI Observability App — named capabilities" section: 4 app tabs, platform differentiators, new capabilities (Agent Topology and Dependency, Prompt Debugging and Management, AI Coding Agent Monitoring, RUM for AI); agent trajectory support added to evals description.

**`gaps.md`** — 51% stat source partially resolved; new "Arize: competitor AND pending acquisition" conflict note; new facts-not-yet-verified items (95% MIT stat, $189B→$4.8T market size).

---

## 2026-09-16 — FY27 JuneRally SE AI Pitch deck (94 pages) read and integrated

**Source added to `sources.yaml`** — new `internal:` section (tier: internal, cadence: none, CONFIDENTIAL, pages: 94, last_read: 2026-09-16). Every claim sourced only from this deck requires a public-source backup before external use.

**`product-truth.md`** (`last_verified` → 2026-09-16):
- Sources header: pitch deck added.
- **Dynatrace Assist — rebuilt from the models up** (new section): Claude Sonnet 4.6 on AWS Bedrock confirmed; 28 skills following Anthropic Agent Skills standard; NL2DQL fine-tuned model replacing RAG (now "already available" — resolves AMA ⚠); side-panel UI.
- **Dynatrace Intelligence — current status** (new section): GA status breakdown table (Foundation, Agents, Assist, MCP Server all GA; Agentic Workflows = Preview; dt-ctl and Dynatrace for AI open source).
- **Autonomous SRE Agent — ROADMAP** (new section): explicitly flagged as not shipped; V1 as agentic workflow; do not use in external claims.
- **Cloud SRE Agents** (new sub-section): orchestrates AWS/Azure/Google SRE agents across multicloud; AWS DevOps agent integration.
- **MCP Server 4-step security workflow** (new sub-section): Problem → MCP → Grail + Causal AI → GitHub notification → Copilot code fix.
- **Visual agent builder** (no-code, new sub-section).
- **dtctl** (expanded): built-in skill file detail; dtctl + Claude Code + GitHub customer anecdote (directional only — no public attribution).
- **AI Observability capabilities expanded**: cost monitoring with SLOs/predictions powered by Davis AI; model version A/B testing; guardrails monitoring from model providers; multi-modal agent explainability (AgentCore, Strands, Google ADK, LangChain, OpenAI Agents, MCP).
- Video transcript NL2DQL flag updated from ⚠ roadmap → resolved (now "already available" per deck).

**`positioning.md`** — new "Closing statement / elevator pitch" section: "You can't scale AI you can't see..." quote from deck; Built for AI vs. Powered by AI frame.

**`gaps.md`** — new "Roadmap items" section: Autonomous SRE Agent and Agentic Workflows flagged as not GA. Video item #2 (NL2DQL) partially resolved: confirmed available, "Opus 4.6" model name still inconsistent with confirmed "Claude Sonnet 4.6."

---

## 2026-09-16 — Seven customer stories added

**New `customers:` section added to `sources.yaml`** (all tier: primary, cadence: quarterly, last_fetched: 2026-09-16):
- InPost (Logistics) — AI monitoring for agentic systems; Kubernetes 2-min ID / 7-min resolution; token control.
- CDL (UK Insurtech) — Bedrock AI observability; CSAT +10%; tools 10→1; onboarding days→minutes.
- Accenture ALIP (Insurance) — 40% observability cost cut; 90% MTTR improvement; 99.50%→99.98% availability; 20% LLM token reduction. Strongest quantified proof in corpus.
- Vitality Group (Insurance) — ~$1M log cost savings; 90%+ logging cost reduction; 15-25% engineering productivity gain. Vitality AI on Google Vertex.
- FreedomPay (Financial Services) — expanded story (3B+ transactions, 130+ countries); qualitative; original quote already in corpus.
- Vodafone (Telco) — Grail log management; 8TB→18TB/day; avoided 3-4x cost increase; 8,000 dashboards in 8 weeks.
- Vestmark (Financial Services) — OpenLLMetry for AI agent visibility; $1.9T AUM platform; qualitative.

**`proof-points.md`** — major update (`last_verified` → 2026-09-16): bottom line rewritten to reflect quantified proof now available; all 7 customer stories added with quotes, metrics, Dynatrace use, audience fit, and source. FreedomPay entry expanded from single quote to full story. "What's missing" section updated.

---

## 2026-09-16 — Two knowledge base sources added

**Sources added to `sources.yaml`** (both tier: primary, cadence: quarterly, last_fetched: 2026-09-16):
- https://www.dynatrace.com/knowledge-base/ai-observability/ — published 2026-03-17. AI observability definition, 6-layer framework (conflict with 7-layer solutions page — see gaps.md #4), named managed platforms. Cache: `knowledge-base-ai-observability.txt`.
- https://www.dynatrace.com/knowledge-base/ai-agent-observability/ — last updated 2026-06-29. Definition, four risk categories, three core pillars (telemetry, behavioral monitoring, governance), five-step implementation, named frameworks. Cache: `knowledge-base-ai-agent-observability.txt`.

**`product-truth.md`** — new section "AI agent observability — risks, pillars, and implementation" added before the Agentic AI support section. Sources header updated with both KB URLs. Inline conflict note on the 6-layer framework discrepancy.

**`gaps.md`** — new positioning conflict #4: KB page 6-layer framework vs. solutions page 7-layer framework.

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
