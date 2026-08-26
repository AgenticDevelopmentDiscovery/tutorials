---
title: "Tutorial 34 — Markdown & Pandoc: Docs as Source"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 34 — Markdown & Pandoc: Docs as Source

> Student-led tutorial (~15 min). Write once in plain text, build PDFs, slides, and Word docs from the same source.

## What it is
Markdown is a lightweight, plain-text markup language: headings, lists, links, code blocks, and emphasis expressed in characters you can read raw. Because it is plain text, it diffs cleanly, lives in version control, and is editable by both humans and agents without a binary editor in the loop. Pandoc is the "universal document converter" that turns one markup format into dozens of others.

Together they enable *docs-as-source* (sometimes "docs-as-code"): a single canonical Markdown manuscript is the source of truth, and every published artifact — a PDF via LaTeX, a `.docx` for a collaborator, Beamer or reveal.js slides for a talk, HTML for the web — is a *build output*, not a hand-maintained copy. Pandoc parses the source into an internal document AST and renders that AST into each target, so formatting stays consistent across outputs.

## Why it matters for agentic development
Agents are good at editing text and terrible at editing binary `.docx` or `.pptx` blobs. Keeping the canonical form in Markdown means an agent can propose a precise, reviewable diff to your paper or slides, and the build step deterministically regenerates the rendered artifacts. This is exactly the loop this course runs on: prose is data, builds are reproducible, and review happens on diffs.

## Key ideas to cover
- Markdown basics, and "flavors" (CommonMark, GitHub-Flavored, Pandoc Markdown) — know which one your tool expects.
- Pandoc as an AST-based converter: source → internal representation → many targets.
- Front-matter / metadata blocks (title, author, date, bibliography) drive templates.
- Citations: `--citeproc` + a `.bib` file + a CSL style gives you formatted references — key for the capstone paper.
- Math: `$...$` LaTeX math survives into PDF and HTML (via MathJax).
- Output targets: PDF (needs a LaTeX engine), `.docx`, Beamer/reveal.js slides, HTML.
- Templates and `--include-in-header` to control the look without touching content.
- Separation of *content* (Markdown) from *presentation* (template/CSS/LaTeX).

## Hands-on / demo
Start from a two-paragraph `report.md` with a metadata block and one citation. Run `pandoc report.md -o report.pdf` to get a typeset PDF, then `pandoc report.md -o report.docx` and `pandoc -t beamer report.md -o slides.pdf` from the *same file* — show that one source yields a paper, a Word doc, and a slide deck. Add `--citeproc --bibliography refs.bib` and watch a `[@key]` turn into a formatted reference. Tie it back: this is how the capstone report and these course materials are built, and the build belongs in a one-command runner (see Tutorial 35) so it is reproducible on any rig.

## Connections
- Capstone: the paper-style report is authored in Markdown and built to PDF with citations via Pandoc.
- The course's own build: these tutorials are Markdown source; the same toolchain renders the course.
- C1 (agentic coding): agents edit Markdown as text and produce reviewable diffs instead of opaque binaries.
- Reproducibility: rendered outputs are disposable build artifacts, so the source stays the single point of truth.

## Further reading
- Pandoc User's Guide (the manual; covers readers, writers, citations, templates).
- CommonMark spec and the GitHub-Flavored Markdown documentation.
- Citation Style Language (CSL) styles repository for reference formatting.
- The "docs-as-code" / "docs-as-source" pattern as described in technical-writing literature.
