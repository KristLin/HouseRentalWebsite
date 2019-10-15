<template>
  <div>
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <div class="container">
      <div class="card-body">
        <div class="filter-option">
          <label for>Suburb:</label>
          <input type="text" />
          <label for>Price:</label>
          <input type="text" />
          <br />
          <label for>Start Date:</label>
          <!-- <input type="date" /> -->
          <label for>Leave Date:</label>
          <!-- <input type="date" /> -->
          <button @click="searchHouse" class="btn btn-primary">Search</button>
        </div>
      </div>
      <h5>Search Result:</h5>
      <HouseCards v-bind:houses="houses" />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import HouseCards from "@/components/HouseCards.vue";

export default {
  name: "search",
  components: {
    HouseCards
  },

  data() {
    return {
      houses: this.$route.params.houses,
      suburn: this.$route.query.suburn
    };
  },

  methods: {
    searchHouse() {
      window.console.log("searching...");
    }
  },
  beforeRouteEnter: (to, from, next) => {
    // if the params is empty, call the backend to get data.
    if (Object.keys(to.params).length === 0) {
      to.params.houses = [
        {
          _id: 2,
          title: "title 2",
          description: "description 2",
          cover: "/house_images/2.jpg",
          suburb: "suburb 2",
          price: "price 2"
        },
        {
          _id: 3,
          title: "title 3",
          description: "description 3",
          cover: "/house_images/3.jpg",
          suburb: "suburb 3",
          price: "price 3"
        }
      ];
      // houses = this.$axios
      //   .get("/api/houses/")
      //   .then(res => window.console.log(res))
      //   .catch(err => window.console.log(err));
    }
    next();
  }
};
</script>

<style scoped>
.container {
  padding-top: 2rem;
  min-height: 500px;
}
</style>