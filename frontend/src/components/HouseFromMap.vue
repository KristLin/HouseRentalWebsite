<template>
  <!-- Page Content -->
  <div>
    <div id="house-display" v-if="house">
      <div id="intro" class="card">
        <!-- carousel -->
        <div
          id="carouselExampleIndicators"
          class="carousel slide"
          data-ride="carousel"
          v-if="house.cover"
        >
          <ol class="carousel-indicators active">
            <!-- cover image -->
            <li data-target="#carouselExampleIndicators" data-slide-to="0"></li>
            <!-- other images -->
            <li
              data-target="#carouselExampleIndicators"
              :key="idx"
              v-for="(index, idx) in house.images"
              :data-slide-to="idx+1"
            ></li>
          </ol>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img class="card-img-top map-house-cover-display" :src="house.cover" />
            </div>
            <div class="carousel-item" :key="idx" v-for="(index, idx) in house.images">
              <img class="card-img-top map-house-cover-display" :src="house.images[idx]" />
            </div>
          </div>
          <a
            class="carousel-control-prev"
            href="#carouselExampleIndicators"
            role="button"
            data-slide="prev"
          >
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
          </a>
          <a
            class="carousel-control-next"
            href="#carouselExampleIndicators"
            role="button"
            data-slide="next"
          >
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
          </a>
        </div>

        <!-- if there is no cover data, text will be shown up -->
        <div class="map-house-cover-display" v-if="!house.cover">
          <p class>House Cover</p>
        </div>

        <!-- house info -->
        <div class="card-body">
          <h3 class="card-title text-left">{{ house.title }}</h3>
          <h6 class="text-left">${{house.price}} per night</h6>
          <h6 class="text-left">
            {{house.tenant_num}}
            <i class="fas fa-user mr-4"></i>
            {{ house.size }} m
            <sup class="mr-4">2</sup>
            {{ house.suburb }}
          </h6>
          <h6 class="text-left">{{ house.location }}</h6>
          <div class="rating-div"></div>

          <!-- house rating and rating number -->
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
          <p class="mt-2" v-if="parseInt(house.rating_num) === 0">This house has no rating yet.</p>
        </div>
      </div>

      <!-- click the button to go to the House page -->
      <div id="learnMore" class="card card-outline-secondary my-2">
        <button class="my-btn form-control" @click="goToHousePage">More Info</button>
      </div>

      <!-- house descripiton -->
      <div id="description" class="card card-outline-secondary my-2">
        <div class="card-header">House Description</div>
        <div class="card-body">
          <p class="text-left">{{ house.description }}</p>
        </div>
      </div>

      <!-- house available facilities -->
      <div id="facility" class="card card-outline-secondary my-4">
        <div class="card-header">House Facility</div>
        <div class="card-body">
          <i class="fas fa-wifi map-house-facility-icon" v-if="house.wifi"></i>
          <i class="fas fa-utensils map-house-facility-icon" v-if="house.kitchen"></i>
          <i class="fas fa-car map-house-facility-icon" v-if="house.carpark"></i>
          <i class="fas fa-snowflake map-house-facility-icon" v-if="house.ac"></i>
        </div>
      </div>
    </div>
    <!-- show text if no marker was clicked -->
    <div class="house-display-hint" v-if="!house">
      <p>Click marker in the map to see house detail.</p>
    </div>
  </div>

  <!-- /.container -->
</template>

<script>
import StarRating from "vue-star-rating";

export default {
  name: "HouseFromMap",
  components: {
    StarRating
  },
  props: {
    house: {}
  },
  // check if the params are lost
  methods: {
    goToHousePage() {
      this.$router.push({
        name: "house",
        query: { houseId: this.house._id },
        params: { house: this.house }
      });
    }
  },
  created() {}
};
</script>

<style>
#house-display {
  max-height: 500px;
  overflow: auto;
}

#description {
  max-height: 400px;
  overflow: auto;
}

.map-house-cover-display {
  height: 250px;
  width: 100%;
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

.house-display-hint {
  margin-top: 100px;
  margin-bottom: 100px;
}

.map-house-facility-icon {
  font-size: 1.5rem;
  margin-left: 1rem;
  margin-right: 1rem;
}
</style>
