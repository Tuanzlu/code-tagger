<template>
  <header-admin-nav></header-admin-nav>
  <div class="allUser">
    <a-table bordered :columns="columns" :data-source="dataSource" :loading="loading" :pagination="pagination">
      <template #title>用户管理</template>
      <template #bodyCell="{ column, record }">
        <template v-if="column.dataIndex === 'del'">
          <a-button danger @click="showModal(record)">删除用户</a-button>
          <a-modal v-model:visible="visible" @ok="handleDel">
            <div style="margin: 20px">
              <p>
                <label>确定删除用户'{{ deletingRecord }}'？</label>
              </p>
              <p><label>输入管理员密码：</label><a-input-password style="width: 200px" v-model:value="admin_pw" /></p>
            </div>
            <template #footer>
              <a-button key="back" @click="handleCancel">取消</a-button>
              <a-button key="submit" type="primary" @click="handleDel">确认</a-button>
            </template>
          </a-modal>
        </template>
      </template>
    </a-table>
  </div>
</template>
<script>
import { defineComponent, reactive, ref } from "vue";
import HeaderAdminNav from "@/components/HeaderAdminNav.vue";
import { postData } from "@/api/webpost";
import { getData } from "@/api/webget";
import path from "@/api/path.js";
import { message } from "ant-design-vue";

export default defineComponent({
  components: {
    HeaderAdminNav,
  },
  setup() {
    const dataSource = ref([]);
    getDataList();
    let admin_pw = ref("");
    const visible = ref(false);
    let deletingRecord = ref("");
    const showModal = (record) => {
      deletingRecord.value = record.username;
      // console.log(deletingRecord.value);
      visible.value = true;
    };
    const loading = reactive(false);
    const columns = reactive([
      {
        title: "用户名",
        dataIndex: "username",
        align: "center",
        key: "username",
      },
      {
        title: "手机号",
        dataIndex: "telphone",
        align: "center",
        key: "telphone",
      },
      {
        title: "代码文件",
        dataIndex: "numFile",
        align: "center",
        key: "numFile",
      },
      {
        title: "标签",
        dataIndex: "numTag",
        align: "center",
        key: "numTag",
      },
      {
        title: "标注关系",
        dataIndex: "numRelation",
        align: "center",
        key: "numRelation",
      },
      {
        title: "操作",
        align: "center",
        dataIndex: "del",
      },
    ]);

    const pagination = reactive({
      position: ["bottomLeft"],
      pageSize: 10, //每页条数，所有页设置统一的条数
      pageSizeOptions: ["10", "20", "30"], //每页显示的条数，每页设置不同的条数
      total: dataSource.value.length, //数据总数
    });

    const handleCancel = () => {
      visible.value = false;
    };

    function handleDel() {
      let params = new URLSearchParams();
      params.append("userId", deletingRecord.value);
      params.append("adminpassword", admin_pw.value);
      console.log(admin_pw);
      let url = path.website.admin_removeUser;
      postData(url, params).then((res) => {
        console.log(res);
        if (res.state === "success") {
          visible.value = false;
          getDataList();
          deletingRecord.value = "";
          message.success(res.description);
        } else {
          message.error(res.description);
        }
      });
    }

    function getDataList() {
      //进入页面时加载用户数据
      //将用户数据赋值给dataSource即可
      let params = new URLSearchParams();
      let url = path.website.getUserList;
      getData(url, params).then((res) => {
        console.log(res);
        dataSource.value = res;
        console.log(dataSource.value);
      });
    }

    return {
      visible,
      showModal,
      dataSource,
      getDataList,
      loading,
      columns,
      handleCancel,
      handleDel,
      admin_pw,
      pagination,
      deletingRecord,
    };
  },
});
</script>
<style scoped>
.allUser {
  min-height: 650px;
  /* background-size: cover; */
  /* background: #eeeded; */
  padding-top: 50px;
  width: 80%;
  margin: auto;
}
</style>
