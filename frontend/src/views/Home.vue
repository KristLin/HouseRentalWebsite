<template>
  <div>
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <div class="container">
      <div class="card-body">
        <h2 class="card-title">Find your favorite accommodation</h2>
        <p class="card-text">Thousands of choices for you in New South Wales.</p>
        <div class="filter-option">
          <label for>Suburb:</label>
          <input type="text" v-model="searchData.suburb" />
          <router-link
            class="btn btn-primary"
            :to="{ name: 'search', params: { suburb: this.searchData.suburb }}"
          >Search</router-link>
          <!-- <button @click="searchHouse" class="btn btn-primary">Search</button> -->
        </div>
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

export default {
  name: "home",
  components: {
    HouseCards
  },
  props: {},
  data() {
    return {
      searchData: {
        suburb: ""
      },
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

  methods: {}

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