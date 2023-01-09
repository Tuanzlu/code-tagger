import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    // 首页
    path: "/",
    name: "index",
    component: () => import("../views/Index.vue"),
  },
  {
    // 平台使用说明
    path: "/intro",
    name: "intro",
    component: () => import("../views/Intro.vue"),
  },
  {
    // 登录
    path: "/login",
    name: "login",
    component: () => import("../views/Login.vue"),
  },
  {
    // 注册
    path: "/register",
    name: "register",
    component: () => import("../views/Register.vue"),
  },
  {
    // 修改密码
    path: "/modifypw",
    name: "modifypw",
    component: () => import("../views/ModifyPW.vue"),
  },
  {
    // 在线代码编辑器
    path: "/editor",
    name: "editor",
    component: () => import("../views/Editor.vue"),
  },
  {
    // 代码库+标签库目录
    path: "/personalIndex",
    name: "personalIndex",
    component: () => import("../views/PersonalIndex.vue"),
  },
  {
    // 代码库
    path: "/code",
    name: "code",
    component: () => import("../views/CodeManage.vue"),
  },
  {
    // 标签库
    path: "/tag",
    name: "tag",
    component: () => import("../views/TagManage.vue"),
  },
  {
    // 所有用户列表
    path: "/alluser",
    name: "alluser",
    component: () => import("../views/AllUser.vue"),
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
