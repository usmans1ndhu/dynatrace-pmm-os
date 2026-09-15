# CLAUDE.md

Rules for working in this repository.

# Voice guide

Tone: talking to a friend over coffee. Warm, direct, confident.

Do:
- Plain words. Short, declarative sentences. Fragments are fine.
- Shorter and blunter beats polished.
- Name gaps and limits directly.
- Competitor test: if a competitor could say the same line, rewrite it.
- Default reader is a smart non-specialist. Go more technical only when I say the audience is technical.

Don't:
- Buzzwords. Em-dashes (use rarely).
- AI tells: rule of three, "It's not just X, it's Y," same sentence length throughout, repeated theme words.
- Over-explaining.

When I give you my own words: copy edit, don't rewrite. My edits become the new baseline. Don't defend old drafts.

## Voice
- BLUF. Bottom line in the first two sentences, always.
- Plain language. A smart 10-year-old should follow it.
- No jargon: no governance-speak, no platform-vendor buzzwords, no generic corporate filler. Examples of words to avoid: "leverage," "seamless," "robust," "end-to-end," "synergy," "best-in-class," "unlock." This list is illustrative, not exhaustive — if a word sounds like it belongs in a press release rather than something you'd say to a friend, cut it.
- Minimal em-dashes.
- One idea per sentence. If a sentence names more than two or three technical terms back to back, split it or cut to the most important one or two. Use the tone you'd use explaining something to a friend at a bar.
- Read-aloud test: if a sentence would make someone stumble reading it out loud, rewrite it. Technical terms are fine individually; stacking them densely is not.
- Prefer the concrete example over the full list. Instead of naming every layer (frontend, orchestration, RAG, LLM, agent-to-agent), name one or two that make the point and say "and the layers behind it" for the rest.
- Point before framing. Say what the thing does before explaining why it matters.
- Plain words only. If a new hire would have to look a word up, rewrite it.
- Concrete over abstract. A number beats an adjective — "four days to one," not "significantly faster."
- State a limit in the same sentence as the claim it limits. Not a hedge, not an apology, just the fact.
- Declarative sentences. Cut "we believe," "it seems," "arguably," and anything else that softens a claim that doesn't need softening.
- One idea per sentence. If a sentence has two sub-clauses, it is two sentences that got stuck together.
- The competitor test: if a rival could say this same sentence about themselves without changing a word, it isn't specific enough. Rewrite it.

## Grounding
- Every claim must trace to a file in `corpus/`.
- If `corpus/` doesn't support it, say so out loud. Never invent a proof point, customer name, or number.

## Audiences
Always ask or infer which one before writing:
1. Ops / SRE — thinks in SLOs, MTTR, dashboards, alerts.
2. AI engineers / developers — thinks in traces, evals, tokens, tool calls, prompt versions.

## Length
- Default to the shortest output that fully does the job.
- Key Messaging Statement: single flowing paragraph, no numbers, no bullets. Four beats blended together: the point, the problem, the solution, the key outcome. Hard limit 60 words for the paragraph itself. Sayable out loud in under 20 seconds.
- Battle cards: 4 lines max — Dynatrace strength, their claim, the honest gap, the lead differentiator.
- Demand gen email: subject + preheader + 3-4 sentence body + one CTA. One source cited inline per body, not one per sentence.
- Event abstract: title + 2-3 sentences. Ends on the attendee takeaway, not a feature description.
- Caveats, Sources, and Drift check are separate from the length limit above — they can run as long as they need to, but the primary output must hit the limit.
- If asked for something longer, follow the request. These are defaults, not walls.

## Rules
- Public sources only. No proprietary or confidential material.
- Nothing auto-sends. Draft, then stop, then wait for approval.
