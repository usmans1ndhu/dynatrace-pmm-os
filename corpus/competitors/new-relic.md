---
title: Competitor — New Relic (AI Monitoring)
last_verified: 2026-08-28
audience: both
sources:
  - https://newrelic.com/platform/ai-monitoring
---

# New Relic — AI Monitoring

**Bottom line: New Relic's pitch is "AI observability for modern applications" — full-stack APM extended down into the AI call, with cost control and model comparison. It is squarely an ops/APM story; the public page shows thin named-integration detail and no attributed AI customer quotes.**

## Positioning

Headline: "AI observability for modern applications." (https://newrelic.com/platform/ai-monitoring)

Description: "Build, run, and optimize AI-powered applications confidently with full-stack observability, performance insights, and cost control across your AI stack." Tagline: "Observability makes AI your business partner." (https://newrelic.com/platform/ai-monitoring)

## What they claim to observe

Source: https://newrelic.com/platform/ai-monitoring

- Response time and quality metrics; token tracking (request tokens used)
- APM golden signals; infrastructure monitoring; performance dashboards
- AI metrics summaries; model response consolidation with in-depth insights; outlier identification
- Trace visibility from prompt to response, "including user feedback"
- Issue detection: bias, hallucination, toxicity
- Cost monitoring and custom alerts; model comparison across cost, performance, quality
- Prompt and response analysis
- Multi-agent AI agent mapping and interaction visualization; tool-call tracking by AI agents
- Distributed tracing with "granular agent/tool visibility"; latency and error identification
- MCP server call monitoring "across full request lifecycle"
- Model prediction tracking and drift detection
- Alert management and applied intelligence

## Named integrations

Source: https://newrelic.com/platform/ai-monitoring (the public page names few explicitly)

- **Models:** OpenAI
- **Vector databases:** Pinecone
- **Frameworks:** LangChain
- **Protocol:** Model Context Protocol (MCP)
- **Adjacent New Relic products referenced:** New Relic Security RX, New Relic alerts

> The page implies broader library coverage ("across your AI stack") but does not enumerate it. New Relic's AI monitoring has historically instrumented more libraries (e.g. Bedrock, Azure OpenAI, various SDKs) via its APM agents — not verified from a primary page in this pass. Flagged in gaps.md.

## Public customer proof

Case-study links shown on the page — **none specific to AI monitoring, and no quotes** (https://newrelic.com/platform/ai-monitoring):
- Domino's — "How Domino's optimizes digital ordering at global scale"
- EveryMatrix — "Fueling year-on-year growth with business insights"
- Verizon — "Reliability across massive distributed systems"
- William Hill — "Improving customer experience during peak traffic"

No AI-monitoring customer quote or metric is public on this page. See gaps.md.

## Read vs. Dynatrace

- Same "extend the platform you own" wedge, but New Relic's framing is **APM-first** — AI as another tier of the app, less of a distinct quality discipline.
- Weakest of the five on **public proof** for the AI product specifically.
- No acquisition move comparable to Dynatrace/Arize observed in this pass.
- Pricing model (New Relic's usage-based / per-user platform pricing) is a differentiator worth researching — not captured here.
