<template>
  <div>
    <div class="row">
      <!-- three types of recommendations: same suburb; close price; same tenant number -->
      <ul class="list-group list-group-horizontal ml-auto my-1">
        <li class="list-group-item type-option-item" :class="{active: chosenType==='suburb'}" @click="chosenType='suburb'">Same Suburb</li>
        <li class="list-group-item type-option-item" :class="{active: chosenType==='price'}" @click="chosenType='price'">Close Price</li>
        <li class="list-group-item type-option-item" :class="{active: chosenType==='tenant_num'}" @click="chosenType='tenant_num'">Same Tenant Number</li>
      </ul>
    </div>
    <!-- same suburb recommendations -->
    <div class="row" v-if="chosenType==='suburb'">
      <div
        class="col-lg-4 col-sm-4 mb-0"
        @click="clickHouse(house)"
        :key="house._id"
        v-for="house in recommendedHouses.same_suburb"
      >
        <div class="card zoom h-100">
          <!-- house cover -->
          <img class="card-img-top recommend-house-cover-display" :src="house.cover" alt="house-cover" />
          <div class="card-body p-0">
            <!-- house title -->
            <small class="card-title">{{ house.title }}</small>
            <br />

            <!-- house size and tenant number -->
            <small>
              {{house.tenant_num}}
              <i class="fas fa-user mr-4"></i>
              {{ house.size }} m
              <sup>2</sup>
            </small>
            <br />

            <!-- house rating and rating number -->
            <star-rating
              :inline="true"
              :rating="parseFloat(house.rating)"
              :read-only="true"
              :show-rating="false"
              v-bind:increment="0.01"
              v-bind:star-size="12"
              v-if="parseInt(house.rating_num) !== 0"
            ></star-rating>
            <small class="mx-2" v-if="parseInt(house.rating_num) !== 0">({{ house.rating_num }})</small>
            <small class="mb-0" v-if="parseInt(house.rating_num) === 0">No rating yet.</small>
          </div>

          <!-- house suburb and price -->
          <div class="card-footer p-1">
            <small class="text-muted">{{house.suburb}} - ${{house.price}}</small>
          </div>
        </div>
      </div>
    </div>

    <!-- close price recommendations -->
    <div class="row" v-if="chosenType==='price'">
      <div
        class="col-lg-4 col-sm-6 mb-0"
        @click="clickHouse(house)"
        :key="house._id"
        v-for="house in recommendedHouses.close_price"
      >
        <div class="card zoom h-100">
          <!-- house cover -->
          <img class="card-img-top recommend-house-cover-display" :src="house.cover" alt="house-cover" />
          <div class="card-body p-0">
            <!-- house title -->
            <small class="card-title">{{ house.title }}</small>
            <br />

            <!-- house size and tenant number -->
            <small>
              {{house.tenant_num}}
              <i class="fas fa-user mr-4"></i>
              {{ house.size }} m
              <sup>2</sup>
            </small>
            <br />

            <!-- house rating and rating number -->
            <star-rating
              :inline="true"
              :rating="parseFloat(house.rating)"
              :read-only="true"
              :show-rating="false"
              v-bind:increment="0.01"
              v-bind:star-size="12"
              v-if="parseInt(house.rating_num) !== 0"
            ></star-rating>
            <small
              class="mx-2"
              v-if="parseInt(house.rating_num) !== 0"
            >({{ house.rating_num }})</small>
            <small class="mb-0" v-if="parseInt(house.rating_num) === 0">No rating yet.</small>
          </div>

          <!-- house suburb and price -->
          <div class="card-footer p-1">
            <small class="text-muted">{{house.suburb}} - ${{house.price}}</small>
          </div>
        </div>
      </div>
    </div>

    <!-- same tenant number recommendations -->
    <div class="row" v-if="chosenType==='tenant_num'">
      <div
        class="col-lg-4 col-sm-4 mb-0"
        @click="clickHouse(house)"
        :key="house._id"
        v-for="house in recommendedHouses.same_tenant_num"
      >
        <div class="card zoom h-100">
          <!-- house cover -->
          <img class="card-img-top recommend-house-cover-display" :src="house.cover" alt="house-cover" />
          <div class="card-body p-0">
            <!-- hosue title -->
            <small class="card-title">{{ house.title }}</small>
            <br />

            <!-- house size and tenant number -->
            <small>
              {{house.tenant_num}}
              <i class="fas fa-user mr-4"></i>
              {{ house.size }} m
              <sup>2</sup>
            </small>
            <br />

            <!-- house rating and rating number -->
            <star-rating
              :inline="true"
              :rating="parseFloat(house.rating)"
              :read-only="true"
              :show-rating="false"
              v-bind:increment="0.01"
              v-bind:star-size="12"
              v-if="parseInt(house.rating_num) !== 0"
            ></star-rating>
            <small class="mx-2" v-if="parseInt(house.rating_num) !== 0">({{ house.rating_num }})</small>
            <small class="mb-0" v-if="parseInt(house.rating_num) === 0">No rating yet.</small>
          </div>

          <!-- house suburb and price -->
          <div class="card-footer p-1">
            <small class="text-muted">{{house.suburb}} - ${{house.price}}</small>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import StarRating from "vue-star-rating";

export default {
  name: "RecommendHouses",
  components: { StarRating },
  props: {
    recommendInfo: {
      house_id: "",
      suburb: "",
      price: ""
    }
  },
  data() {
    return {
      recommendedHouses: {
        same_suburb: [],
        close_price: [],
        same_tenant_num: [],
      },
      chosenType: "suburb"
    };
  },
  methods: {
    clickHouse(house) {
      // get another House page's name to avoid pushing data to the same page
      let nextPathName = this.$route.name === "house" ? "house2"  : "house"
      this.$router.push({
        name: nextPathName,
        query: { houseId: house._id },
        params: { house: house }
      });
    }
  },
  created() {
    // get recommmended houses from backend
    this.$axios
      .get("/api/houses/recommend", { params: this.recommendInfo })
      .then(response => {
        this.recommendedHouses = response.data;
      })
      .catch(error => {
        window.console.log(error);
      });
  }
};
</script>

<style scoped>
.recommend-house-cover-display {
  width: 100%;
  height: 80px;
  object-fit: cover;
}

.list-group-item {
    border-color: black;
}

.list-group-item.active {
    background-color: black;
}

.type-option-item {
    font-size: 10px;
    padding: 5px;
}

.my-btn {
  border: none;
  background-color: #3c9d9b;
  color: white;
}

.my-btn:hover {
  border: none;
  background-color: black;
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