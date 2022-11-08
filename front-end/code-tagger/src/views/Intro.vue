<template>
  <header-nav></header-nav>
  <div class="container">
    <div class="header-title"><h3>平台使用说明</h3></div>
    <a-divider style="margin-top: -5px"></a-divider>
    <div class="main">
      <div class="section">
        <h4>个人首页</h4>
        <h5>
          首页轮播图或导航栏处点击‘FAQ问答管理’即可进入操作页面，包含应用
          列表、FAQ问题列表、训练历史、流程列表、流程图等页面。
        </h5>
        <h5 v-for="(i, index) in list" :key="index">{{ i }}</h5>
      </div>
      <a-divider></a-divider>
      <div class="section">
        <h4>代码库</h4>
        <h5>首页轮播图或导航栏处点击‘在线聊天机器人’即可进入操作页面。</h5>
        <h5 v-for="(i, index) in list2" :key="index">{{ i }}</h5>
      </div>
      <a-divider></a-divider>
      <div class="section">
        <h4>标签库</h4>
        <h5>首页轮播图或导航栏处点击‘在线对话标注’即可进入操作页面，包含标 注数据列表和添加标注页面。</h5>
        <h5 v-for="(i, index) in list3" :key="index">{{ i }}</h5>
      </div>
      <a-divider></a-divider>
      <div class="section">
        <h4>标注关系</h4>
        <h5>首页轮播图或导航栏处点击‘在线对话标注’即可进入操作页面，包含标 注数据列表和添加标注页面。</h5>
        <h5 v-for="(i, index) in list4" :key="index">{{ i }}</h5>
      </div>
    </div>
  </div>
</template>
<script>
import HeaderNav from "@/components/HeaderNav.vue";

export default {
  components: {
    HeaderNav,
  },
  setup() {
    let list = ["功能介绍：", "个人首页：", "1)	查看代码文件列表：", "在线编辑器页面：", "1)	新建标注关系："];
    let list2 = ["功能介绍：", "代码管理页面：", "1)	新增代码文件：", "代码文件详情页面：", "1)	删除代码文件"];
    let list3 = ["功能介绍：", "标签管理页面：", "1)	新增标签：", "标签详情页面：", "1)	删除标签"];
    let list4 = ["功能介绍：", "标注关系管理页面：", "1)	新增标注关系：", "标注关系详情页面：", "1)	删除标注关系"];

    return {
      list,
      list2,
      list3,
      list4,
    };
  },
};
</script>

<style scoped>
.container {
  width: 1000px;
  background-color: rgb(247, 243, 243);
  margin: 0 auto 20px auto;
  padding: 20px 100px;
}
.header-title {
}
.main {
}
.section {
}
</style>
