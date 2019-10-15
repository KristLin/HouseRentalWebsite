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
          <!-- <router-link
            class="btn btn-primary"
            :to="{ name: 'search', params: { suburb: this.searchData.suburb }}"
          >Search</router-link>-->
          <button class="btn btn-primary" @click="searchHouse">Search</button>
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
    searchHouse() {
      this.$router.push({
        name: "search",
        query: { suburb: this.searchData.suburb },
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