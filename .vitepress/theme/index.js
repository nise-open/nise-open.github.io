import DefaultTheme from 'vitepress/theme'
import Carousel from './components/Carousel.vue'

export default {
  ...DefaultTheme,
  enhanceApp({ app }) {
    app.component('Carousel', Carousel)
  }
}