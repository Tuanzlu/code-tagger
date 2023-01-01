<template>
  <header-nav></header-nav>
  <div class="container">
    <div class="main">
      <div class="btn-bar">
        <a-button class="btn">
          <template #icon><folder-outlined /></template>
          保存
        </a-button>
        <a-button class="btn">
          <template #icon><delete-outlined /></template>
          删除
        </a-button>
        <button @click="changeTheme($event)">黑夜</button>
        <button @click="changeMode($event)">C++</button>
        <a-select v-model:value="mode" style="width: 100px">
          <a-select-option value="cpp">C++</a-select-option>
          <a-select-option value="asm">asm</a-select-option>
        </a-select>
      </div>
      <codemirror
        v-model="code"
        placeholder="Code gose here..."
        :style="style"
        :mode="mode"
        :spellcheck="spellcheck"
        :autofocus="autofocus"
        :indent-with-tab="indentWithTab"
        :tabSize="tabSize"
        :extensions="extensions"
        @ready="log('ready', $event)"
        @change="log('change', $event)"
        @focus="log('focus', $event)"
        @blur="useEditedCode"
      />
    </div>
  </div>
</template>

<script>
import HeaderNav from "@/components/HeaderNav.vue";
import { Codemirror } from "vue-codemirror";
import { javascript } from "@codemirror/lang-javascript";
import { cpp } from "@codemirror/lang-cpp";

import { oneDark } from "@codemirror/theme-one-dark";
import { reactive, defineComponent, ref, toRefs } from "vue";
import { FolderOutlined, DeleteOutlined } from "@ant-design/icons-vue";

export default defineComponent({
  components: {
    Codemirror,
    HeaderNav,
    FolderOutlined,
    DeleteOutlined,
  },
  setup() {
    let mode = ref("cpp");
    const code = ref(`console.log('Hello, world!')`);
    let selectValue = "cpp";
    let dateTime = "黑夜";
    const options = reactive({
      style: { height: "400px" },
      mode: "text/x-c++src",
      spellcheck: true,
      autofocus: true,
      indentWithTab: true,
      tabSize: 2,
      extensions: [cpp(), oneDark], //传递给CodeMirror EditorState。创建({扩展})
    });

    // 方法
    // 失去焦点时,使用已编辑的代码
    function useEditedCode() {
      console.log("@@@blur@@@code:", code.value);
      console.log("@@@blur@@@cpp:", cpp);
    }

    // 改变主题
    function changeTheme(e) {
      console.log("options.extensions:", options.extensions);
      if (e.target.innerHTML === "黑夜") {
        options.extensions = [];
        dateTime = e.target.innerHTML = "白天";
      } else {
        options.extensions = [oneDark];
        dateTime = e.target.innerHTML = "黑夜";
      }
    }
    // 改变模式
    function changeMode(e) {
      console.log("selectValue:", selectValue);
      if (selectValue === "cpp") {
        if (dateTime === "黑夜") options.extensions = [javascript(), oneDark];
        else options.extensions = [javascript()];
        selectValue = "javascript";
        e.target.innerHTML = "javascript";
        options.mode = "text/x-javascript";
      } else {
        if (dateTime === "黑夜") options.extensions = [cpp(), oneDark];
        else options.extensions = [cpp()];
        selectValue = "cpp";
        e.target.innerHTML = "C++";
        options.mode = "text/x-c++src";
      }
    }
    return {
      code,
      mode,
      selectValue,
      dateTime,
      ...toRefs(options),
      log: console.log,
      useEditedCode,
      changeTheme,
      changeMode,
    };
  },
});
</script>

<style scoped>
.container {
  min-height: 600px;
}
.main {
  width: 80%;
  min-width: 600px;
  margin: auto;
  padding-bottom: 80px;
  /* border: 1px solid red; */
  min-height: 500px;
}
.btn {
  margin: 10px 10px 10px 0;
}
</style>
