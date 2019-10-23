<template>
  <div>
    <div class="container">
      <h3 class="mb-4">Search Houses</h3>
      <SearchInput :searchData="searchData" @searchHouse="searchHouse" />
      <div>
        <hr />
        <h5 v-if="!this.houses.length" class="my-4">Sorry, there is not result...</h5>
        <HouseCards v-bind:houses="houses" />
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
      houses: []
    };
  },

  methods: {
    searchHouse() {
      window.console.log("searching...");
      window.console.log(this.searchData);
      this.$axios
        .get("/api/houses/", { params: this.searchData })
        .then(response => {
          // JSON responses are automatically parsed.
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
  margin-top: 30px;
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
</style>