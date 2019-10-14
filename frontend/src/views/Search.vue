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
            <br>
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
      houses: [
        {
          _id: 1,
          title: "title 1",
          description: "description 1",
          cover: "url 1",
          suburb: "suburb 1",
          price: "price 1"
        },
        {
          _id: 2,
          title: "title 2",
          description: "description 2",
          cover: "url 2",
          suburb: "suburb 2",
          price: "price 2"
        },
        {
          _id: 3,
          title: "title 3",
          description: "description 3",
          cover: "url 3",
          suburb: "suburb 3",
          price: "price 3"
        }
      ]
    };
  },

  methods: {
    searchHouse() {
      window.console.log("searching...");
    }
  }

  // get random house data for the home page
  // mounted() {
  //   axios
  //     .get("localhost:5000/houses/random")
  //     .then(houses => (this.houses = houses))
  //     .catch(function(error) {
  //       // handle error
  //       console.log(error);
  //     });
  // }
};
</script>

<style scoped>
.container {
  padding-top: 2rem;
  min-height: 500px;
}
</style>