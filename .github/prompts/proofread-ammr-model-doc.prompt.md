---
name: "Proofread AMMR model documentation"
description: "Correct grammar, spelling, and flow of one or more AMMR model description pages under Docs/Applications without changing information."
argument-hint: "Change TARGET_MODELS below, then run this prompt"
agent: "agent"
---

Proofread the AMMR model documentation for each model listed below.

`TARGET_MODELS`: `FreePosture`

Read and follow [docs-proofread.instructions.md](../instructions/Application/docs-proofread.instructions.md) in full. `TARGET_MODELS` is a comma-separated list of one or more canonical model/application names; treat each entry as canonical and do not guess a different spelling. Process the models one at a time, in the order listed: for each, locate its target page under `Docs/Applications/` and correct grammar, spelling, punctuation, and readability without adding, removing, or otherwise changing information, then validate the result before moving on to the next model.
