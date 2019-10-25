<template>
  <div>
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
  margin-top: 100px;
  margin-bottom: 80px;
}

.jumbotron {
  padding-top: 0;
  padding-bottom: 0;
}
</style>