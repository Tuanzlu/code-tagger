<template>
  <header-nav></header-nav>
  <div class="container">
    <div class="main">
      <mark-list-by-label :label="labelId" :id="userId"></mark-list-by-label>
    </div>
  </div>
</template>

<script>
import HeaderNav from "@/components/HeaderNav.vue";
import { useRoute } from "vue-router";
import MarkListByLabel from "@/components/MarkListByLabel.vue";
export default {
  components: { HeaderNav, MarkListByLabel },
  setup() {
    const route = useRoute();
    let userId = window.localStorage.getItem("userId");
    let labelId = route.query.labelId;
    return {
      labelId,
      userId,
    };
  },
};
</script>

<style scoped>
.container {
  min-height: 600px;
}
.main {
  margin: auto;
  width: 60%;
  height: 500px;
}
</style>
