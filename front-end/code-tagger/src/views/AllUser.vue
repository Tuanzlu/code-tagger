<template>
  <header-nav></header-nav>
  <div class="allUser">
    <a-table
      :columns="columns"
      :data-source="dataSource"
      :loading="loading"
      :pagination="pagination"
      style="width:90%"
    >
    <template #bodyCell="{ column, record  }">
        <template v-if="column.dataIndex === 'del'">
          <a-button @click="handleDel(record )">删除用户</a-button>
        </template>
      </template>
      
    </a-table>
    </div>
  </template>
  <script>
  import { defineComponent, reactive, ref } from 'vue';
  import HeaderNav from "@/components/HeaderNav.vue";
  
  export default defineComponent({
    components: {
      HeaderNav,
    },
    setup() {
      const dataSource = reactive([
      {
    username: 'John Brown',
    telphone: '111',
    numFile: 1,
    numTag: 2,
    numRelation: 3,
  }, {
    username: 'Jim Green',
    telphone: '222',
    numFile: 1,
    numTag: 2,
    numRelation: 3,
  }, {
    username: 'Joe Black',
    telphone: '333',
    numFile: 1,
    numTag: 2,
    numRelation: 3,
  }
      ])
      const loading = reactive(false)
      const columns = reactive([{
        name: 'Username',
        title: '用户名',
        dataIndex: 'username',
        align:"center",
        key: 'username',
      },
      {
        name: 'Telphone',
        title: '手机号',
        dataIndex: 'telphone',
        align:"center",
        key: 'telphone',
      },
      {
        name: 'Code Files',
        title: '代码文件',
        dataIndex: 'numFile',
        align:"center",
        key: 'numFile',
      },
      {
        name: 'Tags',
        title: '标签',
        dataIndex: 'numTag',
        align:"center",
        key: 'numTag',
      },
      {
        name: 'Relations',
        title: '标注关系',
        dataIndex: 'numRelation',
        align:"center",
        key: 'numRelation',
      },
      {
        title: '操作',
        align:"center",
        dataIndex:'del',
      }
    ])
  
  const pagination=reactive({
    position:['bottomLeft'],
         pageSize: 10, //每页条数，所有页设置统一的条数
         pageSizeOptions: ['10', '20', '30'], //每页显示的条数，每页设置不同的条数
         total: dataSource.length, //数据总数
      }) 
  
  const handleDel = (value)=>{
    //执行删除接口，删除一条数据
       console.log(value)
  }
  
  const getDataList=()=>{
    //进入页面时加载用户数据
    //将用户数据赋值给dataSource即可
    console.log("加载用户数据")
  }
  
  //进入页面执行加载用户数据的函数
  getDataList()
  
  
      return {
        dataSource,
        loading,
        columns,
        handleDel,
        pagination,
      };
    },
  });
  </script>
  <style scoped>
  .allUser{
    display: flex;
    justify-content: center;
    height: 100%;
    background-size: cover;
    background: #eeeded;
    padding-top: 50px;
    padding-left: 10%;
  }
  </style>
  