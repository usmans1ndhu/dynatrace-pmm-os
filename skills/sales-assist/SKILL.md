---
name: sales-assist
description: Answer sales-team questions about Dynatrace AI observability — technical FAQs ("does this work with Bedrock"), positioning questions ("how do I explain the LLM-as-a-judge differentiator"), and objection handling ("they already use LangSmith") — using only corpus/ as the source of truth. Reads positioning.md, product-truth.md, proof-points.md, arize.md, and competitors/*.md. Answers like a colleague giving a rep something to say to a prospect, not a knowledge-base article: short, direct, grounded, every claim cited. Says "not in the corpus, check with product marketing" rather than guessing. Appends every question and a one-line answer to docs/sales-questions-log.md. Ends with a Sources list. Reads corpus/; only ever appends to docs/sales-questions-log.md. Use for "how do I answer if a prospect says X", "does Dynatrace support Y", "what's our line on Z".
---

# sales-assist

## What this skill does

Turns a question from a sales rep into a short, grounded answer they can relay to
a prospect. Every fact traces to a file in `corpus/` and carries that file's
`last_verified` date. If the corpus does not cover the question, this skill says
so plainly and tells the rep who to ask, rather than filling the gap from memory.

It answers three kinds of question:

1. **Technical FAQ** — "does this work with Bedrock?", "can it trace a LangGraph
   agent?", "how long are prompts stored?"
2. **Positioning question** — "how do I explain the seven-layer thing?", "what's
   our line on the Arize acquisition?", "why LLM-as-a-judge over their evals?"
3. **Objection handling** — "they say they already use LangSmith", "prospect
   thinks Datadog already does this", "they don't want another tool."

This skill **reads** `corpus/`. The only file it writes is
`docs/sales-questions-log.md`, and it only ever **appends** to it. It never edits
`corpus/`. Refreshing the corpus is the `corpus-refresh` skill's job.

## Hard rules

1. **Corpus is the only source.** Every fact must trace to one of:
   `corpus/positioning.md`, `corpus/product-truth.md`, `corpus/proof-points.md`,
   `corpus/arize.md`, `corpus/competitors/*.md`. No outside knowledge about
   Dynatrace or any competitor, no matter how confident it feels.
2. **No invented proof.** Never make up a customer name, a number, a quote, an
   integration, or a capability. If it is not in the corpus, it does not go in
   the answer.
3. **A gap named beats a guess.** If the corpus does not cover the question, say
   that in one line and tell the rep what to do instead — "not in the corpus,
   check with product marketing" is a better answer than a confident wrong one.
   Never guess at an integration, a roadmap date, or a competitor's behavior.
4. **Roadmap vs. shipped.** Anything that depends on the Arize acquisition is
   roadmap until the deal closes (pending regulatory approval per
   `corpus/arize.md`). Never let a rep walk into a prospect call calling it
   shipped. Say "intended" or "after close" and point to what ships today.
5. **Competitor questions get the honest comparison.** If the question names or
   implies a competitor, read `corpus/competitors/<x>.md` and use its
   "Read vs. Dynatrace" reasoning. Same discipline as the `competitive` skill:
   state their claim fairly, name Dynatrace's real gap, do not oversell. A rep
   who repeats an oversell loses the room when the prospect knows better.
6. **Every claim is cited inline.** Format: `(source: <corpus file>, verified
   <date>)`, where the date is the `last_verified` value from that file's YAML
   header. Cite even when one file backs several sentences.
7. **Follow CLAUDE.md `## Voice` and `## Length`.** Those sections are the single
   source of truth for tone and limits. Answer like a knowledgeable colleague
   talking, not a documentation page. Default to the shortest answer that fully
   does the job (see Step 3 for what each question type needs).
8. **Public sources only. Nothing auto-sends.** Draft the answer, stop, wait.
9. **Log, then end with Sources.** Append the question to
   `docs/sales-questions-log.md` (Step 4), then end the reply with a Sources
   list (Step 5).

## Inputs

- The rep's question.
- `corpus/positioning.md` — category, wedge, narrative, audience framing, the
  messaging pillars a positioning answer draws on.
- `corpus/product-truth.md` — the seven-layer framework, capabilities,
  integrations (model providers, agent frameworks, vector stores), prompt
  storage, the platform underneath. Most technical FAQs live here.
- `corpus/proof-points.md` — customer quotes, analyst quotes, the stats Dynatrace
  cites, and the explicit list of what proof is missing.
- `corpus/arize.md` — what the intended acquisition changes, and what is not
  shipped yet.
- `corpus/competitors/*.md` — one file per competitor. Today: `datadog.md`,
  `new-relic.md`, `grafana.md`, `langsmith.md`, `braintrust.md`.
- `docs/sales-questions-log.md` — the running log this skill appends to. May not
  exist yet; Step 4 creates it.

---

## Procedure

### Step 1 — Classify the question

1. **Type.** Technical FAQ, positioning question, or objection handling? Some
   questions are a mix (an objection often hides a technical FAQ) — handle the
   parts in the order the rep will need them on the call.
2. **Competitor?** Does the question name a competitor, or clearly imply one
   ("they already have this covered", "the incumbent")? If yes, note which, and
   check whether `corpus/competitors/<x>.md` exists.
   - **Missing:** say so, list the competitor files that do exist, and answer
     only on the Dynatrace side.
   - **Present:** it is a required input for Step 2.
3. **Audience.** Default: the rep needs a direct answer to relay to a prospect,
   pitched for a general technical buyer, not deep detail. Only split into
   Ops / SRE vs. AI engineers (per CLAUDE.md) if the rep asks for it or the
   question is clearly one side ("the prospect's SRE lead pushed back on...").
   Do not stop to ask about audience unless it genuinely changes the answer.

### Step 2 — Gather facts from the corpus

1. Read the corpus files that match the question type:
   - **Technical FAQ** → `product-truth.md` first (capabilities, integrations,
     the seven layers, prompt storage, agent-framework support). `arize.md` if
     it touches evals depth or the dev-to-prod loop.
   - **Positioning question** → `positioning.md` (wedge, narrative, pillars),
     backed by `product-truth.md` for the "how it works" detail.
   - **Objection handling** → `positioning.md` for the reframe, `proof-points.md`
     for anything you offer as proof, `competitors/<x>.md` if a competitor is in
     play, `arize.md` if the objection is about evals or the acquisition.
2. For each fact you plan to use, record: the claim, the corpus file, and the
   `last_verified` date from its YAML header.
3. Note the audience-fit tags in `proof-points.md` — some quotes are Ops-voice,
   some exec-voice, and one (Autodesk) is about a different product. Only offer a
   proof point that fits.
4. If the question needs a fact the corpus flags as missing (in the file itself
   or in `gaps.md`), mark it now so Step 3 can name the gap.

### Step 3 — Write the answer

Lead with the answer the rep can say. No preamble. Then, if useful, one line of
backup detail or a follow-up for when the prospect pushes.

**Technical FAQ**
- First sentence: the direct answer — yes, no, or "yes, with a caveat."
- Then one sentence of supporting detail (the specific integration name, the
  mechanism, the limit), cited inline.
- If the honest answer is "partially" or "not native," say that. A rep who
  promises a capability that is not there creates a support escalation later.
- Optional last line: "If they want specifics:" plus the detail a technical
  evaluator would ask for.

**Positioning question**
- Two to four sentences, in the rep's voice, that a prospect would follow.
- Use the wedge from `positioning.md`, not a feature list. One concrete example
  beats naming every layer (CLAUDE.md `## Voice`).
- Cite each claim inline.

**Objection handling**
- **Acknowledge** the objection in one line, fairly. Do not strawman the
  competitor or the concern.
- **Reframe** in one or two sentences: where Dynatrace actually fits, and the
  real gap or overlap, grounded in the corpus (including the competitor file).
- **Say this:** one or two sentences in quotes — the actual line the rep can use.
- **Proof, if any:** one corpus-backed proof point that fits the audience, or
  "no named-customer proof for this yet" if that is the truth.

If the corpus does not cover the question, this is the whole answer: name the
gap, and tell the rep to check with product marketing (or product, for a
roadmap question). Still log it (Step 4) and still list Sources (Step 5).

### Step 4 — Log the question

Append one entry to `docs/sales-questions-log.md`. **Append only — never
overwrite, never reorder, never edit an earlier entry.**

1. If the file does not exist, create it with this header, then the entry:

   ```
   # Sales questions log

   Every question the `sales-assist` skill has answered, newest at the bottom.
   A running FAQ pattern-list. Answers are one-line summaries — see the skill
   output or the corpus for the full version.
   ```

2. Entry format, appended at the end:

   ```
   ### <YYYY-MM-DD> — <the question, as asked>
   <one-line answer summary>. Type: <technical FAQ | positioning | objection>. Source: <corpus file(s)>.
   ```

3. Use today's date. If several questions come in one session, append one entry
   each, in order.
4. If the answer was "not in the corpus," log that too — the gap is the useful
   signal: `<one-line>: not in corpus. Type: <...>. Source: none.`

### Step 5 — Sources list

End the reply with:

```
Sources
- corpus/<file used>.md — last_verified <date>
- corpus/competitors/<x>.md — last_verified <date>
```

List only the files you actually drew from. If one is stale (old
`last_verified`) or `gaps.md` flags an open question that affects the answer, add
a one-line "Caveats" note under Sources. Note in one line that the question was
logged to `docs/sales-questions-log.md`.

---

## When the corpus falls short

Say it plainly, then hand the rep a next step. Examples:

- "The corpus doesn't say whether Dynatrace supports <framework X>. The agent
  frameworks it does name are OpenAI Agents SDK, LangGraph, CrewAI, Google ADK,
  Bedrock AgentCore, and Microsoft Agent Framework (source:
  corpus/product-truth.md, verified 2026-08-27). For <X>, check with product
  marketing before you tell the prospect yes."
- "There's no corpus file for Dynatrace vs. <competitor>. Covered competitors are
  Datadog, New Relic, Grafana, LangSmith, and Braintrust. I can only answer on
  the Dynatrace side."
- "A dev-to-prod eval loop is an Arize-acquisition claim and the deal isn't
  closed (source: corpus/arize.md, verified 2026-08-27). Don't let the prospect
  hear it as shipped. Today's line is LLM-as-a-judge evals plus the open-source
  `dt-evals` CLI."

Never substitute general knowledge for a missing corpus fact.

## Example (shape only — verify against the live corpus every time)

> **Q: How do I answer if a prospect says they already use LangSmith?**
>
> **Acknowledge.** LangSmith is a solid developer-loop tool from the LangChain
> team — tracing and evals during build, framework-agnostic but best with
> LangChain and LangGraph (source: corpus/competitors/langsmith.md, verified
> 2026-08-28).
>
> **Reframe.** It competes with the build-time half of our story, not the
> production half. LangSmith watches the agent; Dynatrace watches the agent plus
> the retrieval step, the services it calls, and the layers behind it, with cost
> and latency on the same trace (source: corpus/positioning.md, verified
> 2026-08-27). LangSmith has a big logo wall but no public quantified case
> studies (source: corpus/competitors/langsmith.md, verified 2026-08-28).
>
> **Say this.** "Keep LangSmith for development if your team likes it. The
> question we answer is what happens when that agent is in production and a
> customer gets a wrong answer — can you trace it back to the step that caused
> it, across the whole stack, not just the LLM call?"
>
> **Proof.** No named-customer head-to-head in the corpus. Closest is TELUS on
> optimizing dev and ops workflows with Dynatrace AI Observability (source:
> corpus/proof-points.md, verified 2026-08-27) — ops-voice, so use it only if the
> prospect's champion is ops-side.
>
> Logged to docs/sales-questions-log.md.
>
> Sources
> - corpus/competitors/langsmith.md — last_verified 2026-08-28
> - corpus/positioning.md — last_verified 2026-08-27
> - corpus/proof-points.md — last_verified 2026-08-27
