---
name: "Update AMMR model documentation"
description: "Update one or more AMMR model description pages under Docs/Applications using the repository documentation rules and verified model sources."
argument-hint: "Change TARGET_MODELS below, then run this prompt"
agent: "agent"
---

Update the AMMR model documentation for each model listed below.

`TARGET_MODELS`: `LegPressMachine`

Read and follow [docs.instructions.md](../instructions/Application/docs.instructions.md) in full. `TARGET_MODELS` is a comma-separated list of one or more canonical model/application names; treat each entry as canonical and do not guess a different spelling. Process the models one at a time, in the order listed: for each, use the rules to locate its target page and verified model sources, make the smallest necessary documentation change, and validate the result before moving on to the next model.

Important compliance requirement: do not stop after fixing the first obvious error. Before considering a model done, audit the entire edited page for all required link forms and formatting rules, including Markdown links, HTML links, DOI URLs, Sphinx references, `{anylink-file}` entries, and links inside admonitions, figures, footnotes, and code-adjacent prose. Every link must use the required repository syntax and open in a new browser tab where required. If a person is named anywhere in the page or provenance, include a working public profile/contact link when one is available and keep it adjacent to the person’s name. Check the page against the instructions as a whole, not just the specific problem you noticed first. Only declare the model complete after the page passes this full compliance review.