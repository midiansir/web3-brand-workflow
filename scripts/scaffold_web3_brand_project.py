#!/usr/bin/env python3
"""Create a Web3 brand workflow project skeleton."""

from __future__ import annotations

import argparse
from pathlib import Path


FILES: dict[str, str] = {
    "00-governance-and-rules/00-production-rules.md": """# Production Rules

## Project Brief

| Field | Content |
| --- | --- |
| Project name |  |
| Current stage |  |
| Track |  |
| Target audience |  |
| Current deliverable |  |

## Operating Rules

1. Confirm source ids, public boundaries, risk terms, and owner questions first.
2. Do not publish unsupported claims.
3. Visual and UI output must follow the current VI system and visual risk blocklist.
""",
    "00-governance-and-rules/01-delivery-index.md": """# Delivery Index

| Folder | Purpose | Status |
| --- | --- | --- |
| day1-intake-risk | Sources, stage, risk, owner questions | Draft |
| day2-text-deliverables | Website, X, Medium, community, AMA | Draft |
| day3-visual-system | VI, tokens, visual risks, acceptance | Draft |
| day4-production-assets | Asset briefs, prompts, multilingual checks | Draft |
""",
    "day1-intake-risk/00-project-stage-table.md": """# Project Stage Table

| Field | Current judgment | Source id | Public handling |
| --- | --- | --- | --- |
| Project name |  |  |  |
| Project category |  |  |  |
| Current stage |  |  |  |
| Target users |  |  |  |
| User action |  |  |  |
| Public facts |  |  |  |
| Internal-only facts |  |  |  |
| Risk expressions |  |  |  |
| Owner questions |  |  |  |
| Stage boundary |  |  |  |
""",
    "day1-intake-risk/01-source-claim-inventory.md": """# Source Claim Inventory

| Source id | Raw statement | Public-safe expression | Use case | Risk handling | Owner question |
| --- | --- | --- | --- | --- | --- |
| R1 |  |  |  |  |  |
""",
    "day1-intake-risk/02-risk-blocklist.md": """# Risk Blocklist

| Risk category | Risk terms | Source id | Public handling | Visual handling |
| --- | --- | --- | --- | --- |
| Token and claim | token, claim, airdrop |  |  |  |
| Yield and rewards | yield, rewards, APY |  |  |  |
| Financing and endorsement | funded, investor-backed |  |  |  |
| Partnership | partner, strategic partnership |  |  |  |
| Launch status | now live, public launch, open registration |  |  |  |
""",
    "day1-intake-risk/03-owner-questions.md": """# Owner Questions

| Id | Question | Impact area | Owner | Handling before confirmation |
| --- | --- | --- | --- | --- |
| Q01 | Is the current public stage confirmed? | Website, X, community, visual |  | Use conservative stage wording |
""",
    "day1-intake-risk/04-agent-brief-template.md": """# Agent Brief Template

```text
You are working on a Web3 brand communication project.
Project name: [project name]
Current stage: [stage]
Target audience: [audience]
Current task: [deliverable]
Allowed source ids: [R1-Rn]
Public copy may only state: [public facts]
Internal-only risks and owner questions: [risk items]
Keep a source id for every major judgment.
Visual prompts must include VI rules, exclusions, post-generation checks, and owner questions.
If raster image generation is requested, use gpt-image-2 directly.
```
""",
    "day2-text-deliverables/00-positioning-and-hero-copy.md": """# Positioning And Hero Copy

| Module | Content | Source id | Blocked claims | Owner questions |
| --- | --- | --- | --- | --- |
| One-line positioning |  |  |  |  |
| Hero H1 |  |  |  |  |
| Hero subcopy |  |  |  |  |
| CTA |  |  |  |  |
""",
    "day2-text-deliverables/01-x-thread-and-posts.md": """# X Thread And Posts

| Post | Purpose | Source id | Blocked claims | Owner questions |
| --- | --- | --- | --- | --- |
| 1 | Opening and positioning |  |  |  |
| 2 | User problem |  |  |  |
| 3 | Product, world, or ecosystem direction |  |  |  |
| 4 | Current stage |  |  |  |
| 5 | Official update and safety reminder |  |  |  |
""",
    "day2-text-deliverables/02-medium-outline.md": """# Medium Outline

1. Title
2. Opening
3. Background problem
4. Project position
5. Product, world, or ecosystem modules
6. Current stage
7. Official update and safety reminder
""",
    "day2-text-deliverables/03-community-and-ama.md": """# Community And AMA

| Module | Public-safe answer | Cannot answer or pending | Source id |
| --- | --- | --- | --- |
| Welcome message |  |  |  |
| FAQ |  |  |  |
| AMA outline |  |  |  |
| Safety reminder |  |  |  |
""",
    "day2-text-deliverables/04-publishing-checklist.md": """# Publishing Checklist

| Check | Pass standard | Result | Owner note |
| --- | --- | --- | --- |
| Source traceability | Every major claim has a source id |  |  |
| Stage accuracy | Preparation is not written as live launch |  |  |
| Risk expression | No unconfirmed token, yield, funding, partner, audit, or scale claims |  |  |
| Multilingual consistency | Other languages do not add new facts |  |  |
""",
    "day3-visual-system/00-visual-source-index.md": """# Visual Source Index

| Source id | File or asset | Usable content | Risk or permission issue |
| --- | --- | --- | --- |
| V1 |  |  |  |
""",
    "day3-visual-system/01-strategy-to-visual-anchors.md": """# Strategy To Visual Anchors

| Brand judgment | Visual anchor | Allowed elements | Blocked direction | Source id |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
""",
    "day3-visual-system/02-light-vi-system.md": """# Light VI System

| Item | Rule |
| --- | --- |
| Visual positioning sentence |  |
| Visual keywords |  |
| Blocked visual direction |  |
| Primary background |  |
| Secondary background |  |
| Text color |  |
| Accent color |  |
| Motif |  |
| Image style |  |
| UI tone |  |
""",
    "day3-visual-system/03-visual-tokens.md": """# Visual Tokens

| Token type | Name | Value or rule | Use case | Owner question |
| --- | --- | --- | --- | --- |
| Color | Primary |  |  |  |
| Typography | H1 |  |  |  |
| Component | Card |  |  |  |
""",
    "day3-visual-system/04-vi-test-prompts.md": """# VI Test Prompts

| Field | Content |
| --- | --- |
| Test purpose |  |
| VI rules |  |
| Target platform |  |
| Ratio and size |  |
| On-image text |  |
| Required exclusions |  |
| Post-generation checks |  |
| Owner questions |  |
""",
    "day3-visual-system/05-visual-risk-blocklist.md": """# Visual Risk Blocklist

| Problem type | Common mistake | Fix instruction | Risk level |
| --- | --- | --- | --- |
| Financialized trading | K-line, trading screen, asset balance | Replace with real project scene or information path | Red |
| Reward misdirection | Coins, claim button, reward chest | Remove reward visuals | Red |
""",
    "day3-visual-system/06-vi-acceptance-table.md": """# VI Acceptance Table

| Asset | Purpose | Color fit | Text readable | Risk clear | Fix needed | Status |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | Pending |
""",
    "day4-production-assets/01-asset-brief-table.md": """# Asset Brief Table

| Asset id | Asset type | Platform | Size | Main message | Source | Owner questions |
| --- | --- | --- | --- | --- | --- | --- |
| APP-01 | X main image | X | 16:9 |  |  |  |
""",
    "day4-production-assets/02-visual-prompt-pack.md": """# Visual Prompt Pack

## Universal Exclusions

Token, airdrop, yield, APY, funding, confirmed partners, audit badge, coins, candlestick chart, bank building, trading screen, public launch, guaranteed access.

## APP-01

| Field | Content |
| --- | --- |
| Asset id | APP-01 |
| Asset type |  |
| VI rules |  |
| Ratio and size |  |
| On-image text |  |
| Required exclusions |  |
| Post-generation checks |  |
| Owner questions |  |
""",
    "day4-production-assets/03-multilingual-baseline.md": """# Multilingual Baseline

| Base copy | English | Other language | Rewrite restrictions |
| --- | --- | --- | --- |
|  |  |  |  |
""",
    "day4-production-assets/04-multilingual-vi-check.md": """# Multilingual VI Check

| Language | Text length | Readable on image | Fact consistency | Risk terms | Fix needed |
| --- | --- | --- | --- | --- | --- |
| EN |  |  |  |  |  |
| Other |  |  |  |  |  |
""",
}


DIRS = [
    "01-whitepaper",
    "02-brand-logo",
    "03-brand-ip",
    "04-website-and-hero",
    "05-x-and-social",
    "06-medium-and-longform",
    "07-community-and-ama",
    "08-posters-and-visual-assets",
    "09-multilingual-assets",
    "10-publishing-checks",
    "90-production-tools",
    "99-archive",
]


def write_file(path: Path, content: str, force: bool) -> None:
    if path.exists() and not force:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a Web3 brand workflow project skeleton.")
    parser.add_argument("project_name", help="Project folder name")
    parser.add_argument("--output-root", default=".", help="Parent directory for the project")
    parser.add_argument("--force", action="store_true", help="Overwrite existing starter markdown files")
    args = parser.parse_args()

    root = Path(args.output_root).expanduser().resolve() / args.project_name
    root.mkdir(parents=True, exist_ok=True)

    for directory in DIRS:
        (root / directory).mkdir(parents=True, exist_ok=True)

    for relative_path, content in FILES.items():
        write_file(root / relative_path, content, args.force)

    print(root)


if __name__ == "__main__":
    main()
