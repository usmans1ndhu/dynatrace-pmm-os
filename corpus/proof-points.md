---
title: Proof Points — Dynatrace AI Observability
last_verified: 2026-09-22
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
  - https://www.dynatrace.com/customers/western-governors-university/
  - https://www.dynatrace.com/customers/careem/
  - https://www.dynatrace.com/customers/cimb/
  - https://www.dynatrace.com/customers/macquarie-bank/
  - https://www.dynatrace.com/customers/sicredi/
---

# Proof Points

**Bottom line: Seven customer stories added 2026-09-16. The strongest AI-specific proof: Accenture (90% MTTR improvement, 20% LLM token reduction, 40% observability cost cut), InPost (Kubernetes issue ID'd in 2 min, resolved in 7 min), CDL (tools reduced 10→1, CSAT +10%), and Vitality (~$1M logging cost reduction, 90%+ cost cut). FreedomPay and TELUS are qualitative but senior. Vodafone and Vestmark are platform/Grail stories that support the foundation wedge. Five Autonomous Operations stories added 2026-09-17. WGU updated to correct URL 2026-09-22; all stories expanded to full depth.**

---

## Customer proof — AI Observability

### InPost (Logistics)

**Company overview:** InPost is a European logistics company specializing in parcel delivery and automated locker networks. Operating across 9 markets, the company has undergone rapid expansion — more than doubling its parcel locker network in two years. InPost is pursuing a cloud-first operating model through a partnership with Google Cloud, with a target of 98% next-day delivery across Europe.

**Scale:** 1.4 billion parcels delivered annually; 18 million annual customers; 61,000+ parcel lockers; 14.7 billion PLN revenue (2025).

**Problem before Dynatrace:** InPost faced difficulty monitoring large volumes of telemetry data from AI workloads, with no visibility into AI model performance or user interactions. They could not identify abnormal behavior such as excessive token consumption. Rapid expansion, acquisitions, and a shift to cloud-native operations compounded complexity, and efficient incident investigation was impossible.

**Dynatrace solutions implemented:**
- Grail (data lakehouse platform) for telemetry centralization
- Dynatrace Intelligence for AIOps and anomaly detection
- MCP (Model Context Protocol) — natural language querying of observability data
- AI observability for monitoring AI shopping agents, logistics forecasting models, and workforce planning models
- OpenTelemetry support across the stack
- Root cause analysis engine for pre-impact issue resolution

**AI use cases observed by Dynatrace:**
- Shopping agent: token consumption monitoring and cost control
- Logistics forecasting models: AI-driven parcel volume prediction
- Workforce planning models: AI-assisted scheduling
- AI-assisted software development: visibility into internal tool adoption

**How Dynatrace solved it:** Dynatrace consolidated telemetry from 61,000+ lockers and multiple AI workloads into Grail. The MCP integration enables developers to query observability data via natural language instead of manual query authorship. AI workloads are monitored for token usage, latency, and anomalous behavior, enabling cost control and faster issue triage.

**Technologies and integrations:** Google Cloud (cloud partnership), Kubernetes, OpenTelemetry.

**Named spokesperson:**
**Mateusz Piasta, Lead Site Reliability Engineer, InPost:**
> "Dynatrace is a big part of why my team is thriving. Observability is mission critical in an AI-first world."

> "Dynatrace gives us real-time visibility across more than 61,000 lockers, helping us maintain consistent service quality."

> "Dynatrace provides visibility into how our AI shopping agent is being used, helping us control token consumption."

> "Observability is mission critical in an AI first world and Dynatrace gives us visibility to reduce blast radius."

**Metrics:**
- Kubernetes incident identified in 2 minutes, resolved within 7 minutes
- 98% next-day delivery target enabled by reliable AI forecasting and observability

Source: https://www.dynatrace.com/customers/inpost-ai/, verified 2026-09-22
Audience fit: Ops/SRE, AI engineers.

---

### CDL (UK Insurtech)

**Company overview:** CDL is a UK-based insurtech provider that powers approximately 60% of UK insurance purchases through aggregators and brokers. The company processes over 1 trillion transactions annually. CDL's platform forms the critical infrastructure — the "veins" — of the UK personal lines insurance market, enabling digital service providers to build consumer-facing websites and applications.

**Recognition:** Ranked in BusinessCloud's InsurTech 50.

**Problem before Dynatrace:** CDL had no visibility into token consumption or LLM costs when they began embedding generative AI into their platform. They operated a fragmented toolchain of 10 separate observability solutions. Identifying issues within their interconnected insurance ecosystem was difficult, and their approach was entirely reactive. They also needed transparency and governance around AI implementation to meet ISO 42001 AI management system certification requirements.

**Dynatrace solutions implemented:**
- AI observability for Amazon Bedrock: full visibility into LLM calls, responses, and costs
- OpenLLMetry support: industry-standard LLM telemetry
- Dynatrace SDK: custom instrumentation for CDL's insurance platform
- Unified observability platform: consolidated metrics, logs, and traces across API Gateway, Lambda, and Bedrock into one system
- Apdex tracking: performance measurement aligned to user experience
- Cost modeling for LLMs: identifying token inefficiencies and pricing models

**How Dynatrace solved it:** Dynatrace provided unparalleled insight into Amazon Bedrock operations through OpenLLMetry support, enabling CDL to model LLM costs, govern AI usage transparently, and accelerate their AI roadmap. The platform replaced 10 fragmented tools with a single source of truth, shifting CDL from reactive to proactive issue resolution.

**Technologies and integrations:** AWS (API Gateway, Lambda, Amazon Bedrock), Anthropic model (version tracking capability identified), OpenLLMetry.

**Named spokespeople:**

**Matt Eisengruber, Head of Architecture, CDL:**
> "To gain our customers' trust, we're going after ISO 42001 certification — AI management system certification. And one of the things that it requires is transparency."

> "When we first started using AI, we knew we needed AI observability and industry standard."

> "AWS gives us the capability to use AI, and Dynatrace gives us the confidence."

> "With the AI observability Dynatrace provides, we were able to accelerate our roadmap significantly."

> "In the generative AI space...Dynatrace helps us ensure responses are consistent and aligned with our AI ethics."

**Chris Buckley, Head of Operations, CDL:**
> "The combination of AWS and Dynatrace put us on the front foot when it comes to cost modeling LLMs."

> "Dynatrace changed the game for CDL...allowing us to go from being reactive to proactively resolving issues before they affect our customers."

**Metrics:**
- CSAT score increased by 10%
- Observability tools reduced from 10 to 1
- Onboarding time for new team members reduced from days to minutes
- LLM token consumption costs reduced by identifying inefficiencies

Source: https://www.dynatrace.com/customers/cdl/, verified 2026-09-22
Audience fit: AI engineers, compliance/governance.

---

### Accenture Life and Annuity Software / ALIP (Insurance SaaS)

**Company overview:** Accenture Life Insurance and Annuity Platform (ALIP) is a modular SaaS solution that transforms new business and policy administration in insurance. It provides comprehensive functionality across the insurance lifecycle, enabling providers to differentiate, improve efficiency, and build customer loyalty. ALIP is named a Leader by Everest Group and won two 2024 XCelent Awards.

**Problem before Dynatrace:** ALIP operated fragmented, custom-built observability tools with no unified visibility. They needed observability across both AWS and Azure cloud environments. Incident resolution times were measured in days rather than minutes. Rising AI adoption costs required optimization. The complexity of modern cloud service architectures — including Quote in a Box, a multi-system pricing engine — made root cause identification slow.

**Dynatrace solutions implemented:**
- Unified observability platform: consolidated 4 monitoring tools and 1 log management solution into one
- Davis AI: automated issue analysis and prediction across the full stack
- Grail: log ingestion alongside telemetry data (metrics, traces, logs unified)
- Live Debugger: real-time production code insights for root cause isolation without reproduction steps
- AI observability: visibility into LLM token consumption across ALIP's agentic AI implementations
- Multi-cloud coverage: unified visibility across AWS and Azure environments

**How Dynatrace solved it:** By replacing five fragmented tools with Dynatrace's unified platform, ALIP eliminated the visibility gaps that delayed incident response. Davis AI automated issue analysis and prediction. Live Debugger enabled real-time root cause isolation. AI observability surfaced token consumption inefficiencies, reducing LLM costs by 20%.

**Technologies and integrations:** AWS, Microsoft Azure, Quote in a Box pricing engine, LLM and agentic AI implementations.

**Named spokesperson:**

**Gaurav Bansal, Managing Director – Product and Technology, Accenture Life and Annuity Software:**
> "Dynatrace gives us X-Ray vision, so we see not only what's happening, but what caused it."

> "With Dynatrace, we ultimately don't have to worry about managing service complexity because we have a partner innovating constantly."

**Metrics:**
- 40% reduction in observability and log management costs
- 90% improvement in MTTR
- Platform availability improved from 99.50% to 99.98%
- 20% reduction in LLM token consumption

Source: https://www.dynatrace.com/customers/accenture/, verified 2026-09-22
Audience fit: Ops/SRE, exec.

---

### Vitality Group (Behavioral Health Insurance)

**Company overview:** Vitality Group is the world's largest behavioral engagement platform, with 49 million members across 40 countries. Part of Discovery Group, Vitality uses behavioral science, economics, and insurance insights to encourage healthier lifestyle choices. The company is developing Vitality AI in partnership with Google to deliver personalized health recommendations leveraging Vertex technology, Gemini models, and 60 million life years of accumulated health data.

**Problem before Dynatrace:** Vitality's log management solution, Elasticsearch, became unaffordable and could not scale with the company's growth. They lacked end-to-end observability across their AI stack. Fragmented monitoring tools reduced engineering efficiency. Log management costs were unsustainable.

**Dynatrace solutions implemented:**
- Grail: replaced Elasticsearch for log consolidation and management; dramatic cost reduction
- Unified observability platform: end-to-end visibility from AI model training and inference to member-facing recommendations
- Clouds App: cloud resource optimization across both AWS and Google Cloud
- AI model performance visibility: monitoring Vitality AI's Vertex AI and Gemini-based recommendations

**AI stack observed by Dynatrace:** Google Vertex AI, Google Gemini models, 60 million life years of health data powering personalized recommendations.

**How Dynatrace solved it:** Dynatrace replaced Elasticsearch with Grail, eliminating unsustainable log management costs. The unified platform provided end-to-end visibility across Vitality AI's training, inference, and member recommendation layers, and enabled active optimization of cloud spend across AWS and Google Cloud. Integration partner Mediro facilitated deployment.

**Technologies and integrations:** Google Vertex AI, Google Gemini AI models, AWS, Google Cloud, Mediro (integration partner).

**Named spokesperson:**

**Hushan Padayachee, Chief Information Officer, Vitality:**
> "Observability is mission critical in an AI-first world. Dynatrace provides answers rather than more data to review and analyze."

> "Dynatrace enabled us to replace our existing log monitoring solution, Elasticsearch."

> "Dynatrace has allowed us to improve productivity across operations and engineering teams by 15 to 20%."

> "Dynatrace has allowed us to significantly optimize our AWS and Google Cloud spend."

**Metrics:**
- ~$1 million saved in log management and analytics expenses
- 90%+ reduction in logging costs
- 15–25% improvement in engineering and operations team productivity
- AWS and Google Cloud spend optimized

Source: https://www.dynatrace.com/customers/vitality-2/, verified 2026-09-22
Audience fit: Ops/SRE, exec.

---

### FreedomPay (Financial Services / Payments)

**Company overview:** FreedomPay is a financial services company providing payment infrastructure for secure, high-volume transactions. The organization operates across retail, hospitality, and financial services sectors, present at hundreds of thousands of sites globally. Key customers include top 5 food service providers and 100+ airports.

**Scale:** 3 billion+ transactions globally; operations across 130+ countries on 5 continents.

**Problem before Dynatrace:** FreedomPay needed to embed generative AI into its platform for transaction analysis, fraud detection, and customer support automation — while maintaining enterprise-grade reliability. The primary challenge: monitoring AI model behavior, token consumption, and costs within a cloud-native Azure architecture without sacrificing visibility or control. AI introduces a level of variability unlike traditional software: the same input can produce different outputs, latency fluctuates, and compliance standards for financial services require full audit trails.

**Dynatrace solutions implemented:**
- End-to-end AI observability with OpenLLMetry: full visibility across every AI interaction
- Unified metrics, logs, and traces: proactive issue identification before transaction flows are impacted
- LLM usage optimization: token cost tracking and reduction
- Compliance and transparency: traceability of AI interactions for financial services governance
- Consolidated monitoring: reduced tool complexity and accelerated team onboarding

**How Dynatrace solved it:** Dynatrace provided immediate insight into how FreedomPay's AI services were performing — cost, quality, latency, and reliability — in a single view. OpenLLMetry gave FreedomPay the standard-compliant telemetry needed to satisfy financial services governance requirements while optimizing AI spend. Full observability accelerated time-to-market for new AI capabilities.

**Technologies and integrations:** Microsoft Azure, OpenLLMetry.

**Named spokesperson:**

**Mark Tomlinson, Senior Director of Observability and Performance, FreedomPay:**
> "We knew early on that if we were going to scale AI responsibly, observability had to come first. Without visibility into how these models behave, you can't build the trust required for enterprise adoption."

> "Dynatrace gave us immediate insight into how our AI services were performing."

> "AI introduces a level of variability we've never had to manage before. Dynatrace gives us the controls to manage that."

> "With Dynatrace, we can ensure consistency, performance, and alignment with our standards."

Source (original quote): https://www.dynatrace.com/solutions/ai-observability/
Source (expanded story): https://www.dynatrace.com/customers/freedompay-3/, verified 2026-09-22
Audience fit: Ops/SRE, exec.
Note: Qualitative; no hard outcome metric published.

---

### TELUS (Telco)

**Company overview:** TELUS is a major Canadian telecommunications company. TELUS is combining agentic AI initiatives with Dynatrace AI Observability to optimize development and operations workflows.

**Named spokesperson:**

**Kulvir Gahunia, Director of the Site Reliability Office, TELUS:**
> "By combining our Agentic AI initiatives with Dynatrace's AI Observability capabilities, we've successfully optimized our development and operations workflows."

Source: https://www.dynatrace.com/solutions/ai-observability/
Audience fit: Ops/SRE.
Note: Qualitative only; no quantified outcome. No dedicated customer story page found.

---

## Customer proof — Autonomous Operations

Complementary to AI Observability. These stories support the "Powered by AI" pillar — from insight to trusted action.

### Careem (Technology / Super-app — Uber company)

**Company overview:** Careem is the "Everything App for the Middle East," operating as an Uber subsidiary since 2019. The platform integrates 20+ services including ride-sharing, food delivery, grocery shopping, and payments. Careem runs entirely on AWS with 800+ microservices on Amazon EKS, processing billions of API calls daily.

**Scale:** 75M+ customers; 3.5M+ Captains (drivers); 20+ services; 800+ microservices; 40TB raw logs processed daily; billions of API calls daily.

**Problem before Dynatrace:** Careem operated a fragmented observability stack with tool overlap and infrastructure redundancy. The team manually processed 40TB of raw logs daily, creating operational noise and high costs. Multiple monitoring systems required manual maintenance. Incident detection and root cause identification were slow. The model was entirely reactive, with limited context-aware analysis and growing scaling challenges as the service portfolio expanded.

**Dynatrace solutions implemented:**
- AI-powered observability platform: consolidated fragmented tools into one authoritative source
- Automated instrumentation: automated data collection across the AWS environment, reducing manual work
- Full-stack monitoring: mobile applications, backend services, Amazon EKS, Apache Kafka
- Unified metrics, logs, and traces: replaces raw log analysis with contextual insight
- AI-driven root cause analysis: accelerates root cause identification from hours to minutes
- Log management with contextual analysis: noise reduction and cost governance
- User experience monitoring: end-to-end visibility into customer-facing surfaces
- AI incident management agent: automatic rollback triggering for self-healing workflows
- Cost governance and usage controls: replaces excessive raw log processing

**How Dynatrace solved it:** Dynatrace eliminated tool overlap and infrastructure redundancy by consolidating Careem's observability into one platform. Automated data collection replaced manual maintenance across multiple systems. AI-powered analysis connected metrics, logs, and traces, enabling sub-2-minute incident detection and 6x faster root cause identification. Self-healing integrations with automatic rollback move Careem toward autonomous operations.

**Technologies and integrations:** AWS (all cloud infrastructure), Amazon EKS (container orchestration), Apache Kafka (messaging), AI incident management agent with automatic rollback capabilities.

**Named spokespeople:**

**Alaa Alkhdarat, Senior SRE Manager, Careem:**
> "By consolidating our observability stack with Dynatrace, we have saved approximately 10,000 engineering hours per year and unlocked a 65% cost reduction vs the previous stack."

> "Dynatrace helps us use logs more efficiently, giving our teams the right data in the right context while reducing noise and cost."

**Ricardo Fernandes, VP Software Engineering, Careem:**
> "Dynatrace has cut our MTTD by 84% to under two minutes and helps us identify root causes more than six times faster."

> "Dynatrace has helped us shift observability from something we had to build and maintain ourselves into a capability we can use to advance the business."

**Metrics:**
- 65% cost reduction vs. previous observability stack
- 84% reduction in MTTD — now under 2 minutes
- 6x faster root cause identification
- ~10,000 engineering hours saved annually
- 99.99% availability SLA maintained

Source: https://www.dynatrace.com/customers/careem/, verified 2026-09-22
Audience fit: Ops/SRE, exec.
Tag: Autonomous Operations + AI Observability

---

### CIMB Bank (Financial Services — ASEAN)

**Company overview:** CIMB Bank is the fifth largest banking group by assets in ASEAN. Founded in 1987 as Bank of Commerce, CIMB serves over 30 million customers with a focus on digital banking across mobile and online channels. In Malaysia alone, their mobile retail banking applications process approximately 100 million transactions monthly.

**Scale:** RM778.7 billion total assets (2025); RM7.9 billion net profit (2025); 33,000+ staff; 30M+ customers across ASEAN; ~100 million mobile transactions/month in Malaysia.

**Problem before Dynatrace:** CIMB had limited visibility across complex hybrid environments. Incident investigation required "war rooms" — extended manual sessions where engineers pieced together where problems were occurring across disparate systems. Engineers spent excessive time troubleshooting rather than innovating. Manual log searching to find root causes was time-consuming and unreliable. The bank's digital banking platform demanded 24/7 reliability that its visibility tooling couldn't support.

**Dynatrace solutions implemented:**
- Unified observability platform: consolidated telemetry across the entire technology stack
- Fusion center: mission-control hub for real-time service health visibility across hundreds of millions of interactions
- Automated root-cause analysis: surfaces issues in seconds rather than through manual investigation
- Dynatrace Intelligence: deterministic AI-driven decision-making replacing reactive approaches
- AIOps capabilities: proactive incident response before customer impact
- Self-healing workflow initiatives: autonomous operations roadmap underway

**How Dynatrace solved it:** Dynatrace replaced war-room incident investigation with a fusion center providing real-time visibility across CIMB's full stack. Automated root-cause analysis identifies issues in seconds. The 90% reduction in alert volume eliminated alert fatigue, allowing engineers to focus on strategic work. Availability scores improved from 0.6 to 0.95.

**Named spokesperson:**

**Ros Yusoff, Group CTO, CIMB Bank:**
> "Dynatrace helps bridge the gap between IT operations and the business by translating complex technical data into clear business KPIs."

> "Our availability scores have improved from around 0.6 to a consistent 0.95 since we adopted Dynatrace."

> "Visibility is everything. Before Dynatrace, we spent time in war rooms piecing together where problems happened."

> "Dynatrace has helped us bring critical incidents close to zero, improving and strengthening operations."

> "We have reduced alert volumes by around 90%, which has completely changed how our teams operate."

**Metrics:**
- Critical incidents reduced to near-zero
- Availability score improved from 0.6 to 0.95
- Alert volumes reduced by 90%
- Root-cause identification in seconds vs. manual war-room investigation

Source: https://www.dynatrace.com/customers/cimb/, verified 2026-09-22
Audience fit: Ops/SRE, exec.
Tag: Autonomous Operations + AI Observability

---

### Macquarie Bank (Financial Services — Australia)

**Company overview:** Macquarie is the retail banking and financial services division of Macquarie Group. Known for delivering safe, secure, simple, and reliable digital banking without legacy technology constraints, Macquarie operates as an agile challenger brand in Australian banking.

**Scale:** 2.2 million customers; A$200B+ in deposits; A$190B+ loan portfolio; targets 99.95% service availability; multi-cloud infrastructure across AWS and Google Cloud Platform.

**Problem before Dynatrace:** Macquarie lacked unified visibility across multi-cloud environments (AWS and GCP). Incident response was reactive, requiring manual investigation across multiple tools. There was no ability to predict or prevent issues proactively. Rapid software delivery — essential for a challenger bank — introduced change risk. Teams lacked shared context across development, reliability, and operations. Industry data: 80% of incidents are caused by change/releases, making automated change validation critical.

**Dynatrace solutions implemented:**
- Dynatrace Intelligence: analyzes system behavior, identifies root causes, and predicts problems before customer impact
- Live Debugger: real-time production code insights without reproduction steps
- Automated Release Verification: tests performance, reliability, and security of new code before promotion
- Unified observability platform: aggregates telemetry from applications, infrastructure, and cloud services across AWS and GCP
- AI as first responder: every incident is investigated by AI, with humans in the loop for guided triage

**How Dynatrace solved it:** Dynatrace enabled Macquarie to shift from reactive to proactive service availability management. The "AI as first responder" model means every incident is automatically investigated before human escalation, reducing time-to-diagnosis. Automated release verification validates changes before production deployment, reducing the risk of introducing incidents. Shared context across teams accelerates collaboration and innovation.

**Technologies and integrations:** Amazon Web Services (AWS), Google Cloud Platform (GCP). Agentic AI and AI-powered coding techniques planned for future implementation.

**Named spokespeople:**

**Phil Grasso-Nguyen, Head of Reliability, Macquarie:**
> "With Dynatrace, we can use AI as a first responder for every incident, with a human in the loop to guide triage."

> "Dynatrace enables us to use AI to reduce risk at every point of change, so we can innovate faster and safer."

> "The best incident is the one that never happens. With Dynatrace, we're building a reliability factory."

> "The capabilities of our technology partners help us push boundaries as a challenger brand."

**Richard Heeley, Head of Technology (BFS Division), Macquarie:**
> "Platforms like Dynatrace play a key role in ensuring we're always there for our customers."

> "Dynatrace helps us move from reactive to proactive service availability management through data, insights, and automation."

**Key outcomes:**
- Significant reduction in major incidents
- Improved MTTD and MTTR
- Proactive reliability and resilience approach
- Safer, faster innovation cycles through automated release verification
- Shared context across development, reliability, and operations teams

Source: https://www.dynatrace.com/customers/macquarie-bank/, verified 2026-09-22
Audience fit: Ops/SRE, exec.
Tag: Autonomous Operations
Note: Outcomes qualitative; no hard metric on incident count or MTTD/MTTR reduction published.

---

### Sicredi (Financial Services — Brazilian Credit Union)

**Company overview:** Sicredi is a leading Brazilian cooperative financial institution founded in 1902, offering 300+ financial services including loans, credit cards, savings accounts, investments, payments, and insurance. The institution operates 1,100+ applications supported by 10,000 components and 7,000 databases, managing 280+ simultaneous business journeys. The organization expanded its agile teams from 40 to 500+ over five years.

**Scale:** $88.6 billion (R$ 454.7 billion) total assets (2025); $60.2 billion (R$ 308.4 billion) total deposits (2025); 50,000+ employees; 10M+ members; 1,100+ applications; 10,000 components; 7,000 databases.

**Problem before Dynatrace:** Sicredi had limited visibility across a complex technology estate of 1,100+ applications. Managing observability across distributed systems was difficult. SLO creation and management was time-consuming — 15 minutes and 6 steps per SLO. The organization could not connect technical metrics to business outcomes. Manual, labor-intensive instrumentation processes slowed teams. Identifying member friction points across digital journeys required manual investigation.

**Dynatrace solutions implemented:**
- Full-stack observability: integrated as a self-service capability into Sicredi's Internal Developer Platform (IDP)
- OpenPipeline: data ingestion and processing technology
- Grail: centralized telemetry management connecting technical performance to business outcomes
- Service-Level Objectives (SLO) management: streamlined from 6 steps to 2, from 15 minutes to 3 minutes
- MCP Server (Model Context Protocol): brings observability data directly into developer workflows and AI assistants
- AI-driven natural language query capabilities: enables AI assistants to analyze telemetry and accelerate debugging
- Business journey mapping: end-to-end visibility from high-level business impact to root cause

**How Dynatrace solved it:** Dynatrace integrated comprehensive observability into Sicredi's IDP as a self-service capability, reducing instrumentation time by 80%. SLO creation was simplified through automated workflows. The MCP Server integration brings telemetry directly into developer tools and AI coding assistants, enabling natural language debugging. Business journey visibility connects every technical metric to member experience outcomes.

**Named spokesperson:**

**Eduardo Abe, Platform Engineering Manager, Sicredi:**
> "Dynatrace helped us reduce the time it takes to instrument our apps with observability by 80%."

> "With Dynatrace, the time it takes to create an SLO has dropped from about 15 minutes to just three, significantly reducing the cognitive effort for our engineers."

> "What Dynatrace gives us is the ability to connect observability telemetry directly to business outcomes. We're no longer just looking at systems – we can see exactly where our members experience friction at every stage of their user journey."

> "The Dynatrace MCP server brings observability data directly into developer workflows, improving developer productivity and enabling AI assistants to analyze telemetry and accelerate debugging."

> "What I value most about Dynatrace is that it makes reliability visible across our entire organisation. It gives everyone a shared view of how our services are performing — which is so powerful, helping our teams innovate faster while delivering the reliable digital experiences our members expect."

**Metrics:**
- 80% reduction in time to instrument applications with observability
- 67% reduction in cognitive load for developers creating SLOs
- SLO creation time: 15 minutes → 3 minutes
- SLO creation steps: 6 → 2
- Enhanced visibility across complete member experience journeys

Source: https://www.dynatrace.com/customers/sicredi/, verified 2026-09-22
Audience fit: Ops/SRE, AI engineers, platform engineering.
Tag: AI Observability

---

### Western Governors University / WGU (Education)

**Company overview:** Western Governors University (WGU) is a leading US nonprofit online education institution founded in 1997. WGU operates fully online and serves students across the United States. Experiencing 20% year-over-year enrollment growth, WGU's technology platform must scale continuously to support an expanding student base.

**Scale:** 192,000+ enrolled students; 500,000+ degrees awarded; 20% year-over-year enrollment growth.

**Problem before Dynatrace:** Before Dynatrace, WGU's biggest issue was lack of visibility across its growing technology ecosystem. Teams could not identify where failures occurred. The previous APM tool lacked fine-grained reporting and actionable dashboards. Complex multi-tool environments created visibility gaps. The inability to pinpoint exact issues quickly meant longer MTTR and risk to the student learning experience.

**Dynatrace solutions implemented:**
- Real-time observability platform: system performance monitoring across WGU's full technology stack
- AWS DevOps Agent integration: native AI-powered automated incident investigation within WGU's AWS deployment
- Automated root cause analysis: pinpoints exact issues quickly without reliance on tribal knowledge
- Business event capture: visibility into the student journey and friction points
- CI/CD pipeline integration: Dynatrace integrated into WGU's AWS deployment pipelines
- Unified log management: consolidated logging across the platform
- Foundation for autonomous operations: Dynatrace positioned as the platform for future AI-driven IT operations agents

**AI capability highlighted — AWS DevOps Agent:** WGU used Dynatrace's integration with an AI-powered AWS DevOps Agent to resolve a production incident in 28 minutes — compared to an estimated 2 hours with manual investigation. This represents a 77% improvement in resolution time for that incident. WGU describes Dynatrace as "critical to our AI vision" for this reason.

**How Dynatrace solved it:** Dynatrace replaced WGU's previous APM tool, which lacked fine-grained reporting. Real-time observability now enables instant identification of where failures occur, eliminating the visibility gaps that previously drove longer MTTR. The AWS DevOps Agent integration showed AI-assisted incident resolution in production: a real incident resolved in 28 minutes instead of the estimated 2 hours. Dynatrace is WGU's "non-negotiable" — the go-to solution for investigating application issues.

**Technologies and integrations:** AWS, AWS Lambda, Amazon EKS (Elastic Kubernetes Service), AWS DevOps Agent.

**Named spokespeople:**

**Angel Marchena, Director of Technical Operations, WGU:**
> "Dynatrace is critical to our AI vision. It gives us real-time assessment of app performance."

> "Before Dynatrace, our biggest issue was lack of visibility. Now we pinpoint exact issues quickly."

**Nate Cummings, Senior Director of Infrastructure, WGU:**
> "Dynatrace has become our go-to solution to investigate application issues."

> "Dynatrace is one of our non-negotiables."

**Metrics:**
- MTTR reduction: from days to hours
- 77% improvement in incident resolution speed for key incidents using AI-powered AWS DevOps Agent
- Production incident resolved in 28 minutes vs. estimated 2 hours

Source: https://www.dynatrace.com/customers/western-governors-university/, verified 2026-09-22
Audience fit: Ops/SRE.
Tag: Autonomous Operations

---

## Customer proof — Platform / Grail (foundation wedge)

These speak to Grail and full-stack observability as the foundation, not AI observability specifically. Use to support the "same platform you already run" wedge.

### Vodafone (Telco)

**Company overview:** Vodafone Group is one of Europe and Africa's largest telecommunications providers, serving approximately 360 million customers across 15 countries with 40+ global telecoms partners. Vodafone generated €40.5bn in revenue (FY'26) and operates complex digital infrastructure spanning 45,000 on-premises servers and multi-cloud environments across all major hyperscalers.

**Problem before Dynatrace:** Vodafone's legacy log management solution had an unsustainable financial model — maintaining their existing log volume would require a 3-4x cost increase from their incumbent provider. Their observability approach was a "patchwork quilt" of disparate solutions. They could not capture and contextualize all observability data at scale. Resolving issues quickly within their complex, distributed infrastructure was difficult, and the existing tooling didn't align with their cloud-first and AI-driven strategic vision.

**Dynatrace solutions implemented:**
- Dynatrace Grail: enabled rapid scaling of log consumption (8TB → 18TB/day) while controlling costs
- Unified observability platform: consolidated logs, metrics, traces, and digital experience monitoring into a single suite
- AI-powered insights: embedded into development and testing cycles for shift-left engineering
- Full-stack observability: covers on-premises (45,000 servers) and all major cloud environments
- Contextualized data querying: any data, any time, without cost concerns
- Foundation for autonomous operations: positioned as the platform for Vodafone's AI and LLM roadmap

**Partnership model:** Vodafone partnered with Dynatrace, Accenture, and AWS to execute the migration. Accenture established a center of excellence. AWS ecosystem integration accelerated adoption. 100% adoption achieved in 8 weeks.

**How Dynatrace solved it:** Dynatrace Grail enabled Vodafone to more than double log ingestion (8TB → 18TB/day) while avoiding the 3-4x cost increase their incumbent would have required. The unified platform replaced the patchwork of disparate solutions with a single source of truth. 8,000 dashboards and 2,500 users migrated in 8 weeks. Dynatrace is described as the foundation for Vodafone's AI roadmap — providing assurance and observability into AI and LLMs going forward.

**Technologies and integrations:** AWS (ecosystem integration), Accenture (systems integrator / center of excellence), all major cloud hyperscalers, 45,000 on-premises servers.

**Named spokespeople:**

**Luke Bradley, Head of Engineering & Transformation, Vodafone Group:**
> "With Dynatrace, we increased ingest from 8TB to over 18TB of logs per day while avoiding a 3-4x increase in logging costs."

> "Vodafone partnered with Dynatrace, Accenture and AWS to modernize our log management capabilities."

> "We achieved 100% adoption in just eight weeks, migrating 8,000 dashboards and nearly 2,500 users from our incumbent logging solution."

> "Dynatrace will play a critical role in Vodafone's AI roadmap by providing assurance and observability into the AI and LLMs."

**Afsheen Rahiman, Head of Test, Release and Environments, Vodafone Three:**
> "Dynatrace gives us faster insight into critical user journeys, which helps us improve the customer experience. We can query any data, any time, without worrying about cost."

**Metrics:**
- Log ingest increased 8TB → 18TB/day
- Avoided 3–4x projected cost increase from incumbent provider
- 8,000 dashboards and 2,500 users migrated in 8 weeks
- 100% adoption achieved in 8 weeks

Source: https://www.dynatrace.com/customers/vodafone/, verified 2026-09-22
Audience fit: Ops/SRE.

---

### Vestmark (Financial Services / Wealth Management)

**Company overview:** Vestmark is a financial services firm providing portfolio management and financial advisor trading platforms. Founded in 2001, Vestmark manages $1.9+ trillion in assets across 4.5 million accounts. Their platform supports time-sensitive trading activity where service unavailability during trading hours could prevent timely trade execution and directly impact client financial outcomes.

**Problem before Dynatrace:** Vestmark had siloed data sources and no unified observability. Teams switched between multiple systems to gather insights, slowing incident response. In a business-critical trading environment where milliseconds matter and downtime creates direct financial consequences, this was unacceptable. The company also lacked visibility into emerging AI agent performance — costs, quality, and reliability of AI systems were opaque.

**Dynatrace solutions implemented:**
- Unified observability platform: consolidated all monitoring into a single source of truth
- Application performance monitoring: end-to-end coverage across the trading platform
- Log management: unified log analysis alongside metrics and traces
- Dynatrace Intelligence: root cause analysis that identifies the precise source of problems
- OpenLLMetry: visibility into AI agent costs, quality, controls, and reliability in real time
- Dynatrace SLO Guardian: planned implementation for automated SLO monitoring
- Pre/post-deployment performance comparison: safer releases in a risk-sensitive trading environment

**How Dynatrace solved it:** Dynatrace eliminated tool-switching by consolidating all observability into one platform. Dynatrace Intelligence identifies root cause automatically ("puts a big red box around the root cause"), pointing teams in the right direction instead of requiring manual log analysis. OpenLLMetry integration extends this visibility to Vestmark's AI agents. Pre/post-deployment comparison enables confident, validated releases for a platform where production errors have direct client consequences.

**Technologies and integrations:** OpenLLMetry (LLM/AI observability standard), Gartner Magic Quadrant (referenced as selection criterion for Dynatrace).

**Named spokespeople:**

**Dan Mezynski, Senior Manager, Observability Engineering, Vestmark:**
> "Dynatrace gives us the confidence to move faster with AI. We can see exactly how our agents are performing—cost, quality, and reliability—all in real time."

> "Dynatrace brings all our data together in one place and turns it into actionable information."

> "When you're responsible for other people's money, reliability isn't optional."

> "Dynatrace puts a big red box around the root cause of a problem and points us in the right direction."

**Justin Keating, Senior Manager, Production Support, Vestmark:**
> "With Dynatrace, we're able to follow the journeys our clients are having day to day."

> "What I love most about Dynatrace is that it brings all of our data together into one place."

**Key outcomes:**
- Unified observability across all data sources, eliminating tool-switching
- Accelerated incident resolution through intelligence-driven root cause identification
- Confident, validated deployments with pre/post-release performance comparison
- Real-time AI agent visibility: cost, quality, and reliability

Source: https://www.dynatrace.com/customers/vestmark/, verified 2026-09-22
Audience fit: AI engineers, financial services.
Note: $1.9T AUM and 4.5M accounts describe the customer's platform, not a Dynatrace outcome. No quantified improvement metric published.

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
- **TELUS** — qualitative only; no dedicated customer story page found.
- **FreedomPay** — no hard outcome metric in the story.
- **Vestmark** — no quantified improvement cited; AUM figures describe the customer, not a Dynatrace outcome.
- **Macquarie** — outcomes qualitative; no hard MTTD/MTTR numbers published.
- **Autodesk** — conditional tense; Intelligence story, not AI Observability.
- **Rob Strechay's analyst affiliation** — still unverified (gaps.md).
- **Survey stats** — underlying reports not linked by Dynatrace for any of the three stats above.
- **Whitepaper** content not fetched.
