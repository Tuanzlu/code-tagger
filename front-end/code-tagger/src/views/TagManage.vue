<template>
  <header-nav current="tag"></header-nav>

  <div class="container">
    <div class="up_bar"></div>
    <div class="main">
      <div class="table-area">
        <div class="tag-table">
          <a-table
            class="table"
            bordered
            :row-selection="TagRowSelection"
            :row-key="(record) => record.id"
            :data-source="TagDataSource.dataSource"
            :columns="TagColumns"
            :scroll="scrollY"
          >
            <template #title>标签库</template>
          </a-table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderNav from "@/components/HeaderNav.vue";
import { reactive } from "vue";

export default {
  components: { HeaderNav },
  setup() {
    let scrollY = reactive({ y: document.body.offsetHeight - 265 });
    const TagPagination = reactive({
      total: 100,
      showTotal: (total) => `共 ${total} 条`,
      pageSize: 50,
      showQuickJumper: true,
    });
    let alldataList = [];
    const TagColumns = [
      {
        title: "标签名称",
        key: "tag_name",
        dataIndex: "tag_name",
        // width: "15%",
      },
      {
        title: "现有标注数",
        key: "relation_time",
        dataIndex: "relation_time",
        // width: "20%",
      },
    ];
    const TagDataSource = reactive({
      dataSource: [
        {
          id: "1",
          tag_name: "test",
          relation_time: "20",
        },
        {
          id: "2",
          tag_name: "test",
          relation_time: "20",
        },
      ],
    });

    const TagRowSelection = {
      onChange: (selectedRowKeys, selectedRows) => {
        selectedTest = selectedRowKeys;
      },
    };
    return {
      scrollY,
      TagPagination,
      TagColumns,
      TagDataSource,
      TagRowSelection,
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
