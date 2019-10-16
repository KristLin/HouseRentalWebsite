<template>
  <div>
    <div class="container">
      <SearchInput :searchData="searchData" @search="searchHouse" />
      <div>
        <h5>Search Result:</h5>
        <HouseCards v-bind:houses="houses" />
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import SearchInput from "@/components/SearchInput.vue";
import HouseCards from "@/components/HouseCards.vue";


export default {
  name: "search",
  components: {
    SearchInput,
    HouseCards,

  },

  data() {
    return {
      searchData: {
        suburb: this.$route.query.suburb,
      },
      houses: this.$route.params.houses,
    };
  },

  methods: {
    searchHouse () {
      window.console.log("searching...")
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
  },
  mounted() {
    // Used for testing
    // window.console.log(this.searchData);
  }
};
</script>

<style scoped>
.container {
  padding-top: 2rem;
  min-height: 500px;
}
.filter-label {
  font-size: 13px;
}
.filter-row {
  height: 100px;
}
.filter-input {
  margin: auto;
}
.datepicker-height {
  height: 50%;
}
</style>