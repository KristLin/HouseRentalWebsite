<template>
  <div>
    <div class="row">
      <div
        class="col-lg-4 col-sm-6 mb-4"
        @click="clickHouse(house)"
        :key="house._id"
        v-for="house in houses"
      >
        <div class="card h-100">
          <img class="card-img-top" :src="house.cover" alt="house-cover" />
          <div class="card-body">
            <h4 class="card-title">{{house.title}}</h4>
            <p class="card-text text-left">{{handleDescription(house.description)}}</p>
          </div>
          <div class="card-footer">
            <small class="text-muted">{{house.suburb}}</small>
            <br />
            <small class="text-muted">${{house.price}}</small>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HouseCards",
  props: { houses: Array },
  methods: {
    clickHouse(house) {
      this.$router.push({
        name: "house",
        query: { houseId: house._id },
        params: { house: house }
      });
    },
    handleDescription(description) {
      return (
        description.substring(0, 150) + (description.length > 150 ? " ..." : "")
      );
    }
  }
};
</script>

<style scoped>
img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}
.card-title {
  min-height: 50px;
}
</style>