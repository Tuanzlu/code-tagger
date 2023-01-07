<template>
  <header-nav></header-nav>
  <div class="container">
    <div class="main" @mouseup="mytest">
      <div class="btn-bar">
        <a-button class="btn" @click="modifyCode">
          <template #icon><folder-outlined /></template>
          保存
        </a-button>
        <a-popconfirm title="是否确定删除？" ok-text="Yes" cancel-text="No" @confirm="deleteCode">
          <a-button class="btn">
            <template #icon><delete-outlined /></template>
            删除
          </a-button>
        </a-popconfirm>

        <!-- <a-button @click="changeTheme($event)">黑夜</a-button> -->
        <a-select v-model:value="lang" :options="selectOptions" @change="handleSelectChange" style="width: 120px">
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
        @cursorActivity="cursorActivity"
        @ready="handleReady"
        @change="handleChange"
        @focus="handleFocus"
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

import { message } from "ant-design-vue";
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
    let lang = ref("c");
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

    const selectOptions = ref([
      {
        value: "c",
        label: "C/C++",
      },
      {
        value: "js",
        label: "Javascript",
      },
    ]);

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
        //添加语言转换逻辑 根据文件语言改变
      });
    }

    function modifyCode() {
      let params = new URLSearchParams();
      params.append("userId", userId);
      params.append("codeId", codeId);
      params.append("language", lang.value);
      params.append("code_new", code.value);
      let url = path.website.modifyCode;
      postData(url, params).then((res) => {
        console.log(res);
      });
    }

    function deleteCode() {
      let params = new URLSearchParams();
      params.append("userId", userId);
      params.append("codeId", codeId);
      let url = path.website.removeCode;
      postData(url, params).then((res) => {
        console.log(res);
        if (res.state === "success") {
          message.success("success");
          router.push({
            name: "code",
          });
        }
      });
    }

    function mytest() {
      let selectedCode = window.getSelection().toString();
      console.log(selectedCode);
    }

    function cursorActivity(cm) {
      console.log(cm);

      let cur = cm.getCursor();
      console.log(cur);
      getPositionTag(cm, cur);
    }

    function getPositionTag(cm, cur) {
      let range = cm.getViewport();
      range.from = Math.min(range.from, cur.line);
      range.to = Math.max(cur.line + 1, range.to);
      // 获取开始-结束标签位置
      let match = Codemirror.findMatchingTag(cm, cur, range);
      if (match) {
        let { open, close } = match;
        // 获取开始 结束标签的文本
        console.log(cm.getRange(open.from, close ? close.to : open.to));
      }
    }

    // 方法
    // 失去焦点时,使用已编辑的代码
    function useEditedCode() {
      // console.log("@@@blur@@@code:", code.value);
      // console.log("@@@blur@@@cpp:", cpp);
    }

    const handleSelectChange = (value) => {
      console.log(`selected ${value}`);
      if (value === "c") {
        options.extensions = [cpp()];
        selectValue = "cpp";
        options.mode = "text/x-c++src";
      } else if (value === "js") {
        options.extensions = [javascript()];
        selectValue = "javascript";
        options.mode = "text/x-javascript";
      }
    };

    function handleChange(e) {
      console.log("change:", e);
    }

    function handleReady(e) {
      console.log("ready:", e);
    }

    function handleFocus(e) {
      console.log("focus:", e);
    }

    return {
      code,
      lang,
      selectValue,
      ...toRefs(options),
      log: console.log,
      useEditedCode,
      modifyCode,
      deleteCode,
      mytest,
      getPositionTag,
      cursorActivity,
      handleChange,
      handleFocus,
      handleReady,
      handleSelectChange,
      selectOptions,
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
