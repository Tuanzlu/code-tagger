import { createApp } from "vue";
import Antd from "ant-design-vue";
import App from "./App";
import "ant-design-vue/dist/antd.css";
import router from "./router";
import { Codemirror } from "vue-codemirror";
createApp(App).use(router).use(Antd).use(Codemirror).mount("#app");
