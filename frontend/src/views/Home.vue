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
          <div
            class="carousel-item"
            :class="{active: idx===0}"
            :key="idx"
            v-for="(item, idx) in carouselItems"
          >
            <img width="100%" height="100%" :src="item.imageSrc" />
            <div class="container">
              <div class="carousel-caption" :class="{'text-left': idx===0,'text-right':idx===2}">
                <h1>
                  <strong>{{ item.title }}</strong>
                </h1>
                <h4>{{ item.description }}</h4>
                <button
                  class="btn btn-lg carousel-btn my-4"
                  type="button"
                  @click="item.buttonClickFunction"
                >{{ item.buttonText }}</button>
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
        <div class="text-center">
          <h2 class="font-weight-bold my-4">Why is it so great?</h2>
          <p class="lead mx-auto" style="margin-bottom: 70px">We offer you best user experience.</p>
          <div class="row">
            <div class="col-lg-4 col-md-4 col-sm-12" :key="idx" v-for="(item, idx) in featureItems">
              <i class="fas feature-icon mb-4" :class="item.icon"></i>
              <h4 class="font-weight-bold mb-4">{{ item.title }}</h4>
              <p class="grey-text mb-md-0" style="margin-bottom: 2rem">{{ item.description}}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

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
          title: "Explore with us.",
          description: "Find your dreaming house in an easy way.",
          imageSrc: require("@/assets/homepage_carousel_images/1.jpg"),
          buttonText: "Search",
          buttonClickFunction: () => {
            this.$router.push({
              name: "search"
            });
          }
        },
        {
          title: "Join us.",
          description: "Join us with thousands of users.",
          imageSrc: require("@/assets/homepage_carousel_images/3.jpg"),
          buttonText: "Sign up here",
          buttonClickFunction: () => {
            this.$router.push({
              name: "signup"
            });
          }
        },
        {
          title: "Welcome to Bomb Shrimp",
          description: "What are we and what do we offer?",
          imageSrc: require("@/assets/homepage_carousel_images/2.jpg"),
          buttonText: "About us",
          buttonClickFunction: () => {
            this.$router.push({
              name: "about"
            });
          }
        }
      ],
      featureItems: [
        {
          title: "Search Engine",
          description: "Search the houses in the way you like, even in map.",
          icon: "fa-search"
        },
        {
          title: "Save Money",
          description: "We offer price worthy renting houses.",
          icon: "fa-money-bill-alt"
        },
        {
          title: "Reviews & Ratings",
          description: "Share your review and rating with others.",
          icon: "fa-comments"
        }
      ]
    };
  },

  methods: {}
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
  margin-top: 5rem;
  margin-bottom: 8rem;
}

.feature-icon {
  font-size: 4rem;
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

  .feature-icon {
    font-size: 3rem;
  }
}

@media screen and (max-width: 767px) {
  .features {
    margin-bottom: 4rem;
  }
}
</style>