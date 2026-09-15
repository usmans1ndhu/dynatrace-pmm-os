---
title: Competitor — LangSmith (LangChain)
last_verified: 2026-08-28
audience: ai-engineers  # developer-first; less of an ops/SRE story
sources:
  - https://www.langchain.com/langsmith
---

# LangSmith — Agent & LLM Observability Platform

**Bottom line: LangSmith is the developer-loop tool from the LangChain team — trace, eval, and monitor agents, framework-agnostic but strongest with LangChain/LangGraph. It competes with the Arize half of Dynatrace's story, not the ops half. Big logo wall, no public quantified case studies.**

## Positioning

Headline: "LangSmith: Agent & LLM Observability Platform." Tagline: "Know what your agents are really doing." (https://www.langchain.com/langsmith)

Description: "LangSmith Observability gives you complete visibility into agent behavior. Trace your preferred framework or integrate LangSmith with any agent stack using our Python, Typescript, Go, or Java SDKs." (https://www.langchain.com/langsmith)

## What they claim to observe

Source: https://www.langchain.com/langsmith

**Tracing:**
- "See exactly what your agent is doing step by step. Pinpoint the issues hurting latency, cost, and response quality."
- Native tracing for popular agent frameworks and OpenTelemetry
- Message threading for multi-turn chat

**Monitoring:**
- "Get a real-time view of how your agents are performing"
- Cost tracking
- "Online LLM-as-judge and code evals"
- Tool and agent trajectory monitoring
- Webhook and PagerDuty alerts

**Insights:**
- "Automatically analyze and cluster your traces to detect usage patterns"
- Unsupervised topic clustering; templates for error analysis; executive summary with key findings

**SmithDB:**
- "Purpose-built database for agent traces with sub-second performance"
- JSON key-path filtering and trajectory queries
- Self-hosting option for data residency

## Named integrations

Source: https://www.langchain.com/langsmith

- **Frameworks / libraries:** LangChain, LangGraph, DeepAgents, OpenAI SDK, Anthropic SDK, Vercel AI SDK, LlamaIndex, OpenTelemetry
- **SDKs:** Python, TypeScript, Go, Java
- **Infra / platforms:** AWS, GCP, Azure, Kubernetes, Postgres, object storage

## Public customer proof

**No attributed quotes, metrics, or case studies** on the page. It shows 25+ customer logos, including: Vanta, Clay, Rippling, Lyft, Gong, Harvey, Abridge, Autodesk, Bristol Myers Squibb, Workday, Cisco, Monday.com, Nvidia, Bridgewater, ServiceNow, Coinbase, Rakuten, Elastic, Uber, Zip. (https://www.langchain.com/langsmith)

Note: Autodesk appears on both this logo wall and in Dynatrace's Dynatrace Intelligence quote (proof-points.md) — same company, different tools; not a conflict.

See gaps.md — LangChain has published deeper LangSmith case studies elsewhere (customer stories page) not fetched in this pass.

## Read vs. Dynatrace

- **Not a full-stack ops competitor.** No infrastructure, no APM, no business-impact layer. Compares to Dynatrace's AI Observability only on trace + eval.
- Directly overlaps the **Arize acquisition** (arize.md): dev-loop tracing + evals + a purpose-built trace database (SmithDB vs. Arize's, vs. Dynatrace's Grail).
- Strength: incumbency with LangChain-based teams; framework-native depth.
- Weakness for enterprise ops buyer: no operational correlation to infra, cost-at-the-business-process level, or root cause across the stack.
