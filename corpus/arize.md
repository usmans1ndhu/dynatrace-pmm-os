---
title: The Arize Acquisition — Post-Close
last_verified: 2026-10-07
audience: both
sources:
  - https://www.dynatrace.com/news/blog/dynatrace-completes-acquisition-of-arize/  # primary; Steve Tack, Oct 1 2026
  - https://www.dynatrace.com/news/blog/dynatrace-intends-to-acquire-arize/  # primary; original announcement Aug 13 2026
  - https://www.dynatrace.com/solutions/ai-observability/
  - https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability
  - https://www.efficientlyconnected.com/dynatrace-arise-ai-observability-acquisition/  # secondary
  - Customer Facing Positioning - Dynatrace + Arize.pptx  # internal customer-facing deck; local OneDrive; verified 2026-10-07
  - sales_arize_faq_post-close-2.docx  # CONFIDENTIAL INTERNAL USE ONLY; Sales FAQ post-close; local OneDrive; verified 2026-10-07
  - "Arize _ Dynatrace messaging - Sept 18.docx"  # INTERNAL; product positioning document Sept 18 2026; local OneDrive Arize M&A folder; verified 2026-10-07
---

# The Arize Acquisition — Post-Close

**Bottom line: Dynatrace completed the acquisition of Arize on October 1, 2026. The deal brings the pre-production AI evaluation and developer tooling layer (Arize AX, Phoenix, OpenInference) that Dynatrace's ops-centric platform lacked. The combined vision is "full-lifecycle AI observability" — Arize to build and evaluate, Dynatrace to run and operate. Sold independently through H2 FY27; DPS integration expected within 12–18 months.**

---

## Deal facts

- **Announced:** August 13, 2026. Author: Steve Tack (CPO, Dynatrace). (https://www.dynatrace.com/news/blog/dynatrace-intends-to-acquire-arize/)
- **CLOSED:** October 1, 2026. Confirmed via primary source: Steve Tack blog post. (https://www.dynatrace.com/news/blog/dynatrace-completes-acquisition-of-arize/)
- **Type:** Acquisition (definitive agreement → completed)
- **Price / deal terms:** Not disclosed publicly.
- **Arize leadership joining Dynatrace:** Jason Lopatecki (CEO) and Aparna Dhinakaran (CPO). (blog + secondary source)

---

## What Arize brings

| Asset | What it is | Status |
|---|---|---|
| **Arize AX** | Managed enterprise platform for AI observability, evaluation, and continuous improvement. Available as managed SaaS or self-hosted in customer's VPC. | Available standalone |
| **Phoenix** | Open-source AI observability and evaluation engine. Used by 4,000+ enterprises. Built on OpenTelemetry and OpenInference. Trace applications, run evaluations, investigate failures. | Open-source; Dynatrace committed to continuity |
| **OpenInference** | Open instrumentation spec for AI tracing, compatible with OpenTelemetry. In June 2026, OTel formally accepted a code grant of OpenInference GenAI instrumentation from Arize. Now being added incrementally to OTel's GenAI instrumentation project. | Open standard; continues as independent open project |
| **ADB** | Purpose-built data store for AI observability data. (Secondary source; not named in Dynatrace primary announcement — verify before external use.) | Unconfirmed from primary |

**What Arize workflows enable:**
- Inspect agent trajectories, model calls, retrieval, tool use, context, performance, and cost
- Run evaluations against real datasets
- Compare experiments and model/prompt versions
- Feed production lessons back into the next development iteration
- Hallucination detection, output-quality scoring, RAG and agent evaluation

**Where Arize shines:** The pre-production build-and-eval loop — before a model, prompt, RAG pipeline, or agent is released to production.

**Who Arize is for:** AI/ML engineers, AI builders, data scientists — the people creating AI, not operating it.

---

## Core narrative — Why Dynatrace + Arize

Source: "Arize _ Dynatrace messaging - Sept 18.docx" (internal, 2026-10-07).

AI agents are becoming part of production software — calling tools, interacting with data, triggering workflows, affecting customer and business outcomes. Understanding why an agent failed requires more than trace data alone: teams need to see both whether the agent's decision was accurate and safe, and what was happening across the production system around it.

Both disciplines build on tracing as a shared foundation, but each extends it differently:
- AI teams use agent and LLM execution traces, evaluations, and experiments to assess whether an agent behaved correctly
- SRE/Platform teams trace the full transaction — across services, infrastructure, users, and business context — to understand how the system as a whole is operating

Today those two views remain separate. Without shared context, neither team can fully explain how AI behavior and system behavior interact, what caused a failure, or how it affected customers and the business.

**The core answer:**
- Arize answers whether the agent is accurate and safe
- Dynatrace answers whether the system around it is healthy
- Connecting the two gives teams a view of what the AI did, whether it worked, what else contributed, and what to improve next

**Why now:** AI is increasingly driving the workflows that run production systems — with agents calling tools, interacting with services and data, and taking action across production. Traditional availability and performance signals cannot tell a team whether an agent made the right decision, used the right information, or delivered the intended outcome. AI-specific evaluation provides that context, but may not reveal that a failure originated in an upstream service, data source, or infrastructure constraint. Operating production AI requires both AI-specific quality context and full-stack operational context.

---

## External pitch language (Event Floor / conference version)

Source: "Arize _ Dynatrace messaging - Sept 18.docx" (internal, 2026-10-07). External-facing language approved for conference use.

**Core pitch:**
> Production AI agents and production software are becoming one operational system. Arize remains the focused product for AI engineering teams, with the context and workflows to evaluate, investigate, and improve how agents and applications behave across development and production. Dynatrace provides the broader operational data and context around those systems, spanning applications, services, infrastructure, user experience, and business processes. Together, the vision is to connect Arize's agent observability and AI engineering workflows with Dynatrace's production data foundation, helping AI engineering and production operations understand what happened, why, what it affected, and what to improve next.

**TL;DR:**
> AI agents now operate across real production systems, but AI teams and SRE teams still see different parts of the story. Arize remains the focused product for AI engineering teams, helping them prove agents are accurate and make them better, while Dynatrace provides the broader production data and operational context around them. Together, Arize and Dynatrace combine deep agent observability with full production context, so teams can tell whether an agent is right and whether the system around it is healthy, in one connected offer.

---

## Combined vision — "Full-lifecycle AI observability"

Source: https://www.dynatrace.com/news/blog/dynatrace-completes-acquisition-of-arize/, Customer Facing Positioning deck (internal, 2026-10-07).

**Official tagline (internal deck):** "Dynatrace and Arize are coming together to help you build, run, and continuously improve AI you can trust."

**Headline framing:** "Two leaders. One AI lifecycle."

The three stages of the combined lifecycle:
1. **Build** — Evaluate models, prompts, RAG, and agents with Arize before release
2. **Run** — Operate in production with Dynatrace: topology, real users, cost, and reliability
3. **Improve** — Close the loop: production findings become the next evaluation, continuously

**The problem framing (blog):**
- AI engineering, SRE/platform, and business teams work in separate disciplines with disconnected signals and workflows
- AI can fail silently — a healthy-looking service can still produce wrong outputs
- Changes to models, prompts, retrieval, tools, data, or workflows can alter behavior, so evaluation should happen throughout the lifecycle, not only before deployment
- Lessons learned should become datasets, regression tests, evaluators, or experiments

---

## How the products fit together — the boundary

Source: "Arize _ Dynatrace messaging - Sept 18.docx" (internal, 2026-10-07).

Arize AX and Dynatrace are complementary products that answer different questions about AI in production.

**Arize AX** tells a team whether its agents are accurate and improving: it evaluates agent behavior, finds where an agent went wrong, and gives AI engineering teams the workflows to test and ship a fix. Built for AI and ML engineering teams that own the full agent lifecycle — from pre-release evaluation through monitoring agent behavior in production; goes deep on the AI itself, from the prompt to the model's final answer or the agent's decision.

**Dynatrace** tells a team whether those agents are running and functioning properly: it monitors reliability, latency, cost, and dependencies across the applications, services, and infrastructure the agent touches. Built for SRE, platform, and operations teams that run the wider production environment; goes deep on the system the AI runs in, from the service call to infrastructure and business process, and makes AI visible alongside everything else they operate.

**The boundary (important for positioning):**
> You would not run your SRE team on Arize, because it does not carry the application, infrastructure, user, and business context they operate; and you would not run your AI engineering team on Dynatrace AI Observability alone, because it monitors AI in production but is not where prompts, models, and agents get evaluated, tested, and improved. Two fit-for-purpose tools for two organizations, built to work together.

The two products meet at the trace — which is why a team needs both: not just to find where something broke, but to continuously know whether the AI is behaving accurately and safely, and how the system around it is performing.

---

## The joint workflow to show (key demo scenario)

Source: "Arize _ Dynatrace messaging - Sept 18.docx" (internal, 2026-10-07). Use this as the anchor scenario in demos and discovery.

1. **Dynatrace raises a problem** on an AI feature (e.g., a Signal-driven alert on an LLM's answer quality or cost)
2. **The SRE hands it to the AI engineer with one click** — "analyze and tune in Arize" — with context carrying over
3. **The engineer reproduces it in the Arize playground**, tests a fix, and ships
4. **Dynatrace confirms the fix in production**

> A central SRE team watching 500 applications will never fix the agent itself; the hand-off is the point.

The reverse direction — from an Arize finding to the infrastructure cause in Dynatrace — is planned.

Today: an Arize skill can already pull Dynatrace data into Arize agents.

---

## Positioning framework — when to lead with which

Source: Sales FAQ post-close (internal, CONFIDENTIAL, 2026-10-07) and Customer Facing Positioning deck (internal, 2026-10-07).

### Lead with Dynatrace AI Observability when:
- **Persona:** SRE, Platform Engineering, or Ops — not the team writing prompts or agent logic
- **Use cases:** Entry point is production; troubleshooting degradation or inefficiencies in the full stack (applications, services, infrastructure including GPUs)

### Lead with Arize when:
- **Persona:** AI/ML engineer, AI builder, or data scientist
- **Use cases:** Entry point is pre-production; building or evaluating a model, prompt, RAG pipeline, or agent; ask centers on experimentation, hallucination detection, output-quality scoring, or comparing prompt/model versions

### Position both (Dynatrace + Arize) when:
- **Persona:** Senior executive or C-suite: CAIO, CIO, CTO, Head of AI
- **Use cases (six "better together" scenarios):**
  1. **Experiments with production behavior** — Arize proves what works in dev; Dynatrace shows what happens when it meets real traffic
  2. **Traces with full-stack context** — Arize traces model/prompt/retrieval/agent path; Dynatrace traces application dependencies and infrastructure
  3. **Evaluations with operational signals** — Arize supplies model quality verdict; Dynatrace supplies operational cost (latency, errors, throughput, spend in same decision)
  4. **AI workloads with their infrastructure** — Arize surfaces AI behavior; Dynatrace surfaces GPU, dependency, and data-source conditions driving it
  5. **Agent workflows with business outcomes** — Arize shows how the agent reasoned; Dynatrace shows what it did to the business (real transaction, not just a trace ID)
  6. **Production signals feeding engineering improvement cycles** — Dynatrace detects the problem; Arize turns it into the next evaluation

### Segment guidance (internal, sales FAQ):
- **Commercial:** Lead with Arize (and Bindplane) for velocity sales motion — fast lands, new logo volume
- **Enterprise / Strategic / Global:** Position full portfolio; leverage Arize AEs as specialists + AI COE for AI Observability

---

## Day 1 messaging guardrails — what to say and not say

Source: "Arize _ Dynatrace messaging - Sept 18.docx" (internal, 2026-10-07). These apply to all external content until updated by messaging owners.

### SAY (approved Day 1 language)

- Arize and Dynatrace have complementary capabilities today.
- Arize remains the focused AI engineering product; Dynatrace provides the broader production platform and data foundation around it.
- Arize provides deep AI engineering context and workflows.
- Dynatrace provides broader operational context across the production environment.
- The products remain independently available.
- The vision is a more connected toolchain and operating loop over time.
- Customers can use Arize, Dynatrace, or both.
- Arize answers whether the agent is accurate and improving; Dynatrace answers whether it is running reliably and what it costs. Build and improve AI with Arize, run it with Dynatrace, and close the loop.

### DO NOT SAY (prohibited Day 1 language)

- ~~"One integrated platform"~~ or ~~"single pane of glass"~~ on Day 1
- ~~"Arize replaces Dynatrace AI Observability"~~ or ~~"Dynatrace AI Observability is enough for AI engineering teams"~~
- ~~"Phoenix is the free tier, trial, or on-ramp to AX"~~
- ~~"Arize AX is being folded into APM"~~
- Do NOT refer to Arize as "Arize by Dynatrace" or "Arize, a Dynatrace company" in external-facing collateral or speaking
- Do NOT make specific integration, packaging, or delivery commitments that have not been approved
- Do NOT use language implying that production findings already flow automatically between Dynatrace and Arize
- Do NOT say to any customer: ~~"Arize will stop working with Datadog / Grafana / other platforms."~~ — It will not.
- Evidence: Only make claims supportable by existing evidence. Use Arize evidence for Arize claims and Dynatrace evidence for Dynatrace claims. No quantified or outcome-based claims about Arize + Dynatrace together yet (no combined customer evidence).

---

## Customer cohorts — existing customers

Source: "Arize _ Dynatrace messaging - Sept 18.docx" (internal, 2026-10-07).

**Core joint value proposition (same for every cohort):**
1. **Fit for purpose:** Arize AX for the AI engineering team, Dynatrace for the SRE/platform/operations team — each the leader for its user
2. **One company from Day 1:** one relationship, best of breed on both sides, with the products moving closer together over time
3. **More than the sum:** a problem found in Dynatrace can be handed to the AI engineer to fix and validate in Arize; Arize's evaluation signals strengthen Dynatrace Intelligence

### Cohort A — Dynatrace customers using AI Observability

**Users:** SRE and platform/ops teams run Dynatrace. AI/ML engineering teams build the agents — some already use the Dynatrace app for prompt debugging and LLM-as-judge checks; others use separate tools. Platform or technology leaders typically own the commercial relationship.

**Current use cases:** Monitor AI application reliability, latency, cost; trace agents alongside services and infrastructure; check AI output quality in production; diagnose full-stack issues.

**Joint value prop:**
- Your AI observability is about to get a lot better: the leading AI evaluation technology is brought into the platform you already run
- Dynatrace Intelligence gains new signals: Arize Signal findings and evaluation results become inputs to problem detection and root cause
- Agent and prompt evaluation, playgrounds, and experiments are delivered through Arize AX — that is where your AI engineering team goes to fix what Dynatrace finds
- Remediation: a Dynatrace problem on an AI feature hands off to Arize with context ("analyze and tune in Arize"); the fix is tested there and validated back in production
- See production AI metrics such as agent topology, token cost and forecasts, latency and errors of AI features
- Expand capabilities for AI observability and evaluations, specifically for AI/ML engineering teams

### Cohort B — Dynatrace customers using a competitor for AI observability (or none yet)

**Users:** SRE and platform/infrastructure teams use Dynatrace for core observability. AI/ML engineering teams often sit outside the observability relationship and use separate tools. The platform buyer can connect the two groups.

**Current use cases:** Monitor applications, infrastructure, logs, user experience. Treat AI applications like other services, with limited visibility into agent behavior or quality.

**Joint value prop:**
- Competitive take-out without changing the observability stack: switch on Dynatrace AI Observability inside the platform you already run, and give the AI engineering team Arize AX for the depth the competitor lacks
- If you want the best-of-breed tool for your AI engineering team, let Arize show you what it has; if you want AI inside one platform, that platform is now getting the leading AI evaluation technology built in
- Choosing LangSmith, Langfuse, or Datadog for AI means two vendors that will never integrate; choosing Arize means one company and integrations already being built
- Give the AI engineering teams, who today work outside the observability platform, a purpose-built tool for their job: evaluation, datasets, experiments

> **Note (internal):** Lead with Dynatrace when the buyer is the platform team and consolidation is the driver; lead with AX when an AI engineering team is active (often visible as Phoenix usage) and quality — not uptime — is the pain point.

### Cohort C — Arize-only customers

**Users:** AI/ML engineers and AI platform teams build and improve AI systems. Heads of AI or CTOs own AI outcomes and the Arize relationship. SRE and platform teams typically use another observability platform.

**Current use cases:** Trace and evaluate agent behavior; investigate failures; test changes; improve prompts, models, and agents; govern AI systems across teams.

**Joint value prop:**
- Land with Arize. Nothing you use goes away: Arize keeps working with Datadog, Grafana, or any observability platform you run today; investment in AX and Phoenix continues
- Building agents and running production are becoming the same system; any joint capabilities are optional and additive; Arize customers get first access
- Do NOT propose replacing the customer's observability stack. Raise Dynatrace only if the customer asks or is already consolidating; win/maintain the Arize account first
- If the customer asks what Dynatrace would add: root cause of failures that start outside the agent (the service, database, or host behind a bad trace); cost and user impact alongside the trace; one on-call process for AI and everything else in production

---

## Customer profiles — new customer personas

Source: "Arize _ Dynatrace messaging - Sept 18.docx" (internal, 2026-10-07). Use for new-logo motion and lead-with guidance.

| Persona | What they value | Lead with | Key use cases |
|---|---|---|---|
| **AI engineer / LLM app developer** | Speed to start; seeing exactly why an agent failed; confidence a model change improves quality before it ships | Lead with Arize — Phoenix for open-source entry; AX for managed/team workflows | Arize: trace sessions, evaluate quality, understand failures. DT: production quality checks, prompt debugging. Arize adds datasets, experiments, agent-level evaluation, playground |
| **ML engineer / AI platform team** | Consistent quality and governance across many teams and agents; early warning on recurring production failures; control over data location (SaaS, VPC, on-prem) | Lead with Arize AX; add Dynatrace for the production system around the AI | Arize: evaluate AI quality, detect recurring failures, govern workflows. DT: connect agent behavior to services, infrastructure, reliability, cost. Together: determine whether a problem sits in the agent or surrounding production |
| **Head of AI / CAIO** | Evidence AI is accurate, safe, and improving release over release; visibility of cost and business delivery; clear ownership between AI team and operations | Lead with both, anchored on Arize; position DT as the production context around AX | Arize: measure AI quality and turn failures into tested improvements. DT: track reliability, cost, user experience, business impact. Together: connect AI engineering and operations in one improvement loop |
| **SRE / Platform / Operations** | Uptime, latency, fast root cause; one platform for everything they run; low-effort instrumentation and token spend control | Lead with Dynatrace; introduce AX when AI team needs deeper evaluation | DT: monitor uptime, latency, cost, dependencies; root cause with Dynatrace Intelligence; automate triage with Autonomous SRE Agent (ROADMAP). Arize: evaluate AI behavior and test improvements when the agent itself is failing |
| **CIO / CTO / VP Platform** | Fewer vendors and one accountable relationship; security, compliance, and governance for AI; predictable spend and credible roadmap | Lead with Dynatrace for the enterprise platform; position AX as specialist AI engineering layer | DT: enterprise observability, security, and governance foundation. Arize: specialist platform for AI evaluation and improvement. Together: one strategic relationship across production operations and AI engineering |
| **Data scientist / classic ML team** | Knowing when model accuracy or input data has drifted; one platform for classic ML and GenAI; enterprise access controls and deployment options | Lead with Arize AX Enterprise | Arize: monitor model performance, drift, data quality; govern classic ML and GenAI in one platform; support enterprise deployment and access controls |

---

## What changes for customers (post-close)

Source: https://www.dynatrace.com/news/blog/dynatrace-completes-acquisition-of-arize/

- **Arize AX and Phoenix remain available as standalone offerings** — no immediate changes to either product
- **Existing Arize customers:** Full support continues; continuity in existing deployments; will gain access to Dynatrace's enterprise-scale production telemetry and operational context over time
- **Existing Dynatrace customers:** Gain a roadmap covering the full AI lifecycle including AI-native evaluation frameworks and Phoenix/developer community tools not previously available
- **Joint customers:** More unified experience connecting AI quality and performance to business outcomes
- **Phoenix builders:** Continue as they are — Dynatrace committed to open-source stewardship

---

## Go-to-market and commercial details (internal, post-close)

Source: Sales FAQ post-close (CONFIDENTIAL INTERNAL USE ONLY, verified 2026-10-07). Do not cite externally.

- **Selling:** Arize and Dynatrace sold independently through H2 FY27; co-selling starts immediately
- **DPS integration:** Arize expected to be integrated into Dynatrace Platform Subscription (DPS) within 12–18 months
- **Pricing:** No changes to Arize pricing currently; will remain separate from Dynatrace through H2 FY27
- **Quoting:** All Arize quoting done by Arize AEs through H2 FY27
- **Salesforce integration:** Arize into Dynatrace Salesforce — H1 FY28
- **Arize fiscal year:** Ends January 2027; Arize AEs compensated per their own plan through then
- **Compensation for Dynatrace sellers:** Quota attainment + commissions on registered/approved/closed Arize opportunities (2 months in arrears); counts toward accelerators; does NOT automatically count toward Club (must hit 100% Dynatrace quota independently first)
- **AI CoE contact:** ai-coe@dynatrace.com
- **Marketplaces:** Arize available on AWS (qualified for MPOPP), MS, GCP (separately from Dynatrace; two separate private offers if sold together); GCP MCCP qualification in progress
- **Partner Program:** Dynatrace Partners can sell Arize; required language added to applicable Order Forms on deal-by-deal basis; counts toward Partner Level
- **Territory changes:** None through FY27; will adjust on Dynatrace fiscal year (April)

---

## Arize competitive battle cards (internal use only)

Source: "Arize _ Dynatrace messaging - Sept 18.docx" (internal, 2026-10-07). Do not use in customer-facing content — internal sales context only.

The Arize competitive set breaks into two camps:
- **Broad observability with AI investment:** Datadog — leads with platform consolidation; has invested in AI observability (OSS: Lapdog; managed SaaS offering). Strongest when SRE or platform teams own the problem, or the customer already uses Datadog.
- **AI-native developer and evaluation platforms:** Langfuse, LangSmith, Braintrust — lead with developer-friendly tracing and evaluation workflows.

**Arize's common advantage across all:** The depth of the AI engineering loop across development and production — open instrumentation (OpenInference/OTel), agent-native tracing, production investigation, evaluations, datasets, experiments, agentic workflows, and enterprise-ready data and deployment options. Individual feature gaps tend to close quickly; the stronger story is the philosophy and workflow behind those capabilities.

### vs. Datadog

Position: A credible full-stack AI observability offering inside a much broader APM, infrastructure, security, and cost platform. Strongest when SRE or platform teams own the problem, customer already uses Datadog, or procurement prioritizes consolidation.

**How Arize wins:** Lead on AI quality and continuous improvement. Arize goes deeper in evaluation, datasets, experimentation, agent investigation, and the workflow from production finding to tested change. Data ownership, OpenInference, Phoenix, and AI-native developer workflows further differentiate. 
> ⚠ Avoid old claims that Datadog lacks evals, prompts, or experiments. The sharper distinction: **Datadog optimizes for observing AI in production; Arize optimizes for improving how AI behaves.**

**Demo anchor:** Show how AX connects a production finding to evaluation, investigation, and a tested change within the customer's AI engineering workflow.

### vs. Langfuse

Position: OSS-first, developer-friendly platform with low-friction self-hosting, strong community adoption, and solid tracing and prompt-management workflows.

**How Arize wins:** Arize spans both open-source control and enterprise production workflows. Phoenix provides a complete open-source option; AX adds real-time scale, monitoring and alerting, richer evaluation and experimentation, production-to-dataset workflows, agentic investigation, governance, and commercial support.

**Demo anchor:** Show how Phoenix and AX support different operating models — customer-operated tooling vs. commercially supported enterprise workflows.

### vs. LangSmith

Position: Polished development and evaluation platform with strong distribution through the LangChain and LangGraph ecosystem. Particularly strong in datasets, experiments, debugging, and developer UX.

**How Arize wins:** Lead with framework independence, openness, and production depth. Arize maintains OpenInference, supports consistent workflows across frameworks, provides deeper session- and trajectory-level analysis, and connects production monitoring to evaluation and experimentation. Data portability, Data Fabric, and mature self-hosted enterprise deployments strengthen the case.

**Demo anchor:** Show instrumentation portability and required workflows across models and frameworks, using a current comparison of deployment and integration options.

### vs. Braintrust

Position: Design-led, developer-first platform with strong evaluation and experimentation workflows, appealing UX, and strong motion among startups and AI-native teams.

**How Arize wins:** Lead with continuous production improvement and agent-native depth. Arize connects monitoring, production investigation, session and multi-agent evaluation, datasets, experiments, and human review. OpenTelemetry and OpenInference interoperability, enterprise deployment and governance, plus Signal, Alyx, and Managed Agents create a clearer path from production failure to tested improvement.

**Demo anchor:** Show the path from a production issue to trajectory evaluation, a reviewable proposed change, and a full-agent experiment.

---

## Arize competitive landscape (post-close)

Source: Sales FAQ post-close (internal, 2026-10-07).

Arize's named competitors: **LangSmith, Braintrust, Langfuse, W&B (Weights & Biases), Datadog**

These are the competitors for Arize's AI evaluation and pre-production tooling category — different from Dynatrace's primary observability competitors. Do not conflate the two competitive sets.

---

## Open-source commitments

- Dynatrace will continue supporting Phoenix independently (open-source stewardship)
- Dynatrace will continue stewardship of OpenInference, maintaining vendor-neutral access for developers
- OpenInference GenAI instrumentation formally accepted into OpenTelemetry (June 2026 code grant from Arize)
- "Dynatrace plans to keep supporting the open, builder-first approach behind Phoenix, OpenInference, and their communities"

Source: https://www.dynatrace.com/news/blog/dynatrace-completes-acquisition-of-arize/

---

## Product integration roadmap — what's known

- Near-term focus: find where connecting Arize's tracing, evaluation, experimentation, and improvement workflows with Dynatrace context creates the most value
- Roadmap will be communicated by AI CoE in collaboration with R&D
- DPS integration: 12–18 months
- Salesforce (CRM): H1 FY28
- **Bluebox product:** Continues to be built and operated independently; teams will coordinate with Arize to integrate AI Observability functionality into roadmap (internal FAQ — verify meaning of "Bluebox" before citing)
- No integration timelines or specific product merger plans are public

---

## What this resolves vs. what remains open

**Resolved:**
- Deal is CLOSED (October 1, 2026) — primary source confirmed
- Arize is NO LONGER a named competitor — remove from all competitive framing; update positioning.md
- Phoenix at 4,000+ enterprises — confirmed via secondary source; consistent with open-source prominence
- Founders: Jason Lopatecki (CEO), Aparna Dhinakaran (CPO) — confirmed via primary source
- AX available self-hosted in customer VPC — confirmed via internal deck

**Still open:**
- Specific product integration roadmap and timeline beyond "12–18 months to DPS"
- Pricing and packaging of the combined offering post-DPS integration
- Whether "Arize" brand survives long-term as a named product within Dynatrace
- ADB (Arize data store) — named only in secondary source; verify from primary
- "Bluebox" product reference — not explained in FAQ; verify meaning and public status
- Analyst placement for Arize in its own category (AI evaluation / pre-production tooling)
