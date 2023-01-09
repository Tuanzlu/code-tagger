<template>
  <header-nav></header-nav>
  <div class="container">
    <a-form
      :model="formState"
      v-bind="layout"
      name="nest-messages"
      :validate-messages="validateMessages"
      @finish="onFinish"
      class="login-form"
    >
      <h1 style="text-align: center">修改密码</h1>

      <a-form-item :name="['user', 'telphone']" label="手机号" :rules="[{ required: true }]">
        <a-input v-model:value="formState.user.telphone" />
      </a-form-item>

      <a-form-item :name="['user', 'old_password']" label="旧密码" :rules="[{ required: true }]">
        <a-input-password v-model:value="formState.user.old_password" />
      </a-form-item>

      <a-form-item :name="['user', 'new_password']" label="新密码" :rules="[{ required: true }]">
        <a-input-password v-model:value="formState.user.new_password" />
      </a-form-item>

      <a-form-item :name="['user', 'new_password_again']" label="再次输入密码" :rules="[{ required: true }]">
        <a-input-password v-model:value="formState.user.new_password_again" />
      </a-form-item>

      <a-form-item :wrapper-col="{ offset: 8, span: 16 }">
        <a-button type="primary" html-type="submit" @click="handleModifyPW()">修改密码</a-button>
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
        telphone: "",
        old_password: "",
        new_password: "",
        new_password_again: "",
      },
    });
    const onFinish = (values) => {
      console.log("Success:", values);
    };
    function handleModifyPW() {
      let params = new URLSearchParams();
      params.append("telphone", formState.user.telphone);
      params.append("old_password", formState.user.old_password);
      params.append("new_password", formState.user.new_password);
      params.append("new_password_again", formState.user.new_password_again);
      let url = path.website.register;
      postData(url, params).then((res) => {
        console.log(res);
        if (res.state === "success") {
          message.success(res.description);
          router.push({
            name: "login",
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
      handleModifyPW,
    };
  },
});
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  background-size: cover;
  background: #eeeded;
}
.login-form {
  border-radius: 6px;
  background: #ffffff;
  width: 450px;
  padding: 25px 25px 5px 25px;
}
</style>
