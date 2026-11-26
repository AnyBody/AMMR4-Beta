---
description: "Use when only proofreading and polishing an existing AMMR application/model description page under Docs/Applications/ is requested, without adding, removing, or changing information."
applyTo: "Docs/Applications/**/*.md"
---

# Application model documentation — proofreading only

Use this guidance when the task is limited to improving the wording of an existing page under `Docs/Applications/` by making it clearer, more natural, and easier to read. The goal is to polish the text already present on the page, while allowing small added words or phrasing changes when they improve clarity without changing the underlying meaning.

## Scope

- Do not add new facts, figures, parameters, limitations, citations, or links. Do not remove existing information, even if it seems redundant, outdated, or unverified.
- Work only from the target `.md` page itself. Do not open, read, or consult `Application/**/*_notes.md` files, `.any` model sources, or any other non-Markdown file; this pass is not a content-accuracy review and does not require verifying facts against the model implementation.
- Do not change YAML front matter values (`gallery_title`, `gallery_image`, `anylink`), the H1 title's meaning, headings' meaning, admonition types (`note`/`warning`), figure references, AnyLink/repository blocks, or bibliography entries and their DOIs. Any edits must stay within the existing text and preserve its meaning.
- Do not restructure the page (reordering sections, splitting/merging sections) unless the reordering itself is required to fix a grammar or flow problem within a single paragraph or list.
- Do not pull in information from other sources, infer missing details, or rewrite the page to add context that is not already present.

## What to fix

- Correct grammar, spelling, punctuation, verb tense, and subject-verb agreement errors.
- Fix awkward phrasing, run-on sentences, and unclear pronoun references while preserving the original meaning and all stated facts.
- Improve sentence and paragraph flow: reorder clauses, combine or split sentences, adjust transitions, and add or refine words where needed so the text reads naturally and is easier to understand, while staying within the information already present on the page.
- When a short explanatory list or slight reformatting would make an existing set of options, configuration choices, or similar groupings clearer to readers, convert the text into a simple list or similar reader-friendly structure while keeping the same information and meaning. Use natural phrasing such as `X can be set to:` followed by concise nested entries like `"Option": explanation` or `- Option: explanation`, which makes the content easier to scan without changing the substance.
- Normalize terminology, capitalization, and punctuation to be consistent throughout the page when the inconsistency is a grammatical or stylistic issue (e.g., inconsistent capitalization of the same model name, inconsistent use of the degree symbol `°`).
- Keep technical identifiers, filenames, macros, switches, code identifiers, and AnyScript syntax in backticks exactly as they already appear.
- Keep numerical values, units, and citation content unchanged; only correct their surrounding grammar.

## Before finishing

- Re-read the diff and confirm every change is a grammar, spelling, or flow correction with no net change in information conveyed.
- Verify no links, paths, macros, or citation markers were altered.
- Build the documentation with `pixi run -e docs docs` when the environment is available; fix any new warnings introduced by the edit.
