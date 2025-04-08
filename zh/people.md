---
layout: page
titleTemplate: 网络智能与安全实验室
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
    avatar: '/apple-touch-icon.png',
    name: '鲁力',
    title: '教授,负责人'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '宋超',
    title: '副教授'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '姜辉',
    title: '研究员'
  }
]

const PHDStudents = [
    {
    avatar: '/apple-touch-icon.png',
    name: '李松璠',
    title: '博士研究生'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '宋一杭',
    title: '博士研究生'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '张翀',
    title: '博士研究生'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '孟千贺',
    title: '博士研究生'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '李圣雨',
    title: '博士研究生'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '王晗',
    title: '博士研究生'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '张睿喆',
    title: '博士研究生'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '胡瑞林',
    title: '博士研究生'
  }
]

const MasterStudents = [
    {
    avatar: '/apple-touch-icon.png',
    name: '高泽涛',
    title: '硕士研究生,2022'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '贺洁伟',
    title: '硕士研究生,2022'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '黄健锋',
    title: '硕士研究生,2022'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '李博宇',
    title: '硕士研究生,2022'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '任政',
    title: '硕士研究生,2022'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '符宇轩',
    title: '硕士研究生,2023',
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '胡成昕',
    title: '硕士研究生,2023'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '李金哲',
    title: '硕士研究生,2023'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '唐宇阳',
    title: '硕士研究生,2023'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '滕孟辰',
    title: '硕士研究生,2023'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '鲜坤阳',
    title: '硕士研究生,2023'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '徐康林',
    title: '硕士研究生,2023'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '赵一泽',
    title: '硕士研究生,2023'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '陈旭羿',
    title: '硕士研究生,2024'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '何亚男',
    title: '硕士研究生,2024'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '贺俣顺',
    title: '硕士研究生,2024'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '吉志学',
    title: '硕士研究生,2024'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '刘俊晖',
    title: '硕士研究生,2024'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '庞旭',
    title: '硕士研究生,2024'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '吴树伟',
    title: '硕士研究生,2024'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '谢晨晨',
    title: '硕士研究生,2024'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '杨晨',
    title: '硕士研究生,2024'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '张皓',
    title: '硕士研究生,2024'
  }
]
</script>

<VPTeamPage>
  <VPTeamPageTitle>
    <template #title>导师</template>
  </VPTeamPageTitle>
  <VPTeamMembers size="medium" :members="coreMembers" />
  <VPTeamPageSection>
    <template #title>博士生</template>
    <template #members>
      <VPTeamMembers size="small" :members="PHDStudents" />
    </template>
  </VPTeamPageSection>
  <VPTeamPageSection>
    <template #title>硕士生</template>
    <template #members>
      <VPTeamMembers size="small" :members="MasterStudents" />
    </template>
  </VPTeamPageSection>
</VPTeamPage>