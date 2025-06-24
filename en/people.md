---
layout: page
title: People
---

<script setup>
import {
  VPTeamPage,
  VPTeamPageTitle,
  VPTeamMembers,
  VPTeamPageSection
} from 'vitepress/theme'


const coreMembers = [
  {
    name: 'Chao Song',
    title: 'Associate Professor'
  },
  {
    name: 'Li Lu',
    title: 'Professor,Director'
  },
    {
    name: 'Hui Jiang',
    title: 'Research Assistant'
  }
]

const PHDStudents = [
    {
    avatar: 'apple-touch-icon.png',
    name: 'Songfan Li',
    title: 'PH.D. Student'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Yihang Song',
    title: 'PH.D. Student'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Chong Zhang',
    title: 'PH.D. Student'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Qianhe Meng',
    title: 'PH.D. Student'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Shengyu Li',
    title: 'PH.D. Student'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Han Wang',
    title: 'PH.D. Student'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Ruizhe Zhang',
    title: 'PH.D. Student'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Ruilin Hu',
    title: 'PH.D. Student'
  }
]

const MasterStudents = [
    {
    avatar: 'apple-touch-icon.png',
    name: 'Zetao Gao',
    title: 'Ms,2022'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Jiewei He',
    title: 'Ms,2022'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Jianfeng Huang',
    title: 'Ms,2022'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Boyu Li',
    title: 'Ms,2022'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Zheng Ren',
    title: 'Ms,2022'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Yuxuan Fu',
    title: 'Ms,2023',
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Chengxin Hu',
    title: 'Ms,2023'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Jinzhe Li',
    title: 'Ms,2023'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Yuyang Tang',
    title: 'Ms,2023'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Mengchen Teng',
    title: 'Ms,2023'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Kunyang Xian',
    title: 'Ms,2023'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Kanglin Xu',
    title: 'Ms,2023'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Yize Zhao',
    title: 'Ms,2023'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Xuyi Chen',
    title: 'Ms,2024'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Yanan He',
    title: 'Ms,2024'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Yushun He',
    title: 'Ms,2024'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Zhixue Ji',
    title: 'Ms,2024'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Junhui Liu',
    title: 'Ms,2024'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Xu Pang',
    title: 'Ms,2024'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Shuwei Wu',
    title: 'Ms,2024'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Chenchen Xie',
    title: 'Ms,2024'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Chen Yang',
    title: 'Ms,2024'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Hao Zhang',
    title: 'Ms,2024'
  }
]
</script>

<!-- # People -->

<VPTeamPage>
  <VPTeamPageTitle>
    <template #title>Supervisors</template>
  </VPTeamPageTitle>
  <VPTeamMembers size="medium" :members="coreMembers" />
  <VPTeamPageSection>
    <template #title>PHD Students</template>
    <template #members>
      <VPTeamMembers size="small" :members="PHDStudents" />
    </template>
  </VPTeamPageSection>
  <VPTeamPageSection>
    <template #title>Master Students</template>
    <template #members>
      <VPTeamMembers size="small" :members="MasterStudents" />
    </template>
  </VPTeamPageSection>
</VPTeamPage>