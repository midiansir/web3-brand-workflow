---
name: web3-brand-workflow
description: Web3 brand strategy, narrative, copywriting, launch planning, visual prompt, image generation, website UI, app UI, IP mascot, poster, long-image, whitepaper, X, Medium, community, AMA, GTM, and commercial brand-delivery workflow. Use when the user asks to build or improve a Web3 branding or promotion workflow skill, start a Web3 brand full case from raw materials, join an existing Web3 project at one deliverable, write Web3 project narratives or whitepapers, produce X/Medium/community/AMA content, create Web3 visual prompts or gpt-image-2 assets, or implement Web3 official website, DApp, mint, dashboard, launch, or app UI assets.
---

# Web3 Brand Workflow

## Operating Mode

Use this skill for Web3 project brand strategy and production. Treat the first task as source-boundary work, not copywriting.

Start by deciding one of two modes:

| Mode | Use when | First action |
| --- | --- | --- |
| Full-stack | The user wants a full Web3 brand case from raw project materials. | Build or inspect the Day1 to Day4 source system before producing final assets. |
| Plug-in | The user only needs one part, such as a whitepaper, X post, poster, website UI, or app UI. | Read the smallest source set needed for that output, then check stage, risk, tone, and existing assets. |

If the user provides no usable source files, ask for project stage, track, source materials, target audience, and required deliverable. If enough source files exist locally, inspect them first and only ask for missing decisions.

## Required Loading

Load references only when needed:

| Task | Read |
| --- | --- |
| README, public repository content, public examples, screenshots, case studies, demo assets, or social posts that may expose client material | `references/confidentiality-and-public-release.md` |
| New project intake, diagnosis, source mapping, risk rules, narrative direction | `references/intake-risk-and-narrative.md` and `references/source-project-patterns.md` |
| Whitepaper, brand manifesto, X, Medium, community, AMA, GTM, BP, proposal | `references/text-deliverables.md` |
| Poster, long image, visual prompt, IP mascot, website UI, app UI, DApp, mint page, launch page, roadmap visual | `references/visual-ui-production.md` |
| Creating a new local project folder | Run `scripts/scaffold_web3_brand_project.py` |

When a referenced file is loaded, use it as procedural instruction, not as fixed copy. Replace project facts, risk terms, tone, VI, and deliverables with the current project's source material.

## Workflow

1. Establish source boundaries.
   - Number raw sources as `R1`, `R2`, `R3` when the project does not already have source ids.
   - Separate `confirmed public facts`, `internal-only facts`, `risk expressions`, and `待确认`.
   - Do not turn chat notes, old posters, investor hints, or draft mechanisms into public facts.
   - For any public repository, public example, README, case display, screenshot, demo, or social post, remove client names, local paths, private filenames, unreleased facts, partner names, funding details, and identifiable combinations of facts before publishing.
   - If sensitive material has already been committed to a public repository, changing the latest file is not enough. Purge or rebuild public history.

2. Diagnose the project.
   - Identify track, stage, target user, user action, proof level, official entry, and current communication goal.
   - Decide whether the project is infrastructure, DeFi, GameFi/IP, SocialFi, NFT, L1/L2, RWA, AI/Web3 tool, DAO/community, or a mixed project.
   - For mixed projects, choose the lowest-risk public story first and keep high-risk mechanisms in `待确认`.

3. Calibrate tone.
   - Offer 2 to 3 narrative routes when the user asks for strategy, naming, brand direction, website direction, or full-case work.
   - Do not force one Web3 tone across all projects. DeFi, infrastructure, IP/game, and early Beta SaaS projects need different language and visuals.

4. Structure before long-form output.
   - For whitepapers, Medium long articles, brand manifestos, launch plans, GTM, BP, proposals, or official website structures, provide an outline or section framework first and wait for confirmation unless the user explicitly asks for a direct full draft.
   - For short posts, image prompts, UI patches, or narrow deliverables, produce the deliverable directly after minimal risk checking.

5. Produce the asset.
   - Text assets must preserve source ids or a visible source/risk trail when the task is internal.
   - Public-facing assets must remove internal-only facts and unsupported claims.
   - Visual assets must state VI rules, exact platform size, on-image text, required exclusions, generation checks, and owner confirmation items.
   - If image generation is requested, use gpt-image-2 directly. If the model is unavailable in the current environment, prepare the exact prompt and report the blocker.
   - UI implementation should produce usable HTML/CSS/JS or React/Tailwind code, then verify it in a browser when a dev server or local page is involved.

6. Check commercial readiness.
   - Verify stage accuracy, risk words, visual exclusions, source support, platform fit, mobile readability, and file placement.
   - For plans, include timeline, resources, owners or roles, expected metrics, and launch checkpoints when the user asks for commercial execution.

## Local Project Skeleton

For a new project folder:

```bash
python scripts/scaffold_web3_brand_project.py "ProjectName" --output-root "/path/to/projects"
```

This creates Day1 to Day4, 01 to 10 deliverable folders, `90-生产工具`, and `99-归档`, with starter markdown files for intake, risk, narrative, copy, VI, prompt packs, multilingual materials, and release checks.
