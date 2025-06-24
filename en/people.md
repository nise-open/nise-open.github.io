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
    avatar: 'apple-touch-icon.png',
    name: 'Chao Song',
    title: 'Associate Professor'
  },
  {
    avatar: '/apple-touch-icon.png',
    name: 'Li Lu',
    title: 'Professor, Director'
  },
  {
    avatar: 'apple-touch-icon.png',
    name: 'Hui Jiang',
    title: 'Research Assistant Professor'
  }
]

const phdStudents  = [
    {
    avatar: 'apple-touch-icon.png',
    name: 'Qianhe Meng'
  },
      {
    avatar: 'apple-touch-icon.png',
    name: 'Ruilin Hu'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Han Wang'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Ruizhe Zhang'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Ruilin Hu'
  },
      {
    avatar: 'apple-touch-icon.png',
    name: 'Yize Zhao'
  },
]

const msStudents = [
    {
    avatar: 'apple-touch-icon.png',
    name: 'Zetao Gao',
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Jiewei He',
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Jianfeng Huang',
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Boyu Li',
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Zheng Ren',
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Yuxuan Fu',
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Chengxin Hu'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Jinzhe Li'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Yuyang Tang'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Mengchen Teng'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Kunyang Xian'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Kanglin Xu'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Yize Zhao'
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Xuyi Chen',
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Yanan He',
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Yushun He',
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Zhixue Ji',
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Junhui Liu',
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Xu Pang',
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Shuwei Wu',
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Chenchen Xie',
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Chen Yang',
  },
    {
    avatar: 'apple-touch-icon.png',
    name: 'Hao Zhang',
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
      <VPTeamMembers size="small" :members="phdStudents " />
    </template>
  </VPTeamPageSection>
  <VPTeamPageSection>
    <template #title>Master Students</template>
    <template #members>
      <VPTeamMembers size="small" :members="msStudents" />
    </template>
  </VPTeamPageSection>
  <VPTeamPageSection>
    <template #title>Alumni</template>
    
## PhD Alumni

- Shengyu Li
- Songfan Li
- Chong Zhang
- Yihang Song
- Muhammad Jawad Hussain

## Master Alumni

  </VPTeamPageSection>
</VPTeamPage>
