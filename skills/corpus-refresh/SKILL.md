---
name: corpus-refresh
description: Refresh the PMM OS corpus from its registered sources. Reads corpus/sources.yaml, refetches sources that are due by cadence, diffs each against corpus/.cache/, and — only for changed sources — shows the diff, proposes an edit, and waits for approval before writing. Also scans rss_feeds for new URLs not yet registered and proposes them for approval. Never overwrites a corpus file without showing the diff first. Use when asked to "refresh the corpus", "check sources", "update Dynatrace research", or on a regular cadence.
---

# corpus-refresh

## What this skill does

Keeps `corpus/` current and honest. It refetches registered sources on schedule,
detects what actually changed, and turns every change into a reviewed edit — never
a silent overwrite. It also watches RSS feeds for new sources worth adding.

## Hard rules

1. **Never write a corpus file without showing the diff first.** Every proposed edit
   is shown and approved before it lands.
2. **Grounding holds.** Every fact added to the corpus gets an inline source URL.
   If a source doesn't support a claim, don't add the claim.
3. **Never resolve a conflict silently.** If a refetched source contradicts another
   source or the current corpus text, present both and let the user decide.
4. **Public sources only.** Never fetch or add anything behind a login or marked
   confidential.
5. **Nothing auto-sends and nothing auto-commits.** Draft, stop, wait.
6. **New sources are opt-in.** Feed entries are proposed, never auto-added or
   auto-fetched.

## Inputs

- `corpus/sources.yaml` — the source registry (`sources`, `rss_feeds`, `competitors`).
- `corpus/.cache/*.txt` — the diff baseline: the raw text captured at last fetch.
- Today's date — to evaluate cadence.

---

## Procedure

### Step 1 — Load and select due sources

1. Read `corpus/sources.yaml`.
2. For each entry under `sources:`, compute whether it is **due**:
   - `weekly`  → due if `last_fetched` is null or ≥ 7 days ago
   - `monthly` → due if `last_fetched` is null or ≥ 28 days ago
   - `quarterly` → due if `last_fetched` is null or ≥ 90 days ago
   - `status: blocked` → still attempt on its cadence, but expect failure; if it
     fails again, leave `last_fetched: null` and note it.
3. Skip `competitors:` entries whose `url` is null (nothing to fetch yet). List them
   once as "still unresearched" so they stay visible.
4. Print the plan: which sources are due, which are skipped and why.

### Step 2 — Refetch and diff

For each due source:

1. Fetch the URL (WebFetch; fall back to a headful/JS-capable fetch for known bot
   walls like the community board).
2. If the fetch **fails**: report it, set/keep `last_fetched: null`, add or update a
   row in `gaps.md` under "Sources we could not fetch". Move on.
3. If the fetch **succeeds**: normalize to text and diff against
   `corpus/.cache/<cache filename>`.
4. Classify:
   - **Unchanged** (no meaningful diff — ignore boilerplate, nav, timestamps):
     go to Step 3.
   - **Changed**: go to Step 4.

### Step 3 — Unchanged: bump last_verified only

1. Update `last_fetched` for that source in `sources.yaml` to today.
2. In the `owner_file`, update the `last_verified:` date in the YAML header to today
   **only if** every source feeding that file is now re-verified as of today.
   (If one source in the file is still stale or blocked, leave the header date at the
   oldest re-verified date and say so.)
3. Do **not** touch the `.cache/` file (content is identical).
4. No CHANGELOG entry for a pure re-verify — but note it in the run summary.

### Step 4 — Changed: show diff, propose edit, wait

1. Show the user the **content diff** (old cached text vs. new fetched text),
   trimmed to the substantive changes.
2. Identify which claims in the `owner_file` are affected.
3. **Propose a specific edit** to the `owner_file`:
   - new/changed facts, each with its inline source URL
   - if the new text conflicts with another source or existing corpus text, present
     **both versions with both source URLs** and ask which to keep (or keep both with
     a conflict note) — never pick silently
   - keep the file's voice per `CLAUDE.md` (BLUF, plain language, minimal em-dashes)
4. **Stop and wait for approval.** Options to offer: approve as-is / approve with
   changes / reject / defer.
5. On approval:
   - write the edit to the `owner_file`
   - update that file's `last_verified:` header to today
   - overwrite `corpus/.cache/<cache filename>` with the newly fetched text
     (this becomes the new baseline)
   - update `last_fetched` in `sources.yaml` to today
   - **append a CHANGELOG.md entry**: `## <date> — <source url> — <file(s)> — <summary>`
6. On rejection/defer: update `last_fetched` (we did fetch it), do **not** update the
   cache (so the change is detected again next run), do **not** edit the corpus file.
   Note the deferred change in the run summary.

### Step 5 — New-source detection (RSS)

For each entry under `rss_feeds:`:

1. Fetch the feed URL.
2. Extract every entry's URL, title, and publication date.
3. Compare each entry URL against:
   - all `url` values under `sources:`
   - all `url` values under `competitors:`
   - URLs already proposed and rejected in a previous run (keep a short
     `rejected_urls:` list in `sources.yaml` or a sibling note so we don't re-propose)
4. For any URL **not** already known, show **only**: title, link, publication date.
   **Do not fetch the full content yet.**
5. Present the list and ask which to add. The user picks; add only what is approved.
6. For each approved URL:
   - ask for / infer `tier`, `cadence`, and `owner_file` following the same pattern
     as existing entries (official Dynatrace blog/docs → `primary`; news-ish or
     fast-moving → `weekly`/`monthly`; deep static posts → `quarterly`; pick the
     `owner_file` by topic — acquisition news → `arize.md`, product/capability →
     `product-truth.md`, category/narrative → `positioning.md`, customer/stats →
     `proof-points.md`)
   - add the entry under `sources:` with `last_fetched: null` and a new
     `cache:` filename (slug of the URL)
   - **now** fetch it, and run it through Step 2 → Step 4 (diff against an empty
     baseline = all new; propose the edit; wait for approval)
7. For URLs the user declines, add them to the `rejected_urls:` list so they aren't
   re-surfaced every week.
8. Update the feed's `last_fetched` to today.

### Step 6 — Run summary

Print:
- sources re-verified unchanged
- sources changed + approved (with CHANGELOG lines)
- sources changed + deferred/rejected
- sources that failed to fetch (and the `gaps.md` rows added)
- new URLs surfaced from feeds, and which were added
- any conflicts raised and how the user resolved them

Do not commit anything. Do not send anything.

---

## Cache filename convention

Slug of the URL: drop the scheme, replace `/` and `?` and `&` and `=` with `-`,
lowercase, trim trailing dashes, add `.txt`. Keep it stable once assigned — it's the
key that ties a source to its baseline.

Examples:
- `https://www.dynatrace.com/solutions/ai-observability/` → `solutions-ai-observability.txt`
- `https://docs.dynatrace.com/docs/dynatrace-intelligence` → `docs-dynatrace-intelligence.txt`

## Every cache file starts with a header

```
SOURCE: <url>
FETCHED: <date>
METHOD: <how>
STATUS: <ok | blocked | ...>
---
<raw text>
```
