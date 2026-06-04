with open('.vitepress/theme/styles.css', 'r') as f:
    css = f.read()

# Fix the paper titles selector
old_selector = """.vp-doc ul > li > strong:first-child,
.vp-doc ol > li > strong:first-child {
  color: #2563eb;
  font-size: 1.05em;
  display: inline-block;
  margin-bottom: 4px;
}

.dark .vp-doc ul > li > strong:first-child,
.dark .vp-doc ol > li > strong:first-child {
  color: #60a5fa;
}"""

new_selector = """.vp-doc ul > li > strong:first-child,
.vp-doc ol > li > strong:first-child,
.vp-doc ul > li > p:first-child > strong:first-child,
.vp-doc ol > li > p:first-child > strong:first-child {
  color: #2563eb;
  font-size: 1.05em;
  display: inline-block;
  margin-bottom: 4px;
}

.dark .vp-doc ul > li > strong:first-child,
.dark .vp-doc ol > li > strong:first-child,
.dark .vp-doc ul > li > p:first-child > strong:first-child,
.dark .vp-doc ol > li > p:first-child > strong:first-child {
  color: #60a5fa;
}"""

css = css.replace(old_selector, new_selector)

# Update Link hover to Gold
old_links = """.vp-doc a {
  color: var(--vp-c-brand-1);
  font-weight: 500;
  text-decoration: underline;
  text-decoration-color: transparent;
  text-decoration-thickness: 2px;
  text-underline-offset: 4px;
  transition: all 0.25s ease;
}

.vp-doc a:hover {
  color: var(--vp-c-brand-2);
  text-decoration-color: var(--vp-c-brand-soft);
}"""

new_links = """.vp-doc a {
  color: var(--vp-c-brand-1);
  font-weight: 500;
  text-decoration: underline;
  text-decoration-color: transparent;
  text-decoration-thickness: 2px;
  text-underline-offset: 4px;
  transition: all 0.25s ease;
}

.vp-doc a:hover {
  color: #d97706; /* Gold/Amber hover */
  text-decoration-color: rgba(217, 119, 6, 0.3);
}

.dark .vp-doc a:hover {
  color: #fbbf24;
  text-decoration-color: rgba(251, 191, 36, 0.4);
}"""

css = css.replace(old_links, new_links)

# Add Gold Badges and Blockquotes
gold_extras = """

/* Gold Accents & Badges */
.gold-badge {
  color: #d97706;
  font-weight: bold;
  background: linear-gradient(120deg, #f59e0b, #d97706);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display: inline-block;
}

.dark .gold-badge {
  color: #fbbf24;
  background: linear-gradient(120deg, #fbbf24, #f59e0b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* Gold border for Blockquotes to add elegance */
.vp-doc blockquote {
  border-left-color: #f59e0b;
  background: rgba(245, 158, 11, 0.05);
  padding-right: 16px;
  border-radius: 0 8px 8px 0;
}

.dark .vp-doc blockquote {
  border-left-color: #fbbf24;
  background: rgba(251, 191, 36, 0.1);
}
"""

if "gold-badge" not in css:
    css += gold_extras

with open('.vitepress/theme/styles.css', 'w') as f:
    f.write(css)

