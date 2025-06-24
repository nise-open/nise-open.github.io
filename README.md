# NISE Lab Official Site

Source code for the Network Intelligence & Security Laboratory official website, built with VitePress.

* 🌐 **Live Site**: [https://www.nise.ac.cn](https://www.nise.ac.cn)
* 🗃️ **GitHub Repo**: [https://github.com/nise-open/nise-open.github.io](https://github.com/nise-open/nise-open.github.io)

---

## 🧩 Project Structure

```
/
├─ .github/
│   └─ workflows/deploy.yml       # GitHub Actions for build + deploy
├─ .vitepress/
│   ├─ config/
│   │   ├─ index.ts              # merges shared + en + zh via `locales`
│   │   ├─ shared.ts             # shared VitePress config
│   │   ├─ en.ts                 # English-specific config
│   │   └─ zh.ts                 # Chinese-specific config
│   └─ theme/
│       ├─ index.ts             # custom theme extension
│       └─ styles.css           # theme styles
├─ en/                          # English content
│   └─ *.md                     # index, people, publication, etc.
├─ zh/                          # Chinese content
│   └─ *.md                     # mirror structure for Chinese
├─ public/                      # static assets
├─ CNAME                         # custom domain setup
├─ LICENSE
└─ package.json
```

---

## 🌐 i18n / Localization

Your setup uses VitePress i18n via separate config files (`en.ts` & `zh.ts`) and directory-based content (`/en`, `/zh`).
Ensure `locales` is configured in `.vitepress/config/index.ts`:

```ts
import shared from './shared'
import en from './en'
import zh from './zh'
export default defineConfig({
  ...shared,
  locales: {
    root: { label: 'English', lang: 'en-US', link: '/en/', ...en },
    zh: { label: '简体中文', lang: 'zh-CN', link: '/zh/', ...zh }
  }
})
```

---

## ⚙️ Build & Run

Install dependencies (recommended: [bun](https://bun.sh), [yarn](https://yarnpkg.com), or npm):

```bash
# Prefer bun
git clone https://github.com/nise-open/nise-open.github.io.git
cd nise-open.github.io
bun install

# Or use yarn
yarn install

# Or use npm
npm install
```

Run dev server:

```bash
bun run docs:dev
# or
yarn docs:dev
# or
npm run docs:dev

# open http://localhost:3000/en/ or /zh/
```

Build production:

```bash
bun run docs:build
# or
yarn docs:build
# or
npm run docs:build
```

---

## 🚀 Deploy via GitHub Pages

Workflow defined in `.github/workflows/deploy.yml` uses VitePress build and GitHub Pages actions.
A typical workflow would:

1. Trigger on push to `main`
2. Checkout, setup Node
3. `npm ci` → `npm run docs:build`
4. Deploy `.vitepress/dist` via `configure-pages`, `upload-pages-artifact`, and `deploy-pages`

---

## 🛠️ Theme & Extensions

* Contains a custom theme in `.vitepress/theme/`.
* Add support for Vue components, styling via CSS.
* You may further integrate plugins like pagefind (search) or shiki code highlighting.

---

## ✍️ Content Guidelines

* Write Markdown under `/en/` and `/zh/`, mirroring file structure.
* Use frontmatter (`lang`, `title`) as needed.
* You can embed Vue components in Markdown.
* Static assets (logos, icons) go into `public/`.

---

## ✅ Contributing

We welcome PRs & issues:

1. Fork the repo
2. Create a branch (`feat/...` or `fix/...`)
3. Add/modify pages, translations, config
4. Open a PR with clear context

---

## 📄 License

MIT — see [LICENSE](LICENSE)

---

## 📬 Contact

* 📧 Email: [public@nise.ac.cn](mailto:public@nise.ac.cn)
* 🔗 Lab Website: [https://www.nise.ac.cn](https://www.nise.ac.cn)
