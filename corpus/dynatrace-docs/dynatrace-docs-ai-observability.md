# Dynatrace Docs Truth: AI Observability

**Source root:** https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability
**Captured:** 2026-09-03
**Scope:** Overview page through Integrations page, all nested sub-pages (docs only — Dynatrace Hub listing pages excluded per scope decision)
**Pages captured:** 18
**Corpus status:** Source-of-truth reference. Facts below are paraphrased from docs, not verbatim. Marketing-style claims are flagged in Notes.

---

## 1. What AI Observability is (Overview)

**Source:** `/dynatrace-for-ai-observability` · Updated Aug 28, 2026

AI observability = collecting, analyzing, and correlating telemetry to understand how AI systems, agents, and LLMs behave — including in production. Covers LLMs, AI agents, orchestration layers, and their downstream impact on apps/infra.

**Key metrics tracked:** stability (success vs. failure rate), latency, load, model drift, data drift, cost (tokens/fees/resources).

**Platform capabilities:** monitoring, logging, metrics & performance analysis, visualization, anomaly detection, explainability/interpretability.

**Key use cases (as stated by docs):**
- Monitor service health/performance against SLOs
- Monitor service quality and cost (error budgets, consumption validation)
- Evaluate response quality (online LLM-as-a-judge, regression catching, score drift)
- End-to-end tracing/debugging of prompt flows
- Build trust / reduce compliance & audit risk (full input/output audit trail, data lineage)

**Instrumentation paths (four):** Traceloop OpenLLMetry, OpenTelemetry + GenAI semantic conventions, OpenInference (Arize AI standard), Dynatrace OneAgent (zero-code).

**Stack coverage claimed:** foundational models, vector databases, RAG orchestration frameworks — "every layer" of modern AI apps.

**Provider/platform integrations named on this page:** OpenAI, Amazon Bedrock, NVIDIA NIM, Ollama, Traceloop OpenLLMetry, OpenInference.
**Vector DB/semantic cache integrations named:** Milvus, Weaviate, Qdrant.
**Orchestration frameworks named:** LangChain.
**Infra monitoring:** GPU/TPU metrics (Google TPU, NVIDIA GPU) — temperature, memory, etc.

Note: Dynatrace's own product (Dynatrace Intelligence) uses this same AI observability approach internally for self-monitoring — a "we eat our own dog food" proof point.

---

## 2. AI Observability app (product/UI)

**Source:** `/ai-observability-app` · Updated Aug 28, 2026

**Prerequisites:** Dynatrace Platform Subscription (DPS) license with Metrics/Traces/Logs powered by Grail capabilities, plus 10 specific permission scopes.

**Cost note (important for objection handling):** Some out-of-the-box dashboards use span queries that consume "Traces powered by Grail – Query" — billed **even if AI Observability isn't fully configured or shows no data.** Dynatrace states they're actively working to reduce this by moving away from span queries. *(Flag: this is a real cost-objection risk point — worth having ready for Sales Assist skill.)*

**Five tabs:** Overview, Explorer, Prompts, Agents topology, Evaluations (Preview).

- **Overview tab:** landscape at a glance — providers, agents, model versions, services, LLM requests, token usage, cost trends. Links into ready-made dashboards.
- **Explorer tab:** shared Dynatrace interface pattern (consistent across domains). Two views: Model Providers table, Service explorer. Covers errors, traffic/latency, cost, guardrail outcomes, drill-down to logs/traces/vulnerabilities.
- **Prompts tab:** prompt version management — non-technical stakeholders (PMs, SMEs, compliance) can review in-UI without code changes. Decouples prompt changes from deployments with instant rollback. A/B testing on live traffic. Export to JSON.
- **Agents topology tab:** visualizes agent-tool-LLM chains, handovers, schedulers; anomaly/root-cause detection across the chain.
- **Evaluations tab (Preview, governed by preview terms — not GA, subject to change):** LLM-as-a-judge scoring written back as `bizevents`, linked to source trace. Pass/fail rates, score distribution, drift detection.

**"What's coming next" (as of Aug 2026):** AI model/services explorer with richer detail views; Smartscape integration (agent topology rendered as Smartscape intents alongside services/K8s/cloud).

**Guardrails positioning (consistent across docs):** *Dynatrace does not enforce runtime guardrails.* Providers (Bedrock, Azure OpenAI, OpenAI) expose guardrail signals; Dynatrace captures/visualizes them. This is a repeated, deliberate distinction — good to hold precisely in messaging.

---

## 3. Terms & concepts (glossary)

**Source:** `/terms-and-concepts` · Updated Jul 27, 2026

Key defined terms: RAG, Agents, Agentic (systems), Guardrails, Evaluations/Evals, LLM-as-a-judge, Code evals, Online evals, Offline evals, Instrumentation, Traces, Traceloop span kind (`workflows`/`task`/`agent`/`tool`), OpenTelemetry GenAI semantic conventions.

**Useful distinctions for messaging:**
- **Code evals** = deterministic, rule-based (exact match, regex, JSON validation) — fast/cheap, complements LLM-as-a-judge.
- **Online evals** = live production traffic, unlabeled, sampled, surfaces drift/edge cases in real time.
- **Offline evals** = curated/labeled dataset, pre-release, full control over test distribution but limited real-world coverage.

---

## 4. Getting started — four instrumentation paths

**Source:** `/get-started` (index) · Updated Jul 30, 2026

| Path | Best for | Code changes required |
|---|---|---|
| **OneAgent** | Zero-code, host-based auto-instrumentation | None |
| **OpenLLMetry** (Traceloop) | Popular AI frameworks, auto-instrumentation | SDK install + init |
| **OpenTelemetry (native)** | Full control, vendor-neutral | Manual span/attribute instrumentation |
| **OpenInference** (Arize AI standard) | Apps already using Arize's convention | SDK install + normalization step |

### 4a. OneAgent (`/get-started/oneagent`, published Jun 9, 2026)
Zero-instrumentation: OneAgent captures model name, token counts, latency, prompt content with **no code changes**. Covers Python AI SDKs: AWS Bedrock, OpenAI, LangChain (natively supported); Anthropic, Cohere, Groq, Mistral AI, Ollama, Google GenAI, CrewAI, Haystack are **experimental sensors** — functional, accelerated release cadence, **not covered by support SLAs**, attribute completeness is best-effort. Prompt capture (prompt text + response) currently supported only for AWS Bedrock and OpenAI (including as LangChain's underlying model).

### 4b. OpenLLMetry (`/get-started/openllmetry`, updated May 4, 2026)
Traceloop's OTel-based SDK. `pip install traceloop-sdk`, initialize with `Traceloop.init()`. Adds `@workflow`/`@task`/`@agent`/`@tool` annotations. Node.js support exists but **does not support metrics** (traces only).

### 4c. OpenTelemetry native (`/get-started/opentelemetry`, updated May 28, 2026)
Direct OTel SDK instrumentation using `gen_ai.*` semantic-convention attributes (`gen_ai.operation.name`, `gen_ai.provider.name`, `gen_ai.request.model`, `gen_ai.usage.input_tokens`/`output_tokens`, etc.). Most flexible, most manual effort.

### 4d. OpenInference (`/get-started/openinference`, updated Jul 22, 2026)
**Competitive-intel note:** OpenInference is Arize AI's semantic convention (`llm.model_name`, `llm.token_count.*`), distinct from OTel's `gen_ai.*` standard. Dynatrace explicitly supports **normalizing Arize's format into Dynatrace's native format** — meaning an org standardized on Arize Phoenix/OpenInference instrumentation can still feed Dynatrace without rewriting instrumentation. Two normalization paths: (1) OTel Collector + `genainormalizer` processor (full message reconstruction, requires Docker/Collector), or (2) Dynatrace OpenPipeline (server-side, no Collector, but uses a fallback for full message history). Detailed attribute mapping table exists in the doc if needed for technical FAQ.

---

## 5. Evaluations (two related but distinct capabilities)

**Important distinction for messaging — these are two different things:**

1. **`dt-evals`** (`/get-started/llm-judge-evaluation`, published Jul 28, 2026): open-source **CLI** for continuous/automated LLM-as-a-judge evaluation of production traces. Supports OpenAI, Anthropic, Azure OpenAI, Google Gemini Enterprise Platform (Vertex AI), Amazon Bedrock as judge providers. 10+ built-in evaluators (user frustration, toxicity, irrelevance, hallucination, faithfulness, PII leakage, prompt injection, bias). Masks PII (emails, phone, credit card, SSN) before sending to judge — **never sent externally**. Can gate CI/CD pipelines (`--ci` flag, non-zero exit on threshold breach). Runs against a **7-day rolling baseline** for drift detection.

2. **Agent evaluations (in-UI / Evaluations tab)** (`/agent-evaluations`, published Aug 5, 2026): **manual/UI-driven** evaluation — configure an LLM provider as judge (Anthropic, OpenAI, Microsoft Foundry, Azure OpenAI, Google Gemini, Vertex AI, AWS Bedrock, custom OpenAI-compatible endpoint), create custom evaluation methods with your own judge system prompt, run against captured prompt runs from the Prompts tab. **Hard UI limit: max 30 evaluations per manual run** (selected prompt runs × methods) — for larger/recurring/CI use, docs explicitly redirect to `dt-evals`.

**Both features are currently Preview** (governed by preview terms, not GA, may change materially).

---

## 6. Metrics reference (technical depth — for Sales Assist / technical FAQ)

**Source:** `/metrics-reference` · Published Jul 2, 2026

Four distinct data-source categories Dynatrace ingests for GenAI:
1. **OpenTelemetry-native metrics** — `gen_ai.client.*`, `gen_ai.server.*`, `gen_ai.workflow.*`, `gen_ai.invoke_agent.*`, `gen_ai.execute_tool.*` — emitted directly by instrumentation, ingested as-is (not calculated by Dynatrace).
2. **Dynatrace span-derived visualizations** — built directly from `gen_ai.*` span attributes, no separate metric instrument.
3. **Vendor-native metrics** — sent directly by the AI platform/gateway (Bedrock, Azure OpenAI, NVIDIA NIM, Kong AI Gateway).
4. **Other OTel/third-party sources** — self-derived (e.g., parsed from inference-server logs).

**Notable/quotable technical facts:**
- Dynatrace's requirement levels for `gen_ai.request.model`/`gen_ai.response.model` are **stricter than upstream OTel semantic conventions** (marked Required vs. OTel's "conditionally required"/"recommended") because the app needs both to populate model filters and charts.
- If `gen_ai.client.token.usage` metric is missing: cost tiles silently show **$0 with no error**. If `gen_ai.client.operation.duration` is missing: latency tiles show **empty, no error**. (Useful troubleshooting/FAQ content — also a fair caveat: failure mode is silent, not alerted.)
- Vendor-specific signals visualized: Bedrock guardrail activation/content/PII/topics/words + prompt caching; Azure OpenAI prompt/content filter results; NVIDIA NIM Prometheus metrics (latency, GPU cache usage, throughput) — vLLM exposes the same metric set since NIM proxies vLLM's metrics unchanged; Google Gemini/Vertex safety ratings are **not yet visualized** (ingestible via DQL only); Kong AI Gateway request/token/latency metrics.
- Two "other ready-made dashboards": **Model versioning/A-B testing** (built entirely from span attributes, not the client metrics) and **Audit trail** (reads `bizevents` where `event.type == "gen_ai.auditing"` — governance/compliance use case).

---

## 7. Sample use cases (6 tutorials — mostly technical/proof, light on positioning)

**Source:** `/sample-use-cases` (index) · Updated Jul 30, 2026

| Use case | What it proves |
|---|---|
| AI model versioning & A/B testing | Compare model/provider versions on cost, latency, token use via dashboard + custom metadata |
| AI data governance (Amazon Bedrock) | 5+ year audit retention via custom Grail bucket + OpenPipeline routing; ties to EU AI Act / US AI Executive Order compliance narrative |
| RAG pipeline observability | Full worked example: LangChain + Pinecone + Ollama chatbot, traced end-to-end via OpenLLMetry |
| End-to-end observability on Kubernetes | OneAgent + OpenLLMetry/OTel Collector combo for full-stack K8s + AI correlation; includes vulnerability visibility on AI workloads |
| OpenAI Observability | Token/cost tracking via logs or custom metrics; Davis AI auto-detects GPT slowdowns as root cause of downstream issues |
| Conversation ID & session tracking (RUM) | Links frontend browser sessions (RUM) to backend AI agent spans via `gen_ai.conversation.id`, so a full multi-turn conversation is queryable as one unit even across separate trace IDs — **published Jul 14, 2026, newest use case, strong differentiator for frontend-to-backend AI debugging** |

*Note: these are code-heavy tutorials. Full code samples exist in the source docs but are excluded here as low positioning value — pull from source URL if needed for a technical deep-dive deliverable.*

---

## 8. Agent frameworks & protocols supported

**Source:** FAQ page, confirmed "Yes" — Amazon Bedrock Strands & AgentCore, OpenAI Agents, Gemini agents, Google ADK, AWS Strands, MCP protocol (multi-agent communication monitoring).

**Microsoft Agent Framework** (`/integrations/microsoft-agent-framework`, published Jun 17, 2026): framework has **built-in native OTel support** — no additional Dynatrace SDK required, self-instruments with `gen_ai.*` conventions out of the box. Python and .NET. Backed by Azure OpenAI or GitHub Models. *Caveat surfaced in Dynatrace community (not the doc page itself, so treat as secondary/unverified): this applies to agents built on Azure AI Agent Service, not directly to Microsoft Copilot Studio's low-code canvas.*

---

## 9. Integrations catalog (full page — docs scope, Hub pages excluded)

**Source:** `/integrations` · Updated Aug 28, 2026

| Category | Named integrations |
|---|---|
| AI agents | Amazon Bedrock AgentCore (+ Gateway), AWS Strands Agents, Google ADK, LangGraph, MCP agent monitoring, Microsoft Agent Framework, OpenAI Agents, Pydantic AI |
| Model providers/platforms | OpenAI, Amazon Bedrock, CrewAI, Azure AI Foundry, Anthropic, Gemini, DeepSeek, NVIDIA NIM, Red Hat OpenShift AI, Vertex AI, Mistral AI, Ollama, Amazon SageMaker, Hugging Face, Replicate, Cohere, Groq, Together AI, IBM watsonx AI, Amazon Textract/Translate/Nova, Nutanix AI |
| AI coding agent monitoring | Claude Code, Gemini CLI, OpenAI Codex, GitHub Copilot SDK, OpenCode, OpenClaw |
| Vector stores | Pinecone, LanceDB, Chroma, Milvus, Weaviate, Qdrant, Elasticsearch, Marqo |
| Orchestration frameworks | LangChain, Haystack, LlamaIndex, Langfuse |
| Infrastructure/compute | Google Cloud TPUs, TensorFlow Keras, NVIDIA GPU, vLLM |
| Security/governance/traffic | Kong AI Gateway, LiteLLM |

*Note: this list changes frequently (published date on this page is a rolling "Updated" stamp) — treat as directional, verify current count before quoting a total integration number externally.*

---

## 10. FAQ highlights (objection-handling ready)

**Source:** `/frequently-asked-questions` · Updated Jul 27, 2026

- **"Who enforces guardrails?"** → Not Dynatrace. Provider-level (e.g., Bedrock Guardrails) enforces; Dynatrace ingests/visualizes the outcome signals only. (Repeated 3rd time across docs — treat as a firm, deliberate positioning line, not an oversight.)
- **"Does this cost extra to query?"** → Yes, some dashboards consume Traces-powered-by-Grail Query capacity even with no data flowing yet. Mitigations: sampling variables, restrict dashboard access, prefer metric-based tiles.
- **"What if I already use ready-made dashboards?"** → Still supported, but Dynatrace's docs steer customers toward the AI Observability app as "primary entry point" — dashboards are explicitly framed as more limited/inconsistent for GenAI workflows going forward.

