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
          <template #icon><plus-outlined /></template>
          添加标注
        </a-button>
        <a-modal v-model:visible="visible" @ok="addMark">
          <div style="margin: 20px">
            <p v-if="adding === false">
              <label>标签：</label>
              <a-select v-model:value="label" :options="labelOptions" @change="handleLabelChange" style="width: 120px">
              </a-select>
              <a-button style="margin: 10px" type="small" @click="changeAdding"><plus-outlined />添加标签</a-button>
            </p>
            <p v-if="adding === true">
              <label>新增标签：</label>
              <a-input style="width: 120px" v-model:value="addingLabel" />
              <a-button style="margin: 10px" type="small" @click="changeAdding"><left-square-outlined />返回</a-button>
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
            v-model="code"
            placeholder="Code gose here..."
            :style="style"
            :mode="mode"
            :spellcheck="spellcheck"
            :autofocus="autofocus"
            :indent-with-tab="indentWithTab"
            :tabSize="tabSize"
            :extensions="extensions"
            @mouseup="handleMouseEvent"
          />
        </div>

        <mark-list ref="markRF" :docid="codeId" :id="userId"></mark-list>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderNav from "@/components/HeaderNav.vue";
import { Codemirror } from "vue-codemirror";
import { javascript } from "@codemirror/lang-javascript";
import { cpp } from "@codemirror/lang-cpp";
import { python } from "@codemirror/lang-python";
import { java } from "@codemirror/lang-java";
import { php } from "@codemirror/lang-php";
import { postData } from "@/api/webpost";
import { getData } from "@/api/webget";
import path from "@/api/path.js";
import { useRouter, useRoute } from "vue-router";
import MarkList from "@/components/MarkList.vue";
import { message } from "ant-design-vue";
import { reactive, defineComponent, ref, toRefs } from "vue";
import { FolderOutlined, LeftSquareOutlined, PlusOutlined, DeleteOutlined } from "@ant-design/icons-vue";

export default defineComponent({
  components: {
    Codemirror,
    MarkList,
    HeaderNav,
    FolderOutlined,
    DeleteOutlined,
    PlusOutlined,
    LeftSquareOutlined,
  },
  setup() {
    let adding = ref(false);
    let addingLabel = ref("");
    let markRF = ref();
    const router = useRouter();
    const route = useRoute();
    const visible = ref(false);
    const showModal = () => {
      visible.value = true;
      getLabelList();
    };
    let lang = ref("C/C++");
    let label = ref("");
    let selectCode = ref("");
    const code = ref("");
    const options = reactive({
      style: { minHeight: "400px" },
      mode: "text/x-c++src",
      spellcheck: true,
      autofocus: true,
      indentWithTab: true,
      tabSize: 2,
      extensions: [cpp()], //传递给CodeMirror EditorState。创建({扩展})
    });

    const selectOptions = ref([
      {
        value: "C/C++",
        label: "C/C++",
      },
      {
        value: "Javascript",
        label: "Javascript",
      },
      {
        value: "Python",
        label: "Python",
      },
      {
        value: "Java",
        label: "Java",
      },
      {
        value: "PHP",
        label: "PHP",
      },
    ]);

    const labelOptions = ref([]);

    let userId = window.localStorage.getItem("userId");
    let codeId = route.query.codeId;

    getCode();

    function getCode() {
      let params = {
        userId: userId,
        codeId: codeId,
      };
      let url = path.website.getCode;
      getData(url, params).then((res) => {
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
        if (res.state === "success") {
          message.success("success");
          router.push({
            name: "code",
          });
        }
      });
    }

    function handleMouseEvent(e) {
      selectCode.value = window.getSelection().toString();
    }

    const handleSelectChange = (value) => {
      changeMode(value);
    };

    function changeMode(mode) {
      if (mode === "C/C++") {
        options.extensions = [cpp()];
        lang.value = "C/C++";
        options.mode = "text/x-c++src";
      } else if (mode === "Javascript") {
        options.extensions = [javascript()];
        lang.value = "Javascript";
        options.mode = "text/javascript";
      } else if (mode === "Python") {
        options.extensions = [python()];
        lang.value = "Python";
        options.mode = "text/x-python";
      } else if (mode === "PHP") {
        options.extensions = [php()];
        lang.value = "PHP";
        options.mode = "text/x-php";
      } else if (mode === "Java") {
        options.extensions = [java()];
        lang.value = "Java";
        options.mode = "text/x-java";
      }
    }

    function addMark() {
      let params = new URLSearchParams();
      params.append("userId", userId);
      params.append("codeId", codeId);
      params.append("code", selectCode.value);
      if (adding.value === true) {
        params.append("new", true);
        params.append("labelId", addingLabel.value);
      } else {
        params.append("labelId", label.value);
      }
      let url = path.website.addMark;
      postData(url, params).then((res) => {
        if (res.state === "success") {
          visible.value = false;
          message.success(res.description);
          markRF.value.getCodeMark();
          addingLabel.value = "";
          adding.value = false;
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
        labelOptions.value = [];
        for (let i of res.rst) {
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

    function handleLabelChange(value) {
      label.value = value;
    }
    const handleCancel = () => {
      visible.value = false;
    };

    function changeAdding() {
      adding.value = !adding.value;
    }

    return {
      addingLabel,
      adding,
      changeAdding,
      markRF,
      code,
      lang,
      ...toRefs(options),
      modifyCode,
      deleteCode,
      userId,
      codeId,
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
