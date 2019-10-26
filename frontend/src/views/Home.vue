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
              width="100%"
              height="100%"
              src="../assets/homepage_carousel_images/1.jpg"
              alt="First slide"
            />
            <div class="container">
              <div class="carousel-caption text-left">
                <h1>
                  <strong>Welcome to Bomb Shrimp</strong>
                </h1>
                <h4>Start your jounery. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Donec id elit non mi porta gravida at eget metus. Nullam id dolor id nibh ultricies vehicula ut id elit.</h4>
                <button
                  class="btn btn-lg carousel-btn"
                  type="button"
                  @click="searchRoute"
                >Explorations</button>
              </div>
            </div>
          </div>
          <div class="carousel-item">
            <img
              width="100%"
              height="100%"
              src="../assets/homepage_carousel_images/2.jpg"
              alt="First slide"
            />
            <div class="container">
              <div class="carousel-caption">
                <h1>
                  <strong>Welcome to Bomb Shrimp</strong>
                </h1>
                <h4>Start your jounery. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Donec id elit non mi porta gravida at eget metus. Nullam id dolor id nibh ultricies vehicula ut id elit.</h4>
                <button class="btn btn-lg carousel-btn" type="button" @click="aboutRoute">About us</button>
              </div>
            </div>
          </div>
          <div class="carousel-item">
            <img
              width="100%"
              height="100%"
              src="../assets/homepage_carousel_images/3.jpg"
              alt="First slide"
            />
            <div class="container">
              <div class="carousel-caption text-right">
                <h1>
                  <strong>Welcome to Bomb Shrimp</strong>
                </h1>
                <h4>Start your jounery. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Donec id elit non mi porta gravida at eget metus. Nullam id dolor id nibh ultricies vehicula ut id elit.</h4>
                <button
                  class="btn btn-lg carousel-btn"
                  type="button"
                  @click="joinRoute"
                >Sign up here</button>
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
      <!-- 2. more on homepage -->
      <div class="features mx-auto">
        <div class="text-center my-5">
          <h2 class="font-weight-bold my-5">Why is it so great?</h2>
          <p class="lead mx-auto mb-5">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit,
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.
          </p>
          <div class="row">
            <div class="col-md-4">
              <i class="fas fa-chart-area fa-3x red-text"></i>
              <h5 class="font-weight-bold my-4">Analytics</h5>
              <p class="grey-text mb-md-0 mb-5">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reprehenderit
                maiores aperiam minima assumenda deleniti hic.
              </p>
            </div>

            <div class="col-md-4">
              <i class="fas fa-book fa-3x cyan-text"></i>
              <h5 class="font-weight-bold my-4">Tutorials</h5>
              <p class="grey-text mb-md-0 mb-5">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reprehenderit
                maiores aperiam minima assumenda deleniti hic.
              </p>
            </div>

            <div class="col-md-4">
              <i class="far fa-comments fa-3x orange-text"></i>
              <h5 class="font-weight-bold my-4">Support</h5>
              <p class="grey-text mb-0">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reprehenderit maiores
                aperiam minima assumenda deleniti hic.
              </p>
            </div>
          </div>
        </div>
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
    searchRoute() {
      this.$router.push({
        name: "search"
      });
    },
    aboutRoute() {
      this.$router.push({
        name: "about"
      });
    },
    joinRoute() {
      this.$router.push({
        name: "signup"
      });
    }
  }

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
  margin-top: 100px;
  margin-bottom: 80px;
}

/* button on carousel image */
.carousel-button {
  margin: 1rem auto;
  width: 200px;
}

.my-btn {
  border: none;
  background-color: #3c9d9b;
  color: white;
}

.my-btn:hover {
  border: none;
  background-color: black;
  color: white;
}

.features {
  width: 80%;
  min-height: 500px;
}

.carousel-item {
  height: 700px;
  background-color: black;
}
.carousel-item img {
  width: 100%;
  height: 700px;
  object-fit: cover;
  mask: linear-gradient(to bottom, rgba(0, 0, 0, 1), rgba(0, 0, 0, 0.7));
}

.carousel-btn {
  color: white;
  background-color: #3c9d9b;
}
.carousel-btn:hover {
  color: white;
  background-color: black;
}

@media screen and (max-width: 991px) {
  .carousel-item {
    height: 600px;
  }
  .carousel-item img {
    height: 600px;
  }
  .carousel-caption h1 {
    font-size: 2rem;
  }

  .carousel-caption h4 {
    font-size: 1.6rem;
  }
}

@media screen and (max-width: 780px) {
  .carousel-item {
    height: 450px;
  }
  .carousel-item img {
    height: 450px;
  }
  .carousel-caption h1 {
    font-size: 1.6rem;
  }

  .carousel-caption h4 {
    font-size: 1.2rem;
  }
  .carousel-btn {
    font-size: 0.8rem;
  }
}

@media screen and (max-width: 780px) {
  .carousel-caption h1 {
    font-size: 1.2rem;
  }

  .carousel-caption h4 {
    font-size: 0.8rem;
  }
}

.features {
  margin-top: 5rem;
  width: 80%;
  min-height: 550px;
}
</style>