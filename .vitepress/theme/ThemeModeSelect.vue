<script setup lang="ts">
import { computed, onMounted, onUnmounted, ref } from 'vue'
import { useData } from 'vitepress'

type ThemeMode = 'light' | 'dark' | 'auto'

const storageKey = 'vitepress-theme-appearance'
const mode = ref<ThemeMode>('auto')
const systemDark = ref(false)
const { lang } = useData()

const isZh = computed(() => {
  return lang.value.startsWith('zh')
})

const label = computed(() => isZh.value ? '主题' : 'Theme')
const options = computed(() => isZh.value
  ? [
      { value: 'light', text: '白天' },
      { value: 'dark', text: '夜间' },
      { value: 'auto', text: '跟随设备' }
    ]
  : [
      { value: 'light', text: 'Light' },
      { value: 'dark', text: 'Dark' },
      { value: 'auto', text: 'System' }
    ])

function readMode(): ThemeMode {
  if (typeof localStorage === 'undefined') return 'auto'
  const value = localStorage.getItem(storageKey)
  return value === 'light' || value === 'dark' || value === 'auto' ? value : 'auto'
}

function applyMode(value: ThemeMode) {
  mode.value = value
  localStorage.setItem(storageKey, value)
  document.documentElement.classList.toggle(
    'dark',
    value === 'dark' || (value === 'auto' && systemDark.value)
  )
}

function handleSystemChange(event: MediaQueryListEvent) {
  systemDark.value = event.matches
  if (mode.value === 'auto') applyMode('auto')
}

onMounted(() => {
  const media = window.matchMedia('(prefers-color-scheme: dark)')
  systemDark.value = media.matches
  applyMode(readMode())
  media.addEventListener('change', handleSystemChange)
  onUnmounted(() => media.removeEventListener('change', handleSystemChange))
})
</script>

<template>
  <label class="NiseThemeMode" :title="label">
    <span class="NiseThemeModeLabel">{{ label }}</span>
    <select
      v-model="mode"
      class="NiseThemeModeSelect"
      :aria-label="label"
      @change="applyMode(mode)"
    >
      <option v-for="option in options" :key="option.value" :value="option.value">
        {{ option.text }}
      </option>
    </select>
  </label>
</template>
