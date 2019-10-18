<template>
  <div>
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <div>
      <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
        <ol class="carousel-indicators">
          <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
          <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
          <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
        </ol>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img
              class="d-block w-100"
              src="../assets/homepage_carousel_images/1.jpg"
              alt="First slide"
            />
            <div class="header-text hidden-xs">
              <div class="col-md-12 text-center">
                <h2>
                  <span>
                    Welcome to
                    <strong>LOREM IPSUM</strong>
                  </span>
                </h2>
                <br />
                <h3>
                  <span>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</span>
                </h3>
                <br />
                <div class="carousel-button">
                  <button class="btn btn-dark form-control" @click="learnMore">Learn More</button>
                </div>
              </div>
            </div>
          </div>
          <div class="carousel-item">
            <img
              class="d-block w-100"
              src="../assets/homepage_carousel_images/2.jpg"
              alt="Second slide"
            />
            <div class="header-text hidden-xs">
              <div class="col-md-12 text-center">
                <h2>
                  <span>
                    Welcome to
                    <strong>LOREM IPSUM</strong>
                  </span>
                </h2>
                <br />
                <h3>
                  <span>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</span>
                </h3>
                <br />
                <div class="carousel-button">
                  <button class="btn btn-dark form-control" @click="learnMore">Learn More</button>
                </div>
              </div>
            </div>
          </div>
          <div class="carousel-item">
            <img
              class="d-block w-100"
              src="../assets/homepage_carousel_images/3.jpg"
              alt="Third slide"
            />
            <div class="header-text hidden-xs">
              <div class="col-md-12 text-center">
                <h2>
                  <span>
                    Welcome to
                    <strong>LOREM IPSUM</strong>
                  </span>
                </h2>
                <br />
                <h3>
                  <span>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</span>
                </h3>
                <br />
                <div class="carousel-button">
                  <button class="btn btn-dark form-control" @click="learnMore">Learn More</button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <a
          class="carousel-control-prev"
          href="#carouselExampleIndicators"
          role="button"
          data-slide="prev"
        >
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="sr-only">Previous</span>
        </a>
        <a
          class="carousel-control-next"
          href="#carouselExampleIndicators"
          role="button"
          data-slide="next"
        >
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="sr-only">Next</span>
        </a>
      </div>
      <div class="features">
        <p>Features Intro</p>
      </div>
      <!-- <div class="card-body">
        <h2 class="card-title">Find your favorite accommodation</h2>
        <p class="card-text">Thousands of choices for you in New South Wales.</p>
        <SearchInput :searchData="searchData" @searchHouse="searchHouse" />
      </div>

      <h5>You might be intesested in these accommodation..</h5>
      <hr />

      <HouseCards v-bind:houses="houses" />-->
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HouseCards from "@/components/HouseCards.vue";
// import SearchInput from "@/components/SearchInput.vue";

export default {
  name: "home",
  components: {
    // SearchInput,
    // HouseCards
  },
  props: {},
  data() {
    return {
      carouselItems: [
        {
          title: "Welcome to LOREM IPSUM",
          subtitle: "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
          imageSrc: "../assets/homepage_carousel_images/1.jpg"
        },
        {
          title: "Welcome to LOREM IPSUM",
          subtitle: "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
          imageSrc: "../assets/homepage_carousel_images/2.jpg"
        },
        {
          title: "Welcome to LOREM IPSUM",
          subtitle: "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
          imageSrc: "../assets/homepage_carousel_images/2.jpg"
        }
      ]
    };
  },

  methods: {
    learnMore() {
      this.$router.push({
        name: "search",
      });
    }
  },

  // get random houses for homepage display
  // created() {
  //   this.$axios
  //     .get("/api/houses/random")
  //     .then(response => {
  //       // JSON responses are automatically parsed.
  //       this.houses = response.data;
  //     })
  //     .catch(err => {
  //       window.console.log(err);
  //     });
  // }
};
</script>

<style scoped>
.container {
  padding-top: 2rem;
  min-height: 500px;
}
.carousel-item {
  height: 550px;
}

/* button on carousel image */
.carousel-button {
  margin: 1rem auto;
  width: 200px;
}

.btn-dark {
  border: none;
  background-color: #3c9d9b;
}

/* Carousel Header Styles */
.header-text {
  position: absolute;
  top: 40%;
  left: 1.8%;
  right: auto;
  width: 96%;
  color: #fff;
}

.header-text h2 {
  font-size: 40px;
}

.header-text h2 span {
  background-color: #3c9d9b;
  padding: 10px;
}

.header-text h3 span {
  background-color: #000;
  padding: 15px;
}
</style>