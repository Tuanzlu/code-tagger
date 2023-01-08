<template>
  <header-nav></header-nav>
  <div class="container">
    <div class="main">
      <div class="btn-bar">
        <a-button class="btn" @click="modifyCode">
          <template #icon><folder-outlined /></template>
          保存
        </a-button>
        <a-button class="btn" @click="showModal">
          <template #icon><folder-outlined /></template>
          添加标注
        </a-button>
        <a-modal v-model:visible="visible" @ok="addMark">
          <div style="margin: 20px">
            <p>
              <label>标签：</label>
              <a-select v-model:value="label" :options="labelOptions" @change="handleLabelChange" style="width: 120px">
              </a-select>
            </p>
          </div>
          <template #footer>
            <a-button key="back" @click="handleCancel">取消</a-button>
            <a-button key="submit" type="primary" @click="addMark">确认</a-button>
          </template>
        </a-modal>
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
      <div class="middle-view">
        <div style="width: 750px; margin-right: 20px">
          <codemirror
            ref="cm"
            v-model="code"
            placeholder="Code gose here..."
            :style="style"
            :mode="mode"
            :spellcheck="spellcheck"
            :autofocus="autofocus"
            :indent-with-tab="indentWithTab"
            :tabSize="tabSize"
            :extensions="extensions"
            @focus="handleFocus"
            @mouseup="handleMouseEvent"
          />
        </div>

        <mark-list ref="markRF" :id="userId"></mark-list>
      </div>
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
import MarkList from "@/components/MarkList.vue";
import { message } from "ant-design-vue";
// import { oneDark } from "@codemirror/theme-one-dark";
import { reactive, defineComponent, ref, toRefs, onMounted } from "vue";
import { FolderOutlined, DeleteOutlined } from "@ant-design/icons-vue";

export default defineComponent({
  components: {
    Codemirror,
    MarkList,
    HeaderNav,
    FolderOutlined,
    DeleteOutlined,
  },
  setup() {
    let markRF = ref();
    const router = useRouter();
    const route = useRoute();
    const visible = ref(false);
    const showModal = () => {
      visible.value = true;
      getLabelList();
    };
    let lang = ref("c");
    let label = ref("");
    let selectCode = ref("");
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
    const cm = ref();
    onMounted(() => {
      console.log(markRF.value);
      // cm.value.on("cursorActivity", (cm) => {
      //   let test = cm.getSelection();
      //   console.log(test);
      // });
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

    const labelOptions = ref([
      {
        value: "test_label_1",
        label: "test_label_1",
      },
      {
        value: "test_label_2",
        label: "test_label_2",
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
        lang.value = res.rst[0].language;
        changeMode(lang.value);
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
        if (res.state === "success") {
          message.success("success");
        } else {
          message.error("fail");
        }
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

    function handleMouseEvent(e) {
      console.log(e);
      selectCode.value = window.getSelection().toString();
      console.log(selectCode.value);
    }

    const handleSelectChange = (value) => {
      console.log(`selected ${value}`);
      changeMode(value);
    };

    function changeMode(mode) {
      if (mode === "c") {
        options.extensions = [cpp()];
        selectValue = "cpp";
        options.mode = "text/x-c++src";
      } else if (mode === "js") {
        options.extensions = [javascript()];
        selectValue = "javascript";
        options.mode = "text/x-javascript";
      }
    }

    function addMark() {
      let params = new URLSearchParams();
      params.append("userId", userId);
      params.append("codeId", codeId);
      params.append("labelId", label.value);
      params.append("code", selectCode.value);
      params.append("new", true);
      let url = path.website.addMark;
      postData(url, params).then((res) => {
        console.log(res);
        if (res.state === "success") {
          visible.value = false;
          message.success(res.description);
          markRF.value.getUserMark();
        } else {
          message.error(res.description);
        }
      });
    }

    function getLabelList() {
      let params = {
        userId: userId,
      };

      let url = path.website.getLabelList;
      getData(url, params).then((res) => {
        console.log(res);
        labelOptions.value = [];
        for (let i of res.rst) {
          console.log(i);
          labelOptions.value.push({
            value: i.label_name,
            label: i.label_name,
          });
        }
        if (labelOptions.value.length !== 0) {
          label.value = labelOptions.value[0].value;
        }
      });
    }

    // function handleChange(e) {
    //   console.log("change:", e);
    // }

    // function handleReady(e) {
    //   console.log("ready:", e);
    // }

    function handleFocus(e) {
      console.log("focus:", e);
      console.log(cm.value.cursor);
    }

    function handleLabelChange(value) {
      label.value = value;
      console.log(value);
    }
    const handleCancel = () => {
      visible.value = false;
    };
    return {
      markRF,
      code,
      lang,
      selectValue,
      ...toRefs(options),
      modifyCode,
      deleteCode,
      // mytest,
      // handlecursorActivity,
      handleFocus,
      // handleReady,
      cm,
      userId,
      getLabelList,
      handleSelectChange,
      handleLabelChange,
      handleMouseEvent,
      visible,
      showModal,
      addMark,
      handleCancel,
      labelOptions,
      label,
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
.middle-view {
  display: flex;
  justify-content: space-between;
}
</style>
