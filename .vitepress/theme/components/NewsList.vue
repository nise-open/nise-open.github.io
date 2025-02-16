<template>
    <div class="news-list">
      <div class="news-item" v-for="(news, index) in newsData" :key="index">
        <a :href="news.link" class="news-link">
          <img :src="news.image" alt="news.title" class="news-image" />
          <h3 class="news-title">{{ news.title }}</h3>
          <p class="news-description">{{ news.description }}</p>
        </a>
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps } from 'vue'
  
  // 接收父组件传递的 props
  defineProps({
    newsData: {
      type: Array,
      required: true
    }
  })
  </script>
  
  <style scoped>
  .news-list {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: flex-start; 
  }

  .news-item {
    flex: 0 0 23%; 
    box-sizing: border-box;
  }
  
  .news-image {
    width: 100%;
    height: 200px;
    object-fit: cover;
  }
  
  .news-title {
    font-size: 18px;
    margin: 10px 0;
  }
  
  .news-description {
    font-size: 14px;
    color: #666;
  }
  
  .news-link {
    text-decoration: none;
    color: inherit;
  }
  </style>