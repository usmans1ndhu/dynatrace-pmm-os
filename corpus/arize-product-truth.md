---
title: Arize — Product Capabilities Reference
last_verified: 2026-10-08
audience: internal
sources:
  - https://arize.com/  # product overview
  - https://arize.com/products/ax/  # AX platform
  - https://arize.com/products/alyx/  # Alyx agent
  - https://arize.com/products/adb/  # ADB datastore
  - https://arize.com/products/self-hosted/  # self-hosted
  - https://arize.com/phoenix/  # Phoenix open source
  - https://docs.arize.com/arize  # documentation
  - https://arize.com/customers/  # customer proof points
  - https://arize.com/pricing  # pricing and tiers
  - https://arize.com/integrations  # integrations catalog
---

# Arize — Product Capabilities Reference

**Bottom line: Arize is an AI engineering platform built for teams that own the full agent lifecycle — from development and evaluation through production monitoring and continuous improvement. The core offering is Arize AX (managed SaaS or self-hosted). The open-source foundation is Phoenix. The connecting standard is OpenInference (OTel-compatible). The AI engineering agent within the platform is called Alyx. The purpose-built datastore is ADB.**

---

## Platform overview

**Tagline:** "The agent observability and evaluation platform. Turn production signals into continual learning so your agents improve with every interaction."

**Scale (self-reported):**
- 1 trillion spans processed
- 1 billion evals per year
- 5 million downloads per month (combined Phoenix + OpenInference)

**The four-stage workflow:**
1. **Observe** — Trace everything; see what the agent actually did
2. **Evaluate** — Score whether the agent is getting better or worse
3. **Learn** — Build datasets and run experiments to test fixes
4. **Improve (via Signal + Alyx)** — Surface issues automatically; go from finding to fix without manual trace review

---

## Arize AX — Managed AI Engineering Platform

**URL:** https://arize.com/products/ax/
**Available as:** Managed SaaS (Free/Pro/Enterprise) or Self-Hosted (Enterprise only)

### Core capability areas

**Signal**
- Built-in worker that scans traces on a schedule (every 6 hours by default; configurable 3 hours to monthly)
- Groups recurring failure patterns into ranked **issues**
- Each issue contains: overview of failure pattern, trace evidence, proposed fix (prompt/code/config/eval change)
- Enterprise: attaches to GitHub repo, opens fix PRs automatically; choose AI provider (Anthropic/Claude Code, OpenAI/Codex, or Cursor)
- Free: 10 issues/month. Pro: 25 issues/month. Enterprise: unlimited

**Managed Agents**
- Enterprise only (currently included at no extra charge with Signal)
- Pre-built templates:
  - Debug & Fix: "Investigate failing traces," "Fix a bug in your repo"
  - Incident & On-Call: "SRE / On-Call," "Incident Commander," "Triage a monitor alert"
  - Monitor & Optimize: Cost Agent, "Recurring health check"
  - Coming soon: Security agent (PII/secrets/prompt-injection), Prompt Optimization agent, Eval/Quality agents
- Modes: Session (one-off with steering) or Automation (cron schedule or metric threshold trigger)
- Harness options: Claude Code, Codex, Cursor (more planned)
- Sandbox: Arize-managed Kubernetes (Daytona and Vercel planned)
- Outputs: investigation markdown, eval labels, dataset rows, PRs (when repo write access granted)
- **Code changes arrive as PRs — Managed Agents do not deploy to production**

**Swarm Observability**
- Tracks status and performance across an entire agent swarm in real time
- Enterprise only

**Evaluation**
- Evaluator types: LLM-as-a-Judge, Agent-as-a-Judge, code evaluators, human annotations
- **Agent-as-a-Judge (Enterprise):** Agent explores exported trace data and scores from plain-language instructions; no template variable mapping required. Results appear on traces, in dashboards, and in task run history. Creates versioned, reusable evaluators.
  - Supported harnesses: Claude Code (today); Cursor, Codex, Hermes, OpenClaw (coming soon)
- Evaluator alignment: calibrates automated scores against human judgment; Alyx can assist
- Third-party eval libraries: Ragas, Microsoft Azure AI Evaluation, NVIDIA RAG Metrics via Ragas
- Online eval tasks: configurable date range, query filter, sampling rate

**Experiment**
- Three types:

| Type | Tests | Runs on | Multi-step/tools |
|---|---|---|---|
| Playground experiment | A single prompt | Arize-hosted | No |
| Code experiment | A Python function | Your Python runtime | Yes |
| Agent experiment | A deployed remote agent | Your hosted infrastructure | Yes |

- **Remote Agent Experiments:** Run a dataset against any customer-hosted remote agent. Accepts any framework — LangGraph, CrewAI, OpenAI Agents SDK, Claude Agent SDK, or custom. Endpoint must accept/return JSON via POST. Request templating via `{{dataset.<field>}}` syntax. W3C `traceparent` header sent for trace linking.
- Results: full request/response, nested traces, failure details, evaluator scores, cross-experiment comparison

---

## Alyx — AI Engineering Agent

**URL:** https://arize.com/products/alyx/
**Tagline:** "Plans and runs multi-step AI engineering workflows on its own"
**Positioning:** Same orchestration approach as Cursor and Claude Code, applied to AI engineering

### Where it appears
- **Home view:** Full-page chat with history and suggested workflows
- **Side chat:** Opens over any page with Cmd+L (macOS) / Ctrl+L (Windows/Linux)
- **Surfaces:** Trace slideover, Prompt Playground, Eval and Task Builders, Traces search bar (AI Search), Traces page, Datasets/Experiments, sessions, labeling queues, dashboards, Signal

### Core use cases
- **Failures to evaluation coverage:** Finds recurring failures in traces, diagnoses, proposes reusable evaluator with evaluation task, data sources, and variable mappings
- **Prompt comparison:** Creates prompt variants, runs experiments against dataset with attached evaluation, analyzes results; generates synthetic examples, refines prompts, saves to Prompt Hub
- **Custom views:** Generates custom layouts for traces, sessions, annotation-queue records from plain-language description
- **Evaluator alignment:** Selects annotation columns, sets up agreement checks, runs experiments, iterates on evaluator template

### Full capability areas
- Signal insights: reads issues, links to evidence/traces, checks for open PRs
- Trace search: lists traces, inspects spans, inputs/outputs/errors, builds semantic and multi-span filters
- Aggregations: counts, averages, sums, percentages, latency, cost, token usage with grouping and sorting
- Evaluators: creates/updates LLM-as-a-judge and code evaluators; configures classification choices and data sources
- Evaluation tasks: sets up project or dataset tasks; supports historical runs and skip-previously-evaluated
- Agent-as-a-judge (Enterprise): proposes agent-based evaluators and tasks
- Datasets: lists/previews, inspects columns, filters rows, creates/appends from spans or synthetic examples
- Prompts and experiments: reads/loads/edits prompts; runs background experiments; compares scores/outputs/token usage
- Annotations and labeling queues: creates labels/scores, annotates spans, creates/edits queues with reviewer instructions
- Dashboards: creates dashboards from scratch or templates; time series, statistic, bar-chart, text, and pivot-table widgets
- Setup and documentation: finds projects/assets, helps with API keys, instrumentation, AX CLI

### Model selection
- Arize-managed: Azure OpenAI, Anthropic
- Bring your own: OpenAI, Anthropic, Gemini, Azure OpenAI, Vertex AI, AWS Bedrock, NVIDIA NIM, OpenAI-compatible custom endpoints

### Long-term memory
- Remembers: role and preferences, goals and progress, project/asset learnings, team conventions
- Does NOT keep: transcripts, IDs, URLs, live metrics
- Per-user, scoped to each space

---

## ADB — AI-Native Datastore

**URL:** https://arize.com/products/adb/
**Tagline:** "AI-native datastore for observability and evaluation data"

### Core capabilities
- Unifies observability and evaluation data in open formats (Apache Iceberg)
- Zero-copy access across AI and data stack
- Cloud-backed with smart active caching (hot/cold storage tiers)
- Self-reported: up to 100x lower cost than other platforms
- Store and query years of data

### Performance benchmarks (self-reported)
- Query latency p95: <1 second
- Query 1 billion GenAI traces: 0.8 seconds
- Competitor A: 3.2s | Competitor B: 9.1s | Competitor C: 2.1s

### Architecture
- Iceberg-backed open table format
- Compute-storage separation
- OTEL ingest + real-time streaming
- Connects natively to BigQuery, Databricks, or Snowflake via DataFabric (Enterprise)
- No data exports or duplication required

### Deployment
- Cloud-backed within Arize AX (SaaS)
- Self-hosted Arize AX (separate product, Enterprise)

---

## Self-Hosted Arize AX

**URL:** https://arize.com/products/self-hosted/
**Availability:** Enterprise only

### Included capabilities
- Same core platform as SaaS: agent/LLM observability, tracing, online/offline evaluations, prompt optimization, datasets/experiments, Alyx AI assistant
- Uses ADB (AI-native OLAP database)
- Data, authentication, APIs, and UI inside your infrastructure

### Deployment options
- **Cloud platforms:** GCP, Azure, AWS, Oracle Cloud
- **Kubernetes environments:** OpenShift, K3s, Rancher, Tanzu, and other Kubernetes distributions
- **Connectivity modes:**
  - Connected: direct outbound access to Arize distribution services
  - Semi-restricted: limited outbound through proxy or firewall allowlist
  - Air-gapped: no outbound connectivity; artifacts transferred through offline process (private container registry + internal artifact repo)
- Reference Terraform templates for GCP, Azure, AWS

### Infrastructure requirements
- Kubernetes cluster (GKE, AKS, EKS, OpenShift, K3s, Rancher, Tanzu)
- Persistent block storage
- Object store: GCS, S3-compatible, or Azure Blob storage

### Security and compliance
- SOC 2 Type II
- ISO 27001
- HIPAA-ready
- Air-gapped deployment for regulated and classified environments
- SAML 2.0 SSO: Okta, Entra, OneLogin, Ping
- RBAC role mapping through IdP
- Arize does NOT store customer data in this model

### Cost model
- Predictable infrastructure costs with reserved instances and enterprise agreements
- No usage-based platform pricing

---

## Phoenix — Open-Source AI Observability

**URL:** https://arize.com/phoenix/
**License:** ELv2
**GitHub:** 10k+ stars, 346 forks

### Community metrics
- 3M+ monthly downloads
- 10k+ GitHub stars
- 7k+ community members
- 22M+ monthly OTel instrumentation downloads

### Core features

**Tracing**
- Step-by-step views of application runs: model calls, retrieval, tool use, custom logic
- Accepts traces over OpenTelemetry (OTLP)
- Auto-instrumentation: LlamaIndex, LangChain, DSPy, Mastra, Vercel AI SDK, OpenAI, Bedrock, Anthropic
- Languages: Python, TypeScript, Java

**Evaluation**
- LLM-based evaluators (pre-built and custom)
- Code-based checks
- Human annotations in UI
- Dataset evaluators for automated experiment testing
- Integrations: Phoenix evals, Ragas, DeepEval, Cleanlab

**Prompt engineering**
- Prompt Management: version, store, deploy prompts
- Prompt Playground: compare prompts and models side by side
- Span Replay: replay LLM calls with different inputs
- Prompts in Code: sync prompts across environments via SDK

**Datasets and experiments**
- Create datasets from traces, uploaded code, or CSV files
- Run experiments to compare application versions on same inputs
- Attach reusable dataset evaluators as automated test cases

**PXI (built-in AI agent)**
- "Talk with your traces" — investigate issues, add annotations, run experiments
- Phoenix skills for coding agents

### Deployment
- Local: `uvx arize-phoenix serve` (at `http://localhost:6006`)
- Docker: pull and start container
- Kubernetes: Helm deployment
- Cloud: Phoenix capabilities within Arize AX managed platform

### Quick start for coding agents
- `uvx arize-phoenix serve`
- `npx -y @arizeai/phoenix-cli setup`
- `px setup` — supports Claude Code, Codex, Cursor, OpenCode

**Phoenix vs. AX distinction (from Arize's own messaging):**
> Phoenix is a product in its own right — local developer tool, shared internal platform, or permanent production system. Arize AX provides a different operating model: commercial support, managed production workflows at scale, continuous production monitoring through Signal, and enterprise governance. Teams can use Phoenix, AX, or both.

---

## OpenInference — Open Tracing Standard

**URL:** https://github.com/Arize-ai/openinference
**License:** Apache-2.0
**Stats:** ~1.3k stars, 346 forks, 2,360 commits

### What it is
- Open-source conventions and plugins complementary to OpenTelemetry
- Adds AI-specific semantic conventions on top of OTel tracing
- Works with any OpenTelemetry-compatible backend
- Natively supported by Phoenix and Arize AX
- OTel formally accepted code grant from Arize in June 2026 — now being added incrementally to OTel GenAI instrumentation project

### Supported languages and instrumentations

**Python:** Agno, AG2, OpenAI, OpenAI Agents, Claude Agent SDK, LlamaIndex, DSPy, AWS Bedrock, LangChain, MCP, MistralAI, Portkey, Guardrails, VertexAI, CrewAI, Haystack, LiteLLM, Groq, Instructor, Anthropic, BeeAI, Google GenAI, Google ADK, Autogen AgentChat, PydanticAI, smolagents, Pipecat, Strands Agents, Together AI, Ollama, Cohere

**TypeScript/JavaScript:** AWS Bedrock, Bedrock Agent Runtime, BeeAI, LangChain.js, MCP, OpenAI, Anthropic, Claude Agent SDK, Vercel AI SDK, TanStack AI middleware

**Java:** LangChain4j, Spring AI, annotation-based tracing (ByteBuddy), Google ADK Java

**Go:** Anthropic Go SDK, official OpenAI Go SDK (requires Go 1.25+)

---

## Integrations — Full List

### LLM providers (tracing)
Amazon Bedrock, Anthropic, Cohere, Google GenAI, Groq, LiteLLM, Mistral AI, Ollama, OpenAI, OpenRouter, Together AI, Vertex AI

### Python agent frameworks
Agno, AG2, AutoGen, Amazon Bedrock Agents, AutoGen AgentChat, Bedrock AgentCore, BeeAI, Claude Agent SDK, CrewAI, DSPy, Google ADK, Guardrails AI, Haystack, Instructor, LangChain, LangGraph, LlamaIndex, LlamaIndex Workflows, MCP, Microsoft Agent Framework, NVIDIA NeMo Agent Toolkit, Open Agent Spec, OpenAI Agents SDK, Pipecat, Portkey, Pydantic AI, Semantic Kernel, Smolagents, Strands Agents SDK

### TypeScript/JavaScript agent frameworks
Amazon Bedrock Agents, BeeAI, Claude Agent SDK, LangChain.js, Mastra, MCP, OpenAI Agents JS, TanStack AI, Vercel AI SDK, TypeSafe AI

### Java
Annotations, Arconia, Google ADK for Java, LangChain4j, Spring AI

### Coding agents
Claude Code, Codex, GitHub Copilot, Cursor, Devin, Gemini CLI, Kiro, OpenCode

### Eval LLM-as-a-judge providers
Amazon Bedrock, Anthropic, Gemini, LiteLLM, Mistral AI, OpenAI, Vertex AI

### Eval libraries
Phoenix Evals, Microsoft Azure AI Evaluation, Ragas, NVIDIA RAG Metrics via Ragas

### Platforms
Dify, Flowise, LangFlow, OpenRouter, Prompt flow, TrueFoundry

---

## Pricing tiers

| Feature | Free | Pro ($50/mo) | Enterprise (custom) |
|---|---|---|---|
| Signal issues | 10/month | 25/month | Unlimited |
| Span volume | 25k/month | 50k/month | Custom |
| Storage | 1 GB/month | 10 GB/month | Custom |
| Retention | 15 days | 30 days | Custom |
| Deployment | SaaS | SaaS | SaaS or self-hosted |
| Custom Managed Agents | No | No | Yes |
| GitHub repo access (fix PRs) | No | No | Yes |
| Custom AI provider | Arize-managed | Arize-managed | BYOK + Arize-managed |
| Swarm observability | No | No | Yes |
| Agent-as-a-Judge | No | No | Yes |
| Agent experimentation | No | No | Yes |
| Data Fabric (BigQuery/Databricks/Snowflake) | No | No | Yes |
| Agent trajectory visualizations | No | No | Yes |
| Prompt serving and versioning | No | No | Yes |
| Enterprise SSO (SAML 2.0) | No | No | Yes |
| Audit logs | No | No | Yes |
| Self-hosted deployment | No | No | Yes |
| Data regions | US, EU, CA | US, EU, CA | US, EU, CA |
| Support | Community | Email + Standard SLAs | Dedicated + Custom SLAs |

**All plans — unlimited:** Evaluations, experiments, human annotations, labeling queues, playgrounds, datasets, prompts

---

## Customer proof points

| Customer | Industry | Metric / Outcome |
|---|---|---|
| **LG U+** | Telecom | Agent accuracy 70% → 96% (+26%); AI contact center (AICC) for 30M subscribers; eval-driven development |
| **Wayfair** | E-commerce | Agent accuracy improved 26% (70% → 96%); "Wilma" agent for real-time supplier transfer intervention |
| **AT&T** | Telecom | 40% improvement in accuracy of AI responses |
| **Handshake** | HR/Recruiting | 15+ production-ready LLM use cases deployed in under 6 months |
| **Bazaarvoice** | E-commerce | AI evaluation time cut from "days to minutes" |
| **TheFork** | Dining | 27M monthly visits; agent evals and tracing to boost conversions; on AWS |
| **Booking.com** | Travel | "We were able to intervene before an issue reached production" |
| **PagerDuty** | IT/SRE | Agent quality monitoring; turns quality signals into engineering action |
| **Tripadvisor** | Travel | AI product development lifecycle for agentic travel |
| **Atropos Health** | Healthcare | LLM observability in medical research |

**Other named logos (no public metrics):** Atlassian, Duolingo, Priceline, Reddit

### Customer quotes

> "We adopted an evaluation-driven development approach with Arize AX and continuously improved performance... Arize has been essential for building AI for 30 million subscribers." — **MinKyu Ha**, Team Lead AI Contact Center (AICC), LG U+

> "Thanks to visibility in Arize, we were able to intervene before an issue reached production." — **Amir Bitaraf**, Senior ML Engineer, Booking.com

> "We rely on Arize for both pre-launch development and post-launch debugging." — **Roger Bock**, Staff Engineer, Wayfair

> "The ability to run real-time online evaluations has been crucial as we've developed our agents." — **Ralph Bird**, Principal Engineer, PagerDuty

---

## Key technical specs summary

| Spec | Detail |
|---|---|
| Tracing standard | OpenTelemetry (OTLP) |
| Data format | Open (Apache Iceberg) |
| ADB query latency p95 | <1 second |
| ADB benchmark (1B traces) | 0.8 seconds |
| Auto-instrumented frameworks | 30+ |
| Supported coding agents | Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI, Devin, Kiro, OpenCode |
| Supported languages | Python, TypeScript/JavaScript, Java, Go |
| Phoenix monthly downloads | 3M+ |
| Phoenix GitHub stars | 10k+ |
| Phoenix community members | 7k+ |
| OTEL instrumentation downloads/month | 22M+ |
| Data regions | US, EU, CA |
| Compliance (self-hosted) | SOC 2 Type II, ISO 27001, HIPAA-ready |
| SSO | SAML 2.0 (Okta, Entra, OneLogin, Ping) |
| Kubernetes distributions | GKE, AKS, EKS, OpenShift, K3s, Rancher, Tanzu |
| Object storage | GCS, S3-compatible, Azure Blob |

---

## Competitive comparison pages

- Arize vs. Braintrust: https://arize.com/compare/arize-vs-braintrust/
- Arize vs. LangSmith: https://arize.com/compare/arize-vs-langsmith/
- Arize vs. Langfuse: https://arize.com/compare/arize-vs-langfuse/

---

## What to watch

- Agent-as-a-Judge additional harness support (Cursor, Codex, Hermes, OpenClaw) — listed as "coming soon"
- Managed Agent templates coming soon: Security agent, Prompt Optimization agent, Eval/Quality agents
- Sandbox environments coming soon: Daytona, Vercel
- Startup Enterprise pricing available (not publicly listed)
- ADB DataFabric (BigQuery, Databricks, Snowflake zero-copy) — Enterprise only
