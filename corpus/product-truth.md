---
title: Product Truth — Dynatrace AI Observability
last_verified: 2026-09-16
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
  - https://www.dynatrace.com/knowledge-base/ai-observability/  # knowledge base, 2026-03-17
  - https://www.dynatrace.com/knowledge-base/ai-agent-observability/  # knowledge base, 2026-06-29
  - https://youtu.be/64WwV4K287g  # video transcript, 2026-09-03
  - https://www.youtube.com/live/Hr7c4DTPDa0  # video transcript, 2026-09-03
  - FY27 JuneRally - SE AI Pitch deck .pdf  # internal SE deck, CONFIDENTIAL, verified 2026-09-16; back every claim with a public source before external use
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

Cost and performance monitoring is powered by Davis AI with SLOs, problem alerts, and predictions. If model latency spikes you can see which users were affected; if token consumption is trending toward overspend you see it before month-end, not after. (internal deck, 2026-09-16)

**Model version comparison / A/B testing:** Dynatrace lets you compare model versions side by side — latency, token usage, cost, error rates, output quality — and run A/B tests across model variants. When OpenAI or Anthropic releases a new version or deprecates an old one, you can validate the impact before it surprises you. (internal deck, 2026-09-16)

### Trust & guardrails
Guardrail metrics for bias/misuse; hallucination and prompt-injection detection; PII-leak prevention; toxic-language detection; guardrail effectiveness analysis. (https://www.dynatrace.com/solutions/ai-observability/)

Guardrail monitoring surfaces guardrail outcomes — violations that your model provider detects and reports (hallucinations, PII leakage, toxicity) — so compliance, security, and engineering teams can monitor them, track trends, and alert on them. Dynatrace is the visibility layer, not the AI quality engine itself. (internal deck, 2026-09-16)

### Explainability & tracing
End-to-end request visibility across frontend, backend, orchestration, RAG, LLM, and agentic layers; log/trace and service dependency mapping; automatic root cause detection for errors in LLM chains. (https://www.dynatrace.com/solutions/ai-observability/, https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability)

**Multi-modal Agent Explainability & tracing:** Traces the full execution path of agents — every decision point, every tool invocation, every model call — across frameworks: Amazon AgentCore, Amazon Strands, Google ADK, LangChain, OpenAI Agents, MCP. Follow any request from first user input to agent's final action. (internal deck, 2026-09-16)

### AI evaluations / LLM-as-a-judge
Continuous measurement of accuracy, relevance, grounding; model-drift and safety-issue detection; evaluation-score comparison across versions; quality-drift alerts. (https://www.dynatrace.com/solutions/ai-observability/)

**AI Evaluations** is listed as a NEW capability in the FY27 campaign messaging (v3.0, 2026-07-07): LLM-as-judge for faithfulness, hallucination, toxicity, and **agent trajectory support** (new evaluation type, confirms agents-as-a-whole trajectory can be evaluated, not just individual LLM calls). (internal messaging doc)

The open-source **`dt-evals`** CLI runs online and offline evaluations of LLM and agent quality from GenAI traces. Install via `npm install -g @dynatrace-oss/dt-evals`; key commands are `configure`, `doctor`, and `run`. (https://www.dynatrace.com/news/blog/evaluate-llm-and-agent-quality-in-dynatrace-ai-observability/, verified 2026-09-15)

**Offline mode:** pre-release testing against fixed test sets. **Online mode:** post-deployment monitoring of sampled production traffic. CI gating: `dt-evals run --since 6h --ci` exits non-zero if any evaluator breaches its threshold, blocking a deploy on quality regression. (same source)

**15 built-in evaluators** (written source, verified 2026-09-15; resolves the video's spoken "14"): Relevance, Faithfulness, Hallucination, Answer completeness, Context relevance, Factual accuracy, Summarization quality, Conciseness, Fluency, Toxicity, Bias, PII leakage, Prompt injection, User frustration, Drift detection. Custom evaluators supported. Results appear in the AI Observability app's Prompts view with score badges, queryable via DQL as business events; alerts via Slack and email. (https://www.dynatrace.com/news/blog/evaluate-llm-and-agent-quality-in-dynatrace-ai-observability/, verified 2026-09-15)

**Judge providers for dt-evals:** OpenAI, Anthropic, Google/Vertex/Gemini, AWS Bedrock, Azure OpenAI. (same source)

**dtctl** — Dynatrace CLI for AI Agents; compatible with Claude Code, Cursor, GitHub Copilot, and MCP tools. (same source)

### Compliance & security
Full input/output documentation with data lineage; prompt storage up to 10 years; transparency dashboards for regulatory compliance; infrastructure-data monitoring for carbon-reduction initiatives. (https://www.dynatrace.com/solutions/ai-observability/)

### Metrics tracked at the model layer
Stability (success vs. failure rate), latency (response time), load (request volume), model drift (accuracy change from shifting data), data drift (input consistency), cost (token + resource consumption). (https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability)

## AI agent observability — risks, pillars, and implementation

Source: https://www.dynatrace.com/knowledge-base/ai-agent-observability/, last updated 2026-06-29, verified 2026-09-16.

**Definition.** AI agent observability enables monitoring, tracing, and explanation of how AI agents make decisions by capturing prompts, reasoning chains, outputs, and contextual data.

**Four risks of unobservable agents:**
- Business: incorrect responses damage revenue and customer trust
- Operational: hallucinations and unexpected decision loops degrade performance
- Compliance: missing audit trails create regulatory exposure
- Cost: untracked token usage and model consumption create scaling problems

**Three core pillars:**
1. Telemetry — captures prompts, responses, and tool calls via OpenTelemetry and OpenLLMetry standards
2. Behavioral Monitoring — identifies unsafe actions, hallucinations, and policy deviations; measures latency, throughput, accuracy, and cost
3. Governance — supports audit trails and analyzes guardrail metrics

**Five-step implementation approach:** instrument early → define success metrics → correlate signals → automate oversight → unify monitoring platforms. (same source)

**Named frameworks:** Amazon Bedrock Agent Core, LangChain, OpenAI Agents SDK, Google ADK, MCP-based agents. (same source)

> Note: The KB page also presents a **6-layer framework** (Application, Orchestration, Agentic, Model and LLM, Semantic Search and Vector Database, Infrastructure) that differs from the **7-layer framework** on the solutions page (which adds Business Impact as the top layer and Agent-to-Agent Communication as a distinct layer). The solutions page framing is the resolved canonical external framing — do not cite the KB's 6-layer version externally until aligned. Flagged in gaps.md.

## AI Observability App — named capabilities

Source: FY27 campaign messaging v3.0 (internal, 2026-07-07). These are the named product surfaces:

**AI Observability App — 4 tabs:**
1. Overview — discovery and validation
2. Service health — monitoring and alerting
3. Explorer — slicing and analysis
4. Prompt — manage, test, govern

**Platform differentiators named in the messaging doc:**
- Dynatrace Intelligence (no point solution has this)
- Grail (100% data captured / compliance backbone)
- Smartscape (agent topology visualization)
- OpenTelemetry / OpenLLMetry native (framework-agnostic ingestion)

**NEW capabilities (listed as new in the FY27 messaging):**
- Agent Topology and Dependency
- Prompt Debugging and Management
- AI Coding Agent Monitoring (GitHub Copilot, Claude Code) — confirming this is a named, marketed capability
- RUM (Real User Monitoring) for AI workloads
- AI Evaluations with agent trajectory support (see evals section above)

**In PREVIEW:**
- Agentic Workflows

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

## Dynatrace Assist — rebuilt from the models up

Source: internal SE deck, 2026-09-16 (internal; back with public sources before external use). Cross-references AMA video transcript verified 2026-09-03.

**What it is now.** Rebuilt from "chatbot" to "thinking partner." Four upgrades shipped (deck, 2026-09-16):
1. **Anthropic foundation models** — driver LLM upgraded to Claude Sonnet 4.6, hosted on Amazon Bedrock. Stronger multi-step reasoning, better tool use, more reliable answers on complex investigations when agentic mode is enabled.
2. **Skills knowledge base** — curated knowledge base following the Anthropic Claude Agent Skills standard. Know-how that lived in Dynatrace engineers' minds is now in the product (troubleshooting patterns, best practices, domain expertise). 28 available skills; not all are available in Assist — some are CLI-only. New skills added regularly. Makes Assist agent-ready: same skills can be consumed by AI agents running autonomously via dtctl or MCP servers.
3. **Purpose-built DQL model** — retired the RAG approach for NL→DQL in favor of a fine-tuned model trained on "hundreds of thousands of real DQL examples." Significantly more reliable natural-language-to-DQL in Assist, Notebooks, Dashboards, and via MCP servers. (Resolves the ⚠ from video transcript; the "close to release" claim in the AMA is now "already available" per the deck — flagged in gaps.md video item #2.)
4. **Streamlined chat interface** — new side panel (pinned or floating); no longer a modal. Context stays on screen while Assist sits alongside you.

**Single-flow experience:** Use Assist side-by-side with Dynatrace apps to analyze, drill down, and act without losing context. Assist automatically understands what you are viewing and grounds answers in the active app.

## Dynatrace Intelligence — current status and roadmap

### What's GA (as of deck date, 2026-09-16)

Source: internal SE deck, page 76, 2026-09-16. Internal; verify GA status against public docs before citing externally.

| Capability | Status | Notes |
|---|---|---|
| Intelligence Foundation (consolidation of Davis Root-Cause Agent, Forecast Agent, CoPilot, Davis, Prediction, Anomaly Detection, MCP) | GA | Included with 3rd Gen SaaS tenants |
| Agents: Davis Root-Cause Agent, Forecast Agent, Grail Query Agent, Help Agent | GA | Available through Remote MCP and Assist |
| Dynatrace Assist (agentic chat, plans, reasons, uses tools) | GA | — |
| Dynatrace MCP Server | GA | Each 3rd Gen SaaS Tenant auto-enabled with remote MCP server |
| dt-ctl CLI | Open source | For humans and AI agents alike |
| Dynatrace for AI (skills, prompts, instructions for building agents on Dynatrace context) | Open source | — |
| Agentic Workflows (ready-made workflow templates) | Preview | Not GA; governed by preview terms |

### Autonomous SRE Agent — ROADMAP, not shipped

> **Do not present this as a current capability.** The deck explicitly labels this as a roadmap item.

V1 ships as a ready-made agentic workflow with deep reasoning for root cause, impact assessment, and actionable remediation recommendations — supporting both human-led and fully autonomous operations at production scale. Framed as replacing the "2am on-call" manual triage workflow. Named competitors this closes the gap against: Resolve, Rootly, Traversal (and implicitly Datadog). (internal deck, 2026-09-16)

### Cloud SRE Agents (multicloud)

Orchestrates AWS, Azure, and Google SRE agents to automatically resolve and remediate incidents across multicloud environments. Routes identified issues based on configurable rules; centralizes findings; provides a single audit trail for autonomous operations. Also integrates with the **AWS DevOps agent** for end-to-end automated root cause analysis. (internal deck, 2026-09-16)

### Dynatrace MCP Server — security use case (4-step workflow)

1. Problem detected → triggers Dynatrace MCP Server
2. MCP Server queries Grail for CVE details + runs Causal AI root-cause analysis
3. GitHub is notified with full production context
4. GitHub Copilot auto-generates a code fix — no manual triage needed

Described as "the central hub connecting Dynatrace's observability intelligence to your developer tools." (internal deck, 2026-09-16)

### Visual agent builder (no-code)

A no-code agent builder based on workflows, triggers, schedules, and approvals. Customers can build custom agents as agentic workflows — for example, response agents for specific vulnerabilities, ITSM integration, Kubernetes/cloud scale, or code fixes. Also ships ready-to-use agentic workflow templates as a starting point. (internal deck, 2026-09-16)

### dtctl — developer and AI agent CLI

Ships with a built-in skill file that teaches AI assistants how to operate a customer's Dynatrace environment, so agents can query logs, check SLO status, and trigger workflows out of the box. Result: hours of configuration become a single command; AI agents can act on Dynatrace autonomously.

**Customer anecdote (internal deck, spoken):** One Dynatrace customer used dtctl + Claude Code + GitHub to rewrite a 20+ year old app in a few weeks, correlating pieces of code with live transactional data to remove dead code and improve performance. Not attributable externally — no customer name or public source; treat as directional.

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
- ~~⚠ **Fine-tuned NL→DQL model**~~ **Resolved 2026-09-16:** The AMA (~28:13) described this as "super close" to release. The SE pitch deck (2026-09-16) lists it as "already available" — "replaced RAG approach with purpose-built finetuned model trained on hundreds of thousands of real examples." The video's mention of beating "Opus 4.6 models" is inconsistent with the confirmed model (Claude Sonnet 4.6); do not repeat the "Opus 4.6" name externally. See gaps.md video item #2.
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
