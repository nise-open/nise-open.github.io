import { defineConfig } from 'vitepress'

export const en = defineConfig({
  lang: 'en-US',
  description: 'The website of Intelligent Computing Systems Laboratory at the University of Electronic Science and Technology of China.',

  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'People', link: '/people' },
      { text: 'Publications', link: '/publication' },
      { text: 'Resources', link: '/resource' },
      { text: 'Contact us', link: '/contact' },
    ],

    sidebar: {
      '/resource': [
        {
          text: 'Resources',
          items: [
            { text: 'Overview', link: '/resource' },
            { text: 'Visual Design Guide', link: '/resource/visual-guide' },
          ]
        }
      ],
    },

    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2024-present Intelligent Computing Systems Laboratory'
    }
  }
})
