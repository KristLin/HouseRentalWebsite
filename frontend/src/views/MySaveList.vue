<template>
  <div>
    <div class="container">
      <h3 class="mb-4">My Save List</h3>
      <hr />
      <SearchInput :searchData="searchData" @searchHouse="searchHouse" />
      <hr />
      <HouseCards v-bind:houses="houses" />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import SearchInput from "@/components/SearchInput.vue";
import HouseCards from "@/components/HouseCards.vue";

export default {
  name: "myHouses",
  components: {
    SearchInput,
    HouseCards
  },

  data() {
    return {
      searchData: {},
      houses: []
    };
  },

  methods: {
    searchHouse() {
      window.console.log("searching...");
      window.console.log(this.searchData);
      this.$axios
        .get("/api/houses/savelist/" + this.$store.getters.getUserId, {
          params: this.searchData
        })
        .then(response => {
          // JSON responses are automatically parsed.
          window.console.log(response.data);
          this.houses = response.data;
        })
        .catch(err => {
          window.console.log(err.response);
        });
    }
  },
  created() {
    this.$axios
      .get("/api/houses/savelist/" + this.$store.getters.getUserId)
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
</style>