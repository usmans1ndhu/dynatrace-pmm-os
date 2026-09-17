---
title: Proof Points — Dynatrace AI Observability
last_verified: 2026-09-16
audience: both
sources:
  - https://www.dynatrace.com/solutions/ai-observability/
  - https://docs.dynatrace.com/docs/dynatrace-intelligence
  - https://www.dynatrace.com/news/blog/dynatrace-intends-to-acquire-arize/
  - https://www.dynatrace.com/news/blog/sre-best-practices-platform-engineering-trends/
  - https://www.dynatrace.com/platform/artificial-intelligence/
  - https://www.dynatrace.com/customers/inpost-ai/
  - https://www.dynatrace.com/customers/cdl/
  - https://www.dynatrace.com/customers/accenture/
  - https://www.dynatrace.com/customers/vitality-2/
  - https://www.dynatrace.com/customers/freedompay-3/
  - https://www.dynatrace.com/customers/vodafone/
  - https://www.dynatrace.com/customers/vestmark/
---

# Proof Points

**Bottom line: Seven customer stories added 2026-09-16. The strongest AI-specific proof: Accenture (90% MTTR improvement, 20% LLM token reduction, 40% observability cost cut), InPost (Kubernetes issue ID'd in 2 min, resolved in 7 min), CDL (tools reduced 10→1, CSAT +10%), and Vitality (~$1M logging cost reduction, 90%+ cost cut). FreedomPay and TELUS are qualitative but senior. Vodafone and Vestmark are platform/Grail stories that support the foundation wedge.**

---

## Customer proof — AI Observability

### InPost (Logistics)

1.4 billion parcels delivered annually; 61,000+ parcel lockers; 18M annual customers; 14.7 billion PLN revenue (2025).

**Mateusz Piasta, Lead Site Reliability Engineer:**
> "Observability is mission critical in an AI first world and Dynatrace gives us the visibility to reduce the blast radius of issues in our agentic systems early."

> "Dynatrace gives us real-time visibility across more than 61,000 lockers, helping us maintain consistent service quality."

**Metrics:**
- Kubernetes issue identified in 2 minutes, resolved within 7 minutes

**Dynatrace use:** Grail, Dynatrace Intelligence, AI monitoring for agentic systems (logistics forecasting, workforce planning, shopping agents), MCP for natural language querying, OpenTelemetry. Key AI use case: controlling excessive token consumption in an AI shopping agent.

Source: https://www.dynatrace.com/customers/inpost-ai/, verified 2026-09-16
Audience fit: Ops/SRE, AI engineers.

---

### CDL (UK Insurtech)

Processes ~60% of UK insurance purchases; 1 trillion+ transactions annually.

**Matt Eisengruber, Head of Architecture:**
> "AWS gives us the capability to use AI, and Dynatrace gives us the confidence."

> "Dynatrace helps us ensure responses are consistent and aligned with our AI ethics."

**Chris Buckley, Head of Operations:**
> "The confidence it gives to our internal governance teams is unparalleled."

**Metrics:**
- CSAT score increased 10%
- Observability tools reduced from 10 to 1
- Onboarding time reduced from days to minutes

**Dynatrace use:** AI observability for Amazon Bedrock, OpenLLMetry, unified observability (metrics, logs, traces), cost optimization, Apdex performance tracking.

Source: https://www.dynatrace.com/customers/cdl/, verified 2026-09-16
Audience fit: AI engineers, compliance/governance.

---

### Accenture Life and Annuity Software / ALIP (Insurance)

> "Dynatrace gives us X-Ray vision, so we see not only what's happening, but what caused it."

> "We ultimately don't have to worry about managing complexity because we have a partner innovating constantly."

**Metrics:**
- 40% reduction in observability and logs costs
- 90% improvement in MTTR
- Platform availability improved from 99.50% to 99.98%
- 20% reduction in LLM token consumption

**Dynatrace use:** Davis AI, Grail (log ingestion + telemetry), Live Debugger, AI observability. Consolidated 4 monitoring tools + 1 log management solution into one platform.

Source: https://www.dynatrace.com/customers/accenture/, verified 2026-09-16
Audience fit: Ops/SRE.

---

### Vitality Group (Insurance)

49 million members across 40 countries. AI-driven health platform (Vitality AI) built on Google Vertex stack.

**Hushan Padayachee, Chief Information Officer:**
> "Observability is mission critical in an AI-first world. Dynatrace provides answers rather than more data to review and analyze."

**Metrics:**
- Close to $1M saved in log management and analytics expenses
- 90%+ reduction in logging costs
- 15–25% improvement in engineering and operations team productivity

**Dynatrace use:** Grail (consolidated logging replacing Elasticsearch), Clouds App (cloud resource optimization), AI model performance visibility, AWS and Google Cloud spend optimization.

Source: https://www.dynatrace.com/customers/vitality-2/, verified 2026-09-16
Audience fit: Ops/SRE, exec.

---

### FreedomPay (Financial Services)

Present at hundreds of thousands of sites; top 5 food service providers and 100+ airports; 3 billion+ transactions globally across 130+ countries.

**Mark Tomlinson, Senior Director of Observability and Performance:**
> "We knew early on that if we were going to scale AI responsibly, observability had to come first. Without visibility into how these models behave, you can't build the trust required for enterprise adoption."

Additional quotes from customer story:
> "Dynatrace gave us immediate insight into how our AI services were performing."

> "With Dynatrace, we can ensure consistency, performance, and alignment with our standards."

**Dynatrace use:** End-to-end AI visibility, OpenLLMetry, unified monitoring (metrics, logs, traces), LLM usage optimization and cost tracking, Microsoft Azure integration.

Source (original quote): https://www.dynatrace.com/solutions/ai-observability/
Source (expanded story): https://www.dynatrace.com/customers/freedompay-3/, verified 2026-09-16
Audience fit: Ops/SRE, exec.
Note: Qualitative; no hard outcome metric in the story.

---

### TELUS (Telco)

**Kulvir Gahunia, Director of the Site Reliability Office:**
> "By combining our Agentic AI initiatives with Dynatrace's AI Observability capabilities, we've successfully optimized our development and operations workflows."

Source: https://www.dynatrace.com/solutions/ai-observability/
Audience fit: Ops/SRE.
Note: Qualitative only; no quantified outcome. No dedicated customer story page fetched.

---

## Customer proof — Autonomous Operations

Complementary to AI Observability. These stories support the "Powered by AI" pillar — from insight to trusted action.

### Careem (Technology / Super-app — Uber company)

75M+ customers; 3.5M+ Captains; 20+ services; 800+ microservices on Amazon EKS; billions of API calls daily; 40TB raw logs processed daily.

**Alaa Alkhdarat, Senior SRE Manager:**
> "By consolidating our observability stack with Dynatrace, we have saved approximately 10,000 engineering hours per year and unlocked a 65% cost reduction."

**Ricardo Fernandes, VP Software Engineering:**
> "Dynatrace has cut our MTTD by 84% to under two minutes and helps us identify root causes more than six times faster."

**Metrics:**
- 65% cost reduction vs. previous observability stack
- 84% reduction in MTTD — under 2 minutes
- 6x faster root cause identification
- ~10,000 engineering hours saved annually
- 99.99% availability SLA maintained

**Dynatrace use:** AI-powered observability, automated instrumentation, root cause analysis, log management, user experience monitoring, AI incident management agent.

Source: https://www.dynatrace.com/customers/careem/, verified 2026-09-17
Audience fit: Ops/SRE, exec.
Tag: Autonomous Operations + AI Observability

---

### CIMB Bank (Financial Services)

Founded 1987; RM778.7B total assets (2025); RM7.9B net profit (2025); 33,000+ staff; 30M+ customers across ASEAN; ~100M mobile transactions/month in Malaysia.

**Ros Yusoff, Group CTO:**
> "Dynatrace helps bridge the gap between IT operations and the business."
> "Before Dynatrace, we spent a lot of time in war rooms trying to piece together where problems were happening."
> "Our availability scores have improved from around 0.6 to a consistent 0.95."

**Metrics:**
- Critical incidents reduced to near-zero
- Availability score improved from 0.6 to 0.95
- Alert volumes reduced by 90%
- Root-cause identification in seconds vs. manual investigation

**Dynatrace use:** Unified observability, AI-powered root cause analysis, AIOps, automation for self-healing workflows.

Source: https://www.dynatrace.com/customers/cimb/, verified 2026-09-17
Audience fit: Ops/SRE, exec.
Tag: Autonomous Operations + AI Observability

---

### Macquarie Bank (Financial Services)

2.2M customers; A$200B+ deposits; A$190B+ loan portfolio. Targets 99.95% service availability.

**Phil Grasso-Nguyen, Head of Reliability:**
> "With Dynatrace, we can use AI as a first responder for every incident, with a human in the loop."
> "Dynatrace enables us to use AI to reduce risk at every point of change, so we can innovate faster and safer."
> "The best incident is the one that never happens."

**Key outcomes:**
- Significant reduction in major incidents
- Improved MTTD and MTTR
- Proactive reliability and resilience approach

**Dynatrace use:** Dynatrace Intelligence, Live Debugger, unified observability. Use cases: AI as first responder, automated release verification (safer innovation), root cause analysis (faster recovery).

Source: https://www.dynatrace.com/customers/macquarie-bank/, verified 2026-09-17
Audience fit: Ops/SRE, exec.
Tag: Autonomous Operations
Note: Outcomes qualitative; no hard metric on incident count or MTTD/MTTR reduction published. Quotes from Phil Grasso-Nguyen (Head of Reliability) are strong for AI-first-responder framing.

---

### Sicredi (Financial Services — Brazilian Credit Union)

Founded 1902; $88.6B total assets; $60.2B total deposits; 50,000+ employees; 10M+ associates; 1,100+ applications; 10,000 components; 7,000 databases.

**Metrics:**
- 80% reduction in time to instrument apps with observability
- 67% reduction in cognitive load for developers
- SLO creation time: 15 minutes → 3 minutes
- SLO process: 6 steps → 2 steps

**Dynatrace use:** Full-stack observability, OpenPipeline, Grail, MCP Server for AI integration, Internal Developer Platform (IDP) integration.

Notable quotes:
> "It makes reliability visible across our entire organisation."

Source: https://www.dynatrace.com/customers/sicredi/, verified 2026-09-17
Audience fit: Ops/SRE, AI engineers, platform engineering.
Tag: AI Observability

---

### WGU — Western Governors University (Education)

140,000+ students; non-profit, fully online university.

> "Dynatrace is the evolution which every technology industry should adopt. It's intelligent, it's agile, and it lives up to the promises it makes."
> "When moving to a new observability platform, we wanted the best in the market."

**Key outcomes:**
- Uninterrupted e-learning platform availability during peak periods
- Proactive issue identification before student impact
- Reduced MTTR for system issues
- Enhanced visibility across cloud-native architecture

**Dynatrace use:** End-to-end observability, Smartscape (topology mapping), automated root cause analysis.

Source: https://www.dynatrace.com/customers/wgu/, verified 2026-09-17
Audience fit: Ops/SRE.
Tag: Autonomous Operations
Note: Qualitative; no hard metric. Unique as the only education sector story in corpus.

---

## Customer proof — Platform / Grail (foundation wedge)

These speak to Grail and full-stack observability as the foundation, not AI observability specifically. Use to support the "same platform you already run" wedge.

### Vodafone (Telco)

~360 million customers across 15 countries; €40.5bn revenue (FY'26); 45,000 on-premise servers.

**Luke Bradley, Head of Engineering & Transformation:**
> "With Dynatrace, we increased ingest from 8TB to over 18TB of logs per day while avoiding a 3-4x increase in logging costs."

> "We achieved 100% adoption in just eight weeks, migrating 8,000 dashboards."

**Metrics:**
- Log ingest increased 8TB → 18TB/day
- Avoided 3–4x projected cost increase from incumbent provider
- 8,000 dashboards and 2,500 users migrated in 8 weeks; 100% adoption

**Dynatrace use:** Grail (log management replacing legacy incumbent), full-stack observability (logs, metrics, traces unified), AI-powered insights, AWS integration. Described as foundation for autonomous operations and AI/LLM observability.

Source: https://www.dynatrace.com/customers/vodafone/, verified 2026-09-16
Audience fit: Ops/SRE.

---

### Vestmark (Financial Services)

$1.9+ trillion assets under management; 4.5 million accounts.

> "Dynatrace gives us the confidence to move faster with AI...all in real time."

> "Dynatrace brings all our data together in one place and turns it into actionable information."

> "Dynatrace puts a big red box around the root cause and points us right."

**Dynatrace use:** APM, log management, Dynatrace Intelligence (root cause analysis), OpenLLMetry (AI agent visibility), SLO Guardian (planned). Use case: unified observability for a trading platform with real-time AI cost and quality insights.

Source: https://www.dynatrace.com/customers/vestmark/, verified 2026-09-16
Audience fit: AI engineers, financial services.
Note: The AUM and account figures describe the platform, not a Dynatrace outcome. No quantified improvement cited.

---

## Customer quotes — Dynatrace Intelligence (adjacent, use with care)

**Alexander Bicalho, Autodesk:**
> The approach "connects insight to action, while keeping our teams in control, could significantly improve performance and reliability as we scale."
Source: https://www.dynatrace.com/platform/artificial-intelligence/
Note: This is about Dynatrace Intelligence (Dynatrace's AI running ops), not AI Observability (observing your AI). Conditional tense ("could"). Don't present as an AI-observability result.

## Analyst quote

**Rob Strechay** (analyst; affiliation not stated on page):
> "deterministic AI...reduces costs, increases trust, and enables supervised autonomy that enterprises can actually scale."
Source: https://www.dynatrace.com/platform/artificial-intelligence/
Note: About Dynatrace Intelligence. Affiliation unverified — see gaps.md.

## Stats Dynatrace cites

| Stat | Context | Source | Caveat |
|---|---|---|---|
| 51% of IT and AI executives cite managing and monitoring AI agents at scale as their top operational challenge | FY27 campaign messaging + Arize acquisition post | **Pulse of Agentic AI Report 2026** (confirmed source, internal messaging doc v3.0) | Underlying report not linked publicly; source name confirmed |
| 95% of AI initiatives deliver zero ROI due to failures in pre-production, scaling, or operationalization | Market opportunity framing | MIT, "The GenAI Divide," June 2025 | Internal messaging doc v3.0 cites this; verify the report is publicly accessible before using externally |
| Global AI market: $189B (2023) → $4.8T by 2033 | Market size for Built for AI framing | Internal messaging doc v3.0 | Underlying source not specified; treat as market framing only |
| Monitoring AI systems is SREs' top use case (58%) | SRE / platform-engineering trends post | https://www.dynatrace.com/news/blog/sre-best-practices-platform-engineering-trends/ | Underlying research not linked; full post not fetched |
| 65% of enterprises investing in AI-driven monitoring and automation | Dynatrace Intelligence blog | https://www.dynatrace.com/news/blog/dynatrace-intelligence-at-the-core-of-autonomous-operations/ | Sourced in the blog without linking the underlying study |

## Capability claims usable as proof (feature-level)

- Prompt storage up to 10 years for compliance / data lineage. (https://www.dynatrace.com/solutions/ai-observability/)
- Open-source `dt-evals` CLI with 15 built-in evaluators for continuous evals. (https://www.dynatrace.com/news/blog/evaluate-llm-and-agent-quality-in-dynatrace-ai-observability/)
- Dynatrace Playground public sandbox with sample data. (https://www.dynatrace.com/solutions/ai-observability/)
- Whitepaper: "Full-Stack AI Observability That Increases ROI and Decreases Business Risks." — title only; not fetched.

## What's missing

- **No head-to-head AI-observability comparison** with a named competitor in any customer story.
- **TELUS** — qualitative only; no dedicated customer story page fetched.
- **FreedomPay** — no hard outcome metric in the story.
- **Vestmark** — no quantified improvement cited; AUM figures describe the customer, not a Dynatrace outcome.
- **Autodesk** — conditional tense; Intelligence story, not AI Observability.
- **Rob Strechay's analyst affiliation** — still unverified (gaps.md).
- **Survey stats** — underlying reports not linked by Dynatrace for any of the three stats above.
- **Whitepaper** content not fetched.
