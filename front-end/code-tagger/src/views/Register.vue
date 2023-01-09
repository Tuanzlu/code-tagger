<template>
  <div class="container">
    <a-form
      :model="formState"
      v-bind="layout"
      name="nest-messages"
      :validate-messages="validateMessages"
      @finish="onFinish"
      class="login-form"
    >
      <h1 style="text-align: center">Register</h1>

      <a-form-item :name="['user', 'name']" label="Name" :rules="[{ required: true }]">
        <a-input v-model:value="formState.user.name" />
      </a-form-item>

      <a-form-item :name="['user', 'telphone']" label="Telphone" :rules="[{ required: true }]">
        <a-input v-model:value="formState.user.telphone" />
      </a-form-item>

      <a-form-item :name="['user', 'password']" label="Password" :rules="[{ required: true }]">
        <a-input-password v-model:value="formState.user.password" />
      </a-form-item>

      <a-form-item :name="['user', 'password_again']" label="Password_again" :rules="[{ required: true }]">
        <a-input-password v-model:value="formState.user.password_again" />
      </a-form-item>

      <a-form-item :wrapper-col="{ offset: 8, span: 16 }">
        <a-button type="primary" html-type="submit" @click="handleRegister()">Register!</a-button>
        <br />
        <router-link to="../login"> Already have an account?</router-link>
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

export default defineComponent({
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
        password_again: "",
      },
    });
    const onFinish = (values) => {
      console.log("Success:", values);
    };
    function handleRegister() {
      let params = new URLSearchParams();
      params.append("username", formState.user.name);
      params.append("telphone", formState.user.telphone);
      params.append("password", formState.user.password);
      params.append("password_again", formState.user.password_again);
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
      handleRegister,
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
