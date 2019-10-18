<template>
  <div>
    <div class="container">
      <SearchInput :searchData="searchData" @searchHouse="searchHouse" />
      <div>
        <h5>Search Result:</h5>
        <hr />
        <p v-if="!this.houses.length" class="my-4">Sorry, there is not result...</p>
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
      searchData: this.$route.query,
      // houses: this.$route.params.houses
      houses: []
    };
  },

  methods: {
    searchHouse() {
      window.console.log("searching...");
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
    if (Object.keys(this.$route.query).length !== 0) {
      this.$axios
        .get("/api/houses/", { params: this.searchData })
        .then(response => {
          // JSON responses are automatically parsed.
          this.houses = response.data;
        })
        .catch(err => {
          window.console.log(err.response);
        });
    } else {
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
  }
};
</script>

<style scoped>
.container {
  padding-top: 2rem;
  min-height: 500px;
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
.datepicker-height {
  height: 50%;
}
</style>