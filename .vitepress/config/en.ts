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
          { text: 'Overview', link: '/research' },
          { text: 'Publications', link: '/publication' },
        ]
      },
      { text: 'Resources', link: '/resource' },
      {
        text: 'Contact us', items: [
          { text: 'Work with us', link: '/work' },
          { text: 'Contact Info', link: '/contact' },
        ]
      }
    ],

    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2024-present NISE Laboratory'
    }
  }
})
