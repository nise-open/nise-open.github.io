---
outline: 2
titleTemplate: 智能计算系统实验室
---

<script setup >
import {
  VPTeamMembers
} from 'vitepress/theme'

const coreMembers = [
  {
    avatar: '/apple-touch-icon.png',
    name: '鲁力',
    title: '教授，负责人',
    desc: '1978年生，博士，教授，博士生导师。电子科技大学计算机科学与工程学院（网络空间安全学院）副院长。主要研究方向为超低功耗高性能无线系统、物联网计算系统、以及无线系统安全。作为项目负责人承担了包括国家自然科学基金重点项目、科技部重点研发计划课题等项目20余项。在ACM MobiCom、USENIX NSDI、ACM ASPLOS等国际顶级学术会议上发表论文80余篇。获得20余项国内专利授权。作为主要成员，在工业控制系统安全方面成果获2019年国家科技进步一等奖。'
  },
  {
    avatar: '/apple-touch-icon.png',
    name: '宋超',
    title: '副教授',
    desc: '博士，副教授。长年从事图数据挖掘领域的研究，主要聚焦于动态图流挖掘、图神经网络建模及图驱动的系统优化。在知名国际会议和国际期刊上发表学术论文50余篇，获得5项国内专利授权。'
  },
  {
    avatar: '/apple-touch-icon.png',
    name: '姜辉',
    title: '助理研究员'
  }
]

const phdStudents = [
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

# 人员
## 现有成员
### 导师
<VPTeamMembers size="medium" :members="coreMembers" />

### 博士研究生
<VPTeamMembers size="small" :members="phdStudents " />

### 硕士研究生
<VPTeamMembers size="small" :members="msStudents" />

## 毕业生
### 博士
- Shengyu Li
- Songfan Li
- Chong Zhang
- Yihang Song
- Muhammad Jawad Hussain

### 硕士
