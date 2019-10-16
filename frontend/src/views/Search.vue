<template>
  <div>
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <div class="container">
      <div class="row">
        <div class="col-lg-3 col-md-6 form-group">
          <label class="filter-label">Keyword:</label>
          <input type="text" class="form-control" placeholder="Keyword" />
        </div>
        <div class="col-lg-3 col-md-6 form-group">
          <label class="filter-label">Suburb:</label>
          <input type="text" class="form-control" placeholder="Suburb" />
        </div>
        <div class="col-lg-3 col-md-6 form-group">
          <label class="filter-label">Price from:</label>
          <input type="input" class="form-control" name="input" placeholder="Min Price" />
        </div>
        <div class="col-lg-3 col-md-6 form-group">
          <label class="filter-label">to:</label>
          <input type="input" class="form-control" name="input" placeholder="Max Price" />
        </div>
      </div>
      <div class="row">
        <div class="col-lg-6 col-md-12 form-group">
          <label class="filter-label">Stay Period:</label>
          <HotelDatePicker class="datepicker-height" />
        </div>
        <div class="col-lg-6 col-md-12 form-group">
          <label class="filter-label">Search</label>
          <button @click="searchHouse" class="btn btn-primary form-control">Search</button>
        </div>
      </div>

      <div class="row">
        <h5>Search Result:</h5>
        <HouseCards v-bind:houses="houses" />
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import HouseCards from "@/components/HouseCards.vue";
import HotelDatePicker from "vue-hotel-datepicker";

export default {
  name: "search",
  components: {
    HouseCards,
    HotelDatePicker
  },

  data() {
    return {
      houses: this.$route.params.houses,
      suburn: this.$route.query.suburn,
      priceRange: [0, 300],
      pricePoints: [0, 100, 200, 300, 400, "over 400"]
    };
  },

  methods: {
    searchHouse() {
      window.console.log("searching...");
    },
    handleDescription(description) {
      return (
        description.substring(0, 100) + (description.length > 100 ? " ..." : "")
      );
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