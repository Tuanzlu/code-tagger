<template>
  <header-nav current="code"></header-nav>

  <div class="container">
    <div class="main">
      <div class="up_bar">
        <a-button @click="showModal">新增代码文件</a-button>
        <a-modal v-model:visible="visible" @ok="addCode">
          <div style="margin: 20px">
            <p><label>代码名称：</label><a-input style="width: 200px" v-model:value="codeName" /></p>
            <p>
              <label>代码语言：</label>
              <a-select v-model:value="lang" :options="selectOptions" style="width: 120px"> </a-select>
            </p>
          </div>
          <template #footer>
            <a-button key="back" @click="handleCancel">取消</a-button>
            <a-button key="submit" type="primary" @click="addCode">确认</a-button>
          </template>
        </a-modal>
      </div>
      <div class="table-area">
        <div class="code-table">
          <a-table
            class="table"
            bordered
            :row-key="(record) => record.code_name"
            :data-source="CodeDataSource"
            :columns="CodeColumns"
            :pagination="CodePagination"
          >
            <template #title>代码库</template>
            <template #bodyCell="{ column, record, text }">
              <template v-if="['code_name'].includes(column.dataIndex)">
                <div>
                  <a-input
                    v-if="editableData[record.code_name]"
                    v-model:value="editableData[record.code_name][column.dataIndex]"
                    style="margin: -5px 0"
                  />
                  <template v-else>
                    {{ text }}
                  </template>
                </div>
              </template>
              <template v-if="column.key === 'action'">
                <div class="editable-row-operations">
                  <span v-if="editableData[record.code_name]">
                    <a-typography-link style="margin: 0 5px" @click="save(record.code_name)">保存</a-typography-link>

                    <a @click="cancel(record.code_name)">取消</a>
                  </span>
                  <span v-else>
                    <a @click="edit(record.code_name)">编辑</a>
                    <a-popconfirm
                      title="是否确定删除？"
                      ok-text="Yes"
                      cancel-text="No"
                      @confirm="deleteOneCode(record)"
                    >
                      <a style="margin: 0 0 0 5px">删除</a>
                    </a-popconfirm>
                    <a style="margin: 0 5px" @click="lookAtCode(record)">查看</a>
                  </span>
                </div>
              </template>
            </template>
          </a-table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderNav from "@/components/HeaderNav.vue";
import { reactive, ref } from "vue";
import { postData } from "@/api/webpost";
import { getData } from "@/api/webget";
import path from "@/api/path.js";
import { message } from "ant-design-vue";
import { cloneDeep } from "lodash-es";
import { useRouter } from "vue-router";

export default {
  components: { HeaderNav },
  setup() {
    const router = useRouter();
    const CodePagination = reactive({
      total: 100,
      showTotal: (total) => `共 ${total} 条`,
      pageSize: 10,
      showQuickJumper: true,
    });
    let alldataList = [];
    const CodeColumns = [
      {
        title: "代码文件名",
        key: "codeId",
        dataIndex: "code_name",
        width: "30%",
        align: "center",
      },
      {
        title: "编程语言",
        key: "language",
        dataIndex: "language",
        width: "20%",
        align: "center",
      },
      {
        title: "修改时间",
        key: "create_time",
        dataIndex: "create_time",
        width: "30%",
        align: "center",
      },
      {
        title: "操作",
        dataIndex: "action",
        key: "action",
        width: "20%",
        align: "center",
      },
    ];
    const CodeDataSource = ref([]);
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
    let lang = ref("C/C++");
    const userId = window.localStorage.getItem("userId");
    // let userId = "lqy";
    let codeName = ref("");
    let modifyingName = ref("");
    getCodeList();
    const visible = ref(false);
    const showModal = () => {
      visible.value = true;
    };

    const editableData = reactive({});
    const edit = (key) => {
      if (Object.keys(editableData).length === 0) {
        editableData[key] = cloneDeep(CodeDataSource.value.filter((item) => key === item.code_name)[0]);
        modifyingName.value = key;
      }
    };
    const save = (key) => {
      Object.assign(CodeDataSource.value.filter((item) => key === item.code_name)[0], editableData[key]);
      let item = JSON.parse(JSON.stringify(editableData[key]));
      modifyCodeId(item.code_name);
      delete editableData[key];
    };

    const cancel = (key) => {
      delete editableData[key];
    };

    function getCodeList() {
      let params = {
        userId: userId,
      };
      let url = path.website.getCodeList;
      getData(url, params).then((res) => {
        CodeDataSource.value = res.rst;
        CodePagination.total = CodeDataSource.value.length;
      });
    }

    const handleCancel = () => {
      visible.value = false;
    };

    function addCode() {
      let params = new URLSearchParams();
      params.append("userId", userId);
      params.append("codeId", codeName.value);
      params.append("language", lang.value);
      let url = path.website.addCode;
      postData(url, params).then((res) => {
        if (res.state === "success") {
          visible.value = false;
          getCodeList();
          codeName.value = "";
          lang.value = "C/C++";
          message.success(res.description);
        } else {
          message.error(res.description);
        }
      });
    }

    function modifyCodeId(code_name) {
      if (code_name === modifyingName.value) {
        modifyingName.value = "";
      } else {
        let params = new URLSearchParams();
        params.append("userId", userId);
        params.append("codeId", modifyingName.value);
        params.append("codeId_new", code_name);
        let url = path.website.modifyCodeID;
        postData(url, params).then((res) => {
          getCodeList();
        });
      }
    }

    function lookAtCode(record) {
      router.push({
        name: "editor",
        query: {
          codeId: record.code_name,
        },
      });
    }

    // 删除一个代码文件
    function deleteOneCode(record) {
      let params = new URLSearchParams();
      params.append("userId", userId);
      params.append("codeId", record.code_name);
      let url = path.website.removeCode;
      postData(url, params).then((res) => {
        message.success("删除成功");
        getCodeList();
      });
    }

    return {
      CodePagination,
      CodeColumns,
      CodeDataSource,
      alldataList,
      addCode,
      deleteOneCode,
      lookAtCode,
      edit,
      cancel,
      save,
      lang,
      selectOptions,
      editableData,
      visible,
      showModal,
      codeName,
      handleCancel,
    };
  },
};
</script>

<style scoped>
.container {
  min-height: 600px;
}
.up_bar {
  /* border: 1px solid red; */
  height: 20px;
  margin: 20px 0;
}
.main {
  margin: auto;
  width: 80%;
  height: 500px;
}
</style>
