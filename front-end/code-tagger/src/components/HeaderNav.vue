<template>
  <div class="menu">
    <div style="cursor: pointer">
      <img class="logo" @click="toIndex" :src="logoUrl" />
    </div>
    <a-menu style="justify-content: flex-end" :selectedKeys="curPage" mode="horizontal" @click="changePage">
      <a-menu-item v-if="isVisitor === false" key="code">代码库</a-menu-item>
      <a-menu-item v-if="!isVisitor" key="tag">标注库</a-menu-item>
      <a-sub-menu key="person">
        <template #icon><UserOutlined /></template>
        <a-menu-item v-if="!isVisitor"> 
          用户名：{{ userId }} 
        </a-menu-item>

        <a-menu-item key="intro">
          <router-link to="../intro">功能介绍</router-link>
        </a-menu-item>

        <a-menu-item v-if="isVisitor" key="login">
          <router-link to="../login">登录</router-link>
        </a-menu-item>

        <a-menu-item v-if="isVisitor" key="register">
          <router-link to="../register">注册</router-link>
        </a-menu-item>

        <a-menu-item key="modifypw">
          <router-link to="../modifypw">修改密码</router-link>
        </a-menu-item>

        <a-menu-item v-if="!isVisitor" key="remove">
          <router-link to="../remove">注销</router-link>
        </a-menu-item>

        <a-menu-item v-if="!isVisitor" key="exit" @click="handleExit()">退出</a-menu-item>
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
  props: {
    current: String,
  },
  components: {
    UserOutlined,
  },
  setup(props) {
    const router = useRouter();
    const userId = window.localStorage.getItem("userId");
    console.log("userId:", userId);
    let isVisitor = ref(true);
    console.log("isVisitor:", isVisitor.value);
    if (userId === null) {
      isVisitor.value = true;
    } else {
      isVisitor.value = false;
    }

    let logoUrl = require("@/assets/logo.png");
    let curPage = [props.current];
    function changePage(item) {
      router.push({
        name: item.key,
      });
    }
    function toIndex() {
      if (isVisitor.value === false) {
        router.push({
          name: "code",
        });
      }
    }

    function handleExit() {
      let params = new URLSearchParams();
      let url = path.website.exit;
      getData(url, params).then((res) => {
        console.log(res);
        if (res.state === "success") {
          message.success(res.description);
          window.localStorage.removeItem("userId");
          isVisitor.value = false;
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
      curPage,
      logoUrl,
      isVisitor,
      toIndex,
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
