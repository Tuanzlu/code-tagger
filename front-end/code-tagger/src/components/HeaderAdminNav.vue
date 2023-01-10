<template>
  <div class="menu">
    <div style="cursor: pointer">
      <img class="logo" :src="logoUrl" />
    </div>
    <a-menu style="justify-content: flex-end" mode="horizontal" @click="changePage">
      <a-sub-menu key="person">
        <template #icon><UserOutlined /></template>
        <a-menu-item> 用户名：{{ userId }} </a-menu-item>
        <a-menu-item key="modifypw"><router-link to="../modifypw">修改密码</router-link></a-menu-item>
        <a-menu-item key="intro"><router-link to="../intro">功能介绍</router-link></a-menu-item>
        <a-menu-item key="exit" @click="handleExit()">退出</a-menu-item>
      </a-sub-menu>
    </a-menu>
  </div>
</template>
<script>
import { defineComponent } from "vue";
import { UserOutlined } from "@ant-design/icons-vue";
import path from "@/api/path.js";
import { ref } from "vue";
import { getData } from "@/api/webget";
import { message } from "ant-design-vue";
import { useRouter } from "vue-router";
export default defineComponent({
  components: {
    UserOutlined,
  },
  setup() {
    const router = useRouter();
    const userId = window.localStorage.getItem("userId");
    console.log("userId:", userId);

    let logoUrl = require("@/assets/logo.png");
    function changePage(item) {
      router.push({
        name: item.key,
      });
    }
    function handleExit() {
      let params = new URLSearchParams();
      let url = path.website.exit;
      getData(url, params).then((res) => {
        console.log(res);
        if (res.state === "success") {
          message.success(res.description);
          window.localStorage.removeItem("userId");

          router.push({
            name: "login",
          });
        } else {
          message.error(res.description);
        }
      });
    }

    return {
      userId,
      logoUrl,
      changePage,
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
