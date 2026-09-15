---
title: Competitor — Datadog (LLM / Agent Observability)
last_verified: 2026-08-28
audience: both
sources:
  - https://www.datadoghq.com/product/llm-observability/
  - https://docs.datadoghq.com/llm_observability/
---

# Datadog — LLM / Agent Observability

**Bottom line: Datadog folds AI monitoring into the platform its buyers already run, and has pushed the story from "LLM Observability" toward "Agent Observability" — offline experimentation plus production monitoring in one place. It is the closest structural analog to Dynatrace's pitch: same platform, new workload, ops signals and quality signals in one trace.**

## Positioning

Headline: "Ship AI agents faster, with confidence." (https://www.datadoghq.com/product/llm-observability/)

Product description: "Evaluate, improve, and trace your AI agents with offline experimentation and production observability in one platform." Positioned as moving teams "from prototype to production faster in one platform" by validating quality before release and running with "enterprise-grade tracing and security." (https://www.datadoghq.com/product/llm-observability/)

Docs definition: "Monitor, troubleshoot, and evaluate your LLM-powered applications, such as chatbots. You can investigate the root cause of issues, monitor operational performance, and evaluate the quality, privacy, and safety of your LLM applications." (https://docs.datadoghq.com/llm_observability/)

> Naming note: the marketing URL still reads `/product/llm-observability/` but the page content and docs increasingly use "Agent Observability." Treat "LLM Observability" and "Agent Observability" as the same Datadog product for now; re-verify the canonical name on next refresh. Flagged in gaps.md.

## What they claim to observe

Operational:
- Token usage and latency; error rates and failures; cost monitoring (https://www.datadoghq.com/product/llm-observability/)
- End-to-end LLM tracing — "trace every agent step"; execution graph inspection; tool decision tracking (https://www.datadoghq.com/product/llm-observability/)
- Each request represented as a trace; spans for "each choice made by an agent or each step of a given workflow"; individual LLM inference spans capture "tokens, error information, and latency" (https://docs.datadoghq.com/llm_observability/)
- Root cause analysis "across full application stack"; outlier detection across span name, workflow type, and pattern topics (https://www.datadoghq.com/product/llm-observability/, https://docs.datadoghq.com/llm_observability/)
- User session correlation (https://www.datadoghq.com/product/llm-observability/)

Quality / safety:
- Quality scores and drift detection; response accuracy (https://www.datadoghq.com/product/llm-observability/)
- Offline and online evaluations; custom and built-in evaluators; hallucination detection (https://www.datadoghq.com/product/llm-observability/)
- Prompt injection detection; PII / sensitive-data scanning and redaction (https://www.datadoghq.com/product/llm-observability/, https://docs.datadoghq.com/llm_observability/)
- "Automated hierarchical topic clustering" via a Patterns feature (https://docs.datadoghq.com/llm_observability/)

Experimentation / dev loop:
- Build datasets from production traces; golden dataset versioning (https://www.datadoghq.com/product/llm-observability/)
- Run experiments comparing prompts, models, configurations (https://www.datadoghq.com/product/llm-observability/)
- Human review and annotation workflows (https://www.datadoghq.com/product/llm-observability/)

Governance:
- Role-based access control (https://www.datadoghq.com/product/llm-observability/)

## Named integrations

Source: https://www.datadoghq.com/product/llm-observability/ unless noted.

- **Model providers:** Anthropic, OpenAI, Gemini, Vertex AI, Bedrock, LiteLLM. Docs lists OpenAI, LangChain, AWS Bedrock, Anthropic as auto-instrumented by the Python SDK "without requiring code modifications." (https://docs.datadoghq.com/llm_observability/)
- **Agent / orchestration frameworks:** LangChain, CrewAI, Pydantic (Pydantic AI), Strands Agents
- **Infra / platforms:** Vercel, AWS, Azure, Google Cloud, Kubernetes
- **SDKs / protocols:** Python, Node.js, Java, OpenTelemetry, HTTP API

## Public customer proof

Quotes (https://www.datadoghq.com/product/llm-observability/):
- **Twine** (AI cybersecurity): "Datadog LLM Observability gives us complete visibility into our agents' reasoning so we can reduce cost, improve reliability, and ship with confidence."
- **Fintool** (AI financial copilot): "We've improved response accuracy and reduced latency, ensuring faster, more reliable insights for our customers."
- **AppFolio** (AI Property Manager): "Helped us ensure high model performance and quality, and allowed us to expand functionality quickly and safely."

Metrics attributed to customers on the page (not individually attributed to a named company in what was captured): "400% faster MTTR," "40% lower token usage per task," "15% faster deployment." (https://www.datadoghq.com/product/llm-observability/) — see gaps.md; confirm which customer each maps to before using.

## Read vs. Dynatrace

- Same core wedge as Dynatrace: one platform, ops + quality together, buyer already owns it.
- Datadog leads harder on the **developer / pre-production loop** (experiments, datasets, golden sets) natively — the capability Dynatrace is buying with Arize.
- Datadog has **named customer quotes with an AI-observability attribution**; Dynatrace's public AI-observability quotes are fewer (TELUS, FreedomPay). See proof-points.md.
- Dynatrace counters with the **infrastructure-to-business-impact span** (seven layers) and Grail as an AI data layer — Datadog's story is more centered on the agent trace.
