---
name: writer
description: Generate market-facing GTM copy for Dynatrace AI observability using only corpus/ as the source of truth, in three modes — Key Messaging Statement (the foundational anchor), Demand Gen copy (campaign email or webinar promo, one CTA), and Event Abstract (session title plus short description). Per-mode length limits come from CLAUDE.md's Length section. Pulls claims only from positioning.md, product-truth.md, proof-points.md, arize.md. Never invents a stat, quote, or capability; names the gap and offers the closest supported alternative instead. Checks Demand Gen and Event Abstract drafts against the latest Key Messaging Statement and flags drift. Leads with the deliverable and puts drift check, caveats, and Sources in an optional Notes section after it. Read-only; never writes to corpus/. Use for "write a campaign email", "draft a KMS", "session abstract for the webinar", "GTM copy for X".
---

# writer

## What this skill does

Writes GTM copy that a marketer could ship, built **only** from `corpus/`. Every
claim traces to a corpus file and carries that file's `last_verified` date. If a
claim you want isn't in the corpus, the skill says so and offers the closest
thing the corpus does support, rather than quietly writing around the hole.

Three modes:

1. **Key Messaging Statement (KMS)** — one foundational statement that everything
   else aligns to.
2. **Demand Gen copy** — a campaign email or webinar promo. Short, sharp, one CTA.
3. **Event Abstract** — a session title plus a short description for a
   conference or webinar listing.

This skill is **read-only**. It never edits or adds to `corpus/`. Refreshing the
corpus is the `corpus-refresh` skill's job.

Tone and length live in CLAUDE.md `## Voice` and `## Length`. That file is the
one place those rules live; this skill does not restate them, it only says what
goes in each piece.

## Hard rules

1. **Corpus is the only source.** Every claim must trace to
   `corpus/positioning.md`, `corpus/product-truth.md`, `corpus/proof-points.md`,
   or `corpus/arize.md`. No outside knowledge, no matter how confident it feels.
2. **No invented proof.** Never make up a stat, a customer name, a quote, a
   number, or a capability. If it isn't in the corpus, it doesn't go in the copy.
3. **Name the gap, then offer the nearest supported thing.** If the strongest
   version of the message needs a claim the corpus can't back (e.g. a hard ROI
   number tied to a named customer), say that in one line and propose the
   closest supported alternative (e.g. a named qualitative SRE quote, or a
   survey stat Dynatrace cites). Do not stretch a weak claim to sound like a
   strong one.
4. **Roadmap vs. shipped.** Anything that depends on the Arize acquisition is a
   roadmap claim until the deal closes (pending regulatory approval per
   `corpus/arize.md`). Never write it as a shipped capability. If a mode needs
   present-tense capability language, use what Dynatrace ships today and note the
   Arize piece as "intended" only where it genuinely helps.
5. **Follow CLAUDE.md `## Voice` and `## Length`.** Those two sections are the
   single source of truth for tone, sentence density, the read-aloud test, the
   buzzword ban, and every per-mode length limit. This skill does not restate
   them — it only says what goes *in* each piece. If a draft reads well aloud,
   keeps one idea per sentence, and hits the CLAUDE.md limit, it passes.
6. **One audience per piece.** Ops / SRE or AI engineers / developers. Ask if
   it isn't obvious (Step 1).
7. **Check for drift.** In Demand Gen and Event Abstract modes, compare the draft
   against the most recent Key Messaging Statement (Step 4). Report the result in
   the Notes section (Step 5), not above the copy.
8. **Public sources only. Nothing auto-sends.** Draft, stop, wait for approval.
9. **Deliverable first, Notes after.** Lead the reply with the copy itself and
   nothing above it. The drift check, caveats, and the Sources list go in a
   separate **Notes** section after a `---`, marked optional (Step 5). For casual
   "just the copy" requests, Notes is one line.

## Inputs

- The request, and the mode if stated.
- `corpus/positioning.md` — category, wedge, narrative, audience framing,
  messaging pillars.
- `corpus/product-truth.md` — the seven-layer framework, capabilities,
  integrations, the platform underneath.
- `corpus/proof-points.md` — customer quotes, analyst quotes, stats Dynatrace
  cites, and an explicit list of what proof is missing.
- `corpus/arize.md` — what the intended acquisition changes, and what is not
  shipped.
- The latest Key Messaging Statement, if one exists — check `docs/` for a file
  whose name contains `kms`, `key-messaging`, or `messaging`, and check whether
  one was generated earlier in this session.

---

## Procedure

### Step 1 — Confirm mode and audience

1. **Mode.** If the request doesn't name one, ask: KMS, Demand Gen, or Event
   Abstract? One question, three options.
2. **Audience.** Per CLAUDE.md:
   - **Ops / SRE** — thinks in SLOs, MTTR, dashboards, alerts.
   - **AI engineers / developers** — thinks in traces, evals, tokens, tool
     calls, prompt versions.
   If the request makes it obvious, infer it and say which you picked in one
   line. If it's genuinely ambiguous, ask. One question, two options.
3. For Demand Gen, also confirm the **asset** (email vs. webinar promo) and the
   **one CTA** (register, book a demo, read the guide, try the Playground). If
   not given, propose one and say so.
4. For Event Abstract, confirm the **venue type** (conference session vs.
   webinar) and any length limit the listing imposes.

### Step 2 — Gather claims from the corpus

1. Read the corpus files relevant to the mode and audience:
   - narrative, wedge, category → `positioning.md`
   - capabilities, the seven layers, integrations, agent-framework support →
     `product-truth.md`
   - quotes, stats, proof, and the "what's missing" section → `proof-points.md`
   - evals depth, dev-to-prod loop, Phoenix/AX/OpenInference → `arize.md`
2. For each claim you plan to use, record: the claim, the source URL (or corpus
   file), and the `last_verified` date from that file's YAML header.
3. Note the audience-fit tags in `proof-points.md` — some quotes are Ops-voice,
   some are exec-voice, and one (Autodesk) is about a different product. Use
   only what fits the chosen audience.
4. If the mode needs a proof point the corpus flags as missing, mark it now so
   Step 3 can handle the gap.

### Step 3 — Draft the copy

#### Mode 1 — Key Messaging Statement

Length and shape: CLAUDE.md `## Length` (flowing paragraph, four blended beats,
60 words). This skill only fills in what each beat holds:

1. **The point** — the one thing this audience should remember.
2. **The problem** — what breaks without this, from `positioning.md`.
3. **The solution** — what Dynatrace does about it, from `positioning.md` and
   `product-truth.md`.
4. **The key outcome** — the result that matters to this audience.

No inline citations in the statement itself — it's meant to be spoken. Every
claim in it must still trace to a corpus file, and those files go in the Notes
Sources list (Step 5).

Caveats, Sources, and the drift check go in the Notes section after the
statement (Step 5), never inside the 60 words.

**Caveats never fold into the statement.** If a claim needs a caveat to stay
honest (an unsourced stat, a roadmap capability, a quote from the wrong
audience), keep the paragraph clean and put the qualification in the Caveats
section. If a claim can't stand on its own without its caveat, use a different
claim.

The KMS is the anchor. Write it so demand gen and abstracts can align to it
without repeating it word for word.

#### Mode 2 — Demand Gen copy

Length and shape: CLAUDE.md `## Length` (subject + preheader + 3-4 sentence body
+ one CTA). Skill-specific rules on top of that:

- Keep the subject line under ~55 characters. BLUF in the first sentence.
- No more than one stat, and only if it's corpus-backed and fits the audience.
- One CTA only. If the brief implies several, pick the primary and say why.
- Webinar promo is the same content in the shorter blurb form CLAUDE.md gives
  for an event abstract, plus the CTA.
- **One inline citation per body, not one per sentence.** Put
  `(source: <file>, verified <date>)` on the single strongest claim only. Every
  other claim still traces to a corpus file, but those go unlinked in the Notes
  Sources list (Step 5). A marketer strips the one citation before shipping.

#### Mode 3 — Event Abstract

Length: CLAUDE.md `## Length` (title + 2-3 sentences).

**Title:** concrete, no colon-salad. Say what the attendee will learn, not just
name a theme.

**Description — this exact structure, in order:**

a. **The main point first.** The problem, one sentence, specific and relatable to
   this audience. Not "AI is hard" — the actual thing that goes wrong for them.
b. **What we'll cover.** One to two sentences. Concrete, not exhaustive: name one
   or two things the session shows, not every capability. Grounded in real
   Dynatrace capability from `product-truth.md`.
c. **The takeaway.** One sentence, and it is not optional. Lead it with "In this
   session, you'll..." (or "In this webinar, you'll...") and finish on what the
   attendee leaves able to do. It must answer "why did I block 30 minutes for
   this," not recap what Dynatrace does. Every abstract ends here, on the payoff,
   never on a feature description.

Other rules:

- No speaker bios, no logistics. Just title and abstract.
- One inline citation on the strongest claim only; the rest go unlinked in the
  Notes Sources list (as in Mode 2).

### Step 4 — Drift check (Demand Gen and Event Abstract only)

1. Locate the most recent KMS: a file in `docs/` matching `kms` /
   `key-messaging` / `messaging`, or one generated earlier this session. If none
   exists, say so in one line and skip the rest of this step.
2. Compare the draft against the KMS on four points:
   - **Audience** — same audience, or a deliberate sub-segment of it?
   - **Problem framing** — same core problem, or has it shifted?
   - **Differentiator** — does the draft lead with the same differentiator the
     KMS names, or a different one?
   - **Proof** — does the draft lean on proof the KMS also uses, or has it
     reached for something stronger-sounding that the KMS deliberately avoided?
3. If the draft is aligned, say so in one line.
4. If it drifts, **flag it plainly** in the Notes section (Step 5): what drifted,
   which direction, and whether it looks intentional. Offer a corrected version
   that snaps back to the KMS. Do not silently "fix" it — the drift might be the
   point.

### Step 5 — Assemble the output

**Lead with the deliverable and nothing above it:**

- **KMS** — the paragraph, plus the one-line word-count / beats note.
- **Demand Gen** — subject, preheader, body, CTA.
- **Event Abstract** — title and description.

Then a `---` separator and a **Notes** section, clearly marked optional, e.g.:

```
---
**Notes** (skip if you just need the copy):
```

Inside Notes, in this order:

1. **Drift check** (Demand Gen and Event Abstract only) — the Step 4 result, one
   line if aligned.
2. **Caveats** — anything that keeps the copy honest: a missing proof point, a
   roadmap capability, a stat used with a hedge, a stale source.
3. **Sources** — every corpus file the copy draws on, with `last_verified`
   dates, as a plain unlinked list. For Demand Gen and Event Abstract, also name
   the KMS you checked against (or note none was found).

List only files you actually drew from.

**Casual or copy-only requests.** If the user clearly just wants the copy
("write me a quick email about X", "fast draft", "just need the blurb"), collapse
Notes to **one line**: the single most important caveat if one exists, otherwise
"No caveats." Skip the full drift check and caveat detail unless they ask — the
full version is always available on request.

---

## When the corpus falls short

Say it in plain words, then offer the nearest real thing. Examples:

- "There's no public hard ROI number tied to a named customer in the corpus
  (source: corpus/proof-points.md, verified 2026-08-27). The closest supported
  proof for an SRE audience is the TELUS quote about optimizing dev and ops
  workflows. I've used that."
- "The corpus doesn't support 'the industry's first' for AI observability. It
  does support that framing for Dynatrace Intelligence, which is a different
  product (source: corpus/product-truth.md, verified 2026-08-27). I've dropped
  the superlative."
- "A dev-to-prod eval loop is an Arize-acquisition claim, and the deal isn't
  closed (source: corpus/arize.md, verified 2026-08-27). I've written the
  present-tense copy around what ships today — LLM-as-a-judge evals and
  `dt-evals` — and left the combined story out."

Never substitute general marketing knowledge for a missing corpus fact.

## Example (shape only — verify against the live corpus every time)

> **Key Messaging Statement — audience: Ops / SRE**
>
> If you already run Dynatrace, AI is a production workload you can't see: an AI
> app can look healthy while giving wrong or unsafe answers. Dynatrace watches it
> across seven layers, GPU to business impact, putting cost spikes, quality
> drift, and guardrail failures on the problem cards you use. It's the platform
> you own, not another tool to staff.
>
> *(59 words. Beats: the point = AI is an unseen production workload on a platform
> you already have; the problem = it fails silently; the solution = seven-layer
> watch on your existing problem cards; the outcome = no new tool to staff.)*
>
> ---
> **Notes** (skip if you just need the copy):
>
> Drift check: no prior KMS found; this is the anchor.
>
> Caveats: no public hard number ties a named customer to an AI-observability outcome; the two named quotes (TELUS, FreedomPay) are qualitative and ops-voice (source: corpus/proof-points.md, verified 2026-08-27).
>
> Sources:
> - corpus/positioning.md — last_verified 2026-08-27
> - corpus/product-truth.md — last_verified 2026-08-27
> - corpus/proof-points.md — last_verified 2026-08-27

For a casual request ("quick KMS for the SRE audience, just the paragraph"), the
same output ends at the beats note, then one line:
`Notes: no named-customer number backs this yet — the proof is qualitative. Full caveats on request.`

---

> **Event Abstract — audience: AI engineers**
>
> **Title:** Debug the AI Failure That Doesn't Throw an Error
>
> Your LLM app can return a confident, wrong, or PII-leaking answer with nothing
> in the logs to show for it. This session walks one bad response back through
> the model call, the retrieval step, and the layers behind it, with the eval
> score and the token cost sitting on the same trace (source:
> corpus/product-truth.md, verified 2026-08-27). In this session, you'll leave
> able to take a complaint about a bad answer and land on the exact step that
> caused it.
>
> ---
> **Notes** (skip if you just need the copy):
>
> Drift check: aligned with docs/kms-ai-observability-ai-engineers.md — same
> audience, same "fails silently" problem, same one-trace differentiator.
>
> Caveats: the dev-to-prod eval loop (Phoenix / Arize AX) is roadmap and is left
> out (source: corpus/arize.md, verified 2026-08-27).
>
> Sources:
> - corpus/product-truth.md — last_verified 2026-08-27
> - corpus/positioning.md — last_verified 2026-08-27
> - corpus/arize.md — last_verified 2026-08-27
> - KMS: docs/kms-ai-observability-ai-engineers.md
