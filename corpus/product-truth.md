---
title: Product Truth — Dynatrace AI Observability
last_verified: 2026-09-15
audience: both
sources:
  - https://www.dynatrace.com/solutions/ai-observability/
  - https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability
  - https://www.dynatrace.com/hub/?filter=ai-ml-observability
  - https://docs.dynatrace.com/docs/dynatrace-intelligence
  - https://www.dynatrace.com/platform/artificial-intelligence/
  - https://www.dynatrace.com/news/blog/why-ai-agents-need-an-ai-lakehouse-in-the-modern-enterprise/
  - https://www.dynatrace.com/news/blog/evaluate-llm-and-agent-quality-in-dynatrace-ai-observability/  # blog, 2026-06-11
  - https://www.dynatrace.com/news/blog/dynatrace-intelligence-at-the-core-of-autonomous-operations/  # blog, 2026-01-28
  - https://youtu.be/64WwV4K287g  # video transcript, 2026-09-03
  - https://www.youtube.com/live/Hr7c4DTPDa0  # video transcript, 2026-09-03
---

# Product Truth

**Bottom line: Dynatrace AI Observability watches generative-AI apps across seven layers, from GPU up to business ROI, and ships pre-built integrations for the major model providers, agent frameworks, and vector databases. It runs on the same Grail data platform and Davis/Smartscape engine as the rest of Dynatrace.**

## The seven-layer observability framework

Source for all seven: https://www.dynatrace.com/solutions/ai-observability/

1. **Business Impact** — productivity gains, support ticket deflection, autonomous operations, ROI.
2. **Application Performance** — end-user experience, availability, reliability of AI-powered apps.
3. **Orchestration Layer** — chain performance, guardrails, prompt caching across frameworks.
4. **Agent-to-Agent Communication** — protocols, command execution, tool usage, multi-agent comms.
5. **Model Integrity** — token usage, cost, stability, latency, errors, resource utilization.
6. **Semantic Caches and Vector Databases** — RAG pipelines, data volume, distribution, retrieval patterns.
7. **Infrastructure Monitoring** — GPU, TPU, compute utilization, saturation, errors.

> Naming note (resolved 2026-08-28): the "Seven-Layer Observability Framework" on the solutions page is the canonical external framing. The docs page (https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability) covers the same span informally — "the complete AI stack, from foundational models and vector databases to RAG orchestration frameworks" — without naming or numbering it. Not a contradiction. Use the seven layers above, cited to the solutions page. See gaps.md → Resolved.

## Capabilities

### Cost reduction & performance
Unified customizable dashboards; intelligent detection of behavioral changes and predicted cost increases; trace-based latency reduction for agents/LLMs; A/B testing insight for model comparison; token-cost monitoring and AI coding-agent reliability. (https://www.dynatrace.com/solutions/ai-observability/)

### Trust & guardrails
Guardrail metrics for bias/misuse; hallucination and prompt-injection detection; PII-leak prevention; toxic-language detection; guardrail effectiveness analysis. (https://www.dynatrace.com/solutions/ai-observability/)

### Explainability & tracing
End-to-end request visibility across frontend, backend, orchestration, RAG, LLM, and agentic layers; log/trace and service dependency mapping; automatic root cause detection for errors in LLM chains. (https://www.dynatrace.com/solutions/ai-observability/, https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability)

### AI evaluations / LLM-as-a-judge
Continuous measurement of accuracy, relevance, grounding; model-drift and safety-issue detection; evaluation-score comparison across versions; quality-drift alerts. (https://www.dynatrace.com/solutions/ai-observability/)

The open-source **`dt-evals`** CLI runs online and offline evaluations of LLM and agent quality from GenAI traces. Install via `npm install -g @dynatrace-oss/dt-evals`; key commands are `configure`, `doctor`, and `run`. (https://www.dynatrace.com/news/blog/evaluate-llm-and-agent-quality-in-dynatrace-ai-observability/, verified 2026-09-15)

**Offline mode:** pre-release testing against fixed test sets. **Online mode:** post-deployment monitoring of sampled production traffic. CI gating: `dt-evals run --since 6h --ci` exits non-zero if any evaluator breaches its threshold, blocking a deploy on quality regression. (same source)

**15 built-in evaluators** (written source, verified 2026-09-15; resolves the video's spoken "14"): Relevance, Faithfulness, Hallucination, Answer completeness, Context relevance, Factual accuracy, Summarization quality, Conciseness, Fluency, Toxicity, Bias, PII leakage, Prompt injection, User frustration, Drift detection. Custom evaluators supported. Results appear in the AI Observability app's Prompts view with score badges, queryable via DQL as business events; alerts via Slack and email. (https://www.dynatrace.com/news/blog/evaluate-llm-and-agent-quality-in-dynatrace-ai-observability/, verified 2026-09-15)

**Judge providers for dt-evals:** OpenAI, Anthropic, Google/Vertex/Gemini, AWS Bedrock, Azure OpenAI. (same source)

**dtctl** — Dynatrace CLI for AI Agents; compatible with Claude Code, Cursor, GitHub Copilot, and MCP tools. (same source)

### Compliance & security
Full input/output documentation with data lineage; prompt storage up to 10 years; transparency dashboards for regulatory compliance; infrastructure-data monitoring for carbon-reduction initiatives. (https://www.dynatrace.com/solutions/ai-observability/)

### Metrics tracked at the model layer
Stability (success vs. failure rate), latency (response time), load (request volume), model drift (accuracy change from shifting data), data drift (input consistency), cost (token + resource consumption). (https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability)

## Agentic AI support

Monitors agent execution paths and tool invocations. Supported agent frameworks named across sources:
- OpenAI Agent SDK / OpenAI Agents (https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability, https://www.dynatrace.com/hub/?filter=ai-ml-observability)
- LangGraph (https://www.dynatrace.com/hub/?filter=ai-ml-observability)
- CrewAI (https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability)
- Google ADK (https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability)
- Amazon Bedrock AgentCore (https://www.dynatrace.com/hub/?filter=ai-ml-observability)
- Microsoft Agent Framework (https://www.dynatrace.com/hub/?filter=ai-ml-observability)
- MCP-based agent-to-agent monitoring (https://www.dynatrace.com/hub/?filter=ai-ml-observability)

## Integrations (Dynatrace Hub, AI/ML observability filter)

Source for this whole section: https://www.dynatrace.com/hub/?filter=ai-ml-observability (as of 2026-08-27; this catalog changes frequently — weekly cadence in sources.yaml)

**Instrumentation essentials:** AI Observability app, OneAgent for GenAI, OpenTelemetry for GenAI, OpenInference.

**Model providers / platforms:** OpenAI & Azure OpenAI (GPT, o1, DALL-E, ChatGPT), Amazon Bedrock, Anthropic (Haiku, Sonnet, Opus), Google Gemini, Azure AI Foundry, CrewAI. The solutions page also lists NVIDIA NIM and Google Vertex AI as supported platforms. (https://www.dynatrace.com/solutions/ai-observability/) The docs page also names Ollama. (https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability)

**AI coding-agent monitoring:** Claude Code, Gemini CLI, OpenAI Codex, GitHub Copilot SDK, OpenCode, OpenClaw.

**Vector / embedding stores:** Pinecone, LanceDB, Chroma, Milvus, Weaviate, Qdrant.

**Orchestration / prompt frameworks:** LangChain, Haystack, LlamaIndex, Langfuse.

**Infra / compute:** Google Cloud TPUs, TensorFlow Keras, NVIDIA GPU, vLLM.

**Gateway / traffic / governance:** Kong AI, LiteLLM.

**Inference:** Groq.

> Integration count (resolved 2026-08-28): there is no single canonical number. The solutions page names 6 marquee platforms, the docs page names ~12 examples plus "many more," and the Hub carries ~39 tiles that change weekly. None is wrong — different scopes. **Do not cite a specific integration count** unless you pull it fresh from the Hub and date it. Name specific integrations instead. See gaps.md → Resolved.

## The platform underneath

- **Grail** — Dynatrace's data lakehouse, positioned as a "purpose-built AI lakehouse" and "context engine" for agents: data unity, semantic store, context engine, trusted action, optimized AI economics; exabyte-scale; live business context via Smartscape. (https://www.dynatrace.com/news/blog/why-ai-agents-need-an-ai-lakehouse-in-the-modern-enterprise/)
- **Smartscape** — live dependency / business-context graph. (same)
- **Davis AI** — causal / deterministic AI for anomaly detection and root cause. Referenced as "deterministic, causation-based analysis" with topology context. (https://docs.dynatrace.com/docs/dynatrace-intelligence)

## Dynatrace Intelligence (a connected pillar, not the same as AI Observability)

"Dynatrace Intelligence" is positioned as "the industry's first agentic operations system," combining deterministic AI (causal AI + Grail + Smartscape) and agentic AI (autonomous reasoning + action under guardrails). (https://www.dynatrace.com/platform/artificial-intelligence/)

Built-in role agents (in Preview): **Developer Agent** (anomaly detection, code-level root cause, proposed fixes), **SRE Agent** (Kubernetes/cloud stabilization, ticket enrichment), **Security Agent** (threat triage, priority scoring, remediation). Natural-language interface: **Dynatrace Assist**. (https://www.dynatrace.com/platform/artificial-intelligence/, https://docs.dynatrace.com/docs/dynatrace-intelligence)

**Deterministic agents** (Bernd Greifeneder, Jan 2026): Root Cause Agent (causal AI-powered), Analytics Agent (distills Grail data), Forecasting Agent (predictive scaling), Operator Agent (orchestration and coordination). Domain-specific agents: mobile crash detection with fix suggestions, security threat monitoring and vulnerability checking. (https://www.dynatrace.com/news/blog/dynatrace-intelligence-at-the-core-of-autonomous-operations/, verified 2026-09-15)

**Maturity journey:** Automated (pre-defined workflows) → Supervised Autonomous (human-approved actions) → Fully Autonomous (independent operation). (same source)

**Named ecosystem integrations:** AWS Kiro, GitHub Copilot, ServiceNow, Azure SRE agent, Atlassian Rovo. (same source)

**Market stat:** 65% of enterprises investing in AI-driven monitoring and automation. (same source — sourced in the blog without a linked study; do not use externally without tracing the underlying report)

**Grail scale:** blog states "petabyte-scale" — note this conflicts with "exabyte-scale" in the lakehouse blog (https://www.dynatrace.com/news/blog/why-ai-agents-need-an-ai-lakehouse-in-the-modern-enterprise/). Do not cite either figure externally without resolving which is current. Logged in gaps.md.

### How it relates to AI Observability — two connected pillars, one platform

AI Observability and Dynatrace Intelligence are **not competing narratives**. They are two connected pillars that sit on the same platform:

- **AI Observability** observes *your* AI — the generative-AI apps, LLMs, and agentic workflows you build and run (the seven layers above).
- **Dynatrace Intelligence** is *Dynatrace's* AI running your operations — the agentic operations system that investigates, advises, and acts.

They share the same foundation: **Grail** (the data lakehouse / context engine), **Smartscape** (the real-time dependency and business-context graph), and **Davis AI** (causal, deterministic analysis). Traces this file collects from a GenAI app land in Grail with Smartscape topology context; that is the same data Intelligence's agents reason over. (Architecture point, per "The platform underneath" above: https://www.dynatrace.com/news/blog/why-ai-agents-need-an-ai-lakehouse-in-the-modern-enterprise/, https://docs.dynatrace.com/docs/dynatrace-intelligence, https://www.dynatrace.com/platform/artificial-intelligence/)

> **Supporting evidence (video, dated).** The Feb 2026 Dynatrace AMA "Dynatrace Intelligence: Get to know the Dynatrace agentic AI platform" (https://www.youtube.com/live/Hr7c4DTPDa0, `verified: 2026-09-03`, auto-captions) states that Dynatrace Intelligence is "fueled by a unified data lakehouse that we call Grail along with Smartscape topology" feeding both Dynatrace's agents and customer-built agents — the same platform the AI Observability app writes into. Consistent with the architecture point above.

## Try / access

Dynatrace Playground — public sandbox with sample data. (https://www.dynatrace.com/solutions/ai-observability/)

---

## From video transcripts (added 2026-09-03)

> Everything below is from auto-generated captions on published Dynatrace videos
> (official channel only). Spoken content is less precise than written docs.
> `verified: 2026-09-03`. Re-check anything marked ⚠ against a written source
> before external use. Conflicts with the rest of this file are logged in gaps.md,
> not silently merged.

### dt-evals — mechanics and workflow

Source: "How to Run LLM Evaluations with dt-evals │ AI Observability", Dynatrace,
https://youtu.be/64WwV4K287g (published 2026-09-01, presenter Josh Hendrick).
Video transcript. `verified: 2026-09-03`.

- **What it is.** Open-source evaluation tool from Dynatrace that "grades your live
  LLM traffic and sends the scores back to the platform." Ships as: a CLI on npm
  (`@dynatrace-oss/dt-evals`), a TypeScript library to embed evals in your own code,
  and deployment templates for AWS Lambda, Google Cloud Run, and Azure Functions.
  Repo: github.com/dynatrace-oss/dt-evals. (timestamp ~00:31, ~08:33)
- **How it works.** If your AI app is OpenTelemetry-instrumented you already emit
  GenAI spans — no extra instrumentation. dt-evals pulls a sample of those spans,
  **masks PII locally before anything leaves the machine**, and sends each
  interaction to a "judge LLM" (provider of your choice) that runs built-in
  evaluators per trace. Scores + reasoning are written back to Dynatrace as
  **business events (bizevents)** linked to the original trace, queryable via DQL
  (bizevent type: GenAI evaluations result). "Your production traces are the eval
  data set." (~00:44–01:19, ~05:36–06:05)
- **Setup — 3 commands.** (1) `npm install -g` the CLI. (2) `dt-evals doctor` —
  validates dependencies, checks tenant permissions, guides generating a scoped
  platform token, writes it to `.env`, asks for the environment URL. (3)
  `dt-evals configure` — names the eval, sets the AI app service, picks the judge
  provider + model, picks evaluators, sets the % of traces to evaluate per run
  (0–100 sampling for cost control) and the timeframe; writes a YAML config you
  can edit later. (~03:20–05:22)
- **Judge providers.** Anthropic, OpenAI, Gemini, Bedrock, Azure AI — "all work
  the same way." Demo used Anthropic with **Claude Haiku 4.5** as an inexpensive
  evaluator model. (~04:15–04:30)
- **Evaluator count — resolved 2026-09-15.** Written source confirms **15 built-in evaluators** (https://www.dynatrace.com/news/blog/evaluate-llm-and-agent-quality-in-dynatrace-ai-observability/, verified 2026-09-15). See "AI evaluations / LLM-as-a-judge" above for the full list. The video's spoken "14" was an undercount; the ⚠ flag is retired. gaps.md item #1 closed.
- **Continuous use.** (1) Schedule via the `cron` option (e.g. hourly, sampling
  10% of the last hour). (2) Gate deployments with the `--ci` flag — exits
  non-zero if any evaluator breaches its threshold; drops into GitHub Actions or
  any CI tool to block a deploy when quality regresses on real recent traffic.
  (~06:34–07:03)
- **Pre-built dashboard.** A dt-evals AI Observability dashboard on the Dynatrace
  Playground: evaluator-health heatmap (healthy vs degrading), worst / most
  actionable failures, per-service evaluation health, recent runs. Downloadable;
  click "Edit" on a tile to see its DQL; filterable by service, AI provider,
  judge model, metric. (~07:04–07:51)
- **AI Observability app** (shown in the same demo): out-of-the-box service-health
  dashboards (model requests, token usage, costs, errors, traffic, latency); a
  **Prompts tab** streaming input/output prompts + metadata; an **agent topology**
  view showing which service, agent, and LLMs are connected; a "View trace" jump
  to the distributed trace; an **Evaluations tab** with prior results and CLI
  install instructions. (~01:48–03:18)

### Dynatrace Intelligence — product state as of ~Feb 2026

Source: "Dynatrace Intelligence: Get to know the Dynatrace agentic AI platform | AMA",
Dynatrace, https://www.youtube.com/live/Hr7c4DTPDa0 (streamed ~Feb 2026, follow-up
to Perform 2026; Wolfgang Beer + Gabby). Video transcript. `verified: 2026-09-03`.
This is the **Intelligence** pillar — a connected pillar with AI Observability, on
the same platform (see "How it relates to AI Observability" above).

- **What it is.** Announced at Perform 2026 by CTO Bernd Greifeneder. The platform
  "evolves to a unified agentic operations system that hosts a lot of different
  agents," fueled by Grail (the data lakehouse) plus Smartscape (real-time
  dependency graph) — feeding both Dynatrace's agents and customer-built custom
  agents. It is both (a) a rebranding umbrella over existing AI (CoPilot, Davis,
  problem detection, prediction, anomaly detection, MCP) and (b) new services,
  algorithms, and components. (~02:54–09:20)
- **The "operator."** A "driver LLM" / "brain" / "core driver model" that
  **Dynatrace Assist** (the overhauled chat, formerly Davis CoPilot chat) now
  routes through. The operator has access to all MCP tools, which is how Assist
  gives cross-platform data insights. Davis CoPilot had the LLM skill + prompt +
  guardrails but **no executable tools**; the operator adds them. (~20:08–23:13)
- **Dynatrace's definition of an AI agent.** "A software system that leverages AI
  to reason, plan, act, and adapt with the goal of completing tasks on behalf of
  humans as well as other systems." Three ingredients: an LLM, a system prompt +
  guardrails, a set of executable tools. (~13:59–14:25)
- **MCP server.** Made the four core gen-AI skills (NL→DQL, DQL→NL, conversational
  recommender, document search) available as gen-AI tools; extended since with DQL
  tools, analyzer tools, and DQL execution. **Remote MCP server is now GA.**
  Dynatrace describes itself as shifting from "API-first" to "**MCP-first**" —
  ecosystem integrations happen through the MCP server. (~21:37–22:24, ~49:10–49:32)
- **Data analyzers as tools.** Example: ask Assist for a forecast + characteristic
  analysis on a custom metric; under the hood it calls a data analyzer, runs a
  Fourier transformation to find the underlying seasonality, returns the
  seasonality (e.g. "daily, 60-minute") + stats. Works on custom data and
  Dynatrace signals. (~17:58–19:23)
- **Environment-aware queries / semantic index.** For custom naming/topology,
  Assist reuses the NL→DQL "environment-aware queries" opt-in; when enabled
  Dynatrace "constantly builds a semantic index in the background" so custom
  names/fields are picked up. (~17:02–17:48)
- ⚠ **Fine-tuned NL→DQL model** "super close" to release, with "massive"
  improvements — internal tests said to beat "the latest, e.g. Opus 4.6 models."
  (~28:13–28:35) Roadmap + spoken; "Opus 4.6" naming unverified.
- **Guardrails.** "Tool execution confirmation" — step-by-step, the user confirms
  each action before an agent takes it. DQL follows standard defaults unless the
  prompt asks to exceed them. Biggest customer-raised risk is **query cost**;
  more cost control is "actively being looked into." (~23:37–25:00)
- **Root cause agent.** Runs automatically and autonomously on every problem/alarm
  Dynatrace detects — no configuration. Renders the impact graph + root-cause
  graph on the Smartscape topology in real time, plus a reasoning graph and the
  health alerts raised along the way (denoised by the agent). Findings are
  expressed in a "problem." The problem view also shows automations/remediations
  triggered by Dynatrace workflows and attaches troubleshooting-guide runbooks.
  (~49:54–53:37)
- **Problem insights / commenting** — GA ~March 2026. A workflow, API, or SDK can
  push additional markdown-rendered insights onto a problem, rendered alongside
  the root-cause info. (~54:01–55:35)
- **Agentic workflow templates** (in preview). Low-barrier automation on top of
  Dynatrace data; structure is a workflow framework with an agent/prompting step
  in the middle. Named examples: direct integration with the **Amazon SRE agent**;
  a **mobile-crash remediation agent**; a **threat-triaging agent** from
  Dynatrace's AppSec team. Small use cases: summarize problems, translate problem
  text, cluster log lines vs. yesterday, sentiment-classify user comments and
  re-ingest. (~55:59–60:46)
- **Four use-case categories** for the agentic operating system: AI assistance
  (bounded tasks), agentic apps (all Dynatrace apps use the agentic framework),
  agentic workflows (customers build their own agents), autonomous intelligence
  (self-determining engine that investigates/decides/acts with human-in-the-loop).
  (~30:10–31:17)
- **Agent-to-agent with ServiceNow.** Integrates with ServiceNow "Now Assist."
  Flow: question in ServiceNow → ServiceNow's operator identifies a
  Dynatrace-answerable question → reaches Dynatrace Intelligence → multiple
  Dynatrace agents invoked (e.g. a **data analytics agent** queries Grail) → a
  "communicator" agent on the ServiceNow side summarizes for the user. Requires
  the ServiceNow AI module; end-user surface is modules like the Service
  Operations Workspace. Same question in the Dynatrace tenant via Assist returns
  an identical answer. (~38:46–47:38)
- **IDE integration.** Developer asks their IDE assistant (Cursor, Claude Code,
  GitHub Copilot — "doesn't matter which") → through the Dynatrace MCP server →
  Dynatrace Intelligence returns logs, traces, RUM data in the IDE. MCP server
  being extended to render **interactive charts in the IDE** (Andy Grabner).
  (~33:19–36:01)
- **Dynatrace CLI.** Open source, on GitHub. Remote-controls a Dynatrace
  environment within the user's permission policies — set alerts, adjust spammy
  thresholds, run forecasts, create synthetic tests — from the IDE.
  (~36:22–37:34) ⚠ Author name spoken as "Christoph Namüller" — verify spelling.
- **"Agents are already in the platform — nothing to enable."** Easiest entry:
  open Dynatrace Assist, ask for a forecast or a problem explanation → the
  forecast agent or root-cause agent answers. (~53:37–54:01)
- **Dynatrace Assist today.** Handles multi-step questions with **agents running
  in parallel**; **self-corrects** syntax errors without user intervention; shows
  step-by-step reasoning and calls out the deterministic inputs behind its
  results. (~61:08–63:24)
