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
