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
  { image: 'apple-touch-icon.png', title: 'Meet our Members: Giray Yağlıkçı discusses his PhD work, RowHammer and future plans', description: 'Interview with Giray discussing his PhD work and future plans.', link: '/news/1' },
  { image: 'apple-touch-icon.png', title: 'RowHammer paper wins the 2024 Jean-Claude Laprie Award', description: 'RowHammer paper awarded the 2024 Jean-Claude Laprie Award.', link: '/news/2' },
  { image: 'apple-touch-icon.png', title: 'Join us for Track 4 at the EFCL Summer School in June', description: 'Join us for Track 4 at the EFCL Summer School in June 2024.', link: '/news/3' },
  { image: 'apple-touch-icon.png', title: 'SAFARI Live Seminar: Jonas Juffinger, July 16 2024', description: 'Join us for an exciting seminar with Jonas Juffinger on July 16, 2024.', link: '/news/4' },
  { image: 'apple-touch-icon.png', title: 'Keynote talk at the Qualcomm Product Security Summit May 17, 2024', description: 'Giray discusses his research at the Qualcomm Summit.', link: '/news/5' },
  { image: 'apple-touch-icon.png', title: 'SAFARI-EFCL Seminar: Reetu Das, May 21 2024', description: 'Join the seminar on May 21 with Reetu Das.', link: '/news/6' },
  { image: 'apple-touch-icon.png', title: 'Abdullah Giray Yağlıkçı successfully defends his PhD', description: 'Congratulations to Abdullah Giray Yağlıkçı on his PhD defense.', link: '/news/7' },
  { image: 'apple-touch-icon.png', title: 'SAFARI Live Seminar: Konstantina Koliohgeorgi, January 29 2024', description: 'Join the seminar with Konstantina Koliohgeorgi on January 29.', link: '/news/8' },
  { image: 'apple-touch-icon.png', title: 'SAFARI Live Seminar: Abdullah Giray Yağlıkçı, January 17 2024', description: 'Join the seminar with Abdullah Giray Yağlıkçı on January 17.', link: '/news/9' },
  { image: 'apple-touch-icon.png', title: 'Meet our Members: Giray Yağlıkçı discusses his PhD work, RowHammer and future plans', description: 'Interview with Giray discussing his PhD work and future plans.', link: '/news/1' },
  { image: 'apple-touch-icon.png', title: 'RowHammer paper wins the 2024 Jean-Claude Laprie Award', description: 'RowHammer paper awarded the 2024 Jean-Claude Laprie Award.', link: '/news/2' },
  { image: 'apple-touch-icon.png', title: 'Join us for Track 4 at the EFCL Summer School in June', description: 'Join us for Track 4 at the EFCL Summer School in June 2024.', link: '/news/3' },
  { image: 'apple-touch-icon.png', title: 'SAFARI Live Seminar: Jonas Juffinger, July 16 2024', description: 'Join us for an exciting seminar with Jonas Juffinger on July 16, 2024.', link: '/news/4' },
  { image: 'apple-touch-icon.png', title: 'Keynote talk at the Qualcomm Product Security Summit May 17, 2024', description: 'Giray discusses his research at the Qualcomm Summit.', link: '/news/5' },
  { image: 'apple-touch-icon.png', title: 'SAFARI-EFCL Seminar: Reetu Das, May 21 2024', description: 'Join the seminar on May 21 with Reetu Das.', link: '/news/6' },
  { image: 'apple-touch-icon.png', title: 'Abdullah Giray Yağlıkçı successfully defends his PhD', description: 'Congratulations to Abdullah Giray Yağlıkçı on his PhD defense.', link: '/news/7' },
  { image: 'apple-touch-icon.png', title: 'SAFARI Live Seminar: Konstantina Koliohgeorgi, January 29 2024', description: 'Join the seminar with Konstantina Koliohgeorgi on January 29.', link: '/news/8' },
  { image: 'apple-touch-icon.png', title: 'SAFARI Live Seminar: Abdullah Giray Yağlıkçı, January 17 2024', description: 'Join the seminar with Abdullah Giray Yağlıkçı on January 17.', link: '/news/9' },
  { image: 'apple-touch-icon.png', title: 'RowHammer paper wins the 2024 Jean-Claude Laprie Award', description: 'RowHammer paper awarded the 2024 Jean-Claude Laprie Award.', link: '/news/2' },
  { image: 'apple-touch-icon.png', title: 'Join us for Track 4 at the EFCL Summer School in June', description: 'Join us for Track 4 at the EFCL Summer School in June 2024.', link: '/news/3' },
  { image: 'apple-touch-icon.png', title: 'SAFARI Live Seminar: Jonas Juffinger, July 16 2024', description: 'Join us for an exciting seminar with Jonas Juffinger on July 16, 2024.', link: '/news/4' },
  { image: 'apple-touch-icon.png', title: 'Keynote talk at the Qualcomm Product Security Summit May 17, 2024', description: 'Giray discusses his research at the Qualcomm Summit.', link: '/news/5' },
  { image: 'apple-touch-icon.png', title: 'SAFARI-EFCL Seminar: Reetu Das, May 21 2024', description: 'Join the seminar on May 21 with Reetu Das.', link: '/news/6' },
  { image: 'apple-touch-icon.png', title: 'Abdullah Giray Yağlıkçı successfully defends his PhD', description: 'Congratulations to Abdullah Giray Yağlıkçı on his PhD defense.', link: '/news/7' },
  { image: 'apple-touch-icon.png', title: 'SAFARI Live Seminar: Konstantina Koliohgeorgi, January 29 2024', description: 'Join the seminar with Konstantina Koliohgeorgi on January 29.', link: '/news/8' },
  { image: 'apple-touch-icon.png', title: 'SAFARI Live Seminar: Abdullah Giray Yağlıkçı, January 17 2024', description: 'Join the seminar with Abdullah Giray Yağlıkçı on January 17.', link: '/news/9' },

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

&nbsp;&nbsp;The NISE laboratory is led by Prof. Li Lu. We are part of the School of Computer Science and Engineering, University of Electronic Science and Technology of China.

&nbsp;&nbsp;Founded in January 2018, the network intelligence and security team is committed to basic research and corresponding system research and development in the fields of wireless systems and security, passive systems, RFID technology, network and system security, data mining and recommendation, and intelligent video analysis. The research team includes 2 professors, 1 senior engineer and 1 associate professor. Among them, there are 2 doctoral supervisors, 1 postdoctoral fellow, 1 master's supervisor, and nearly 30 master's and doctoral students. In the past five years, the team has undertaken a number of projects such as the National Natural Science Foundation of China, the National Key R&D Programme, the National 863 Programme, and the National Science and Technology Support. Won the third prize of Sichuan Provincial Science and Technology Progress Award.

&nbsp;&nbsp;We has made many research achievements in passive wireless perception Internet of Things systems, wireless embedded systems, intelligent information processing, etc., and has published more than 200 papers in well-known Transactions journals and top international academic conferences, including ACM/IEEE. The team has a laboratory area of more than 160 square metres, with complete R&D equipment and various system software, application software and design and development tools; it provides a complete R&D chain from perception front-end design, communication protocols and systems, intelligent information processing, cloud systems, and network security.

## <a href="./pages/news" style="text-decoration: none;">NISE News</a>

<NewsList :newsData="visibleNews" :currentPage="currentPage" :newsPerPage="newsPerPage" />

<div class="pagination">
  <button @click="prevPage" :disabled="currentPage === 1">Previous</button>
  <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
</div>