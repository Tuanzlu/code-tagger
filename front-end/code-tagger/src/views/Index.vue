<template>
  <header-nav current="index"></header-nav>
  <div class="carousel">
    <a-carousel autoplay>
      <div><h3 @click="handleClick(0)">代码库</h3></div>
      <div><h3 @click="handleClick(1)">标注库</h3></div>
    </a-carousel>
  </div>
  <div class="intro"><a @click="handleClick(2)">——平台使用说明</a></div>
</template>
<script>
import HeaderNav from "@/components/HeaderNav.vue";
import { defineComponent } from "vue";
import { useRouter } from "vue-router";

export default defineComponent({
  components: { HeaderNav },
  setup() {
    const router = useRouter();
    function handleClick(index) {
      if (index === 0) {
        router.push({
          name: "code",
        });
      } else if (index === 1) {
        router.push({
          name: "tag",
        });
      } else if (index === 2) {
        router.push({
          name: "intro",
        });
      }
    }
    return {
      handleClick,
    };
  },
});
</script>

<style scoped>
/* For demo */
.ant-carousel :deep(.slick-slide) {
  width: 80%;
  text-align: center;
  height: 360px;
  cursor: pointer;
  line-height: 360px;
  background: #364d79;
  overflow: hidden;
}

.ant-carousel :deep(.slick-slide h3) {
  color: #fff;
}
.carousel {
  width: 80%;
  margin: 50px auto 0 auto;
}
.intro {
  width: 80%;
  margin: 10px auto;
}
</style>
