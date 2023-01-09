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
          <a-menu-item key="login"><router-link to="../login">登陆</router-link></a-menu-item>
          <a-menu-item key="admin" @click="handleAdmin()">以管理员身份运行</a-menu-item>
          <a-menu-item key="register"><router-link to="../register">注册</router-link></a-menu-item>
          <a-menu-item key="modifypw"><router-link to="../modifypw">修改密码</router-link></a-menu-item>
          <a-menu-item key="exit" @click="handleExit()">退出</a-menu-item>
        
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

    function handleExit(){
      let params = new URLSearchParams();
      let url = path.website.exit;
      getData(url, params).then((res) => {
        console.log(res);
        if (res.state === "success") {
          message.success(res.description);
          router.push({
            name: "",
          });
        } else {
          message.error(res.description);
        }
      });
    }

    function handleAdmin(){
      // 待补充判断是否为admin
      let params = new URLSearchParams();
      let url = path.website.exit;
      getData(url, params).then((res) => {
        console.log(res);
        if (res.state === "success") {
          message.success(res.description);
          router.push({
            name: "alluser",
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
      handleExit,
      handleAdmin,
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
