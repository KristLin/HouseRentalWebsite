<template>
  <div>
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <div class="container">
      <div class="card-body">
        <h2 class="card-title">Find your favorite accommodation</h2>
        <p class="card-text">Thousands of choices for you in New South Wales.</p>
        <SearchInput :searchData="searchData" @searchHouse="searchHouse" />
        <!-- <div class="filter-option">
          <label for>Suburb:</label>
          <input type="text" v-model="searchData.suburb" />
          <button class="btn btn-primary" @click="searchHouse">Search</button>
        </div>-->
      </div>

      <h5>You might be intesested in these accommodation..</h5>
      <hr />

      <HouseCards v-bind:houses="houses" />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import HouseCards from "@/components/HouseCards.vue";
import SearchInput from "@/components/SearchInput.vue";

export default {
  name: "home",
  components: {
    SearchInput,
    HouseCards
  },
  props: {},
  data() {
    return {
      searchData: {},
      houses: []
    };
  },

  methods: {
    searchHouse(searchData) {
      // next to implement: add if-control to check if the query is empty
      // if it is empty, no need to pass the query

      this.$router.push({
        name: "search",
        query: searchData,
        params: { houses: this.houses }
      });
    }
  },

  // get random houses for homepage display
  created() {
    this.$axios
      .get("/api/houses/random")
      .then(response => {
        // JSON responses are automatically parsed.
        this.houses = response.data;
      })
      .catch(err => {
        window.console.log(err);
      });
  }
};
</script>

<style scoped>
.container {
  padding-top: 2rem;
  min-height: 500px;
}
.carousel-item {
  height: 200px;
}
</style>