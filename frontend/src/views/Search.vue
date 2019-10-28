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

        <div class="w-50 mx-auto my-4">
          <button class="my-btn form-control" v-if="!showMap" @click="showMap=!showMap">View in Map</button>
          <button class="my-btn form-control" v-if="showMap" @click="showMap=!showMap">View in Cards</button>
        </div>
        <hr />

        <!-- advertisments here -->
        <h5
          v-if="!this.houses.length && this.hasFetchedData && !showMap"
          class="mt-4 mx-auto"
        >Sorry, there is not result...</h5>
        <h5 v-if="!this.hasFetchedData && !showMap" class="mt-4 mx-auto">Searching, please wait...</h5>
        <HouseCards :houses="houses" v-if="this.hasFetchedData && !showMap" />

        <Map :houses="houses" v-if="showMap" />

        <div class="float-right" v-if="!showMap">
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

export default {
  name: "search",
  components: {
    SearchInput,
    HouseCards,
    Map
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
      this.$axios
        .get("/api/houses/", { params: this.searchData })
        .then(response => {
          // JSON responses are automatically parsed.
          this.hasFetchedData = true;
          this.houses = response.data;
        })
        .catch(err => {
          window.console.log(err.response);
        });
    },
    // orderResult(orderType) {
    //   this.houses.sort((a, b) => {
    //     parseFloat(a[orderType]) > parseFloat(b[orderType])
    //       ? 1
    //       : parseFloat(a[orderType]) === parseFloat(b[orderType])
    //       ? parseFloat(a._id) > parseFloat(b._id)
    //         ? 1
    //         : -1
    //       : -1;
    //   });
    // }
  },
  created() {
    this.$axios
      .get("/api/houses/")
      .then(response => {
        // JSON responses are automatically parsed.
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