# 🧬 THE README GENERATOR PROMPT

Paste this into Claude (or any strong model with file/SVG capability). Fill the
`[BRACKETS]`, delete the mode you don't want, and let it rip.

---

You are a senior frontend/SVG designer building the most absurd, tech-geek,
animated GitHub README ever made. Output must be production-ready and drop-in.

## MODE
Build a **[PROFILE | PROJECT]** README.  ← keep ONE

## HARD REQUIREMENTS
- Hand-craft **custom animated SVGs** (do NOT just chain third-party badges).
  Use SMIL `<animate>/<animateTransform>` + in-SVG `<style>` CSS keyframes —
  these are the only animations that survive GitHub's camo image proxy.
- Deliver as real files: `README.md`, an `assets/` folder of SVGs, and any
  workflow files needed (e.g. snake action for profiles).
- Use **relative paths** (`./assets/x.svg`) so they resolve inside the repo.
- Center everything with `<div align="center">`; GitHub strips page-level
  `<script>`/`<style>`, so never rely on them outside SVGs.
- Verify every SVG renders (rasterize to PNG) before delivering. No overflow.

## AESTHETIC
Pick ONE bold direction and commit hard (don't blend): `[cyberpunk terminal |
retro CRT | brutalist mono | vaporwave | hacker-green matrix | synthwave |
blueprint/schematic | glitch-art]`.
Palette: `[3–5 HEX CODES]`. Display font feel: `[mono | pixel | display]`.
The README must have ONE unforgettable signature element.

## SECTIONS
Common: animated hero banner (custom SVG) · typing-SVG tagline · live badges
(views/uptime/status jokes) · animated divider (custom SVG, reused) ·
custom-SVG footer wave.

If PROFILE — also include:
- Animated "boot log" / terminal SVG that types out the bio
- About block (yaml-in-codeblock style is great) + a rotating dev quote
- Tech arsenal grouped by category (skillicons.dev + shields for-the-badge)
- Stats wall: github-readme-stats card, streak stats, top-langs, trophies,
  activity graph — ALL themed to the palette (title_color/text_color/
  icon_color/bg_color/hide_border)
- Contribution **snake** (include the Platane/snk workflow + setup steps)
- Project showcase via pin cards (`/api/pin/?...&repo=`)
- Connect row (email/socials as for-the-badge buttons)

If PROJECT — also include:
- Hero SVG with the project name + animated logo/mark
- One-line hook + animated typing-SVG of the value prop
- Badges: build/CI, license, version, stars, language %, last-commit (shields)
- ✨ Features grid (table with emoji + 1-liners)
- 🏗️ Architecture: a clean Mermaid diagram (```mermaid```) of the system
- ⚡ Quickstart: copy-paste install/run code blocks
- 🧠 Usage example (real code), 🗺️ Roadmap (checkboxes), 🤝 Contributing,
  📜 License, screenshots/GIF demo slot
- Tech-stack badge row

## INPUTS (fill these)
- name / username: `[ ]`
- one-liner identity or project pitch: `[ ]`
- core stack & focus areas: `[ ]`
- featured repos/projects: `[ ]`
- links (email/socials/site): `[ ]`
- anything weird & personal to make it feel human (a joke, a ritual, a fact): `[ ]`

## TONE
Over-the-top tech humor in the copy (fake `htop`/boot logs, shell-command
section headers like `> ./load_arsenal.sh`, uptime/caffeine jokes) — but the
CODE underneath stays clean, valid, and maintainable.

## DELIVERABLES
1. All files, ready to commit.
2. A short SETUP.md (where the repo goes, how to enable the snake, how to recolor).
3. Show me previews and confirm nothing overflows.

Now build it.
