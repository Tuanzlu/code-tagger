<template>
  <div class="menu">
    <div>
      <img class="logo" @click="toIndex" :src="logoUrl" />
    </div>
    <a-menu style="justify-content: flex-end" :selectedKeys="curPage" mode="horizontal" @click="changePage">
      <a-menu-item key="index">首页</a-menu-item>
      <a-menu-item key="code">代码库</a-menu-item>
      <a-menu-item key="tag">标注库</a-menu-item>
      <a-sub-menu key="person">
          <template #icon><UserOutlined /></template>
          <a-menu-item key="login"><router-link to="../login">Log in</router-link></a-menu-item>
          <a-menu-item key="register"><router-link to="../register">Register</router-link></a-menu-item>
          <a-menu-item key="exit" @click="handleExit()">Exit</a-menu-item>
        
      </a-sub-menu>
    </a-menu>
  </div>
</template>
<script>
import { defineComponent } from "vue";
import { UserOutlined } from "@ant-design/icons-vue";
import path from "@/api/path.js";
import { postData } from "@/api/webpost";
import { getData } from "@/api/webget";
import { message } from "ant-design-vue";
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
    // userRoute route
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
        name: "index",
      });
    }

    function handleExit(){
      // 还不太成功
      let params = new URLSearchParams();
      let url = path.website.exit;
      getData(url, params).then((res) => {
        console.log(res);
        if (res.state === "success") {
          message.success(res.description);
          router.push({
            name: "/",
          });
        } else {
          message.error(res.description);
        }
      });
    }

    return {
      curPage,
      logoUrl,
      changePage,
      toIndex,
      handleExit,
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
