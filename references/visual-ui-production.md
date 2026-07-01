# Visual And UI Production

## Day3 VI System

Create or inspect these files before producing visuals:

| File | Purpose |
| --- | --- |
| `00-品牌视觉资料索引.md` | Source images, logo, old posters, screenshots, style references |
| `01-品牌策略到视觉锚点表.md` | Convert narrative into visual rules |
| `02-轻量视觉识别系统.md` | Colors, type, motifs, layout, image style, UI tone |
| `03-视觉母版与设计Token.md` | Reusable tokens for UI and image prompts |
| `04-VI打板提示词包.md` | First visual testing prompts |
| `05-视觉风险与VI偏离排雷词库.md` | Visual mistakes and blocked elements |
| `06-VI验收表.md` | Image or UI acceptance table |

## Prompt Schema

Every commercial image prompt should include:

| Field | Content |
| --- | --- |
| Application id | Stable id, such as `PROJECT-D4-APP-01` |
| Application type | X main image, Medium cover, community announcement, event poster, long image, mascot, UI concept |
| Source files and ids | The exact sources supporting the prompt |
| VI rules | Color, type, motif, composition, UI tone |
| Platform and size | X 16:9, Medium 1600x900, 4:5 1080x1350, long image size, website hero, app screen |
| Audience | Who will see it |
| Main subject | The one thing the image must show |
| On-image text | Exact text, short and proofread |
| Layout | Main areas, hierarchy, spacing, modules |
| Colors and type | Hex values or source-based style rules |
| Required exclusions | Text and visual elements to avoid |
| Post-generation checks | Readability, VI consistency, risk expression, crop fit |
| Owner confirmation | Links, dates, speakers, screenshots, partner logos, product state |

## gpt-image-2 Rule

When raster image generation is requested:

1. Use gpt-image-2 directly.
2. Put the exact platform size and aspect ratio in the prompt.
3. Keep on-image text short. For long copy, generate a designed layout or provide text separately.
4. After generation, inspect dimensions, text readability, visual risk, and VI consistency.
5. If gpt-image-2 is not available, output the exact ready prompt and state that generation is blocked by model availability.

## Visual Risk Checks

Block these unless the project source and owner approval explicitly allow them:

- K-line, trading screen, exchange logo, buy or sell panel
- Coin piles, token icons, airdrop box, claim button, reward chest
- APY, yield dashboard, fee split chart, stable income chart
- Investor logo wall, partner wall, audit badge, legal certificate
- Countdown, open registration, guaranteed access, whitelist pass
- Cash rain, jackpot, lottery wheel, million-prize numbers
- Contract signing, payment counter, limited seats, sales urgency
- User address table, wallet permission popup, personal data dashboard

## Visual Routes

| Project type | Better visual route | Avoid |
| --- | --- | --- |
| SaaS or operations tool | Low-density product modules, entry hub, status cards, official update path | Generic cyber city, trading terminal, reward UI |
| DeFi | Product UI, liquidity route, token-neutral mechanism panels, existing brand colors | APY promise, bribes unless confirmed, fake volume, exchange logo overload |
| IP or GameFi | Characters, world gate, item cards, event visuals, merch display | Token economy visuals, jackpot, financial dashboard |
| Foundation or DAO | Ecosystem map, governance flow, release hub, official documents | Fake institutional badges, partner claims, legal overclaim |
| RWA | Process explanation, evidence checklist, conservative diagrams | Asset-backed return visuals, bank/real estate wealth cues |

## Website And App UI

When implementing Web3 website or app UI:

1. Use current project VI and source-backed copy.
2. Create the real first screen or working page, not a marketing explanation page.
3. For official websites, include hero, project positioning, modules, proof or source-backed assets, current stage, official updates, and safe CTA.
4. For DApp or app UI, include only modules that sources support. Use placeholder states for unconfirmed product areas.
5. Avoid fake wallet connect, asset balances, token prices, yield dashboards, partner logos, audit badges, or public registration flows unless confirmed.
6. Use React and Tailwind when the project already uses them or when the user asks for app-like UI. Use HTML/CSS/JS when a single static deliverable is enough.
7. Verify desktop and mobile viewports with Playwright or browser screenshots when building a frontend. Check for blank screens, overflow, unreadable text, and overlapping UI.

## Common Deliverables

| Deliverable | Required checks |
| --- | --- |
| X main image | Mobile crop, title readability, one message, no risk terms |
| Medium cover | Editorial feel, no fake ranking or claims, title matches article |
| Community announcement | Official channel, safety text, no panic graphics |
| AMA poster | Date/speaker placeholders if unconfirmed, no sensitive topics |
| Event poster | No unconfirmed location, partner, sales policy, or launch claim |
| Long image | Section hierarchy, source-safe claims, mobile reading order |
| IP mascot | Character role, visual consistency, usage rights and final approval |
| Website hero | Brand/product visible in first viewport, safe CTA, next section visible |
| App UI | Supported modules only, no fake wallet or asset data |
| Roadmap visual | No dates or commitments unless confirmed |

## Acceptance Table

Use this after image or UI production:

| Asset | Purpose | VI consistent | Text readable | Source-safe | Risk clear | Platform fit | Fix needed | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  | 待检查 |
