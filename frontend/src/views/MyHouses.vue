<template>
  <div>
    <div class="container">
      <h3 class="mb-4">My Houses</h3>
      <hr />
      <SearchInput :searchData="searchData" @searchHouse="searchHouse" />
      <hr />
      <button
        class="my-btn w-50 m-auto form-control"
        @click="$router.push({name: 'uploadHouse'})"
      >Upload House</button>
      <hr />

      <MyHouseCards v-bind:houses="userHouses" />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import SearchInput from "@/components/SearchInput.vue";
import MyHouseCards from "@/components/MyHouseCards.vue";

export default {
  name: "myHouses",
  components: {
    SearchInput,
    MyHouseCards
  },

  data() {
    return {
      searchData: {},
      userHouses: []
    };
  },

  methods: {
    searchHouse() {
      window.console.log("searching...");
      window.console.log(this.searchData);
      this.$axios
        .get("/api/houses/providedby/" + this.$store.getters.getUserId, {
          params: this.searchData
        })
        .then(response => {
          // JSON responses are automatically parsed.
          window.console.log(response.data);
          this.userHouses = response.data;
        })
        .catch(err => {
          window.console.log(err.response);
        });
    }
  },
  created() {
    if (this.$store.getters.isLoggedIn) {
      if (this.$store.getters.isProvider) {
        window.console.log("current user is provider.");
        this.$axios
          .get("/api/houses/providedby/" + this.$store.getters.getUserId)
          .then(response => {
            // JSON responses are automatically parsed.
            this.userHouses = response.data;
          })
          .catch(err => {
            window.console.log(err.response);
          });
      } else {
        alert("Require provider login!");
        this.$router.push({ name: "home" });
      }
    } else {
      alert("Require provider login!");
      this.$router.push({ name: "home" });
    }
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