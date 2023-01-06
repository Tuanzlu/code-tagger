<template>
  <header-nav current="code"></header-nav>

  <div class="container">
    <div class="up_bar">
      <a-button @click="addCode">新增代码文件</a-button>
      <a-button @click="deleteCode">删除代码文件</a-button>
    </div>
    <div class="main">
      <div class="table-area">
        <div class="code-table">
          <a-table
            class="table"
            bordered
            :row-selection="CodeRowSelection"
            :row-key="(record) => record.id"
            :data-source="CodeDataSource.dataSource"
            :columns="CodeColumns"
            :scroll="scrollY"
          >
            <template #title>代码库</template>
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

export default {
  components: { HeaderNav },
  setup() {
    let scrollY = reactive({ y: document.body.offsetHeight - 265 });
    const CodePagination = reactive({
      total: 100,
      showTotal: (total) => `共 ${total} 条`,
      pageSize: 50,
      showQuickJumper: true,
    });
    let alldataList = [];
    const CodeColumns = [
      {
        title: "代码文件名",
        key: "file_name",
        dataIndex: "file_name",
        // width: "15%",
      },
      {
        title: "修改时间",
        key: "update_time",
        dataIndex: "update_time",
        // width: "20%",
      },
    ];
    const CodeDataSource = reactive({
      dataSource: [
        {
          id: "1",
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          id: "2",
          file_name: "test",
          update_time: "2022/11/8",
        },
      ],
    });

    // const userId = window.localStorage.getItem("userId");
    let userId = "1";
    getCodeList();

    function getCodeList() {
      let params = {
        userId: userId,
      };
      let url = path.website.getCodeList;
      getData(url, params).then((res) => {
        console.log(res);
      });
    }

    // 删除一个问题
    // function deleteOneCorpus(record) {
    //   let params = {
    //     docid: docid,
    //   };
    //   let url = path.website.deleteCorpus;
    //   postData(url, params).then((res) => {
    //     if (res.explain.indexOf("success") !== -1) {
    //       message.success(res.explain);
    //       getList();
    //     } else {
    //       message.error(res.explain);
    //     }
    //   });
    // }

    // 批量删除问题
    // function deleteCorpus() {
    //   let params = {
    //     docid_list: selectedTest,
    //   };
    //   let url = path.website.deleteManyCorpus;
    //   postData(url, params).then((res) => {
    //     if (res.explain.indexOf("success") !== -1) {
    //       message.success(res.explain);
    //       getList();
    //     } else {
    //       message.error(res.explain);
    //     }
    //   });
    // }

    let selectedTest = ref("");
    const CodeRowSelection = {
      onChange: (selectedRowKeys, selectedRows) => {
        selectedTest = selectedRowKeys;
        console.log(selectedRows);
        console.log(selectedTest.value);
      },
    };

    return {
      scrollY,
      CodePagination,
      CodeColumns,
      CodeDataSource,
      CodeRowSelection,
      alldataList,
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
  margin: 20px;
}
.main {
  margin: auto;
  width: 80%;
  height: 500px;
}

.table_area {
  height: 400px;
  /* border: 1px solid red; */
}
</style>
