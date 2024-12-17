import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  lang: 'en-US',
  title: 'NISE Laboratory',
  description: 'The website of the NISE Laboratory at the University of Electronic Science and Technology of China (UESTC).',

  /* prettier-ignore */
  head: [
    ['link', { rel: 'icon', type: 'image/png', href: '/favicon-96x96.png', size: '96x96' }],
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }],
    ['link', { rel: 'shortcut icon', href: '/favicon.ico' }],
    ['link', { rel: 'apple-touch-icon', sizes: '180x180', href: '/apple-touch-icon.png' }],
    ['meta', { name: 'apple-mobile-web-app-title', content: 'NISE' }],
    ['link', { rel: 'manifest', href: '/site.webmanifest' }]
  ],

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    logo: { src: '/favicon.svg', width: 24, height: 24 },

    nav: [
      { text: 'Home', link: '/' },
      { text: 'People', link: '/markdown-examples' },
      { text: 'Courses', link: '/markdown-examples' },
      { text: 'News', link: '/markdown-examples' },
      { text: 'Research', link: '/markdown-examples' },
      { text: 'Publications', link: '/markdown-examples' },
      { text: 'Work with us', link: '/markdown-examples' },
      { text: 'Contact us', link: '/markdown-examples' }
    ],

    sidebar: [
      {
        text: 'Examples',
        items: [
          { text: 'Markdown Examples', link: '/markdown-examples' },
          { text: 'Runtime API Examples', link: '/api-examples' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})
