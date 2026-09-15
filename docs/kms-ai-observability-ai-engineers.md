---
title: Key Messaging Statement — Dynatrace AI Observability
audience: AI engineers
last_verified: 2026-08-27
generated: 2026-08-31
corpus_sources:
  - corpus/positioning.md
  - corpus/product-truth.md
  - corpus/proof-points.md
  - corpus/arize.md
---

# Key Messaging Statement — Dynatrace AI Observability

**Audience: AI engineers**

Your LLM and agent apps are production code a stack trace can't debug: they run
clean and still return wrong, ungrounded, or PII-leaking answers. Dynatrace
traces frontend to agent calls, putting token cost, latency, and eval scores on
the same spans, with root cause inside the chain. You debug a wrong answer and a
slow one in one place.

*(59 words. Beats: the point = your AI app is undebuggable production code; the
problem = it fails silently; the solution = one trace carrying ops and quality
signals with chain-level root cause; the outcome = wrong and slow answers
debugged in the same place.)*

## Drift check

No prior saved Key Messaging Statement in `docs/`. This is the anchor. Demand gen
and event abstracts for the AI-engineer audience should align to it.

## Caveats

- **No developer-voice customer proof in the corpus.** Both named AI Observability
  quotes (TELUS, FreedomPay) are ops/SRE voice, and no public hard number (tokens
  saved, eval-score gain, MTTR) ties to a named customer (source:
  corpus/proof-points.md, verified 2026-08-27). The proof you can verify yourself
  is the open-source `dt-evals` CLI and the public Dynatrace Playground sandbox
  (source: corpus/product-truth.md, verified 2026-08-27).
- **"Ops and quality on the same spans" is positioning, assembled from shipped
  parts.** The one-trace framing traces to corpus/positioning.md (verified
  2026-08-27), which quotes the Arize announcement blog. The underlying pieces
  each ship today per corpus/product-truth.md (verified 2026-08-27): end-to-end
  tracing across frontend, backend, orchestration, RAG, LLM, and agentic layers;
  LLM-as-a-judge evals for accuracy, relevance, grounding; model-layer token cost
  and latency; automatic root cause in LLM chains.
- **The dev-to-prod eval loop is roadmap.** Building and evaluating with Phoenix /
  Arize AX and feeding production results back depends on the Arize acquisition,
  signed 2026-08-13 but not closed, pending regulatory approval (source:
  corpus/arize.md, verified 2026-08-27). Everything in the statement ships today.
  OpenInference instrumentation is already supported.

## Sources

- corpus/positioning.md — last_verified 2026-08-27
- corpus/product-truth.md — last_verified 2026-08-27
- corpus/proof-points.md — last_verified 2026-08-27
- corpus/arize.md — last_verified 2026-08-27
