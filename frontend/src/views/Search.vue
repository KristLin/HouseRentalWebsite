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
        </div>

        <!-- advertisments here -->
        <hr />
        <div class="row">
          <h5
            v-if="!this.houses.length && this.hasFetchedData"
            class="mt-4 mx-auto"
          >Sorry, there is not result...</h5>
          <h5 v-if="!this.hasFetchedData" class="mt-4 mx-auto">Searching, please wait...</h5>
          <HouseCards :houses="houses" v-if="this.hasFetchedData" />
        </div>
        <div class="float-right">
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

export default {
  name: "search",
  components: {
    SearchInput,
    HouseCards
  },

  data() {
    return {
      searchData: {},
      // houses: this.$route.params.houses
      houses: [],
      hasFetchedData: false
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
    }
  },
  // beforeRouteEnter: (to, from, next) => {
  //   // if the params is empty, call the backend to get data.
  //   if (Object.keys(to.params).length === 0) {
  //     this.$axios
  //       .get("/api/houses/random")
  //       .then(response => {
  //         // JSON responses are automatically parsed.
  //         to.params.houses = response.data;
  //       })
  //       .catch(err => {
  //         window.console.log(err);
  //       });

  //     // houses = this.$axios
  //     //   .get("/api/houses/")
  //     //   .then(res => window.console.log(res))
  //     //   .catch(err => window.console.log(err));
  //   }
  //   next();
  // },
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