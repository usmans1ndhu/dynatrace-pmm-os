---
title: The Arize Acquisition
last_verified: 2026-08-27
audience: both
sources:
  - https://www.dynatrace.com/news/blog/dynatrace-intends-to-acquire-arize/
  - https://www.dynatrace.com/solutions/ai-observability/
  - https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability
---

# The Arize Acquisition — What It Changes

**Bottom line: On 2026-08-13 Dynatrace signed a definitive agreement to acquire Arize. Arize brings the developer-facing evaluation and AI-native tracing layer (Phoenix, Arize AX, OpenInference) that Dynatrace's ops-centric platform was thinner on. The deal is not closed — it's pending regulatory approval — and until then the products run separately.**

## The facts

- **Announced:** August 13, 2026. Author of the announcement post: Steve Tack. (https://www.dynatrace.com/news/blog/dynatrace-intends-to-acquire-arize/)
- **Type:** "definitive agreement to acquire." (same)
- **Status:** "Integration pending regulatory approval; existing products and relationships remain unchanged immediately following close." (same)
- **Deal terms (price, structure, headcount):** not disclosed on the announcement page. See gaps.md.

## What Arize brings

| Asset | What it is | Source |
|---|---|---|
| **Phoenix** | Open-source AI observability platform: trace applications, run evaluations, investigate failures during development | https://www.dynatrace.com/news/blog/dynatrace-intends-to-acquire-arize/ |
| **Arize AX** | Managed enterprise platform: agent observability, online evaluations, production monitoring | same |
| **OpenInference** | Open specification for AI tracing, built on OpenTelemetry | same |

## The stated rationale

"AI systems fail differently than traditional software. While conventional applications produce traceable errors, AI applications can appear functional while being inaccurate, biased, or misaligned." (https://www.dynatrace.com/news/blog/dynatrace-intends-to-acquire-arize/)

Framing stat: "51% of agentic AI leaders cite technical challenges managing agents at scale as a top barrier to production deployment." (same; underlying study not linked)

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
