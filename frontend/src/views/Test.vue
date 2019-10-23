<template>
  <div class="container">
      <Map />
  </div>
</template>

<script>
import Map from "@/components/Map.vue";
export default {
  name: "test",
  components: { Map }
};
</script>

<style scoped>
.container {
  padding-top: 2rem;
  min-height: 500px;
}

.jumbotron {
  padding-top: 0;
  padding-bottom: 0;
}
</style>