import { defineConfig } from 'vitepress'

export const en = defineConfig({
  lang: 'en-US',
  description: 'The website of Network Intelligence and Security Laboratory at the University of Electronic Science and Technology of China.',

  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'People', link: '/people' },
      {
        text: 'Research', items: [
          { text: 'Research', link: '/research' },
          { text: 'Publications', link: '/publications' },
        ]
      },
      { text: 'Work with us', link: '/work' },
      { text: 'Contact us', link: '/contact' }
    ],

    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2024-present NISE Laboratory'
    }
  }
})
