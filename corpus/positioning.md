---
title: Positioning — Dynatrace AI Observability
last_verified: 2026-08-27
audience: both  # ops/SRE and AI engineers; sections tagged inline
sources:
  - https://www.dynatrace.com/solutions/ai-observability/
  - https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability
  - https://www.dynatrace.com/news/blog/why-ai-agents-need-an-ai-lakehouse-in-the-modern-enterprise/
  - https://www.dynatrace.com/news/blog/dynatrace-intends-to-acquire-arize/
  - https://www.dynatrace.com/platform/artificial-intelligence/
  - https://www.youtube.com/live/Hr7c4DTPDa0  # video transcript, 2026-09-03
---

# Positioning

**Bottom line: Dynatrace sells AI observability as one piece of a full-stack platform — you watch your AI app in the same place you watch the servers, services, and business process it runs on. The wedge is that AI failures are not normal failures, and the teams running AI in production already run Dynatrace for everything else.**

## The category

"AI observability is the practice of collecting, analyzing, and correlating telemetry across your tech stack to understand how AI systems, agents, and LLMs behave in all environments including production." (https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability)

Dynatrace frames the product as covering "Generative AI applications, LLMs, and agentic workflows" across "performance, explainability, and compliance." (https://www.dynatrace.com/solutions/ai-observability/)

## The core problem (the pitch)

AI systems fail differently from normal software. Regular apps throw errors you can trace. "AI applications can appear functional while being inaccurate, biased, or misaligned." (https://www.dynatrace.com/news/blog/dynatrace-intends-to-acquire-arize/)

So you need to watch two things at once:
- **Is it working?** Latency, cost, errors, load, uptime — the operational signals. (https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability)
- **Is it right?** Accuracy, grounding, drift, hallucination, toxicity, PII leakage, prompt injection — the quality signals. (https://www.dynatrace.com/solutions/ai-observability/)

Dynatrace's claim is that it connects those two views, plus the infrastructure underneath and the business process on top, in one system. (https://www.dynatrace.com/solutions/ai-observability/)

## The wedge

1. **Same platform, new workload.** The buyer already runs Dynatrace for APM, infra, logs, and security. AI observability is an extension of a tool they own, not a new tool to buy, staff, and integrate. (https://www.dynatrace.com/solutions/ai-observability/)
2. **Full stack, not just the model.** Dynatrace positions a seven-layer view from infrastructure up to business impact (see product-truth.md). Competitors that only trace the LLM call miss the layers above and below.
3. **Operational + quality in one trace.** "Connect quality metrics with operational signals like latency and costs" and "investigate AI degradation across the full technology stack." (https://www.dynatrace.com/news/blog/dynatrace-intends-to-acquire-arize/)
4. **The eval gap, filled by acquisition.** Dynatrace was strong on the ops side and thinner on developer-facing evals. The intended Arize acquisition is meant to close that. See arize.md.
5. **Data layer story.** Grail is positioned as a "purpose-built AI lakehouse" / "context engine" for feeding agents trusted, real-time context. (https://www.dynatrace.com/news/blog/why-ai-agents-need-an-ai-lakehouse-in-the-modern-enterprise/)

## Audience framing

**For Ops / SRE:** AI is now a production workload with an SLO. You already page on latency and error rate; now you also page on cost spikes, quality drift, and guardrail failures — in the same dashboards and problem cards. Research cited by Dynatrace: monitoring AI systems ranks as SREs' top use case (58%). (https://www.dynatrace.com/news/blog/sre-best-practices-platform-engineering-trends/)

**For AI engineers / developers:** End-to-end tracing across "frontend, backend, orchestrations, RAG, LLM, and agentic layers," LLM-as-a-judge evaluations, version-to-version score comparison, and root cause detection inside LLM chains. (https://www.dynatrace.com/solutions/ai-observability/) The developer-facing depth (Phoenix, Arize AX, OpenInference) is the Arize side of the story — see arize.md.

## Messaging pillars (as Dynatrace states them)

- **Cost reduction & performance** — dashboards, behavioral-change detection, cost-increase prediction, trace-based latency reduction, A/B model comparison. (https://www.dynatrace.com/solutions/ai-observability/)
- **Trust & guardrails** — bias/misuse metrics, hallucination and prompt-injection detection, PII-leak prevention, toxic-language detection. (https://www.dynatrace.com/solutions/ai-observability/)
- **Explainability & tracing** — end-to-end request visibility, service dependency mapping, automatic root cause in LLM chains. (https://www.dynatrace.com/solutions/ai-observability/)
- **AI evaluations / LLM-as-a-judge** — accuracy, relevance, grounding; drift and safety detection; score comparison across versions; quality-drift alerts. (https://www.dynatrace.com/solutions/ai-observability/)
- **Compliance & security** — full input/output data lineage, prompt storage up to 10 years, transparency dashboards, carbon-reduction monitoring. (https://www.dynatrace.com/solutions/ai-observability/)

## Open positioning questions

See gaps.md. Key open one: how the Dynatrace-native AI observability and the acquired Arize products are positioned relative to each other post-close. (The AI Observability vs. Dynatrace Intelligence question is resolved — two connected pillars on one platform; see gaps.md → Resolved and product-truth.md.)

---

## From video transcripts (added 2026-09-03)

> Auto-generated captions on a published Dynatrace video (official channel).
> Spoken framing, less precise than written positioning pages. `verified: 2026-09-03`.

### Dynatrace Intelligence — the strategic framing

Source: "Dynatrace Intelligence: Get to know the Dynatrace agentic AI platform | AMA",
Dynatrace, https://www.youtube.com/live/Hr7c4DTPDa0 (streamed ~Feb 2026, Wolfgang
Beer + Gabby). Video transcript. `verified: 2026-09-03`.

- **Three phases of AI maturity (the car analogy).** Dynatrace's public way of
  meeting customers where they are:
  1. *AI amplification* — assistance + automation, "do it faster and better."
     Car: power steering, ABS, nav. You are 100% in control. (NL queries, query
     explanations, doc suggestions.)
  2. *AI augmentation* — advice + analysis; "AI goes from a tool to a team
     member." Car: adaptive cruise, lane-keep — it anticipates, advises, takes
     bounded actions; you still drive. (Data conversations, tailored onboarding,
     summaries + insights.)
  3. *AI autonomy* — "the car becomes the driver." You supervise and set the
     destination. (Incident investigation, auto-remediation, observability
     optimization.)
  "We are delivering AI use cases across this entire spectrum … meeting them
  along their own journey." Direction of travel: "an autonomous cloud." (~10:33–13:38)
- **Deliver the value in the context of the user.** The pitch is that Dynatrace
  data shows up in the system the user already works in — the IDE (Cursor, Claude
  Code, Copilot), ServiceNow (Now Assist), Slack for incident commanders — not in
  a separate Dynatrace UI the user has to learn. "We are not asking people to log
  in to a different tool." Cross-platform, agent-to-agent, "second-level
  inception where agents talk to each other." (~32:08–35:39, ~47:38–48:24)
- **"MCP-first" as the integration story.** "The first thing we did when the
  platform was there was be an API-first platform… now being an MCP-first
  platform, we can integrate with all of these different tools in the ecosystem
  because the integrations happen through the MCP server." Remote MCP server is
  GA. (~49:10–49:32)
- **Trust framing.** "Deterministic AI" — every Assist response carries "the
  evidence and the context of how we got to our responses every single step of
  the way," so users can double-check. Guardrails = step-by-step tool-execution
  confirmation. Careful, staged rollout given sensitive data. (~15:31–15:54,
  ~23:37–24:23)
- **Resources / instruction files as "onboarding a new team member."** Customers
  will be able to attach custom domain knowledge (undocumented DQL syntax, "we do
  things a little special here") that both Assist and external agents use —
  "onboard Dynatrace Assist as an additional team member" with your tribal
  knowledge. (~25:32–29:43)

> Note: this AMA describes the **Intelligence** pillar (Dynatrace's AI running
> your operations) on its own terms. That is not a separate or competing story
> from AI Observability (observing your AI) — the two are connected pillars on
> one platform (Grail, Smartscape, Davis). See product-truth.md and gaps.md →
> Resolved.
