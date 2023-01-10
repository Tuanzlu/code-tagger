<template>
  <header-nav></header-nav>
  <div class="container">
    <a-form
      :model="formState"
      v-bind="layout"
      name="nest-messages"
      :validate-messages="validateMessages"
      @finish="onFinish"
      class="remove-form"
    >
      <h1 style="text-align: center">注销</h1>

      <a-form-item :name="['user', 'name']" label="用户名" :rules="[{ required: true }]">
        <a-input v-model:value="formState.user.name" />
      </a-form-item>

      <a-form-item :name="['user', 'telphone']" label="手机号" :rules="[{ required: true }]">
        <a-input v-model:value="formState.user.telphone" />
      </a-form-item>

      <a-form-item :name="['user', 'password']" label="密码" :rules="[{ required: true }]">
        <a-input-password v-model:value="formState.user.password" />
      </a-form-item>

      <a-form-item :wrapper-col="{ offset: 8, span: 16 }">
        <a-button type="primary" danger html-type="submit" @click="handleRemove()">注销</a-button>
      </a-form-item>
    </a-form>
  </div>
</template>

<script>
import { defineComponent, reactive } from "vue";
import path from "@/api/path.js";
import { postData } from "@/api/webpost";
import { message } from "ant-design-vue";
import { useRouter } from "vue-router";
import HeaderNav from "@/components/HeaderNav.vue";

export default defineComponent({
  components: {
    HeaderNav,
  },
  setup() {
    const router = useRouter();

    const layout = {
      labelCol: {
        span: 8,
      },
      wrapperCol: {
        span: 16,
      },
    };
    const validateMessages = {
      required: "${label} is required!",
      types: {
        email: "${label} is not a valid email!",
        number: "${label} is not a valid number!",
      },
      number: {
        range: "${label} must be between ${min} and ${max}",
      },
    };
    const formState = reactive({
      user: {
        name: "",
        telphone: "",
        password: "",
      },
    });
    const onFinish = (values) => {
      console.log("Success:", values);
    };
    function handleRemove() {
      let params = new URLSearchParams();
      params.append("username", formState.user.name);
      params.append("telphone", formState.user.telphone);
      params.append("password", formState.user.password);
      let url = path.website.removeUser;
      postData(url, params).then((res) => {
        console.log(res);
        if (res.state === "success") {
          message.success(res.description);
          router.push({
            name: "register",
          });
        } else {
          message.error(res.description);
        }
      });
    }
    return {
      formState,
      onFinish,
      layout,
      validateMessages,
      handleRemove,
    };
  },
});
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 650px;

  background-size: cover;
  background: #eeeded;
}
.remove-form {
  border-radius: 6px;
  background: #ffffff;
  width: 350px;
  padding: 25px 25px 5px 25px;
}
</style>
