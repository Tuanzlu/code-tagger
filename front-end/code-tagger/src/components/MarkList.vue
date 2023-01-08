<template>
  <a-list style="width: 400px" :dataSource="MarkList">
    <template #renderItem="{ item }">
      <a-list-item>
        <template #actions>
          <a-popconfirm title="是否确定删除？" ok-text="Yes" cancel-text="No" @confirm="deleteOneMark(item)">
            <a key="delete">删除</a>
          </a-popconfirm>
        </template>
        <a-list-item-meta :description="item.code">
          <template #title>
            <a>{{ item.labelID }}</a>
          </template>
        </a-list-item-meta>
      </a-list-item>
    </template>
  </a-list>
</template>

<script>
import { postData } from "@/api/webpost";
import { ref } from "vue";
import { message } from "ant-design-vue";
import { getData } from "@/api/webget";
import path from "@/api/path.js";
export default {
  props: {
    id: String,
    docid: String,
  },
  setup(props, context) {
    let userId = props.id;
    let codeId = props.docid;
    let MarkList = ref([]);
    getCodeMark();
    function getCodeMark() {
      let params = {
        userId: userId,
        codeId: codeId,
      };
      let url = path.website.getCodeMark;
      getData(url, params).then((res) => {
        console.log(res);
        MarkList.value = res.rst;
      });
    }

    function deleteOneMark(item) {
      let params = new URLSearchParams();
      params.append("userId", userId);
      params.append("codeId", item.codeID);
      params.append("code", item.code);
      params.append("labelId", item.labelID);
      let url = path.website.removeMark;
      postData(url, params).then((res) => {
        console.log(res);
        if (res.state === "success") {
          message.success("success");
          getCodeMark();
        }
      });
    }

    return {
      MarkList,
      getCodeMark,
      deleteOneMark,
    };
  },
};
</script>

<style></style>
