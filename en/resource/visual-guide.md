---
outline: 3
---

# Visual Design Guide

This document records the complete visual design system for the Intelligent Computing Systems Laboratory (ICSL) website, serving as a reference for future maintainers.

> [!IMPORTANT] All new pages and elements must strictly follow this guide. Do not introduce independent color systems outside of this specification.

## Design Principles

Three core principles drive this system:

1. **Tech-premium**: Colors are drawn from industrial-grade blue-cyan, aligned with the IoT / computing systems academic identity
2. **Sophisticated**: Restrained color usage — no more than two hues on a single page; shadows carry a blue tint to avoid the "cheap" look of pure-black shadows
3. **Dual-mode legibility**: Light mode uses deep blue for high contrast on white; dark mode uses sky blue / cyan for high contrast on dark backgrounds. Both meet WCAG AA (contrast ratio ≥ 4.5:1)

## Color System

### Brand Colors (Brand Blue / Sapphire)

The lab's brand color is a blue-cyan dual-axis system. No purple.

| Token | Light Mode | Dark Mode | Usage |
| --- | --- | --- | --- |
| `--vp-c-brand-1` | `#0062CC` | `#38BDF8` | Links, buttons, focus rings |
| `--vp-c-brand-2` | `#0080E6` | `#0EA5E9` | Secondary interactive elements |
| `--vp-c-brand-3` | `#0096E6` | `#0284C7` | Border highlights, hover borders |
| `--vp-c-brand-soft` | `rgba(0,98,204,0.12)` | `rgba(56,189,248,0.14)` | Background tinting |

**Color swatches (light):**

<div style="display:flex;gap:8px;margin:12px 0">
  <div style="width:64px;height:36px;background:#0062CC;border-radius:6px;"></div>
  <div style="width:64px;height:36px;background:#0080E6;border-radius:6px;"></div>
  <div style="width:64px;height:36px;background:#0096E6;border-radius:6px;"></div>
  <div style="width:64px;height:36px;background:#06B6D4;border-radius:6px;"></div>
</div>

**Color swatches (dark):**

<div style="display:flex;gap:8px;margin:12px 0">
  <div style="width:64px;height:36px;background:#38BDF8;border-radius:6px;"></div>
  <div style="width:64px;height:36px;background:#0EA5E9;border-radius:6px;"></div>
  <div style="width:64px;height:36px;background:#22D3EE;border-radius:6px;"></div>
  <div style="width:64px;height:36px;background:#7DD3FC;border-radius:6px;"></div>
</div>

### Accent Color (Gold)

Gold is the only warm accent, used exclusively for: award badges and link hover states. Do not introduce additional warm colors elsewhere.

| Context              | Light Mode | Dark Mode |
| -------------------- | ---------- | --------- |
| Badge gradient start | `#D97706`  | `#FBBF24` |
| Badge gradient end   | `#B45309`  | `#F59E0B` |
| Link hover           | `#B45309`  | `#FBBF24` |

<div style="display:flex;gap:8px;margin:12px 0">
  <div style="width:64px;height:36px;background:#D97706;border-radius:6px;"></div>
  <div style="width:64px;height:36px;background:#B45309;border-radius:6px;"></div>
  <div style="width:64px;height:36px;background:#FBBF24;border-radius:6px;"></div>
  <div style="width:64px;height:36px;background:#F59E0B;border-radius:6px;"></div>
</div>

### Forbidden Colors

> [!CAUTION] The following color systems have been removed from the spec. Do not use them in new content:
>
> - **Purple family**: any `purple` / `violet` / `hsl(260~310, ...)` values
> - **Standalone green/teal**: the old `#0f766e` Teal series — replaced by the blue system
> - **Pure red**: the old Hero gradient start `#F04040` is deprecated

## Heading Hierarchy

Heading colors are layered within the blue spectrum. Each level has a distinct shade for quick visual scanning.

| Level | Light Mode              | Dark Mode              |
| ----- | ----------------------- | ---------------------- |
| `h1`  | `#004FA3` (deep blue)   | `#7DD3FC` (light blue) |
| `h2`  | `#0069BF` (mid blue)    | `#38BDF8` (sky blue)   |
| `h3`  | `#0284C7` (bright blue) | `#22D3EE` (cyan)       |

`h2` has a 15% opacity separator line in the same hue — reinforcing hierarchy without being heavy-handed.

## Hero Gradient

The lab name (Hero name) uses gradient text:

```css
/* Light mode */
background: linear-gradient(135deg, #0062cc 0%, #0096e6 40%, #06b6d4 100%);

/* Dark mode */
background: linear-gradient(135deg, #38bdf8 0%, #0ea5e9 45%, #22d3ee 100%);
```

**Design intent**: 135° gradient creates spatial depth. Light mode goes deep-blue → cyan; dark mode goes sky-blue → cyan. Directions are consistent but brightness is inverted, ensuring visual impact in each mode.

## Publication Cards

Publication list items use card layout with the following visual specifications:

| Property                   | Value                                  |
| -------------------------- | -------------------------------------- |
| `background`               | `var(--vp-c-bg-soft)` (theme-adaptive) |
| `border`                   | `1px solid var(--vp-c-divider)`        |
| `border-radius`            | `12px`                                 |
| `padding`                  | `24px`                                 |
| `box-shadow` (light)       | `0 2px 12px rgba(0,62,153,0.04)`       |
| `box-shadow` (dark)        | `0 2px 12px rgba(0,0,0,0.25)`          |
| hover `transform`          | `translateY(-4px)`                     |
| hover `box-shadow` (light) | `0 10px 28px rgba(0,62,153,0.10)`      |
| hover `border-color`       | `var(--vp-c-brand-3)`                  |

> [!TIP] Cards intentionally use blue-tinted shadows (`rgba(0,62,153,…)`) instead of pure black. This is the key detail that separates "premium" from "generic".

## Text and Links

| Element             | Light Mode                       | Dark Mode        |
| ------------------- | -------------------------------- | ---------------- |
| Link default        | `#0062CC`                        | `#38BDF8`        |
| Link hover          | `#B45309` (gold)                 | `#FBBF24` (gold) |
| Paper title (bold)  | `#004FA3`                        | `#7DD3FC`        |
| Secondary body text | `var(--vp-c-text-2)` (framework) | same             |

Link hover jumps from blue to gold — the color temperature contrast draws the eye and signals "clickable → valuable".

## Award Badge

Use `<span class="gold-badge">` for best paper and similar awards:

```html
<span class="gold-badge">*(Best Paper Award)*</span>
```

Renders as a gold gradient text using `-webkit-background-clip: text`. Both modes use warm gold, creating a deliberate warm-vs-cool contrast with the overall cold blue system — acting as a visual anchor.

## Blockquote

```css
border-left-color: #0096e6;
background: rgba(0, 150, 230, 0.05);
border-radius: 0 8px 8px 0;
```

Unlike the old gold blockquote, the current spec uses brand-blue borders. Informational callouts stay coherent with the page color system.

## File Reference

| File                          | Description                                |
| ----------------------------- | ------------------------------------------ |
| `.vitepress/theme/styles.css` | All custom styles — single source of truth |
| `.vitepress/theme/index.ts`   | Theme registration, imports styles.css     |
| `.vitepress/config/shared.ts` | Global site config, head injection         |
| `.vitepress/config/zh.ts`     | Chinese nav, footer, sidebar               |
| `.vitepress/config/en.ts`     | English nav, footer, sidebar               |
