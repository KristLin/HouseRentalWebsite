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
              <h3 class="mb-0">My Save List</h3>
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
          <HouseCards v-bind:houses="houses" />
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