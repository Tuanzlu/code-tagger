<template>
  <header-nav current="person"></header-nav>
  <div class="container">
    <div class="left">
      <div class="code-table">
        <a-table
          class="table"
          bordered
          :data-source="CodeDataSource.dataSource"
          :columns="CodeColumns"
          :scroll="scrollY"
        >
          <template #title> <h3 style="cursor: pointer" @click="handleClick('code')">代码文件</h3></template>
        </a-table>
      </div>
    </div>
    <div class="right">
      <div class="tag-table">
        <a-table class="table" bordered :data-source="TagDataSource.dataSource" :columns="TagColumns" :scroll="scrollY">
          <template #title><h3 style="cursor: pointer" @click="handleClick('tag')">标签</h3></template>
        </a-table>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderNav from "@/components/HeaderNav.vue";
import { reactive } from "vue";
import { useRouter } from "vue-router";

export default {
  components: { HeaderNav },
  setup() {
    const router = useRouter();

    let scrollY = reactive({ y: document.body.offsetHeight - 325 });

    const CodeColumns = [
      {
        title: "文件名",
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
    let alldataList = [];
    const CodeDataSource = reactive({
      dataSource: [
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
        {
          file_name: "test",
          update_time: "2022/11/8",
        },
      ],
    });
    const TagDataSource = reactive({
      dataSource: [
        {
          tag_name: "test",
          relation_time: "20",
        },
        {
          tag_name: "test",
          relation_time: "20",
        },
        {
          tag_name: "test",
          relation_time: "20",
        },
        {
          tag_name: "test",
          relation_time: "20",
        },
        {
          tag_name: "test",
          relation_time: "20",
        },
        {
          tag_name: "test",
          relation_time: "20",
        },
        {
          tag_name: "test",
          relation_time: "20",
        },
        {
          tag_name: "test",
          relation_time: "20",
        },
        {
          tag_name: "test",
          relation_time: "20",
        },
        {
          tag_name: "test",
          relation_time: "20",
        },
        {
          tag_name: "test",
          relation_time: "20",
        },
        {
          tag_name: "test",
          relation_time: "20",
        },
        {
          tag_name: "test",
          relation_time: "20",
        },
        {
          tag_name: "test",
          relation_time: "20",
        },
        {
          tag_name: "test",
          relation_time: "20",
        },
        {
          tag_name: "test",
          relation_time: "20",
        },
      ],
    });

    function handleClick(item) {
      router.push({
        name: item,
      });
    }
    return {
      CodeColumns,
      CodeDataSource,
      scrollY,
      TagColumns,
      TagDataSource,
      alldataList,
      handleClick,
    };
  },
};
</script>

<style scoped>
.container {
  display: flex;
  align-items: center;
  justify-content: space-around;
  /* border: 1px solid red; */
  min-height: 600px;
}
.left {
  width: 650px;
  /* border: 1px solid blue; */
  height: 500px;
}
.right {
  width: 450px;
  /* border: 1px solid green; */
  height: 500px;
}
</style>
