---
title: Competitor — Braintrust
last_verified: 2026-08-28
audience: ai-engineers  # developer/eval-first; not an ops/SRE story
sources:
  - https://www.braintrust.dev/
---

# Braintrust — "Active observability platform for agents"

**Bottom line: Braintrust is eval-first. The loop is: watch production, turn patterns into evals, gate releases on them. It competes with the Arize half of Dynatrace's story and has the strongest named-customer proof of the five competitors (Vercel, Notion, Coursera, Replit, Box, Cloudflare).**

## Positioning

Headline: "Ship quality agents at scale." Sub: "Surface patterns in production, turn them into evals, and improve quality with every release." Self-description: "Braintrust — The active observability platform for agents." (https://www.braintrust.dev/)

## What they claim to observe

Source: https://www.braintrust.dev/

Three pillars:
- **Trace everything** — "Inspect prompts, responses, and tool calls in real time"
- **Measure quality with evals** — "Score outputs with LLMs, code, or humans"
- **Catch issues early** — "Block bad releases before they hit production"

**Observe module:** scalable agent trace ingestion; live performance monitoring; custom views and annotation; "inspect every agent trace and tool call, search across millions of logs, and track latency, cost, and quality."

**Evaluate module:** fast prompt engineering; versioned datasets; automated and human scoring; "run experiments against real datasets, compare prompts and models."

**Discover / Topics module:** automatic pattern discovery; continuous online scoring; quality gates and alerts; "Topics surfaces patterns in real time across task, issues, and sentiment."

**Other:** Loop agent (AI-assisted optimization); custom facets; task-specific trace views; trace-to-dataset conversion; MCP integration; "framework agnostic SDKs."

**Brainstore** — "proprietary database for AI data."

## Named integrations

Source: https://www.braintrust.dev/

- **SDKs:** Python, TypeScript, Go, Ruby, C#
- **Protocol:** MCP (Model Context Protocol)
- Framework-agnostic; the landing page does not enumerate specific model providers or frameworks (those are in the docs, not fetched this pass — see gaps.md)

## Public customer proof

Quotes (https://www.braintrust.dev/):
- **Cloudflare** — Kylie Czajkowski, Engineering Manager, Agent Experience: "We get to iterate directly in development and then ship it to production."
- **Pylon** — Fred Zhao, Software Engineer: "This discipline is what Braintrust was built for."
- **Box** — Matt Terrell & Sidharth Srinivasan, Product Management: "Braintrust is our single source of truth for all of our datasets."
- **Replit** — Luis Héctor Chávez, CTO: "Braintrust helped us identify several patterns that we wouldn't have found."
- **Vercel** — Malte Ubl, CTO: "We didn't realize we needed deep observability until Braintrust."

Case-study metrics (https://www.braintrust.dev/):
- **Coursera** — "45x More feedback with AI grading"
- **Notion** — "<24hrs To deploy a new frontier model" (70 engineers)
- **Graphite** — "5% Reduction in negative rules"

## Read vs. Dynatrace

- **Not an ops competitor.** No infra, APM, GPU, or business-process layer. Overlaps Dynatrace only on trace + eval + dataset workflow.
- Directly overlaps the **Arize acquisition** (arize.md) and LangSmith — the eval-first developer platform category.
- Braintrust's proof (named CTOs, frontier-model deployment speed) is **sharper and more quantified** than Dynatrace's public AI proof. If a prospect is comparing eval tooling, Braintrust wins the reference battle today.
- Dynatrace's answer is scope: Braintrust stops at "is the agent good?"; Dynatrace claims "and is the system healthy, and did the business process improve?"
