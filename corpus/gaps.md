---
title: Gaps — What We Could Not Verify
last_verified: 2026-08-28
audience: internal
sources:
  - https://www.dynatrace.com/solutions/ai-observability/
  - https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability
  - https://www.dynatrace.com/hub/?filter=ai-ml-observability
  - https://docs.dynatrace.com/docs/dynatrace-intelligence
  - https://www.dynatrace.com/platform/artificial-intelligence/
  - https://www.dynatrace.com/news/blog/dynatrace-intends-to-acquire-arize/
  - https://www.dynatrace.com/news/blog/why-ai-agents-need-an-ai-lakehouse-in-the-modern-enterprise/
  - https://community.dynatrace.com/t5/AI/bd-p/AI
  - https://youtu.be/64WwV4K287g  # video transcript, 2026-09-03
  - https://www.youtube.com/live/Hr7c4DTPDa0  # video transcript, 2026-09-03
---

# Gaps

**Bottom line: The initial build covers Dynatrace's own positioning and product pages well. The weak spots are quantified proof, the Arize deal mechanics, the community signal (blocked by a bot wall), and all five competitors (not yet researched).**

## Sources we could not fetch

| Source | Problem | Next step |
|---|---|---|
| https://community.dynatrace.com/t5/AI/bd-p/AI | Cloudflare "Just a moment..." challenge blocks WebFetch (HTTP 403) and curl. No diff baseline. | Fetch headful in a browser, or via an authenticated/JS-capable tool. Then fill the community signal (what users ask about, common complaints, feature requests). |

## Facts we could not verify or quantify

- **No quantified customer ROI.** Every customer reference (TELUS, FreedomPay, Autodesk) is qualitative. No public "cut MTTR by X" or "saved $Y in tokens" tied to a name. (proof-points.md)
- **Survey stats are unsourced.** "51% of agentic AI leaders..." and "58% of SREs..." are cited by Dynatrace without a linked study. Find the underlying reports before using externally.
- **`sre-best-practices-platform-engineering-trends` post not fully fetched.** Only the RSS summary was captured. Full post may have more stats / quotes.
- **Rob Strechay's analyst affiliation** is not stated on the Dynatrace Intelligence page. Verify before attributing.
- **Whitepaper "Full-Stack AI Observability That Increases ROI and Decreases Business Risks"** — title only, not fetched. May contain usable numbers.

## Arize deal — unknown

- Purchase price and deal structure — not disclosed.
- Expected close date — "pending regulatory approval," no date given.
- Product roadmap: will Arize AX / Phoenix keep their names, or fold into Dynatrace branding?
- Pricing and packaging of the combined offering.
- Fate of the existing Arize customer base and Phoenix OSS governance.
- Headcount / team integration.

## Resolved

### 2026-09-03 — AI Observability vs. Dynatrace Intelligence: two connected pillars

**Resolution (team decision, 2026-09-03).** These are **not competing narratives**.
They are two connected pillars on one platform:

- **AI Observability** observes *your* AI — the GenAI apps, LLMs, and agentic
  workflows you build and run (the seven-layer framework).
- **Dynatrace Intelligence** is *Dynatrace's* AI running your operations — the
  agentic operations system that investigates, advises, and acts.

They share the same foundation: **Grail** (data lakehouse / context engine),
**Smartscape** (real-time dependency + business-context graph), and **Davis AI**
(causal, deterministic analysis). This is a product-architecture point, traceable
to the platform pages already in the corpus:
https://www.dynatrace.com/news/blog/why-ai-agents-need-an-ai-lakehouse-in-the-modern-enterprise/,
https://docs.dynatrace.com/docs/dynatrace-intelligence,
https://www.dynatrace.com/platform/artificial-intelligence/. See product-truth.md
→ "How it relates to AI Observability — two connected pillars, one platform."

**Supporting evidence (video, dated).** The Feb 2026 Dynatrace AMA
(https://www.youtube.com/live/Hr7c4DTPDa0, `verified: 2026-09-03`, auto-captions)
states Dynatrace Intelligence is "fueled by a unified data lakehouse that we call
Grail along with Smartscape topology," feeding both Dynatrace's agents and
customer-built agents — the same platform the AI Observability app writes into.
Consistent with the architecture point above.

**Still open (separate item):** how the Dynatrace-native AI observability and the
acquired Arize products are positioned relative to each other post-close. That is
an Arize-deal question, not an Intelligence question. (arize.md, "Arize deal —
unknown" above.)

### 2026-08-28 — Layer framework: canonical framing identified

Re-fetched https://www.dynatrace.com/solutions/ai-observability/ and
https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability side by side.

- **Solutions page** presents a named framework — the **"Seven-Layer Observability
  Framework"** — with these layers in order: Business Impact, Application Performance,
  Orchestration Layer, Agent-to-Agent Communication, Model Integrity, Semantic Caches
  and Vector Databases, Infrastructure Monitoring. (https://www.dynatrace.com/solutions/ai-observability/)
- **Docs page** does **not** name or number a framework. It describes the same span in
  prose: "This approach covers the complete AI stack, from foundational models and vector
  databases to RAG orchestration frameworks, ensuring visibility across every layer of
  modern AI applications." (https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability)

**Canonical:** the **seven-layer framework from the solutions/marketing page** is the
canonical external framing. The docs page does not contradict it — it just covers the
same ground informally. Safe to use "seven-layer" and the layer names above, cited to the
solutions page.

- **Minor caveat:** on this re-fetch the extraction of the solutions page wavered between
  "six" and "seven" in the body text while the framework is titled "seven layers" and the
  diagram shows seven. The seven named layers above match the earlier capture. If you need
  to quote the body copy exactly, re-verify against the live page.

### 2026-08-28 — Integration count: genuinely unresolved

There is **no single canonical integration number**. The three sources each list a
different set at a different scope, and none is wrong:

| Source | Count | Scope |
|---|---|---|
| https://www.dynatrace.com/solutions/ai-observability/ | 6 named | Marquee "supported platforms": Amazon Bedrock, Azure AI Foundry, LangChain, NVIDIA NIM, OpenAI, Google Vertex AI — then "See all technologies" |
| https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability | ~12 named + "many more" | Illustrative examples: OpenAI, Amazon Bedrock, NVIDIA NIM, Ollama, Milvus, Weaviate, Qdrant, LangChain, LangGraph, CrewAI, Google TPU, NVIDIA GPU |
| https://www.dynatrace.com/hub/?filter=ai-ml-observability | ~39 tiles (as of 2026-08-27) | The full live catalog; changes frequently |

**Ruling: do not cite a specific integration number until confirmed.** The Hub is the
authoritative catalog, but its count moves week to week. When a number is needed, pull it
fresh from the Hub at the time of use and date it. For prose, use "the major model
providers, agent frameworks, and vector databases" and name specific integrations rather
than a total.

## Video-transcript conflicts and open items (added 2026-09-03)

Handled the same way as the seven-layer framework conflict (see Resolved above):
logged, not silently resolved. Sources are auto-generated captions from official
Dynatrace videos — spoken, less precise than written docs.

1. **dt-evals evaluator count — resolved 2026-09-15.** Blog post (https://www.dynatrace.com/news/blog/evaluate-llm-and-agent-quality-in-dynatrace-ai-observability/, Kristof Muhi, verified 2026-09-15) is the written Dynatrace source confirming **15 built-in evaluators**: Relevance, Faithfulness, Hallucination, Answer completeness, Context relevance, Factual accuracy, Summarization quality, Conciseness, Fluency, Toxicity, Bias, PII leakage, Prompt injection, User frustration, Drift detection. The video's spoken "14" was an undercount. product-truth.md and CHANGELOG.md updated.

2. **NL→DQL fine-tuned model beating "Opus 4.6".** AMA (~28:13) claims an
   unreleased fine-tuned NL→DQL model "blows out of the water" comparisons to
   "the latest, e.g. Opus 4.6 models." Spoken, roadmap, and the model name is
   unverified (no public "Opus 4.6" confirmed here). Do not repeat externally.

3. **Spoken proper nouns to verify:** Dynatrace CLI author "Christoph Namüller"
   (AMA ~37:34) — spelling from captions, unconfirmed.

## Positioning conflicts and ambiguities (noted, not resolved)

1. **`dt-evals` vs. Arize Phoenix/AX evals.** Both do LLM evals. Overlap unaddressed publicly. (arize.md)
2. **`platform/artificial-intelligence/` URL** resolves to "Dynatrace Intelligence" content that overlaps `docs/dynatrace-intelligence`. May be a redirect; treat as one source until confirmed.
3. **Grail scale: petabyte vs. exabyte.** The Intelligence blog (https://www.dynatrace.com/news/blog/dynatrace-intelligence-at-the-core-of-autonomous-operations/, 2026-01-28) says "petabyte-scale"; the lakehouse blog (https://www.dynatrace.com/news/blog/why-ai-agents-need-an-ai-lakehouse-in-the-modern-enterprise/) says "exabyte-scale." Do not cite either figure externally without resolving which is current. (product-truth.md)

(The layer-framework naming and the integration-count mismatch that were previously listed
here moved to **Resolved** above on 2026-08-28.)

## Competitor research — what we could not verify (first pass 2026-08-28)

First-pass briefs written for all five from each vendor's own public pages
(`corpus/competitors/*.md`). Open items:

- **Datadog product name.** Marketing URL is `/product/llm-observability/` but the page and
  docs increasingly say "Agent Observability." Which is canonical, and is "LLM Observability"
  being retired? Re-verify next refresh. (competitors/datadog.md)
- **Datadog customer metrics.** "400% faster MTTR," "40% lower token usage per task," "15%
  faster deployment" appear on the page but the capture did not tie each to a named customer.
  Confirm attribution before repeating. (competitors/datadog.md)
- **New Relic integrations.** Public AI-monitoring page names only OpenAI, Pinecone, LangChain,
  MCP. Real coverage via APM agents is wider (Bedrock, Azure OpenAI, etc. historically) but
  not verified from a primary page this pass. (competitors/new-relic.md)
- **New Relic AI customer proof.** No quote or metric specific to AI monitoring is public on
  the product page. Case studies shown are general observability, not AI. (competitors/new-relic.md)
- **Grafana has no dedicated product page.** `grafana.com/solutions/llm-observability/` 404s.
  Brief is built from Grafana Cloud docs + Grafana Labs blog. No named AI customer found.
  (competitors/grafana.md)
- **Grafana / OpenLIT integration count.** "50+ GenAI tools" is OpenLIT's claim, not an
  enumerated Grafana list. Do not cite a number without checking OpenLIT's support matrix.
  (competitors/grafana.md)
- **LangSmith deeper case studies.** The `/langsmith` page has a 25+ logo wall but no
  attributed quotes or metrics. LangChain publishes fuller customer stories on a separate
  page, not fetched. (competitors/langsmith.md)
- **Braintrust integrations.** The landing page does not enumerate model providers or
  frameworks; those live in the docs, not fetched this pass. (competitors/braintrust.md)
- **Not researched at all:** competitor pricing, security/compliance certifications, deployment
  models (SaaS vs. self-hosted), and any analyst placement for the five.
- **No cache baseline was overwritten by any prior version** — these are all first fetches.

## AI Observability docs corpus (added 2026-09-03)

- **Gap:** Integrations catalog page (`/integrations`) doesn't state a total count. Hub catalog is described as broader/continuously updated than the docs page.
  **Risk:** Don't quote a specific integration count externally (e.g. "50+ integrations") without re-checking the live Hub filter.
  **Status:** Unverified

- **Gap:** Both eval features — `dt-evals` visualization in-app and the Agent evaluations config UI — are marked Preview, governed by preview terms, not GA.
  **Risk:** Presenting either as fully released/GA in customer-facing material would overstate maturity.
  **Status:** Confirmed as Preview (source: doc page itself) — flag in messaging, not a gap to resolve, just a constraint to respect.

- **Gap:** Microsoft Copilot Studio caveat ("MS Agent Framework support applies to Azure AI Agent Service agents, not Copilot Studio's low-code canvas") came from a Dynatrace community forum post, not the official doc page.
  **Risk:** Could be outdated, wrong, or an individual's interpretation rather than product truth.
  **Status:** Needs confirmation from product/eng before use.

- **Gap:** Market-sizing stats ("$749B AI spend by 2028," IDC citation) live in press releases/blog posts, not the docs tree this corpus file covers.
  **Risk:** Excluded from this corpus entirely — don't let it get pulled in as if it were doc-sourced.
  **Status:** Out of scope, sourced separately if needed, with proper IDC attribution.

- **Gap:** Pricing/licensing beyond "requires DPS + Traces/Metrics/Logs powered by Grail" isn't detailed in this doc tree.
  **Risk:** Any cost-specific claim needs a separate pull from the License docs section.
  **Status:** Not yet sourced.

## Not yet started

- **Pricing** for Dynatrace AI Observability — not captured.
- **Analyst positioning** (Gartner APM/Observability MQ, Forrester Wave) — not captured, for Dynatrace or competitors.
- **Competitive win/loss or head-to-head** material — none.
- **Second competitor pass:** each vendor's docs / customer-stories / pricing pages, to fill the items above.

