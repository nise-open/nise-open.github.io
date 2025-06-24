---
layout: page
title: 人员
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
    name: '宋超',
    title: '副教授'
  },
      {
    avatar: '/apple-touch-icon.png',
    name: '鲁力',
    title: '教授,负责人'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '姜辉',
    title: '助理研究员'
  }
]

const phdStudents  = [
    {
    avatar: '/apple-touch-icon.png',
    name: '孟千贺',
  },
      {
    avatar: '/apple-touch-icon.png',
    name: '胡瑞林',
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '王晗',
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '张睿喆',
  },
      {
    avatar: '/apple-touch-icon.png',
    name: '赵一泽',
  }
]

const msStudents = [
    {
    avatar: '/apple-touch-icon.png',
    name: '高泽涛',
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '贺洁伟',
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '黄健锋',
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '李博宇',
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '任政',
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '符宇轩',
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '胡成昕'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '李金哲'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '唐宇阳'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '滕孟辰'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '鲜坤阳'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '徐康林'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '赵一泽'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '陈旭羿'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '何亚男'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '贺俣顺'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '吉志学'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '刘俊晖'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '庞旭'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '吴树伟'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '谢晨晨'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '杨晨'
  },
    {
    avatar: '/apple-touch-icon.png',
    name: '张皓'
  }
]
</script>

<!-- # 人员 -->

<VPTeamPage>
  <VPTeamPageTitle>
    <template #title>导师</template>
  </VPTeamPageTitle>
  <VPTeamMembers size="medium" :members="coreMembers" />
  <VPTeamPageSection>
    <template #title>博士生</template>
    <template #members>
      <VPTeamMembers size="small" :members="phdStudents " />
    </template>
  </VPTeamPageSection>
  <VPTeamPageSection>
    <template #title>硕士生</template>
    <template #members>
      <VPTeamMembers size="small" :members="msStudents" />
    </template>
  </VPTeamPageSection>
</VPTeamPage>
