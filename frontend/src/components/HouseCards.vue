<template>
  <div>
    <div class="row">
      <div
        class="col-lg-4 col-sm-6 mb-4"
        @click="clickHouse(house)"
        :key="house._id"
        v-for="house in houses"
      >
        <div class="card zoom h-100 shadow">
          <img class="card-img-top house-card-cover-display" :src="house.cover" alt="house-cover" />
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
      </div>
    </div>
  </div>
</template>

<script>
import StarRating from "vue-star-rating";

export default {
  name: "HouseCards",
  props: {
    houses: Array
  },
  components: {
    StarRating
  },
  methods: {
    // when the house card is clicked, it will push the house data to House page
    clickHouse(house) {
      this.$router.push({
        name: "house",
        query: { houseId: house._id },
        params: { house: house }
      });
    },
    // only display first 150 charecters of the description for better representation
    handleDescription(description) {
      return (
        description.substring(0, 150) + (description.length > 150 ? " ..." : "")
      );
    }
  }
};
</script>

<style scoped>
.house-card-cover-display {
  width: 100%;
  height: 200px;
  object-fit: cover;
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