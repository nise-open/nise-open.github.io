---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "NISE Laboratory"
  tagline: "Forging Universal Connectivity"


---

<style scoped>
.pagination {
  margin-top: 20px;
  text-align: center;
}


.pagination button {
  margin: 0 5px;
  padding: 5px 10px;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 5px;
  cursor: pointer;
}

.pagination button:disabled {
  background-color: #ddd;
}
</style>

<script setup>
import { ref, computed } from 'vue'

const images = [
  'apple-touch-icon.png',
  'favicon-96x96.png',
  'apple-touch-icon.png'
]

// 定义新闻数据
const newsData = [
]

// 控制当前页码
const currentPage = ref(1)
const newsPerPage = 12

// 计算总页数
const totalPages = computed(() => Math.ceil(newsData.length / newsPerPage))

// 控制新闻分页
const visibleNews = computed(() => {
  const start = (currentPage.value - 1) * newsPerPage
  return newsData.slice(start, start + newsPerPage)
})

// 翻页控制
const nextPage = () => {
  if (currentPage.value < totalPages.value) currentPage.value++
}

const prevPage = () => {
  if (currentPage.value > 1) currentPage.value--
}
</script>

<Carousel :images="images" :interval="3000" />

The NISE laboratory is led by Prof. Li Lu. We are part of the School of Computer Science and Engineering, University of Electronic Science and Technology of China.

Founded in January 2018, the network intelligence and security team is committed to basic research and corresponding system research and development in the fields of wireless systems and security, passive systems, RFID technology, network and system security, data mining and recommendation, and intelligent video analysis. The research team includes 2 professors, 1 senior engineer and 1 associate professor. Among them, there are 2 doctoral supervisors, 1 postdoctoral fellow, 1 master's supervisor, and nearly 30 master's and doctoral students. In the past five years, the team has undertaken a number of projects such as the National Natural Science Foundation of China, the National Key R&D Programme, the National 863 Programme, and the National Science and Technology Support. Won the third prize of Sichuan Provincial Science and Technology Progress Award.

We has made many research achievements in passive wireless perception Internet of Things systems, wireless embedded systems, intelligent information processing, etc., and has published more than 200 papers in well-known Transactions journals and top international academic conferences, including ACM/IEEE. The team has a laboratory area of more than 160 square metres, with complete R&D equipment and various system software, application software and design and development tools; it provides a complete R&D chain from perception front-end design, communication protocols and systems, intelligent information processing, cloud systems, and network security.

## <a href="./pages/news" style="text-decoration: none;">NISE News</a>

<NewsList :newsData="visibleNews" :currentPage="currentPage" :newsPerPage="newsPerPage" />

<div class="pagination">
  <button @click="prevPage" :disabled="currentPage === 1">Previous</button>
  <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
</div>