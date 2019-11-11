<template>
  <!-- Page Content -->
  <div class="container" v-if="house">
    <div class="row">
      <div class="col-lg-3">
        <!-- sidebar components: go back, navigation, save/remove to/from savelist, book house -->
        <div class="sidebar">
          <!-- go back button -->
          <button class="my-btn form-control my-2" @click="$router.go(-1)">
            <i class="fas fa-chevron-left"></i> Go Back
          </button>

          <!-- sidebar navigation -->
          <div class="collapse show" id="collapseExample">
            <ul class="list-group list-unstyled">
              <!-- the locator seems having an issue -->
              <!-- I put hidden anchor target locations below (not exact where content locates) -->
              <li class="list-group-item p-2">
                <a href="#intro">Intro</a>
              </li>
              <li class="list-group-item p-2">
                <a href="#description">Description</a>
              </li>
              <li class="list-group-item p-2">
                <a href="#facility">Facility</a>
              </li>
              <li class="list-group-item p-2">
                <a href="#recommendations">Recommendation</a>
              </li>
              <li class="list-group-item p-2">
                <a href="#review">Review</a>
              </li>
            </ul>
          </div>

          <!-- save to my list button -->
          <!-- only displayed when it is not saved in user's list -->
          <button
            class="my-btn form-control my-2"
            @click="saveToMyList"
            v-if="!isSaved"
          >Save To My List</button>

          <!-- remove from my list button -->
          <!-- only displayed when it is saved in user's list -->
          <button
            class="my-btn form-control my-2"
            @click="removeFromMyList"
            v-if="isSaved"
          >Remove from My List</button>

          <hr />

          <!-- select time to book button -->
          <button
            class="my-btn form-control mb-2"
            type="button"
            data-toggle="collapse"
            data-target="#collapseExample"
            aria-expanded="false"
            aria-controls="collapseExample"
          >Select Time to Book</button>

          <!-- when the select time button is clicked, the timepicker will show up -->
          <div class="collapse" id="collapseExample">
            <div class="card">
              <!-- check in & check out datepicker and book button -->
              <div class="card-body p-2">
                <!-- data type input, but it is not supported in safari browser -->
                <!-- <small>Check in</small> -->
                <!-- <input type="date" class="form-control" placeholder="yyyy-mm-dd" :min="today" v-model="checkIn" /> -->
                <!-- <input type="date" class="form-control" placeholder="yyyy-mm-dd" v-model="checkIn" /> -->
                <div id="datepicker-div" class="w-100">
                  <datepicker format="yyyy-MM-dd" placeholder="Check in Date" v-model="checkIn"></datepicker>
                </div>
                <!-- data type input, but it is not supported in safari browser -->
                <!-- <small>Check out</small> -->
                <!-- <input type="date" class="form-control" placeholder="yyyy-mm-dd" :min="today" v-model="checkOut" /> -->
                <!-- <input type="date" class="form-control" placeholder="yyyy-mm-dd" v-model="checkOut" /> -->
                <div id="datepicker-div" class="w-100">
                  <datepicker format="yyyy-MM-dd" placeholder="Check out Date" v-model="checkOut"></datepicker>
                </div>
                <!-- book button -->
                <button class="btn btn-warning form-control my-2" @click="bookThisHouse">Book</button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- /.col-lg-3 -->

      <div class="col-lg-9">
        <!-- house intro section -->
        <div id="intro" class="card mt-2">
          <div
            id="carouselExampleIndicators"
            class="carousel slide"
            data-ride="carousel"
            v-if="house.cover"
          >
          <!-- carousel indicators -->
            <ol class="carousel-indicators active">
              <li data-target="#carouselExampleIndicators" data-slide-to="0"></li>
              <li
                data-target="#carouselExampleIndicators"
                :key="idx"
                v-for="(image, idx) in house.images"
                :data-slide-to="idx+1"
              ></li>
            </ol>
            <!-- carousel images: house cover and house images -->
            <div class="carousel-inner">
              <div class="carousel-item active">
                <img class="card-img-top house-cover-display" :src="house.cover" />
              </div>
              <div class="carousel-item" :key="idx" v-for="(image, idx) in house.images">
                <img class="card-img-top house-cover-display" :src="image" />
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
            <!-- hidden anchor location -->
            <div id="description"></div>
          </div>

          <div class="card-body">
            <!-- house basic information: title, price, size, tenant number and location -->
            <h3 class="card-title text-left">{{ house.title }}</h3>
            <h6 class="text-left my-2">${{house.price}} per night</h6>
            <h6 class="text-left">
              {{house.tenant_num}}
              <i class="fas fa-user mr-4"></i>
              {{ house.size }} m
              <sup class="mr-4">2</sup>
              {{ house.suburb }}
            </h6>
            <h6 class="text-left">{{ house.location }}</h6>

            <!-- house rating and rating number-->
            <star-rating
              :inline="true"
              :rating="parseFloat(house.rating)"
              :read-only="true"
              :show-rating="false"
              v-bind:increment="0.01"
              v-bind:star-size="20"
              v-if="parseInt(house.rating_num) !== 0"
            ></star-rating>
            <span
              style="font-weight:bold;"
              class="mx-2"
              v-if="parseInt(house.rating_num) !== 0"
            >({{ house.rating_num }})</span>
            <p
              class="text-left mb-0"
              v-if="parseInt(house.rating_num) === 0"
            >This house has no rating yet.</p>
          </div>
        </div>

        <!-- house description section -->
        <div class="card card-outline-secondary my-4">
          <!-- hidden anchor location -->
          <div id="facility"></div>
          <div class="card-header">House Description</div>
          <div class="card-body">
            <p class="text-left">{{ house.description }}</p>
          </div>
        </div>

        <!-- Available facilities section -->
        <div class="card card-outline-secondary my-4">
          <!-- hidden anchor location -->
          <div id="recommendations"></div>
          <div class="card-header">House Facilities</div>
          <div class="card-body">
            <i class="fas fa-wifi house-page-facility-icon" v-if="house.wifi"></i>
            <i class="fas fa-utensils house-page-facility-icon" v-if="house.kitchen"></i>
            <i class="fas fa-car house-page-facility-icon" v-if="house.carpark"></i>
            <i class="fas fa-snowflake house-page-facility-icon" v-if="house.ac"></i>
          </div>
        </div>

        <!-- recommendations section -->
        <div class="card card-outline-secondary my-4">
          <!-- hidden anchor location -->
          <div id="review"></div>
          <div
            class="card-header p-2"
            style="background-color: #3c9d9b; color: white;"
          >Recommended Houses</div>
          <div class="card-body pt-1">
            <RecommendHouses
              :recommendInfo="{house_id: houseId, suburb: house.suburb, price: house.price, tenant_num: house.tenant_num}"
            />
          </div>
        </div>

        <!-- review section -->
        <div class="card card-outline-secondary my-4">
          <div class="card-header">House Reviews</div>
          <div class="card-body">
            <div class="comment" :key="idx" v-for="(comment, idx) in houseComments">
              <div class="text-left">{{ comment.content }}</div>
              <div class="text-right">
                <star-rating
                  :inline="true"
                  :rating="parseInt(comment.rating)"
                  :read-only="true"
                  text-class="rating-text"
                  v-bind:increment="0.01"
                  v-bind:star-size="20"
                ></star-rating>
              </div>

              <hr />
            </div>

            <!-- show review input and rating input if user is logged in -->
            <div class="post-comment" v-if="$store.getters.isLoggedIn">
              <textarea
                v-model="userComment"
                cols="30"
                rows="6"
                class="form-control my-2"
                placeholder="Review Content"
              ></textarea>
              <div class="rating-div w-100">
                <span class="text-muted mr-2 mb-2">Your Rating:</span>

                <star-rating
                  :inline="true"
                  text-class="rating-text"
                  v-bind:increment="1"
                  v-bind:star-size="20"
                  v-model="userRating"
                ></star-rating>
              </div>
              <button class="my-btn form-control my-4" @click="uploadReview">Leave a review</button>
            </div>

            <!-- if user is not logged in, show the login to review button -->
            <div class="login-to-comment" v-if="!$store.getters.isLoggedIn">
              <button
                class="my-btn form-control my-4"
                @click="$router.push('/login')"
              >Login to post review</button>
            </div>
          </div>
        </div>
        <!-- /.card -->
      </div>
      <!-- /.col-lg-9 -->
    </div>
  </div>
  <!-- /.container -->
</template>

<script>
import StarRating from "vue-star-rating";
import RecommendHouses from "@/components/RecommendHouses.vue";
import Datepicker from "vuejs-datepicker";

export default {
  name: "House",
  components: {
    StarRating,
    RecommendHouses,
    Datepicker
  },
  props: {
    houseFromMap: {}
  },
  data() {
    return {
      houseId: this.$route.query.houseId,
      house: this.$route.params.house,
      isSaved: false,
      houseComments: [],
      userComment: "",
      userRating: 5,
      checkIn: "",
      checkOut: "",
      today: new Date()
        .toLocaleString("en-AU")
        .substring(0, 10)
        .split("/")
        .reverse()
        .join("-")
    };
  },
  methods: {
    saveToMyList() {
      if (!this.$store.getters.isLoggedIn) {
        // if user is not logged in, ask if he/she want to go to the login page
        this.$swal({
          title: "Confirm",
          text: "Need login first. Do you want to go to the login page?",
          icon: "warning",
          buttons: true,
          dangerMode: true
        }).then(choice => {
          if (choice) {
            this.$router.push({ name: "login" });
          }
        });
      } else {
        // if user is already logged in send save house to savelist request to backend
        let user_id = this.$store.getters.getUserId;
        this.$axios
          .get("/api/savelists/" + user_id + "/add/" + this.house._id)
          .then(() => {
            this.isSaved = !this.isSaved;
            this.$swal("Success!", "House is saved to your list!", "success");
          })
          .catch(err => {
            window.console.log(err.response);
          });
      }
    },
    removeFromMyList() {
      if (!this.$store.getters.isLoggedIn) {
        // if user is not logged in, raise a alert
        this.$swal("Warning", "Please log in first!", "warning");
        this.$router.push({ name: "login" });
      } else {
        // if user is already logged in send remove house from savelist request to backend
        let user_id = this.$store.getters.getUserId;
        this.$axios
          .get("/api/savelists/" + user_id + "/remove/" + this.house._id)
          .then(() => {
            // JSON responses are automatically parsed.
            this.isSaved = !this.isSaved;
            this.$swal(
              "Success!",
              "House is removed from your list!",
              "success"
            );
          })
          .catch(err => {
            window.console.log(err.response);
          });
      }
    },
    bookThisHouse() {
      if (!this.$store.getters.isLoggedIn) {
        // if user is not logged in, ask if he/she want to go to the login page
        this.$swal({
          title: "Confirm",
          text: "Need login first. Do you want to go to the login page?",
          icon: "warning",
          buttons: true,
          dangerMode: true
        }).then(choice => {
          if (choice) {
            this.$router.push({ name: "login" });
          }
        });
      } else {
        // check if the check in and check out date are empty
        if (this.checkIn === "" || this.checkOut === "") {
          this.$swal({
            title: "Error",
            text: "You need to select your stay period!",
            icon: "error"
          });
          return;
        }

        let todayDate = new Date(this.today);
        let startDay = new Date(this.checkIn);
        let endDay = new Date(this.checkOut);

        // check if the check in date is before today
        if (startDay.getTime() - todayDate.getTime() < 0) {
          this.$swal({
            title: "Incorrect Check in Time",
            text: "Check in date is before today (" + this.today + ")",
            icon: "error"
          });
          return;
        }

        let millisecondsPerDay = 1000 * 60 * 60 * 24;
        let millisBetween = endDay.getTime() - startDay.getTime();
        let days = millisBetween / millisecondsPerDay;
        // check if the check out date is after check in date
        if (days <= 0) {
          this.$swal({
            title: "Incorrect Time Period",
            text: "Check out date is not after the check in date.",
            icon: "error"
          });
          return;
        }
        // show the book fee and wait for user to confirm
        this.$swal({
          title: "Confirm",
          text: "You need to pay $" + this.house.price * days + " to book it.",
          icon: "warning",
          buttons: ["Cancel", "Pay Now"],
          dangerMode: true
        }).then(choice => {
          if (choice) {
            // simulated processing
            this.$swal({
              title: "Processing...",
              text: "Please wait",
              icon: require("../../static/loading-small.gif"),
              buttons: false,
              closeOnClickOutside: false,
              timer: 3000
            }).then(() => {
              this.$swal("Success!", "You have booked the house!", "success");
            });
          }
        });
      }
    },
    uploadReview() {
      let user_id = this.$store.getters.getUserId;
      // send post comment request to backend
      this.$axios
        .get("/api/comments/add", {
          params: {
            house: this.house._id,
            user: user_id,
            content: this.userComment,
            rating: this.userRating
          }
        })
        .then(() => {
          // update house rating in frontend
          let house_rating_num = parseInt(this.house.rating_num);
          let total_rating = parseFloat(this.house.rating) * house_rating_num;
          window.console.log(
            "total and rating num:",
            total_rating,
            house_rating_num
          );
          this.house.rating_num = house_rating_num + 1;
          this.house.rating =
            (total_rating + parseFloat(this.userRating)) /
            this.house.rating_num;
          window.console.log(
            "after upload:",
            this.house.rating,
            this.house.rating_num
          );

          // push new comment to comment list
          this.houseComments.push({
            user: user_id,
            content: this.userComment,
            rating: this.userRating
          });

          // reset comment input
          this.userComment = "";
          this.userRating = 5;

          window.console.log("Review uploaded!");
          this.$swal("Success!", "You have uploaded the review!", "success");
        })
        .catch(error => {
          window.console.log(error.response.data);
        });
    }
  },
  created() {
    // if all route data are lost, go back to search page
    if (
      Object.keys(this.$route.params).length === 0 &&
      Object.keys(this.$route.query).length === 0 &&
      !this.houseFromMap
    ) {
      window.console.log("no house data to render");
      this.$router.push({ name: "search" });
    }

    // if the route params (house data) is lost
    // request backend for house data and house's comment data using house id in the route's query data
    let house_id = this.houseId ? this.houseId : this.house._id;
    window.console.log("House id:", house_id);
    // get comments data
    this.$axios
      .get("/api/comments/" + house_id)
      .then(response => {
        this.houseComments = response.data;

        // get isSaved data
        if (this.$store.getters.isLoggedIn) {
          let user_id = this.$store.getters.getUserId;
          this.$axios
            .get("/api/savelists/" + user_id + "/check/" + house_id)
            .then(response => {
              this.isSaved = response.data;
              // get house data
              if (this.houseFromMap) {
                // if the house is from the google map, get the data from this.houseFromMap
                this.house = this.houseFromMap;
              } else {
                if (Object.keys(this.$route.params).length === 0) {
                  this.$axios
                    .get("/api/houses/" + house_id)
                    .then(response => {
                      this.house = response.data;
                    })
                    .catch(err => {
                      window.console.log(err.response);
                    });
                }
              }
            })
            .catch(err => {
              window.console.log(err);
            });
        } else {
          // get house data
          if (this.houseFromMap) {
            // if the house is from the google map, get the data from this.houseFromMap
            this.house = this.houseFromMap;
          } else {
            if (Object.keys(this.$route.params).length === 0) {
              this.$axios
                .get("/api/houses/" + house_id)
                .then(response => {
                  this.house = response.data;
                })
                .catch(err => {
                  window.console.log(err.response);
                });
            }
          }
        }
      })
      .catch(error => {
        window.console.log(error.response);
      });
  },
  mounted() {}
};
</script>

<style>
.container {
  padding-top: 2rem;
  min-height: 500px;
  margin-top: 100px;
  margin-bottom: 80px;
}

.house-cover-display {
  width: 100%;
  height: 500px;
  object-fit: cover;
}

.sidebar {
  position: fixed;
  width: 20%;
  z-index: 2;
}

.list-group-item a {
  color: #3c9d9b;
}

@media screen and (min-width: 1040px) {
  .sidebar {
    width: 207px;
  }
}

@media screen and (max-width: 991px) {
  .sidebar ul {
    display: none;
  }
  .sidebar {
    margin: auto;
    position: relative;
    width: 100%;
  }
}

@media screen and (max-height: 500px) {
  .sidebar ul {
    display: none;
  }
}

.my-btn {
  border: none;
  background-color: black;
  color: white;
}

.my-btn:hover {
  border: none;
  background-color: #3c9d9b;
  color: white;
}

.house-page-facility-icon {
  font-size: 2rem;
  margin-left: 2rem;
  margin-right: 2rem;
}

@media screen and (max-width: 510px) {
  .house-page-facility-icon {
    font-size: 1.4rem;
    margin-left: 1.4rem;
    margin-right: 1.4rem;
  }
}

#datepicker-div input {
  padding: 5px;
  font-size: 15px;
  text-align: center;
  width: 100%;
}
</style>
