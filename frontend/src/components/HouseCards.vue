<template>
  <div>
    <div class="card-deck">
      <div class="card" @click="clickHouse(house)" :key="house._id" v-for="house in houses">
        <img :src="house.cover" class="card-img-top house-cover" alt="house-cover" />
        <div class="card-body">
          <h5 class="card-title">{{house.title}}</h5>
          <p class="card-text">{{handleDescription(house.description)}}</p>
        </div>
        <div class="card-footer">
          <small class="text-muted">{{house.suburb}}</small>
          <br />
          <small class="text-muted">${{house.price}}</small>
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
      return description.substring(0, 100) + (description.length > 100 ? " ..." : "")
    }
  }
};
</script>

<style scoped>
img {
  width: 100%; /* You can set the dimensions to whatever you want */
  height: 200px;
  object-fit: cover;
}
</style>