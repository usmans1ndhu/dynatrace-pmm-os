# PMM OS

A portable **product marketing operating system** for AI observability go-to-market (GTM) work.

It is built as a set of **Claude Code skills** plus a **markdown corpus** — no application, no database, no server. Everything is plain text and version-controlled.

## What it is

- **`skills/`** — Claude Code skills that encode repeatable PMM workflows: positioning, messaging, competitive analysis, launch planning, sales enablement, analyst relations, and content production for the AI observability category.
- **`corpus/`** — the source-of-truth markdown knowledge base the skills read from and write to.
  - **`corpus/competitors/`** — per-competitor briefs, feature matrices, and positioning notes.
- **`docs/`** — documentation about the system itself: conventions, corpus schema, and how to extend the skills.

## Design principles

- **Portable.** Clone the repo onto any machine and it works. No installation step, no build, no hosting, no external services to provision.
- **Runs anywhere Claude Code runs.** The skills are the interface. Open Claude Code in this directory and invoke them.
- **Markdown as the substrate.** All knowledge lives in human-readable files that are easy to diff, review, and edit by hand or with an agent.
- **Self-contained.** The corpus travels with the skills, so the operating knowledge and the workflows that use it never drift apart.

## Getting started

1. Clone this repository onto your machine.
2. Open Claude Code in the repository root.
3. Invoke a skill (e.g. `/positioning`, `/competitive`) or ask Claude to work with the corpus directly.

## Layout

```
corpus/                source-of-truth markdown knowledge base
corpus/competitors/    per-competitor briefs and positioning
skills/                Claude Code skills (PMM workflows)
docs/                  documentation about this system
```
