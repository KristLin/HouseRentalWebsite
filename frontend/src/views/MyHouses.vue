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
        <hr />

        <!-- advertisments here -->
        <div class="row">
          <MyHouseCards v-bind:houses="userHouses" />
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