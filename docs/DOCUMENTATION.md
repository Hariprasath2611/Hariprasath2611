# GitHub Profile README Documentation

> **Profile Architecture & Design System for [@HARIPRASATH2611](https://github.com/HARIPRASATH2611)**

---

## 1. Project Overview & Architecture

This repository hosts the profile README for **@HARIPRASATH2611**, styled to match a gamified, dark-mode visual aesthetic.

### Technical Constraints & Solutions

GitHub's Markdown renderer strips `<style>`, `<script>`, custom external web fonts, and most CSS properties. To circumvent these limits:
- **Unified SVG Architecture:** All 5 visual cards and the contribution snake are compiled into a single unified vector canvas at [`assets/profile-animated.svg`](assets/profile-animated.svg).
- **Exact Spacing:** Eliminates irregular spacing artifacts caused by GitHub markdown `<p>` wrappers between separate image tags, enforcing strict `24px`–`28px` card gaps.
- **Embedded Web Fonts:** Base64-encoded WOFF2 font subsets are embedded directly in `<style>` blocks so typography renders identically regardless of OS or GitHub's Camo caching proxy.
- **Dual Animation Engine:** Blends CSS `@keyframes` with native SVG SMIL (`<animateTransform>`, `<animateMotion>`, `<animate>`) ensuring continuous 60fps animations even in isolated image contexts.

---

## 2. Design System & Tokens

### Color Palette

| Token Name | Hex Code | Purpose / Usage |
|:---|:---|:---|
| **Canvas Background** | `#1B1030` | Deep eggplant canvas background and chip fills |
| **Card Surface** | `#2A1A4A` | Main card background surface |
| **Primary Accent** | `#FF8A3D` | Photo banner, active nodes, status dot, snake head |
| **Secondary Accent** | `#B79CFF` | Main Quest badge, footer card surface, labels |
| **Primary Text** | `#F6F1FF` | Headers, titles, skill chip text, contrast text |
| **Muted Text** | `#CFC4EA` | Paragraph text, descriptions, subheadings |
| **Divider / Border** | `#4A3578` | Dashed graph border, branch timelines |

### Contribution Heatmap Levels

- **Level 0 (`#34225A`):** 0 contributions (empty day background)
- **Level 1 (`#6E4FB5`):** 1–3 contributions (muted violet)
- **Level 2 (`#B79CFF`):** 4–6 contributions (bright lilac)
- **Level 3 (`#FFB27A`):** 7–9 contributions (warm peach)
- **Level 4 (`#FF8A3D`):** 10+ contributions (vibrant accent orange)

---

## 3. Typography Stack

1. **Syne 800 (Extra Bold):** Wide geometric display typeface for name, section headers, badges, and footer title.
2. **DM Sans 400/500:** Clean modern sans-serif for bio text, quest objective, and commit descriptions.
3. **Space Mono 400/700:** Technical monospace font for top bar tags, skill chips, terminal commands, and footer link pills.

---

## 4. Component Structure & Living Animations

### 1. Top Bar & Hero Section
- **Top Bar:** Player index (`PLAYER 01`) and handle (`@HARIPRASATH2611`).
- **Floating Photo Card:** Embedded JPEG from [`assets/profile.png`](assets/profile.png) (face unedited) inside an orange `#FF8A3D` container with `"Full stack developer"` banner, gently floating on a 5-second sine wave (`animateTransform`).
- **Hero Bio:** Syne 800 name heading, 3-line DM Sans narrative, and live pulsing orange status indicator (`Open to new projects`).

### 2. Main Quest Card
- High-contrast lilac badge (`MAIN QUEST`) with breathing glow animation.
- Balanced padding (24px horizontal, 14px vertical) around Syne 800 text.
- Description: `"Learning vector databases, and how semantic search is built on top of them."`

### 3. Inventory (Tech Stack)
- Categorized skill rows: **FRONTEND**, **MOBILE**, **BACKEND**, **DATABASE**.
- Staggered micro-flash stroke animation sweep (`chipFlash`) across chips.
- Highlight chip: `"Vector DBs"` styled in vibrant accent orange `#FF8A3D`.

### 4. Commit Log & Contribution Snake
- Terminal header: `"git log --oneline"` with blinking orange terminal cursor.
- **53-Week Contribution Heatmap:** Real 2026 calendar data (2,903 contributions) mapped across 371 grid cells.
- **Real-Data Snake:** Traverses the zigzag path with multi-tier colored trailing body segments and glowing white/orange head.
- **Git Timeline:** 3 featured project entries (`Ryde`, `CCR-App`, `SIH26125-LuminaryForge`) with expanding radar pulse rings on orange nodes.

### 5. Footer ("Join my party")
- Lilac card surface with Syne 800 title (`Join my party`).
- Dark portfolio pill (`hariprasathportfolio-zeta.vercel.app`) with continuous light shine sweep reflection.
- Outlined contact pill (`[hariprasathd26112006@gmail.com]`).

---

## 5. Maintenance & Updates

### Rebuilding the Profile Asset
```bash
# Regenerates assets/profile-animated.svg and assets-src/profile-animated.svg
python scripts/build_full_svg.py
```

### Rendering a Local Verification Screenshot
```bash
# Uses Puppeteer to render a high-res screenshot to assets/profile-animated-render.png
node scripts/render_full_svg.js
```

### Regenerating Documentation Word Document
```bash
# Rebuilds docs/DOCUMENTATION.docx
python scripts/create_docs.py
```

### Accessibility & Reduced Motion
All animations are wrapped in:
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation: none !important;
    transform: none !important;
    filter: none !important;
  }
}
```
Users who have enabled reduced motion in their OS will see the full design in a crisp, static state.
