---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "NISE Laboratory"
  tagline: "Forging Universal Connectivity"

---
<style scoped>

</style>

<script setup>
  const images = [
    '/public/apple-touch-icon.png',
    '/public/favicon-96x96.png',
    '/public/apple-touch-icon.png'
  ]
</script>

<Carousel :images="images" :interval="3000" />