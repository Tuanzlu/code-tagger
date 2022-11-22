<template>
  <div class="menu">
    <div>
      <img class="logo" @click="toIndex" :src="logoUrl" />
    </div>
    <a-menu style="justify-content: flex-end" :selectedKeys="curPage" mode="horizontal" @click="changePage">
      <a-menu-item key="index">首页</a-menu-item>
      <a-menu-item key="code">代码库</a-menu-item>
      <a-menu-item key="tag">标注库</a-menu-item>
      <a-menu-item key="person">
        <a-avatar size="small">
          <template #icon><UserOutlined /></template>
        </a-avatar>
      </a-menu-item>
    </a-menu>
  </div>
</template>
<script>
import { defineComponent } from "vue";
import { UserOutlined } from "@ant-design/icons-vue";
import { useRouter } from "vue-router";
export default defineComponent({
  props: {
    current: String,
  },
  components: {
    UserOutlined,
  },
  setup(props) {
    const router = useRouter();
    let logoUrl = require("@/assets/logo.png");
    let curPage = [props.current];
    function changePage(item) {
      router.push({
        name: item.key,
      });
    }

    function toIndex() {
      // 待补充登录逻辑判断
      router.push({
        path: "/person",
      });
    }
    return {
      curPage,
      logoUrl,
      changePage,
      toIndex,
    };
  },
});
</script>

<style scoped>
.menu {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 70px;
}
.logo {
  margin: 10px 10px 10px 20px;
  height: 45px;
}
</style>
