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
        <a-select v-model:value="mode" style="width: 100px">
          <a-select-option value="cpp">C++</a-select-option>
          <a-select-option value="asm">asm</a-select-option>
        </a-select>
      </div>
      <codemirror
        v-model="code"
        ref="cm"
        placeholder="Code goes here..."
        :style="{ minHeight: '450px', border: 'solid #6c6c6c 1px' }"
        :options="cmOptions"
      />
    </div>
  </div>
</template>

<script>
import HeaderNav from "@/components/HeaderNav.vue";
import { codemirror } from "vue-codemirror";
import { ref } from "vue";
import { FolderOutlined, DeleteOutlined } from "@ant-design/icons-vue";

export default {
  components: {
    codemirror,
    HeaderNav,
    FolderOutlined,
    DeleteOutlined,
  },
  setup() {
    let cmOptions = {
      mode: "text/cpp",
      theme: "idea",
      line: true,
      lineNumbers: true,
      showCursorWhenSelecting: true,
      smartIndent: true,
      indentWithTab: true,
      tabSize: 2,
      autofocus: true,
      matchBrackets: true,
    };

    let code = ref("");
    let mode = ref("cpp");
    return {
      cmOptions,
      code,
      mode,
    };
  },
};
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
