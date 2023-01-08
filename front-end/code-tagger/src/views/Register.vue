<template>
  <h1><center>Register</center></h1>
  <a-form
    :model="formState"
    v-bind="layout"
    name="nest-messages"
    :validate-messages="validateMessages"
    @finish="onFinish"
  >
    <a-form-item 
      :name="['user', 'name']" 
      label="Name" 
      :rules="[{ required: true }]">
      <a-input v-model:value="formState.user.name" />
    </a-form-item>

    <a-form-item 
      :name="['user', 'telphone']" 
      label="Telphone" 
      :rules="[{ required: true }]">
      <a-input v-model:value="formState.user.telphone" />
    </a-form-item>

    <a-form-item 
      :name="['user', 'password']" 
      label="Password" 
      :rules="[{ required: true }]">
      <a-input-password v-model:value="formState.user.password" />
    </a-form-item>
    
    <a-form-item 
      :name="['user', 'password_again']" 
      label="Password_again" 
      :rules="[{ required: true }]">
      <a-input-password v-model:value="formState.user.password_again" />
    </a-form-item>

    <a-form-item :wrapper-col="{ offset: 8, span: 16 }">
      <a-button type="primary" html-type="submit">Register!</a-button>
    </a-form-item>
  </a-form>
</template>
<script>
import { defineComponent, reactive } from 'vue';
export default defineComponent({
  setup() {
    const layout = {
      labelCol: {
        span: 8,
      },
      wrapperCol: {
        span: 8,
      },
    };
    const validateMessages = {
      required: '${label} is required!',
      types: {
        email: '${label} is not a valid email!',
        number: '${label} is not a valid number!',
      },
      number: {
        range: '${label} must be between ${min} and ${max}',
      },
    };
    const formState = reactive({
      user: {
        name: '',
        telphone: '',
        password: '',
        password_again: '',
      },
    });
    const onFinish = values => {
      console.log('Success:', values);
    };
    return {
      formState,
      onFinish,
      layout,
      validateMessages,
    };
  },
});
</script>