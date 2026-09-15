---
title: Proof Points — Dynatrace AI Observability
last_verified: 2026-08-27
audience: both
sources:
  - https://www.dynatrace.com/solutions/ai-observability/
  - https://docs.dynatrace.com/docs/dynatrace-intelligence
  - https://www.dynatrace.com/news/blog/dynatrace-intends-to-acquire-arize/
  - https://www.dynatrace.com/news/blog/sre-best-practices-platform-engineering-trends/
  - https://www.dynatrace.com/platform/artificial-intelligence/
---

# Proof Points

**Bottom line: The public proof is thin and mostly qualitative. Two named AI-observability customer quotes (TELUS, FreedomPay), two more platform/Intelligence quotes (Autodesk, plus an analyst), and a handful of survey stats Dynatrace cites without a linked source. No public hard ROI numbers tied to a named customer yet.**

## Customer quotes — AI Observability

**Kulvir Gahunia, Director of the Site Reliability Office, TELUS:**
> "By combining our Agentic AI initiatives with Dynatrace's AI Observability capabilities, we've successfully optimized our development and operations workflows."
Source: https://www.dynatrace.com/solutions/ai-observability/
Audience fit: Ops/SRE.

**Mark Tomlinson, Senior Director of Observability and Performance, FreedomPay:**
> "We knew early on that if we were going to scale AI responsibly, observability had to come first. Without visibility into how these models behave, you can't build the trust required for enterprise adoption."
Source: https://www.dynatrace.com/solutions/ai-observability/
Audience fit: Ops/SRE, exec.

## Customer quotes — Dynatrace Intelligence (adjacent, use with care)

**Alexander Bicalho, Autodesk:**
> The approach "connects insight to action, while keeping our teams in control, could significantly improve performance and reliability as we scale."
Source: https://www.dynatrace.com/platform/artificial-intelligence/
Note: This is about Dynatrace Intelligence (AI running ops), not AI Observability (observing your AI). Conditional tense ("could"). Don't present as an AI-observability result.

## Analyst quote

**Rob Strechay** (analyst; affiliation not stated on page):
> "deterministic AI...reduces costs, increases trust, and enables supervised autonomy that enterprises can actually scale."
Source: https://www.dynatrace.com/platform/artificial-intelligence/
Note: About Dynatrace Intelligence. Affiliation unverified — see gaps.md.

## Stats Dynatrace cites

| Stat | Context | Source | Caveat |
|---|---|---|---|
| 51% of agentic AI leaders cite technical challenges managing agents at scale as a top barrier to production | Used to frame the Arize acquisition | https://www.dynatrace.com/news/blog/dynatrace-intends-to-acquire-arize/ | Underlying study not linked on the page |
| Monitoring AI systems is SREs' top use case (58%) | SRE / platform-engineering trends post | https://www.dynatrace.com/news/blog/sre-best-practices-platform-engineering-trends/ | Underlying research not linked; read from RSS summary, full post not fetched |
| Platform engineers prioritize AI-powered developer support | Same post | https://www.dynatrace.com/news/blog/sre-best-practices-platform-engineering-trends/ | Qualitative; no number captured |

## Capability claims usable as proof (feature-level, from Dynatrace)

- Prompt storage up to 10 years for compliance / data lineage. (https://www.dynatrace.com/solutions/ai-observability/)
- Open-source `dt-evals` CLI for continuous evals (frustration, toxicity, hallucination, PII, prompt injection). (https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability)
- Dynatrace Playground public sandbox with sample data. (https://www.dynatrace.com/solutions/ai-observability/)
- Whitepaper: "Full-Stack AI Observability That Increases ROI and Decreases Business Risks." (https://www.dynatrace.com/solutions/ai-observability/) — title only; not fetched.

## What's missing

See gaps.md. No quantified customer outcome (cost saved, MTTR reduced, incidents prevented) is public. The strongest available material is category/survey framing plus two qualitative SRE quotes.
