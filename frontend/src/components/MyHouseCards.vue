<template>
  <div>
    <div class="row">
      <div class="col-lg-4 col-sm-6 mb-4" :key="house._id" v-for="house in houses">
        <div class="card shadow" @click="clickHouse(house)">
          <img class="card-img-top" :src="house.cover" alt="house-cover" />
          <div class="card-body">
            <h5 class="card-title">{{ house.title }}</h5>
            <star-rating
              :inline="true"
              :rating="house.rating"
              :read-only="true"
              :show-rating="false"
              v-bind:increment="0.01"
              v-bind:star-size="20"
              v-if="house.rating"
            ></star-rating>
            <span
              style="font-weight:bold;"
              class="mx-2"
              v-if="house.rating"
            >({{ house.rating_num }})</span>
            <p class="mb-0" v-if="!house.rating">No rating yet.</p>
          </div>
          <div class="card-footer">
            <small class="text-muted">{{house.suburb}}</small>
            <br />
            <small class="text-muted">${{house.price}}</small>
          </div>
        </div>
        <button class="my-btn form-control my-1 shadow" @click="updateHouse(house._id)">Update House</button>
        <button class="btn btn-danger form-control shadow" @click="deleteHouse(house._id)">Delete House</button>
      </div>
    </div>
  </div>
</template>

<script>
import StarRating from "vue-star-rating";

export default {
  name: "MyHouseCards",
  props: {
    houses: Array
  },
  components: {
    StarRating
  },
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
    },
    updateHouse(house_id) {
      this.$router.push({
        name: "updateHouse",
        query: { houseId: house_id }
      });
      //   this.$axios
      //     .patch(
      //       "/api/houses/" + this.$store.getters.getUserId + "/" + house_id,
      //       usedUpdatedUserData
      //     )
      //     .then(response => {
      //       window.console.log(response);
      //       alert("User info is updated!");
      //     })
      //     .catch(error => window.console.log(error.response));
    },

    deleteHouse(house_id) {
      if (confirm("Do you really want to delete the house?")) {
        this.$axios
          .delete(
            "/api/houses/" + this.$store.getters.getUserId + "/" + house_id
          )
          .then(response => {
            window.console.log(response);
            alert("House Deleted!");
            //   this.houses = this.houses.filter(function(house) {
            //     return house._id != house_id;
            //   });
            for (var i = this.houses.length - 1; i >= 0; i--) {
              if (this.houses[i]._id === house_id) {
                this.houses.splice(i, 1);
              }
            }
          })
          .catch(error => {
            window.console.log(error.response);
          });
      }
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

.my-btn {
  border: none;
  background-color: black;
  color: white;
}

.my-btn:hover {
  border: none;
  background-color: #3c9d9b;
  color: white;
}
</style>