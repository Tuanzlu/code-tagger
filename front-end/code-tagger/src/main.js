import { createApp } from "vue";
import Antd from "ant-design-vue";
import App from "./App";
import "ant-design-vue/dist/antd.css";
import router from "./router";
import VueCodeMirror from "vue-codemirror";

createApp(App).use(router).use(Antd).use(VueCodeMirror).mount("#app");
