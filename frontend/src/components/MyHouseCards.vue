<template>
  <div>
    <div class="row">
      <div class="col-lg-4 col-sm-6 mb-4" :key="house._id" v-for="house in houses">
        <div class="card" @click="clickHouse(house)">
          <img class="card-img-top" :src="house.cover" alt="house-cover" />
          <div class="card-body">
            <h5 class="card-title">{{ house.title }}</h5>
            <span class="text-warning">&#9733; &#9733; &#9733; &#9733; &#9734;</span>
            <!-- <p class="card-text text-left">{{ handleDescription(house.description) }}</p> -->
          </div>
          <div class="card-footer">
            <small class="text-muted">{{house.suburb}}</small>
            <br />
            <small class="text-muted">${{house.price}}</small>
          </div>
        </div>
        <button class="my-btn form-control my-1" @click="updateHouse(house._id)">Update House</button>
        <button class="btn btn-danger form-control" @click="deleteHouse(house._id)">Delete House</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MyHouseCards",
  props: {
    houses: Array
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
      window.console.log(house_id);
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
      this.$axios
        .delete("/api/houses/" + this.$store.getters.getUserId + "/" + house_id)
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