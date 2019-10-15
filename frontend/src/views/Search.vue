<template>
  <div>
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <div class="container">
      <div class="card-body">
        <div>
          <div class="row text-left">
            <div class="col-lg-4 col-md-6">
              <label class="filter-label">Suburb:</label>
              <input type="text" />
            </div>
            <div class="col-lg-4 col-md-6">
              <label class="filter-label">Min Price:</label>
              <input type="text" />
            </div>
            <div class="col-lg-4 col-md-6">
              <label class="filter-label">Max Price:</label>
              <input type="text" />
            </div>
          </div>
        </div>
        <div class="row text-left">
          <div class="col-lg-4 col-md-6">
            <label class="filter-label">Start:</label>
            <input type="date" />
          </div>
          <div class="col-lg-4 col-md-6">
            <label class="filter-label">Leave:</label>
            <input type="date" />
          </div>
          <div class="col-lg-4 col-md-6">
            <button @click="searchHouse" class="btn btn-primary">Search</button>
          </div>
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
.filter-label {
  text-align: center;
  width: 75px;
}
</style>