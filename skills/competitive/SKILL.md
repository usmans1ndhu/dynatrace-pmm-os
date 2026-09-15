---
name: competitive
description: Answer competitive questions about Dynatrace AI observability using only corpus/ as the source of truth. Reads positioning.md, product-truth.md, proof-points.md, arize.md, and competitors/*.md. Produces a short battle card by default — Dynatrace strength, their claim, the honest gap or caveat, one differentiator to lead with — with an inline source and last_verified date on every claim, and a Sources list at the end. Says so plainly when the corpus does not cover something asked about. Never invents a fact and never writes to corpus/. Use for "how do we compare to X", "battle card vs X", "what do we say against X on Y".
---

# competitive

## What this skill does

Turns a competitive question into a grounded answer built **only** from `corpus/`.
Every claim carries its source and the `last_verified` date of the file it came
from. If the corpus does not cover what was asked, this skill says that out loud
rather than filling the gap from memory.

This skill is **read-only**. It never edits or adds to `corpus/`. Refreshing the
corpus is the `corpus-refresh` skill's job.

## Hard rules

1. **Corpus is the only source.** Every fact must trace to one of:
   `corpus/positioning.md`, `corpus/product-truth.md`, `corpus/proof-points.md`,
   `corpus/arize.md`, `corpus/competitors/*.md`. No outside knowledge about any
   competitor, no matter how confident it feels.
2. **No invented proof.** Never make up a customer name, a number, a quote, or a
   capability. If it is not in the corpus, it does not go in the answer.
3. **Name the gaps.** If `corpus/competitors/<x>.md` does not exist, or exists but
   is silent on the thing asked about, state that plainly: "The corpus doesn't
   cover X." Do not guess.
4. **Every claim is cited inline.** Format: `(source: <url or corpus file>,
   verified <date>)`. The date is the `last_verified` value from the corpus
   file's YAML header. When a single corpus file backs a run of claims, cite it
   on each claim anyway — brevity does not beat traceability here.
5. **Follow CLAUDE.md.** BLUF in the first two sentences. Plain language a smart
   10-year-old could follow. No governance-speak, no vendor buzzwords, no
   corporate filler ("leverage", "seamless", "robust", "end-to-end", "synergy",
   "best-in-class", "unlock", and their cousins). Minimal em-dashes.
6. **Public sources only.** The corpus is already public-only; keep it that way.
   Never pull in anything behind a login.
7. **Nothing auto-sends.** Draft the card, stop, wait.
8. **End with Sources.** Every output ends with a "Sources" list naming every
   corpus file used and its `last_verified` date.

## Inputs

- The question or request (e.g. "how do we compare to Datadog on agent
  observability", "battle card vs LangSmith").
- `corpus/competitors/*.md` — one file per competitor. Today: `datadog.md`,
  `new-relic.md`, `grafana.md`, `langsmith.md`, `braintrust.md`.
- `corpus/positioning.md`, `corpus/product-truth.md`, `corpus/proof-points.md` —
  the Dynatrace side.
- `corpus/arize.md` — what the intended Arize acquisition changes (and what is
  not shipped yet).

---

## Procedure

### Step 1 — Identify the competitor and the angle

1. Pull the competitor name and the topic from the question. "Agent
   observability", "evals", "pricing", "customer proof", "integrations" are all
   different angles and pull from different parts of the corpus.
2. Check whether `corpus/competitors/<competitor>.md` exists.
   - **Missing:** say so. List the competitor files that *do* exist. Offer to
     answer only on the Dynatrace side (positioning / product-truth / proof-points)
     if that is useful, and stop there.
   - **Present:** continue.

### Step 2 — Confirm the audience

Per CLAUDE.md, every piece of writing targets one audience:

1. **Ops / SRE** — thinks in SLOs, MTTR, dashboards, alerts.
2. **AI engineers / developers** — thinks in traces, evals, tokens, tool calls,
   prompt versions.

If the question makes the audience obvious (e.g. "battle card for our SRE team",
"what do I tell a platform engineer", or a topic that is clearly one side like
"eval workflow" → AI engineers), infer it and say which you picked in one line.

If it is genuinely ambiguous, **ask** before writing. One question, two options.

### Step 3 — Gather facts from the corpus

1. Read `corpus/competitors/<competitor>.md` in full. Note its `last_verified`
   date and every source URL in its header.
2. Read the relevant Dynatrace-side file(s):
   - positioning / narrative / wedge → `positioning.md`
   - specific capabilities, the seven-layer framework, integrations →
     `product-truth.md`
   - customer quotes, stats, ROI claims → `proof-points.md`
   - anything about evals depth, dev-to-prod loop, Phoenix/AX/OpenInference →
     `arize.md` (and be clear about what is intended vs. shipped)
3. For each fact you plan to use, record: the claim, the source URL (or corpus
   file), and the `last_verified` date.
4. If the competitor file has a "Read vs. Dynatrace" section, use it — it is the
   pre-reasoned comparison. Do not go beyond what it and the other corpus files
   support.

### Step 4 — Write the battle card (default format)

Keep it short. Four parts, in this order:

1. **BLUF** — one or two sentences: the honest headline of how Dynatrace compares
   to this competitor on this angle, for this audience.
2. **Dynatrace strength** — what Dynatrace does well here, 1–3 bullets, each
   cited inline.
3. **Their claim** — what the competitor says it does, from their corpus file,
   1–3 bullets, each cited inline. State it fairly; do not strawman.
4. **The honest gap or caveat** — where Dynatrace is weaker, where the claim is
   unproven, or where the corpus can't say. Include Dynatrace's own gaps
   (e.g. thin public customer proof, evals depth pending the Arize close). Cited
   inline, including "corpus doesn't cover this" where that is the truth.
5. **Lead with this** — one differentiator to open the conversation on. One
   sentence. Must be supported by a cited claim already in the card.

Then the Sources list (Step 5).

If the user asked for a different format (one-liner, email paragraph, talk
track, longer brief), give them that instead — but keep every inline citation
and still end with Sources.

### Step 5 — Sources list

End every output with:

```
Sources
- corpus/competitors/<competitor>.md — last_verified <date>
- corpus/positioning.md — last_verified <date>
- corpus/<other files used>.md — last_verified <date>
```

List only the files you actually drew from. If any of those files is itself
stale (its `last_verified` is old) or flags open questions in `gaps.md` that
affect this answer, add a one-line "Caveats" note under Sources.

---

## When the corpus falls short

Say it in plain words. Examples:

- "There's no corpus file for **Dynatrace** vs. **Splunk** — the competitors
  covered are Datadog, New Relic, Grafana, LangSmith, and Braintrust."
- "`corpus/competitors/braintrust.md` doesn't list Braintrust's integrations —
  its own landing page doesn't enumerate them (source: braintrust.md, verified
  2026-08-28). I can't fill that in."
- "The corpus has no head-to-head pricing for either product. Nothing public to
  cite."

Never substitute general knowledge for a missing corpus fact. A gap named is
more useful than a guess.

## Example (shape only — verify against the live corpus every time)

> **Battle card: Dynatrace vs. Datadog — agent observability — audience: Ops / SRE**
>
> **BLUF.** Datadog is the closest match to our pitch: one platform, ops and
> quality signals in one trace, buyer already owns it. We win on the span from
> infrastructure to business impact; they're ahead on the pre-production
> developer loop.
>
> **Dynatrace strength**
> - Seven-layer view from infrastructure up to business impact, not just the
>   LLM call (source: corpus/positioning.md, verified 2026-08-27).
> - ...
>
> **Their claim**
> - "Trace every agent step", execution-graph inspection, tool-decision
>   tracking (source: corpus/competitors/datadog.md, verified 2026-08-28).
> - ...
>
> **The honest gap or caveat**
> - Datadog has named customer quotes with an AI-observability attribution;
>   our public AI-observability quotes are fewer — TELUS and FreedomPay
>   (source: corpus/proof-points.md, verified 2026-08-27).
> - Native dev-loop evals depth is the piece we're buying with Arize, not
>   shipped yet (source: corpus/arize.md, verified 2026-08-27).
>
> **Lead with this.** "You already page on latency and errors — we put cost
> spikes, quality drift, and guardrail failures on the same problem card, tied
> to the business process the agent runs."
>
> Sources
> - corpus/competitors/datadog.md — last_verified 2026-08-28
> - corpus/positioning.md — last_verified 2026-08-27
> - corpus/proof-points.md — last_verified 2026-08-27
> - corpus/arize.md — last_verified 2026-08-27
