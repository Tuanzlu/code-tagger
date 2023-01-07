<template>
  <header-nav></header-nav>
  <div class="container">
    <div class="main">
      <div class="btn-bar">
        <a-button class="btn" @click="modifyCode">
          <template #icon><folder-outlined /></template>
          保存
        </a-button>
        <a-button class="btn" @click="deleteCode">
          <template #icon><delete-outlined /></template>
          删除
        </a-button>
        <!-- <a-button @click="changeTheme($event)">黑夜</a-button> -->
        <a-button @click="changeMode($event)">C++</a-button>
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
import { postData } from "@/api/webpost";
import { getData } from "@/api/webget";
import path from "@/api/path.js";
import { useRouter, useRoute } from "vue-router";
// import { oneDark } from "@codemirror/theme-one-dark";
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
    const router = useRouter();
    const route = useRoute();
    let mode = ref("cpp");
    const code = ref("");
    let selectValue = "cpp";
    const options = reactive({
      style: { height: "400px" },
      mode: "text/x-c++src",
      spellcheck: true,
      autofocus: true,
      indentWithTab: true,
      tabSize: 2,
      extensions: [cpp()], //传递给CodeMirror EditorState。创建({扩展})
    });
    let userId = "lqy";
    let codeId = route.query.codeId;

    getCode();

    function getCode() {
      let params = {
        userId: userId,
        codeId: codeId,
      };
      let url = path.website.getCode;
      getData(url, params).then((res) => {
        console.log(res);
        code.value = res.rst[0].code;
      });
    }

    function modifyCode() {
      let params = new URLSearchParams();
      params.append("userId", userId);
      params.append("codeId", codeId);
      params.append("code_new", code.value);
      let url = path.website.modifyCode;
      postData(url, params).then((res) => {
        console.log(res);
      });
    }

    function deleteCode() {
      console.log("delete code");
    }

    // 方法
    // 失去焦点时,使用已编辑的代码
    function useEditedCode() {
      console.log("@@@blur@@@code:", code.value);
      console.log("@@@blur@@@cpp:", cpp);
    }

    // 改变模式
    function changeMode(e) {
      console.log("selectValue:", selectValue);
      if (selectValue === "cpp") {
        options.extensions = [javascript()];
        selectValue = "javascript";
        e.target.innerHTML = "javascript";
        options.mode = "text/x-javascript";
      } else {
        options.extensions = [cpp()];
        selectValue = "cpp";
        e.target.innerHTML = "C++";
        options.mode = "text/x-c++src";
      }
    }
    return {
      code,
      mode,
      selectValue,
      ...toRefs(options),
      log: console.log,
      useEditedCode,
      changeMode,
      modifyCode,
      deleteCode,
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
