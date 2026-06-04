---
titleTemplate: 智能计算系统实验室
outline: 3
---

# 视觉引导方案

本文档记录智能计算系统实验室（ICSL）网站的完整视觉设计系统，供后续维护者参考和延续。

> [!IMPORTANT]
> 所有新增页面和元素应严格遵循本方案，不得引入方案之外的独立色系。

## 设计原则

本方案以三条核心原则为出发点：

1. **科技感**：配色来自工业级蓝青色系，贴合 IoT / 计算系统领域的学术形象
2. **高级感**：克制用色，同一页面主色不超过两个色相；阴影带蓝色调，避免廉价的纯黑阴影
3. **双模式清晰**：亮色模式用深蓝保证白底对比度，暗色模式用浅蓝/青保证深底对比度，均满足 WCAG AA（对比度 ≥ 4.5:1）

## 色彩体系

### 品牌主色（Brand Blue / Sapphire）

实验室品牌色为蓝青双轴体系，不含紫色。

| Token | 亮色模式 | 暗色模式 | 用途 |
|---|---|---|---|
| `--vp-c-brand-1` | `#0062CC` | `#38BDF8` | 链接、按钮、焦点框 |
| `--vp-c-brand-2` | `#0080E6` | `#0EA5E9` | 次级交互元素 |
| `--vp-c-brand-3` | `#0096E6` | `#0284C7` | 边框高亮、hover 边框 |
| `--vp-c-brand-soft` | `rgba(0,98,204,0.12)` | `rgba(56,189,248,0.14)` | 背景浅染色 |

**色块预览（亮色）：**

<div style="display:flex;gap:8px;margin:12px 0">
  <div style="width:64px;height:36px;background:#0062CC;border-radius:6px;"></div>
  <div style="width:64px;height:36px;background:#0080E6;border-radius:6px;"></div>
  <div style="width:64px;height:36px;background:#0096E6;border-radius:6px;"></div>
  <div style="width:64px;height:36px;background:#06B6D4;border-radius:6px;"></div>
</div>

**色块预览（暗色）：**

<div style="display:flex;gap:8px;margin:12px 0">
  <div style="width:64px;height:36px;background:#38BDF8;border-radius:6px;"></div>
  <div style="width:64px;height:36px;background:#0EA5E9;border-radius:6px;"></div>
  <div style="width:64px;height:36px;background:#22D3EE;border-radius:6px;"></div>
  <div style="width:64px;height:36px;background:#7DD3FC;border-radius:6px;"></div>
</div>

### 强调色（Gold Accent）

金色作为唯一的暖色强调，用于：获奖徽章、链接 hover 态。严禁在其他场景引入额外暖色。

| 场景 | 亮色模式 | 暗色模式 |
|---|---|---|
| 获奖徽章渐变起点 | `#D97706` | `#FBBF24` |
| 获奖徽章渐变终点 | `#B45309` | `#F59E0B` |
| 链接 hover 色 | `#B45309` | `#FBBF24` |

<div style="display:flex;gap:8px;margin:12px 0">
  <div style="width:64px;height:36px;background:#D97706;border-radius:6px;"></div>
  <div style="width:64px;height:36px;background:#B45309;border-radius:6px;"></div>
  <div style="width:64px;height:36px;background:#FBBF24;border-radius:6px;"></div>
  <div style="width:64px;height:36px;background:#F59E0B;border-radius:6px;"></div>
</div>

### 禁用色系

> [!CAUTION]
> 以下色系已从方案中移除，新增内容不得使用：
> - **紫色系**：任何 `purple` / `violet` / `hsl(260~310, ...)` 色值
> - **独立绿色系**：旧方案中的 `#0f766e`（Teal）系列，已被蓝色系统替代
> - **纯红色**：旧 Hero 渐变起点 `#F04040` 已废弃

## 标题层级

标题颜色严格按照蓝色系内部明度分层，不同层级颜色有所区分便于扫视。

| 层级 | 亮色模式 | 暗色模式 |
|---|---|---|
| `h1` | `#004FA3`（深蓝） | `#7DD3FC`（淡蓝） |
| `h2` | `#0069BF`（中蓝） | `#38BDF8`（天蓝） |
| `h3` | `#0284C7`（亮蓝） | `#22D3EE`（青） |

`h2` 下方有一条 `15% opacity` 的分割线，颜色与标题同色相，强化层级但不喧宾夺主。

## Hero 首页渐变

实验室名称（Hero name）采用渐变文字：

```css
/* 亮色模式 */
background: linear-gradient(135deg, #0062CC 0%, #0096E6 40%, #06B6D4 100%);

/* 暗色模式 */
background: linear-gradient(135deg, #38BDF8 0%, #0EA5E9 45%, #22D3EE 100%);
```

**设计意图**：135° 角渐变制造空间深度感；亮色从深蓝到青，暗色从天蓝到青，两者方向一致但亮度倒置，确保各自模式下的视觉冲击力。

## 论文卡片

论文列表使用卡片式布局，视觉层次规格如下：

| 属性 | 值 |
|---|---|
| `background` | `var(--vp-c-bg-soft)`（随主题自适应） |
| `border` | `1px solid var(--vp-c-divider)` |
| `border-radius` | `12px` |
| `padding` | `24px` |
| `box-shadow`（亮色） | `0 2px 12px rgba(0,62,153,0.04)` |
| `box-shadow`（暗色） | `0 2px 12px rgba(0,0,0,0.25)` |
| hover `transform` | `translateY(-4px)` |
| hover `box-shadow`（亮色） | `0 10px 28px rgba(0,62,153,0.10)` |
| hover `border-color` | `var(--vp-c-brand-3)` |

> [!TIP]
> 卡片阴影特意使用带蓝色调的 `rgba(0,62,153,…)` 而非纯黑，这是区分"高级感"与"廉价感"的关键细节。

## 文字与链接

| 元素 | 亮色 | 暗色 |
|---|---|---|
| 链接默认 | `#0062CC` | `#38BDF8` |
| 链接 hover | `#B45309`（金） | `#FBBF24`（金） |
| 论文标题加粗 | `#004FA3` | `#7DD3FC` |
| 正文次级文字 | `var(--vp-c-text-2)`（框架自动） | 同左 |

链接 hover 从蓝跳到金，制造色温对比，引导用户注意力并暗示「可点击→有价值」。

## 获奖徽章

`<span class="gold-badge">` 用于最佳论文等获奖标注：

```html
<span class="gold-badge">*(Best Paper Award)*</span>
```

渲染效果为金色渐变文字，使用 `-webkit-background-clip: text` 实现，两种模式下均为暖金色，形成视觉锚点，与整体冷蓝系形成有意的对比。

## 区块引用

```css
border-left-color: #0096E6;
background: rgba(0, 150, 230, 0.05);
border-radius: 0 8px 8px 0;
```

与旧方案的金色 blockquote 不同，当前方案统一为品牌蓝边框，信息类引用与页面整体色系一致。

## 文件位置

| 文件 | 说明 |
|---|---|
| `.vitepress/theme/styles.css` | 全部自定义样式，单一入口 |
| `.vitepress/theme/index.ts` | 主题注册，引入 styles.css |
| `.vitepress/config/shared.ts` | 站点全局配置、head 注入 |
| `.vitepress/config/zh.ts` | 中文导航、页脚、sidebar |
| `.vitepress/config/en.ts` | 英文导航、页脚、sidebar |
