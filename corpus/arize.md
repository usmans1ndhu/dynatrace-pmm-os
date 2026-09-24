---
title: The Arize Acquisition
last_verified: 2026-09-24
audience: both
sources:
  - https://www.dynatrace.com/news/blog/dynatrace-intends-to-acquire-arize/
  - https://www.dynatrace.com/solutions/ai-observability/
  - https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability
  - https://www.efficientlyconnected.com/dynatrace-arise-ai-observability-acquisition/  # secondary; tier: secondary; see note below
---

# The Arize Acquisition — What It Changes

**Bottom line: On 2026-08-13 Dynatrace signed a definitive agreement to acquire Arize. Arize brings the developer-facing evaluation and AI-native tracing layer (Phoenix, Arize AX, OpenInference, ADB) that Dynatrace's ops-centric platform was thinner on. A secondary source (EfficientlyConnected, 2026-09-24) uses past-tense "acquires" suggesting the deal has closed — but this has NOT been confirmed from a Dynatrace primary source. See gaps.md.**

> **Source note on efficientlyconnected.com:** Third-party analysis/commentary site. Tier: secondary. Claims from this source require Dynatrace primary-source backup before external use. The article URL contains a typo ("arise" vs. "arize") — the article itself refers to Arize correctly throughout.

## The facts

- **Announced:** August 13, 2026. Author of the announcement post: Steve Tack (CPO, Dynatrace). (https://www.dynatrace.com/news/blog/dynatrace-intends-to-acquire-arize/)
- **Type:** "definitive agreement to acquire." (same)
- **Status per Dynatrace primary source:** "Integration pending regulatory approval; existing products and relationships remain unchanged immediately following close." (same)
- **Status per secondary source (2026-09-24):** efficientlyconnected.com article uses past-tense "acquires Arize AI" — may indicate deal has closed. Not yet confirmed from Dynatrace's own comms. Flag for verification.
- **Arize AI founders:** Aparna Dhinakaran and Jason Lopatecki. (efficientlyconnected.com)
- **Deal terms (price, structure, headcount):** not disclosed. See gaps.md.

## What Arize brings

| Asset | What it is | Source |
|---|---|---|
| **Phoenix** | Open-source AI observability platform: trace applications, run evaluations, investigate failures during development. Used by 4,000+ enterprises. | https://www.dynatrace.com/news/blog/dynatrace-intends-to-acquire-arize/ + efficientlyconnected.com |
| **Arize AX** | Managed enterprise platform: agent observability, online evaluations, production monitoring | https://www.dynatrace.com/news/blog/dynatrace-intends-to-acquire-arize/ |
| **OpenInference** | Open specification for AI tracing, built on OpenTelemetry | same |
| **ADB** | Purpose-built data store for AI observability data | efficientlyconnected.com (secondary) — not named in Dynatrace primary announcement; verify before external use |

## The stated rationale

"AI systems fail differently than traditional software. While conventional applications produce traceable errors, AI applications can appear functional while being inaccurate, biased, or misaligned." (https://www.dynatrace.com/news/blog/dynatrace-intends-to-acquire-arize/)

Framing stat: "51% of agentic AI leaders cite technical challenges managing agents at scale as a top barrier to production deployment." (same; underlying study not linked)

**Steve Tack (CPO, Dynatrace) quote on the combination:**
> "end-to-end observability that spans both traditional software telemetry and the non-deterministic outputs of AI agents"
Source: efficientlyconnected.com (secondary). This quote is attributed to Tack but not yet verified against a Dynatrace primary source — do not use externally without confirming the original Dynatrace press release or blog.

## Market framing from third-party analysis (secondary — EfficientlyConnected)

Source: https://www.efficientlyconnected.com/dynatrace-arise-ai-observability-acquisition/, verified 2026-09-24. Tier: secondary. Use for analyst perspective and buyer insight only; do not pass off as Dynatrace's own words.

**Strategic framing:** The acquisition positions Dynatrace toward "operational intelligence platform" rather than traditional observability vendor — a market-redefinition move.

**Business case for IT decision-makers (per ECI Research survey data):**
- 48.5% of survey respondents prioritize "enforcing standardized security and compliance guardrails automatically"
- 47.2% weight "developer velocity and ease of integration" most heavily in technical vendor selection
- 52.5% are moderately concerned about vendor lock-in but prioritize functionality over lock-in risk

**Vendor lock-in angle:** Phoenix remaining open-source directly addresses lock-in concerns. Dynatrace's Davis engine provides precedent for building proprietary intelligence atop an open foundation without abandoning the open layer.

**Integration horizon:** Article cites a 12-month evaluation window as the relevant timeframe for assessing integration success.

## Expected combined capabilities (Dynatrace's claims, not yet shipped)

- Compare model performance between development and production environments
- Investigate AI degradation across the full technology stack
- Connect quality metrics with operational signals like latency and costs
- Link agent workflows directly to business outcomes
- Feed production insights back into improvement cycles

Source for all five: https://www.dynatrace.com/news/blog/dynatrace-intends-to-acquire-arize/

## Commitment to open source

"Dynatrace intends to support Phoenix independently and continue stewardship of OpenInference, maintaining vendor-neutral access for developers." (https://www.dynatrace.com/news/blog/dynatrace-intends-to-acquire-arize/)

## Why it matters for positioning

- **Before:** Dynatrace was strong on ops signals (latency, cost, errors, infra, root cause) and had LLM-as-a-judge evals, but limited developer-loop / pre-production tooling.
- **After (intended):** a dev-to-prod story — build and evaluate with Phoenix/AX, run in production with Dynatrace, one feedback loop.
- **Overlap to resolve:** OpenInference is already listed as a Dynatrace Hub instrumentation option (https://www.dynatrace.com/hub/?filter=ai-ml-observability), and Dynatrace already has `dt-evals` (https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability). How `dt-evals` vs. Phoenix/AX evals are positioned post-close is an open question — see gaps.md.

## Open questions

Tracked in gaps.md: deal price and close date; product roadmap (merge vs. keep separate brands); pricing/packaging; what happens to the Arize customer base and the Phoenix OSS governance model; whether "Arize" survives as a product name.
