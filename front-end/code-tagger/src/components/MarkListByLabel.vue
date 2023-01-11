<template>
  <div>
    <h3>'{{ labelId }}'的标注关系</h3>
    <a-list bordered style="white-space: pre-wrap" :dataSource="MarkList">
      <template #renderItem="{ item }">
        <a-list-item>
          <a-list-item-meta :description="item.code">
            <template #title>
              所属文件：<a @click="handleClick(item)">{{ item.codeID }}</a>
            </template>
          </a-list-item-meta>
        </a-list-item>
      </template>
    </a-list>
  </div>
</template>

<script>
import { ref } from "vue";
import { getData } from "@/api/webget";
import path from "@/api/path.js";
import { useRouter } from "vue-router";

export default {
  props: {
    id: String,
    label: String,
  },
  setup(props) {
    const router = useRouter();

    let userId = props.id;
    let labelId = props.label;
    let MarkList = ref([]);
    getLabelMark();
    function getLabelMark() {
      let params = {
        userId: userId,
        labelId: labelId,
      };
      let url = path.website.getLabelMark;
      getData(url, params).then((res) => {
        console.log(res);
        MarkList.value = res.rst;
      });
    }

    function handleClick(item) {
      router.push({
        name: "editor",
        query: {
          codeId: item.codeID,
        },
      });
    }

    return {
      MarkList,
      getLabelMark,
      labelId,
      handleClick,
    };
  },
};
</script>

<style></style>
