<template>
  <div 
    class="carousel-container"
    @mouseenter="pauseAutoPlay"
    @mouseleave="resumeAutoPlay"
  >
    <div class="carousel-track" :style="trackStyles">
      <div 
        v-for="(img, index) in slides" 
        :key="index"
        class="slide"
      >
        <img :src="img" :alt="`Slide ${index}`">
      </div>
    </div>

    <button class="arrow left" @click="prevSlide">‹</button>
    <button class="arrow right" @click="nextSlide">›</button>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'

const props = defineProps({
  images: {
    type: Array,
    required: true,
    validator: arr => arr.length >= 2
  },
  interval: {
    type: Number,
    default: 5000
  }
})

// 创建首尾克隆用于无缝循环
const slides = computed(() => [
  props.images[props.images.length - 1],
  ...props.images,
  props.images[0]
])

const currentIndex = ref(1)
let autoPlayTimer = null
const isTransitioning = ref(true)

const trackStyles = computed(() => ({
  transform: `translateX(-${currentIndex.value * 100}%)`,
  transition: isTransitioning.value ? 'transform 0.5s ease-in-out' : 'none'
}))

const nextSlide = () => {
  isTransitioning.value = true
  currentIndex.value++
  
  if (currentIndex.value === slides.value.length - 1) {
    setTimeout(() => {
      isTransitioning.value = false
      currentIndex.value = 1
    }, 500)
  }
}

const prevSlide = () => {
  isTransitioning.value = true
  currentIndex.value--
  
  if (currentIndex.value === 0) {
    setTimeout(() => {
      isTransitioning.value = false
      currentIndex.value = slides.value.length - 2
    }, 500)
  }
}

// 自动播放控制
const startAutoPlay = () => {
  autoPlayTimer = setInterval(nextSlide, props.interval)
}

const pauseAutoPlay = () => {
  clearInterval(autoPlayTimer)
  autoPlayTimer = null
}

const resumeAutoPlay = () => {
  if (!autoPlayTimer) startAutoPlay()
}

onMounted(startAutoPlay)
onBeforeUnmount(pauseAutoPlay)
</script>

<style scoped>
/* 灰色背景容器 */
.carousel-container {
  position: relative;
  overflow: hidden;
  width: 100%;
  height: 500px;
  background: #f0f0f0 !important; /* 强制灰色背景 */
  margin: 2rem 0;
  border-radius: 8px;
  box-shadow: 0 4px 18px rgba(32, 62, 116, 0.15);
}

.carousel-track {
  display: flex;
  height: 100%;
  width: 100%;
}

.slide {
  flex: 0 0 100%;
  min-width: 100%;
  height: 100%;
}

img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
}

/* 导航按钮样式 */
.arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.5);
  border: none;
  color: white;
  font-size: 2.5rem;
  width: 45px;
  height: 65px;
  cursor: pointer;
  opacity: 0;
  transition: all 0.3s ease;
  border-radius: 4px;
}

.arrow:hover {
  background: rgba(0, 0, 0, 0.8);
}

.carousel-container:hover .arrow {
  opacity: 1;
}

.left { left: 15px; }
.right { right: 15px; }
</style>