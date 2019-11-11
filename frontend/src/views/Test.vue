<template>
  <div>
    <!-- this page is used for testing Google Map API only -->
    <Map :houses="houses" />
  </div>
</template>

<script>
import Map from "@/components/Map.vue";
export default {
  name: "test",
  components: { Map },
  created() {
    // get houses from backend and try to render them in google map
    this.$axios
      .get("/api/houses/")
      .then(response => {
        this.houses = response.data;
        window.console.log(this.houses);
        // this.$forceUpdate();
      })
      .catch(err => {
        window.console.log(err.response);
      });
  }
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