<template>
  <div class="container">
    <h1><center>Log in </center></h1>
    <a-form
    :model="formState"
    name="basic"
    :label-col="{ span: 8 }"
    :wrapper-col="{ span: 8 }"
    autocomplete="off"
    @finish="onFinish"
    @finishFailed="onFinishFailed"
  >
    <a-form-item
      label="Telphone"
      name="telphone"
      :rules="[{ required: true, message: 'Please input your telphone!' }]"
    >
      <a-input v-model:value="formState.telphone" />
    </a-form-item>

    <a-form-item
      label="Password"
      name="password"
      :rules="[{ required: true, message: 'Please input your password!' }]"
    >
      <a-input-password v-model:value="formState.password" />
    </a-form-item>

    <a-form-item name="remember" :wrapper-col="{ offset: 8, span: 16 }">
      <a-checkbox v-model:checked="formState.remember">Remember me</a-checkbox>
    </a-form-item>

    <a-form-item name="login" :wrapper-col="{ offset: 8, span: 16 }">
      <a-button :disabled="disabled" type="primary" html-type="submit" class="login-form-button" @click="handleLogin()">
        Log in
      </a-button>
      Or
      <router-link to="../register">Register now!</router-link>
    </a-form-item>

    </a-form>
  </div>
</template>
<script>
import { defineComponent, reactive } from 'vue';
import path from "@/api/path.js";
import { postData } from "@/api/webpost";
import { getData } from "@/api/webget";
import { message } from "ant-design-vue";
export default defineComponent({
  setup() {
    const formState = reactive({
      telphone: '',
      password: '',
      remember: true,
    });
    const onFinish = values => {
      console.log('Success:', values);
    };
    const onFinishFailed = errorInfo => {
      console.log('Failed:', errorInfo);
    };
    function handleLogin(){
      let params = new URLSearchParams();
      params.append('telphone', formState.telphone);
      params.append('password', formState.password);
      let url = path.website.login;
      postData(url, params).then((res) => {
        console.log(res);
        if (res.state === "success") {
          message.success(res.description);
          router.push({
            name: "code",
          });
        } else {
          message.error(res.description);
        }
      });
    }
    return {
      formState,
      onFinish,
      onFinishFailed,
      handleLogin,
    };
  },
});
</script>

<style scoped>
.container {
  min-height: 600px;
}

</style>