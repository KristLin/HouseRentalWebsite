<template>
  <div>
    <div class="row">
      <div class="col-lg-4 col-sm-6 mb-4" :key="house._id" v-for="house in houses">
        <div class="card zoom shadow" @click="clickHouse(house)">
          <img class="card-img-top my-house-card-cover-display" :src="house.cover" alt="house-cover" />
          <div class="card-body">
            <!-- house title -->
            <h5 class="card-title">{{ house.title }}</h5>

            <!-- house size and tenant number -->
            <h6>
              {{house.tenant_num}}
              <i class="fas fa-user mr-4"></i>
              {{ house.size }} m
              <sup>2</sup>
            </h6>

            <!-- rating and rating number -->
            <star-rating
              :inline="true"
              :rating="parseFloat(house.rating)"
              :read-only="true"
              :show-rating="false"
              v-bind:increment="0.01"
              v-bind:star-size="20"
              v-if="parseInt(house.rating_num) !== 0"
            ></star-rating>
            <span
              style="font-weight:bold;"
              class="mx-2"
              v-if="parseInt(house.rating_num) !== 0"
            >({{ house.rating_num }})</span>
            <p class="mb-0" v-if="parseInt(house.rating_num) === 0">No rating yet.</p>
          </div>

          <!-- house suburb and price -->
          <div class="card-footer">
            <small class="text-muted">{{house.suburb}}</small>
            <br />
            <small class="text-muted">${{house.price}}</small>
          </div>
        </div>

        <!-- update houes button -->
        <button class="my-btn form-control my-1 shadow" @click="updateHouse(house._id)">Update House</button>
        <!-- delete hosue button -->
        <button
          class="btn btn-danger form-control shadow"
          @click="deleteHouse(house._id)"
        >Delete House</button>
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
      // send user to update house page
      this.$router.push({
        name: "updateHouse",
        query: { houseId: house_id }
      });
    },

    deleteHouse(house_id) {
      this.$swal({
        title: "Confirm",
        text: "Are you sure you want to delete the house?",
        icon: "warning",
        buttons: true,
        dangerMode: true
      }).then(choice => {
        if (choice) {
          // send delete request to backend
          this.$axios
            .delete(
              "/api/houses/" + this.$store.getters.getUserId + "/" + house_id
            )
            .then(response => {
              window.console.log(response);
              this.$swal("Success!", "House is deleted!", "success");
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
      });
    }
  }
};
</script>

<style scoped>
.my-house-card-cover-display {
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

.zoom:hover {
  transform: scale(1.02);
}

.zoom:hover .card-body {
  background-color: #fcfcfc;
}

.zoom:hover .card-footer {
  background-color: #eeeeee;
}
</style>