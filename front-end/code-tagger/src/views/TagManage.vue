<template>
  <header-nav current="tag"></header-nav>

  <div class="container">
    <div class="main">
      <div class="up_bar">
        <a-button @click="showModal">新增标签</a-button>
        <a-modal v-model:visible="visible" @ok="addLabel">
          <div style="margin: 20px">
            <p><label>标签名称：</label><a-input style="width: 200px" v-model:value="labelName" /></p>
            <p>
              <label>标签简介：</label>
              <a-textarea style="width: 200px" v-model:value="labelIntro" />
            </p>
          </div>
          <template #footer>
            <a-button key="back" @click="handleCancel">取消</a-button>
            <a-button key="submit" type="primary" @click="addLabel">确认</a-button>
          </template>
        </a-modal>
      </div>
      <div class="table-area">
        <div class="label-table">
          <a-table
            class="table"
            bordered
            :row-key="(record) => record.id"
            :pagination="LabelPagination"
            :data-source="LabelDataSource"
            :columns="LabelColumns"
          >
            <template #title>标签库</template>
            <template #bodyCell="{ column, record, text }">
              <template v-if="['label_name', 'label_intro'].includes(column.dataIndex)">
                <div>
                  <a-input
                    v-if="editableData[record.label_name]"
                    v-model:value="editableData[record.label_name][column.dataIndex]"
                    style="margin: -5px 0"
                  />
                  <template v-else>
                    {{ text }}
                  </template>
                </div>
              </template>
              <template v-if="column.key === 'action'">
                <div class="editable-row-operations">
                  <span v-if="editableData[record.label_name]">
                    <a-typography-link style="margin: 0 5px" @click="save(record.label_name)">保存</a-typography-link>

                    <a @click="cancel(record.label_name)">取消</a>
                  </span>
                  <span v-else>
                    <a @click="edit(record)">编辑</a>
                    <a-popconfirm
                      title="是否确定删除？"
                      ok-text="Yes"
                      cancel-text="No"
                      @confirm="deleteOneLabel(record)"
                    >
                      <a style="margin: 0 0 0 5px">删除</a>
                    </a-popconfirm>
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
import { postData } from "@/api/webpost";
import { getData } from "@/api/webget";
import path from "@/api/path.js";

import { useRouter } from "vue-router";
import { reactive, ref } from "vue";
import { message } from "ant-design-vue";
import { cloneDeep } from "lodash-es";

export default {
  components: { HeaderNav },
  setup() {
    let labelName = ref("");
    let labelIntro = ref("");
    let userId = "lqy";
    let modifyingName = ref("");
    let modifyingIntro = ref("");
    const LabelPagination = reactive({
      total: 100,
      showTotal: (total) => `共 ${total} 条`,
      pageSize: 10,
      showQuickJumper: true,
    });
    let alldataList = [];
    const LabelColumns = [
      {
        title: "标签名称",
        key: "label_name",
        dataIndex: "label_name",
        width: "25%",
      },
      {
        title: "标签简介",
        key: "label_intro",
        dataIndex: "label_intro",
        width: "45%",
      },
      {
        title: "操作",
        dataIndex: "action",
        key: "action",
        width: "30%",
      },
      // {
      //   title: "现有标注数",
      //   key: "relation_time",
      //   dataIndex: "relation_time",
      //   // width: "20%",
      // },
    ];
    const LabelDataSource = ref([]);
    const visible = ref(false);
    const showModal = () => {
      visible.value = true;
    };
    const handleCancel = () => {
      visible.value = false;
    };
    getLabelList();
    function getLabelList() {
      let params = {
        userId: userId,
        detail: true,
      };

      let url = path.website.getLabelList;
      getData(url, params).then((res) => {
        console.log(res);
        LabelDataSource.value = res.rst;
        LabelPagination.total = LabelDataSource.value.length;
      });
    }

    const editableData = reactive({});
    const edit = (record) => {
      let key = record.label_name;
      console.log(key);
      if (Object.keys(editableData).length === 0) {
        editableData[key] = cloneDeep(LabelDataSource.value.filter((item) => key === item.label_name)[0]);
        modifyingName.value = key;
        modifyingIntro.value = record.label_intro;
      }
    };
    const save = (key) => {
      Object.assign(LabelDataSource.value.filter((item) => key === item.label_name)[0], editableData[key]);
      console.log(editableData[key]);
      let item = JSON.parse(JSON.stringify(editableData[key]));
      console.log(item);
      modifyLabelId(item.label_name);
      modifyLabelIntro(item.label_intro);
      delete editableData[key];
    };

    const cancel = (key) => {
      delete editableData[key];
    };

    function addLabel() {
      let params = new URLSearchParams();
      params.append("userId", userId);
      params.append("labelId", labelName.value);
      params.append("label", labelIntro.value);
      let url = path.website.addLabel;
      postData(url, params).then((res) => {
        console.log(res);
        if (res.state === "success") {
          visible.value = false;
          getLabelList();
          labelName.value = "";
          labelIntro.value = "";
          message.success(res.description);
        } else {
          message.error(res.description);
        }
      });
    }

    function modifyLabelId(label_name) {
      if (label_name !== modifyingName.value) {
        console.log(label_name);
        let params = new URLSearchParams();
        params.append("userId", userId);
        params.append("labelId", modifyingName.value);
        params.append("labelId_new", label_name);
        let url = path.website.modifyLabelID;
        postData(url, params).then((res) => {
          console.log(res);
          getLabelList();
        });
      }
    }

    function modifyLabelIntro(label_intro) {
      console.log(modifyingName.value);
      console.log(label_intro);
      if (label_intro === modifyingIntro.value) {
        modifyingIntro.value = "";
      } else {
        let params = new URLSearchParams();
        params.append("userId", userId);
        params.append("labelId", modifyingName.value);
        params.append("label_new", label_intro);
        let url = path.website.modifyLabelIntro;
        postData(url, params).then((res) => {
          console.log(res);
          getLabelList();
        });
      }
    }

    // 删除一个代码文件
    function deleteOneLabel(record) {
      let params = new URLSearchParams();
      params.append("userId", userId);
      params.append("labelId", record.label_name);
      let url = path.website.removeLabel;
      postData(url, params).then((res) => {
        console.log(res);
        if (res.state === "success") {
          message.success("删除成功");
          getLabelList();
        }
      });
    }

    return {
      LabelPagination,
      LabelColumns,
      LabelDataSource,
      alldataList,
      getLabelList,
      deleteOneLabel,
      edit,
      cancel,
      save,
      editableData,
      labelName,
      labelIntro,
      showModal,
      visible,
      handleCancel,
      addLabel,
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
}
.main {
  margin: auto;
  width: 80%;
  height: 500px;
}
.up_bar {
  /* border: 1px solid red; */
  height: 20px;
  margin: 20px 0;
}
.table-area {
  height: 400px;
  /* border: 1px solid red; */
}
</style>
