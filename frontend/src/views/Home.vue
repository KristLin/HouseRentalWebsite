<template>
  <div>
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <div class="container">
      <div class="card-body">
        <h2 class="card-title">Find your favorite accommodation</h2>
        <p class="card-text">Thousands of choices for you in New South Wales.</p>
        <SearchInput :searchData="searchData" @search="searchHouse" />
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
      houses: [
        {
          _id: 1,
          title: "Title 1",
          description:
            "Aliquam mi massa, finibus ut elementum sed, tincidunt ac erat. Sed sagittis consectetur velit at tempor. In non tempor diam, eget pretium purus. Aliquam vel dictum odio, et cursus urna. Fusce convallis sapien dui, blandit convallis enim malesuada aliquam. Maecenas vestibulum tortor ac odio fringilla, in feugiat risus pretium. Donec iaculis eros at bibendum sollicitudin. Proin ultrices est tristique finibus ullamcorper. Pellentesque eleifend, dolor nec viverra luctus, mauris massa maximus libero, quis feugiat dolor diam a dui. Ut pharetra, dui sit amet condimentum mattis, metus ipsum eleifend lorem, vitae varius velit risus nec ipsum. Maecenas vehicula vulputate urna ut pulvinar. Aliquam erat volutpat. Praesent sapien sapien, fringilla sit amet placerat et, gravida interdum nunc. Nullam id tincidunt augue, quis porttitor risus.",
          cover: "/house_images/1.jpg",
          suburb: "Zetland",
          price: "200"
        },
        {
          _id: 2,
          title: "Title 2",
          description:
            "Aliquam mi massa, finibus ut elementum sed, tincidunt ac erat. Sed sagittis consectetur velit at tempor. In non tempor diam, eget pretium purus. Aliquam vel dictum odio, et cursus urna. Fusce convallis sapien dui, blandit convallis enim malesuada aliquam. Maecenas vestibulum tortor ac odio fringilla, in feugiat risus pretium. Donec iaculis eros at bibendum sollicitudin. Proin ultrices est tristique finibus ullamcorper. Pellentesque eleifend, dolor nec viverra luctus, mauris massa maximus libero, quis feugiat dolor diam a dui. Ut pharetra, dui sit amet condimentum mattis, metus ipsum eleifend lorem, vitae varius velit risus nec ipsum. Maecenas vehicula vulputate urna ut pulvinar. Aliquam erat volutpat. Praesent sapien sapien, fringilla sit amet placerat et, gravida interdum nunc. Nullam id tincidunt augue, quis porttitor risus.",
          cover: "/house_images/2.jpg",
          suburb: "Kingsford",
          price: "100"
        },
        {
          _id: 3,
          title: "Title 3",
          description:
            "Aliquam mi massa, finibus ut elementum sed, tincidunt ac erat. Sed sagittis consectetur velit at tempor. In non tempor diam, eget pretium purus. Aliquam vel dictum odio, et cursus urna. Fusce convallis sapien dui, blandit convallis enim malesuada aliquam. Maecenas vestibulum tortor ac odio fringilla, in feugiat risus pretium. Donec iaculis eros at bibendum sollicitudin. Proin ultrices est tristique finibus ullamcorper. Pellentesque eleifend, dolor nec viverra luctus, mauris massa maximus libero, quis feugiat dolor diam a dui. Ut pharetra, dui sit amet condimentum mattis, metus ipsum eleifend lorem, vitae varius velit risus nec ipsum. Maecenas vehicula vulputate urna ut pulvinar. Aliquam erat volutpat. Praesent sapien sapien, fringilla sit amet placerat et, gravida interdum nunc. Nullam id tincidunt augue, quis porttitor risus.",
          cover: "/house_images/3.jpg",
          suburb: "Kensington",
          price: "80"
        }
      ]
    };
  },

  methods: {
    searchHouse(event) {
      window.console.log(event.startDate);
      window.console.log(event.endDate);
      // next to implement: add if-control to check if the query is empty
      // if it is empty, no need to pass the query
      this.$router.push({
        name: "search",
        query: { searchDate: this.searchData },
        params: { houses: this.houses }
      });
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