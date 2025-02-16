import DefaultTheme from 'vitepress/theme'
import Carousel from './components/Carousel.vue'
import NewsList from './components/NewsList.vue'

export default {
  ...DefaultTheme,
  enhanceApp({ app }) {
    app.component('Carousel', Carousel)
    app.component('NewsList', NewsList)
  }
}