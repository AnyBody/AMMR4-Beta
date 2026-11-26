---
description: "Use when creating or updating AMMR application and model description pages published from Docs/Applications/. Consult matching Application/**/*_notes.md files for suggested improvements."
applyTo: "Docs/Applications/**/*.md"
---

# Application model documentation

Use this guidance for the Markdown model-description pages under `Docs/Applications/`, which are used to build the website. Keep the page concise and factual. The corresponding `Application/**/*_notes.md` file is a list of suggestions for improving the website description; it is not itself published documentation or an authoritative source. Verify suggestions against the current `.any` model files and existing documentation before applying them.

## Page structure

Start application pages with YAML front matter:

```yaml
---
gallery_title: "Short gallery title"
gallery_image: "/Applications/images/ModelName.webp"
anylink: Application/<category>/<model-path>/Main.any
---
```

- Use `gallery_title` for the short title shown in the application gallery.
- Use an existing image under `Docs/Applications/images/` when one exists. Preserve the repository's image path convention.
- Add `anylink` when there is a clear main `.any` entry point. Omit it only when the model cannot be opened through AnyLink.
- Preserve already working gallery references and repository entry points. Do not change a working AnyLink or gallery entry just to force a different format. If an “In Model Repository” block lists multiple relevant `.any` files but does not use the folder-and-bullets format below, reformat the block while preserving every listed file, repository path, and working link.
- Use the repository's full path in the entry-point block, not a shortened or blank-label representation.
- Do not change the gallery entry or the “In Model Repository” section merely to force a different format when they are already working. If the page title or `gallery_title` changes, update the matching category `gallery.txt` card title and `:title:` value as well, while preserving its working link, AnyLink, image, and other formatting.
- Keep the front matter before all anchors and headings.

After the front matter:

1. Add the Sphinx-Gallery anchor used by the category gallery, following the naming pattern of nearby pages.
2. Add a single H1 title. Use title case, capitalizing the first letter of each word, and make it describe the model or demonstrated feature.
3. Add the gallery control immediately below the title:

	```markdown
	:::{anylink-gallery}
	:margin:
	:::
	```

4. Write a short opening description that states what the model demonstrates and what activity, body model, data source, or validation study it uses.
5. Explain the main objective and workflow. Mention important configurable parameters, input data, generated outputs, studies, or analysis steps when they are supported by the source model, but do not describe specific user-adjustable values such as simulation frame counts, angular velocities, or other implementation details that the user can already set in the model.
6. Document meaningful limitations, prerequisites, known assumptions, or performance considerations. Use a `warning` admonition text box only for significant model problems, such as the model not having been validated or results being unreliable without further adjustment, following the pattern used in the ADL Gait (beta) page. Use a `note` admonition text box for less serious limitations or useful qualifications.
7. End with the repository entry point using the empty-label AnyLink form for single-file cases:

	```markdown
	:::{admonition} In Model Repository:
	:class: seealso

	{anylink-file}` `
	:::
	```

	If several relevant `.any` files should be listed together, use the same folder-and-bullets format as in [Docs/Applications/Mocap/AnyMocapFeatures.md](Docs/Applications/Mocap/AnyMocapFeatures.md):

	```markdown
	:::{admonition} In Model Repository:
	:class: seealso
	`Application/Some/Folder`

	* {anylink-file}`FileOne.main.any <Application/Some/Folder/FileOne.main.any>`
	* {anylink-file}`FileTwo.main.any <Application/Some/Folder/FileTwo.main.any>`

	:::
	```

	Do not list additional entry points beyond the relevant files for the page. Keep the entry point block format consistent with the established repository pattern. For a multi-file block, format-only normalization is required when the existing block does not use the folder-and-bullets format; do not change its relevant files, repository paths, or links.

8. When the page contains papers, add exactly one `## Bibliography` section at the end of the page after the “In Model Repository” block. Define each bibliography entry as a footnote and reference it from the text with the corresponding footnote marker; do not list the same papers anywhere else.

## Figures and layout

- Do not add new figures. Only add a caption when an existing figure is missing one.
- Make every figure usable at the page's normal size. Avoid images that require horizontal scrolling or are taller than the viewport; resize, crop, split, or redraw them when needed.
- Prefer a figure directive with a responsive width and a descriptive caption over an unbounded raw image. Preserve readable labels and do not enlarge a low-resolution image until it becomes blurry.
- When a figure does not have a caption, add one that explains what the reader is supposed to see and why it matters.
- Rework diagrams or screenshots when the original is cluttered, difficult to read, or inconsistent with the surrounding documentation. Keep the content technically faithful to the model.
- Use the same figure style and list syntax as nearby pages. Do not mix custom HTML, raw Markdown, and Sphinx directives in a way that produces different gray-background or unstyled bullet lists.

## References and links

- Use exactly one `## Bibliography` section for papers, placed at the end of the page after the “In Model Repository” block and all other narrative content.
- Define the papers inside that section as footnote entries, for example `[^paper-name]: Author, A. A. (Year). Title. *Journal*, *volume*(issue), pages. DOI`, and cite them in the text with `[^paper-name]`.
- Do not put paper footnote definitions elsewhere, create a second bibliography, or repeat the papers as a separate list in the body text.
- Place a space before the footnote marker and put it after the punctuation when the reference comes at the end of a sentence, for example `The model was validated. [^paper-name]`.
- When the reference appears in parentheses, place a space before the footnote marker and put it directly after the referenced text inside the parentheses, for example `(validated against experimental data [^paper-name])`.
- Format every reference as: Author, A. A., Author, B. B., & Author, C. C. (Year). Title of the paper. *Journal Name*, *volume*(issue), page range. https://doi.org/DOI
- Use the following as the reference-format example: De Zee, M., Dalstra, M., Cattaneo, P. M., Rasmussen, J., Svensson, P., & Melsen, B. (2006). Validation of a musculo-skeletal model of the mandible and its application to mandibular distraction osteogenesis. *Journal of Biomechanics*, *40*(6), 1192–1201. https://doi.org/10.1016/j.jbiomech.2006.06.024
- Use `et al.` in author lists beyond the first author; avoid phrases such as “X and co-workers” or similar informal alternatives.
- Every cited paper or external source must include a working link when one is available. Prefer a DOI or the publisher's stable page over a fragile search-result URL.
- Verify the DOI URL before adding it; it must resolve to the correct paper and not to a guessed, stale, or mismatched DOI.
- Make every DOI a clickable link that opens in a new browser tab. Use the documentation site's supported link syntax or an HTML link such as `<a href="https://doi.org/DOI" target="_blank" rel="noopener">https://doi.org/DOI</a>`.
- Make every link open in a new browser tab, including DOI links, external links, Sphinx references, and repository file links. Use the documentation site's supported link syntax or `target="_blank"` with `rel="noopener"` where HTML is required.
- When the citation's purpose is not already clear from the surrounding body text, explain naturally what the paper is, why it is relevant, and how it supports the model or interpretation being described. Do not add redundant explanations merely to satisfy a citation rule. Keep each bibliography footnote limited to the citation details and working link.
- If useful information about a cited paper already exists in the page, keep it and improve the wording so it is clearer and more appropriate rather than removing it.
- Keep all paper footnote definitions inside the single `## Bibliography` section; do not add a separate paper list in the body text.
- Make all links open in a new browser tab. Use the project's supported link syntax or safe HTML with `target="_blank"` and `rel="noopener"`; do not add page-specific JavaScript.
- When linking to another model description page, use its relative generated HTML path, including the `.html` suffix, for example `<a href="PedalDemo.html" target="_blank" rel="noopener">Pedal demo simple</a>`. Do not use an extensionless site-root path such as `/Applications/.../PedalDemo`.
- For links to another model description page, always use the explicit relative HTML anchor form with `target="_blank"` and `rel="noopener"`; do not replace it with a Sphinx `{ref}` or another internal-reference form, even when a Sphinx reference is available.
- Prefer Sphinx references for links to AMMR documentation and `{anylink-file}` for repository files. Check that internal links resolve in the documentation build.

## Titles, provenance, and model details

- Keep the H1 title, `gallery_title`, category gallery entry, and model name consistent. If a title needs clarification, update all overview and detail locations together, including both the category gallery card heading and its `:title:` value in `gallery.txt`.
- Choose a title that tells readers what the model is or demonstrates, not only the name of its source folder. Keep the gallery title short while making the page H1 specific.
- Format model titles in title case, capitalizing the first letter of each word, consistently in the H1, `gallery_title`, and category gallery entry. Preserve established acronyms and technical names.
- Include the word “model” in a title only when it is needed to make the subject clear. Since the documentation section already establishes that these entries describe models, omit “model” when the title sounds natural and remains unambiguous without it.
- Read the relevant `.any` files, especially the main entry point, before writing the description. Use the matching `Application/**/*_notes.md` file to identify suggested changes, then verify each suggestion against the model implementation. Include useful details that exist in the `.any` files but are missing from the website page, such as available switches, inputs, outputs, studies, or analysis workflow.
- When you encounter multiline comments in the corresponding `.any` files, read and interpret them in context rather than treating them as text to copy. Identify the model purpose, assumptions, limitations, cause-and-effect relationships, trade-offs, and practical meaning described by the comments. If relevant information is missing from the page, express those conclusions naturally in the most appropriate section of the description, preserving important qualifications without copying irrelevant implementation detail or repeating existing content. Do not infer claims that the comments and model implementation do not support.
- Keep every factual claim traceable to the current model files, reliable repository documentation, or verified metadata. Do not fill gaps with plausible scenarios or general knowledge: do not invent activities, use cases, user behavior, validation, outputs, performance, or measured outcomes. If a conclusion is only an interpretation, label it clearly as such; otherwise omit it.
- Add the creator's name and contact information when it is available in the model metadata, notes, documentation, or repository history. If a person is named anywhere in the model description, provenance, or acknowledgments, include a working public profile/contact link such as a LinkedIn, institutional profile, ORCID, or other verified public profile when one is available. Place the link adjacent to the person’s name and do not invent contact details or expose private information; if no reliable contact is available, omit the section.
- Correct grammar and spelling in the documentation and in explanatory comments or user-facing text in the related `.any` files when they are part of the change. Preserve technical identifiers and AnyScript syntax exactly.

## Writing conventions

- Prefer clear, direct prose over promotional language. Use “This model…” or “The example…” when introducing behavior.
- Use the repository's established names for models, files, studies, switches, and folders. Put filenames, macros, switches, and code identifiers in backticks.
- Explain why a feature matters, not only which file contains it. State what users can change and what they should expect to observe.
- When describing actions available to users, use passive constructions instead of addressing the reader directly or naming users as the actor. For example, write “The parameter can be changed in `Input/Parameters.any`” instead of “Users can change the parameter” or “You can change the parameter.”
- Do not mention specific implementation details that users can already adjust in the model, such as the number of frames used in a simulation or the angular velocity chosen for a movement.
- Do not remove numerical parameter values that are already present in the existing description; preserve them when they provide useful context, even if new numerical implementation details should not be added.
- Write angular values with the degree symbol `°`, not the word “degree” or “degrees”.
- List user-adjustable parameters as a bullet list when they are relevant; keep the list concise and conceptual rather than narrating exact values.
- Do not repeat yourself; if a concept has already been described, do not restate it with different wording later in the page.
- Keep paragraphs focused. Use headings when a page has distinct setup, workflow, results, or limitations sections.
- Link to existing AMMR documentation with Sphinx references instead of duplicating long explanations. In particular, reuse the relevant MoCap, body-model, scaling, or GRF-prediction documentation.
- Check spelling, grammar, and capitalization of model names. Do not silently rename a model in the page title when the repository uses a different canonical name; use the title that best describes the documented application and keep `gallery_title` short.
- Use consistent heading levels, punctuation, terminology, citation formatting, and list formatting throughout the page.

## Before finishing

- Verify every file path, image path, AnyLink target, macro, and referenced study exists.
- Before finishing, audit the entire edited page for every link form, including Markdown links, HTML links, DOI URLs, Sphinx references, `{anylink-file}` entries, and links inside admonitions, figures, footnotes, and code-adjacent prose. Verify that each link is working, uses the required repository syntax, and opens in a new browser tab where required. Do not limit this check to links added or modified during the current edit.
- Treat the Markdown file under `Docs/Applications/` as the website description being edited. Compare it with the corresponding `.any` files and use the matching `Application/**/*_notes.md` file as a change checklist. Resolve conflicts in favor of the current model implementation and mention unresolved limitations rather than inventing details.
- Preserve the local category's anchor and formatting pattern.
- If adding or renaming an application page, update the appropriate `Docs/Applications/<category>/gallery.txt` entry and category index as needed.
- Check the page at desktop and narrow viewport sizes: figures must fit without unwanted scrolling, captions and labels must remain readable, links must be distinguishable, and lists must render with the same style as neighboring pages.
- Check that the model title shown in the overview, gallery, page heading, and AnyLink/repository box describes the same model.
- Build the documentation with `pixi run -e docs docs` when the environment is available; fix warnings and broken links before finishing.
