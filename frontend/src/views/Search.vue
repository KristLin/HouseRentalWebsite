<template>
  <div>
    <div class="container">
      <div id="accordion">
        <!-- search bar here -->
        <div>
          <div id="filterHeading">
            <a
              data-toggle="collapse"
              href="#searchBar"
              role="button"
              aria-expanded="true"
              aria-controls="searchBar"
            >
              <h3 class="mb-0">Search Houses</h3>
            </a>
          </div>

          <div
            id="searchBar"
            class="collapse show"
            aria-labelledby="filterHeading"
            data-parent="#accordion"
          >
            <div class="card-body">
              <SearchInput :searchData="searchData" @searchHouse="searchHouse" />
            </div>
          </div>
          <hr />
        </div>

        <!-- view in map/view in cards button -->
        <div class="w-50 mx-auto my-4" v-if="$store.getters.isLoggedIn">
          <button class="my-btn form-control" v-if="!showMap" @click="showMap=!showMap">View in Map</button>
          <button class="my-btn form-control" v-if="showMap" @click="showMap=!showMap">View in Cards</button>
           <hr />
        </div>

        <!-- advertisments here -->
        <!-- display text if there is no result -->
        <div
          class="mx-auto"
          style="margin-top:100px; margin-bottom:150px"
          v-if="!this.houses.length && this.hasFetchedData && !showMap"
        >
          <h5>Sorry, there is not result...</h5>
        </div>

        <!-- loading animation -->
        <div class="mx-auto" style="margin-top:100px; margin-bottom:150px" v-if="!this.hasFetchedData && !showMap">
          <RingLoader :color="'#96d1c7'" />
          <!-- <h5 v-if="!this.hasFetchedData && !showMap">Searching, please wait...</h5> -->
        </div>

        <!-- search result -->
        <HouseCards :houses="houses" v-if="this.hasFetchedData && !showMap" />

        <!-- view in map -->
        <Map :houses="houses" v-if="showMap" />

        <!-- back to top button -->
        <div class="float-right" v-if="this.hasFetchedData && !showMap">
          <a href="#" style="color: #000;">Back to top</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import SearchInput from "@/components/SearchInput.vue";
import HouseCards from "@/components/HouseCards.vue";
import Map from "@/components/Map.vue";
import { RingLoader } from "vue-spinners-css";

export default {
  name: "search",
  components: {
    SearchInput,
    HouseCards,
    Map,
    RingLoader
  },

  data() {
    return {
      searchData: {},
      // houses: this.$route.params.houses
      houses: [],
      hasFetchedData: false,
      showMap: false
    };
  },

  methods: {
    searchHouse() {
      window.console.log("searching...");
      window.console.log(this.searchData);
      this.hasFetchedData = false;
      // send search request to backend
      this.$axios
        .get("/api/houses/", { params: this.searchData })
        .then(response => {
          this.hasFetchedData = true;
          this.houses = response.data;
        })
        .catch(err => {
          window.console.log(err.response);
        });
    }
  },
  created() {
    // get all houses automatically when this page is created
    this.$axios
      .get("/api/houses/")
      .then(response => {
        this.hasFetchedData = true;
        this.houses = response.data;
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

.filter-label {
  font-size: 13px;
}
.filter-row {
  height: 100px;
}
.filter-input {
  margin: auto;
}

a:hover {
  text-decoration: none;
}
a h3 {
  color: #2c3e50;
}
a h3:hover {
  color: #3c9d9b;
}
</style>