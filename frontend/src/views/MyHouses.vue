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
              <h3 class="mb-0">My Houses</h3>
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

        <hr />
        <button
          class="my-btn w-50 m-auto form-control"
          @click="$router.push({name: 'uploadHouse'})"
        >Upload House</button>
        
        <!-- advertisments here -->
        <hr />
        <!-- display text if there is no result -->
        <div
          class="mx-auto"
          style="margin-top:100px; margin-bottom:150px"
          v-if="!this.userHouses.length && this.hasFetchedData"
        >
          <h5>Sorry, there is not result...</h5>
        </div>

        <!-- loading animation -->
        <div class="mx-auto" style="margin-top:100px; margin-bottom:150px" v-if="!this.hasFetchedData">
          <RingLoader :color="'#96d1c7'" />
          <!-- <h5 v-if="!this.hasFetchedData">Searching, please wait...</h5> -->
        </div>

        <!-- search result -->
        <MyHouseCards v-bind:houses="userHouses" v-if="this.hasFetchedData" />
        
        <!-- back to top button -->
        <div class="float-right" v-if="this.hasFetchedData">
          <a href="#" style="color: #000;">Back to top</a>
        </div>
      </div>
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
      userHouses: [],
      hasFetchedData: false
    };
  },

  methods: {
    searchHouse() {
      window.console.log("searching...");
      this.hasFetchedData = false;
      window.console.log(this.searchData);
      // send search request to backend
      this.$axios
        .get("/api/houses/providedby/" + this.$store.getters.getUserId, {
          params: this.searchData
        })
        .then(response => {
          window.console.log(response.data);
          this.userHouses = response.data;
          this.hasFetchedData = true;
        })
        .catch(err => {
          window.console.log(err.response);
        });
    }
  },
  created() {
    // only allow provider to see this page
    if (this.$store.getters.isLoggedIn) {
      if (this.$store.getters.isProvider) {
        window.console.log("current user is provider.");
        this.$axios
          .get("/api/houses/providedby/" + this.$store.getters.getUserId)
          .then(response => {
            this.userHouses = response.data;
            this.hasFetchedData = true;
          })
          .catch(err => {
            window.console.log(err.response);
          });
      } else {
        window.console.log("Require provider login!");
        this.$router.push({ name: "home" });
      }
    } else {
      window.console.log("Require provider login!");
      this.$router.push({ name: "home" });
    }
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