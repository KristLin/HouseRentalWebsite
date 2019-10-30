<template>
  <div>
    <div class="row">
      <!-- <div class="card-header p-2" style="background-color: #3c9d9b; color: white;">Recommended Houses</div> -->
      <ul class="list-group list-group-horizontal ml-auto my-1">
        <li class="list-group-item type-option-item" :class="{active: chosenType==='suburb'}" @click="chosenType='suburb'">Same Suburb</li>
        <li class="list-group-item type-option-item" :class="{active: chosenType==='price'}" @click="chosenType='price'">Close Price</li>
        <li class="list-group-item type-option-item" :class="{active: chosenType==='tenant_num'}" @click="chosenType='tenant_num'">Same Tenant Number</li>
      </ul>
    </div>
    <div class="row" v-if="chosenType==='suburb'">
      <div
        class="col-lg-4 col-sm-4 mb-0"
        @click="clickHouse(house)"
        :key="house._id"
        v-for="house in recommendedHouses.same_suburb"
      >
        <div class="card h-100">
          <img class="card-img-top" :src="house.cover" alt="house-cover" />
          <div class="card-body p-0">
            <small class="card-title">{{ house.title }}</small>
            <br />
            <small>
              {{house.tenant_num}}
              <i class="fas fa-user mr-4"></i>
              {{ house.size }} m
              <sup>2</sup>
            </small>
            <br />
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
          <div class="card-footer p-1">
            <small class="text-muted">{{house.suburb}} - ${{house.price}}</small>
          </div>
        </div>
      </div>
    </div>

    <div class="row" v-if="chosenType==='price'">
      <div
        class="col-lg-4 col-sm-6 mb-0"
        @click="clickHouse(house)"
        :key="house._id"
        v-for="house in recommendedHouses.close_price"
      >
        <div class="card h-100">
          <img class="card-img-top" :src="house.cover" alt="house-cover" />
          <div class="card-body p-0">
            <small class="card-title">{{ house.title }}</small>
            <br />
            <small>
              {{house.tenant_num}}
              <i class="fas fa-user mr-4"></i>
              {{ house.size }} m
              <sup>2</sup>
            </small>
            <br />
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
          <div class="card-footer p-1">
            <small class="text-muted">{{house.suburb}} - ${{house.price}}</small>
          </div>
        </div>
      </div>
    </div>

    <div class="row" v-if="chosenType==='tenant_num'">
      <div
        class="col-lg-4 col-sm-4 mb-0"
        @click="clickHouse(house)"
        :key="house._id"
        v-for="house in recommendedHouses.same_tenant_num"
      >
        <div class="card h-100">
          <img class="card-img-top" :src="house.cover" alt="house-cover" />
          <div class="card-body p-0">
            <small class="card-title">{{ house.title }}</small>
            <br />
            <small>
              {{house.tenant_num}}
              <i class="fas fa-user mr-4"></i>
              {{ house.size }} m
              <sup>2</sup>
            </small>
            <br />
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
      this.$router.push({
        name: "house",
        query: { houseId: house._id },
        params: { house: house }
      });
    }
  },
  created() {
    this.$axios
      .get("/api/houses/recommend", { params: this.recommendInfo })
      .then(response => {
        this.recommendedHouses = response.data;
        window.console.log(
          "recommendedHouses: " + this.recommendedHouses.same_tenant_num
        );
      })
      .catch(error => {
        window.console.log(error);
      });
  }
};
</script>

<style scoped>
img {
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
</style>