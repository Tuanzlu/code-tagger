<template>
  <header-nav></header-nav>
  <div class="container">
    <div class="main">
      <div class="header-title"><h3>平台使用说明</h3></div>
      <a-divider style="margin-top: -5px"></a-divider>
      <div>
        <div class="section">
          <h4>用户管理</h4>
          <h5>登录管理员身份跳转到用户管理页面，可以对平台已注册用户进行操作，如删除用户。</h5>
          <h5 v-for="(i, index) in list" :key="index">{{ i }}</h5>
        </div>
        <a-divider></a-divider>
        <div class="section">
          <h4>代码库</h4>
          <h5>页面上方导航栏处点击‘代码库’即可进入操作页面。</h5>
          <h5 v-for="(i, index) in list2" :key="index">{{ i }}</h5>
        </div>
        <a-divider></a-divider>
        <div class="section">
          <h4>标签库</h4>
          <h5>页面上方导航栏处点击‘标签库’即可进入操作页面。</h5>
          <h5 v-for="(i, index) in list3" :key="index">{{ i }}</h5>
        </div>
        <a-divider></a-divider>
        <div class="section">
          <h4>标注关系</h4>
          <h5>代码文件首页选中某个文件即可进入操作页面，包含标注数据列表和添加标注页面。</h5>
          <h5 v-for="(i, index) in list4" :key="index">{{ i }}</h5>
        </div>
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
    let list = ["功能介绍：", "用户管理页面：", "1)删除用户", "2)查看用户列表"];
    let list2 = [
      "功能介绍：",
      "代码管理页面：",
      "1)新增代码文件：",
      "代码编辑页面：",
      "1)删除代码文件",
      "2)保存编辑代码",
    ];
    let list3 = ["功能介绍：", "标签管理页面：", "1)新增标签：", "2)删除标签", "3)编辑标签"];
    let list4 = ["功能介绍：", "代码编辑页面：", "1)新增标注关系", "标注关系详情页面：", "1)删除标注关系"];

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
  background-size: cover;
  background: #eeeded;
}
.header-title {
}
.main {
  width: 1000px;
  padding: 20px 100px;

  margin: 0 auto 20px auto;
}
.section {
}
</style>
