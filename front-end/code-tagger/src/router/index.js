import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    // 首页
    path: "/",
    name: "index",
    component: () => import("../views/Index.vue"),
  },
  {
    // 用户登录 未启用
    path: "/login",
    name: "login",
    component: () => import("../views/Login.vue"),
  },
  {
    // 平台使用说明
    path: "/intro",
    name: "intro",
    component: () => import("../views/Intro.vue"),
  },
  {
    // 平台使用说明
    path: "/editor",
    name: "editor",
    component: () => import("../views/Editor.vue"),
  },
  {
    // 平台使用说明
    path: "/person",
    name: "person",
    component: () => import("../views/PersonalIndex.vue"),
  },
  {
    // 平台使用说明
    path: "/register",
    name: "register",
    component: () => import("../views/Register.vue"),
  },
  {
    // 平台使用说明
    path: "/relation",
    name: "relation",
    component: () => import("../views/RelationManage.vue"),
  },
  {
    // 平台使用说明
    path: "/tag",
    name: "tag",
    component: () => import("../views/TagManage.vue"),
  },
  {
    // 平台使用说明
    path: "/code",
    name: "code",
    component: () => import("../views/CodeManage.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
