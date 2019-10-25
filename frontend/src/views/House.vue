<template>
  <!-- Page Content -->
  <div class="container" v-if="house">
    <div class="row">
      <div class="col-lg-3">
        <div class="sidebar">
          <button class="my-btn form-control my-2" @click="$router.go(-1)">
            <i class="fas fa-chevron-left"></i> Go Back
          </button>
          <hr />
          <ul class="list-group">
            <a href="#intro" class="list-group-item">Intro</a>
            <a href="#description" class="list-group-item">Description</a>
            <a href="#conditions" class="list-group-item">Condition</a>
            <a href="#review" class="list-group-item">Review</a>
          </ul>
          <hr />
          <button
            class="my-btn form-control my-2"
            @click="saveToMyList"
            v-if="!isSaved"
          >Save To My List</button>
          <button
            class="my-btn form-control my-2"
            @click="removeFromMyList"
            v-if="isSaved"
          >Remove from My List</button>
          <button class="my-btn form-control my-2" @click="bookThisHouse">Book This House</button>
        </div>
      </div>
      <!-- /.col-lg-3 -->

      <div class="col-lg-9">
        <div id="intro" class="card mt-2">
          <div
            id="carouselExampleIndicators"
            class="carousel slide"
            data-ride="carousel"
            v-if="house.cover"
          >
            <ol class="carousel-indicators active">
              <!-- cover image -->
              <li data-target="#carouselExampleIndicators" data-slide-to="0"></li>
              <!-- other images -->
              <li
                data-target="#carouselExampleIndicators"
                :key="idx"
                v-for="(image, idx) in house.images"
                :data-slide-to="idx+1"
              ></li>
            </ol>
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
          </div>

          <div class="card-body">
            <h3 class="card-title text-left">{{ house.title }}</h3>
            <h6 class="text-left">${{house.price}} per night</h6>
            <star-rating
              :inline="true"
              :rating="house.rating"
              :read-only="true"
              text-class="rating-text"
              v-bind:increment="0.01"
              v-bind:star-size="20"
              v-if="house.rating"
            ></star-rating>
            <p class="text-left" v-if="!house.rating">This house has not received any rating yet.</p>
          </div>
        </div>
        <!-- /.card -->

        <div id="description" class="card card-outline-secondary my-4">
          <div class="card-header">House Description</div>
          <div class="card-body">
            <p class="text-left">{{ house.description }}</p>
          </div>
        </div>

        <div id="conditions" class="card card-outline-secondary my-4">
          <div class="card-header">House Conditions</div>
          <div class="card-body">
            <i class="fas fa-wifi condition-icon" v-if="house.has_wifi"></i>
            <i class="fas fa-smoking condition-icon" v-if="house.smoke_allowed"></i>
            <i class="fas fa-glass-cheers condition-icon" v-if="house.party_allowed"></i>
            <i class="fas fa-dog condition-icon" v-if="house.pet_allowed"></i>
          </div>
        </div>

        <div id="review" class="card card-outline-secondary my-4">
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
            <button class="my-btn form-control my-4" @click="uploadReview">Leave a Review</button>
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

export default {
  name: "House",
  components: {
    StarRating
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
      userRating: 5
    };
  },
  methods: {
    saveToMyList() {
      if (!this.$store.getters.isLoggedIn) {
        alert("please login first!");
        this.$router.push({ name: "login" });
      } else {
        let user_id = this.$store.getters.getUserId;
        this.$axios
          .get("/api/savelists/" + user_id + "/add/" + this.house._id)
          .then(response => {
            // JSON responses are automatically parsed.
            this.isSaved = !this.isSaved;
            alert("house is saved to your list!");
            window.console.log("saving request result:" + response.data);
          })
          .catch(err => {
            window.console.log(err.response);
          });
      }
    },
    removeFromMyList() {
      if (!this.$store.getters.isLoggedIn) {
        alert("please login first!");
        this.$router.push({ name: "login" });
      } else {
        let user_id = this.$store.getters.getUserId;
        this.$axios
          .get("/api/savelists/" + user_id + "/remove/" + this.house._id)
          .then(response => {
            // JSON responses are automatically parsed.
            this.isSaved = !this.isSaved;
            alert("house is removed from your list!");
            window.console.log(response.data);
          })
          .catch(err => {
            window.console.log(err.response);
          });
      }
    },
    bookThisHouse() {
      if (!this.$store.getters.isLoggedIn) {
        alert("please login first!");
        this.$router.push({ name: "login" });
      } else {
        alert("booked! (test)");
      }
    },
    uploadReview() {
      let user_id = this.$store.getters.getUserId;
      this.$axios
        .get("/api/comments/add", {
          params: {
            house: this.house._id,
            user: user_id,
            content: this.userComment,
            rating: this.userRating
          }
        })
        .then(response => {
          window.console.log(response.data);
          alert("Review uploaded!");
        })
        .catch(error => {
          window.console.log(error.response.data);
          alert(error.response.data);
        });
    }
  },
  created() {
    // if the params is empty, call the backend to get the house data.
    if (this.houseFromMap) {
      this.house = this.houseFromMap;
      if (this.$store.getters.isLoggedIn) {
        let user_id = this.$store.getters.getUserId;
        this.$axios
          .get("/api/savelists/" + user_id + "/check/" + this.house._id)
          .then(response => {
            window.console.log(
              "house from map, fetch isSaved: ",
              response.data
            );
            this.isSaved = response.data;
            this.$axios
              .get("/api/comments/" + this.house._id)
              .then(response => {
                window.console.log(response);
                this.houseComments = response.data;
              })
              .catch(error => {
                window.console.log(error.response);
              });
          })
          .catch(err => {
            window.console.log(err);
          });
      }
    } else {
      if (Object.keys(this.$route.params).length === 0) {
        if (Object.keys(this.$route.query).length !== 0) {
          this.$axios
            .get("/api/houses/" + this.$route.query.houseId)
            .then(response => {
              // JSON responses are automatically parsed.
              this.house = response.data;

              if (this.$store.getters.isLoggedIn) {
                let user_id = this.$store.getters.getUserId;
                this.$axios
                  .get("/api/savelists/" + user_id + "/check/" + this.house._id)
                  .then(response => {
                    window.console.log(
                      "only query left, fetch isSaved: ",
                      response.data
                    );
                    this.isSaved = response.data;
                    window.console.log(this.house);
                    this.$axios
                      .get("/api/comments/" + this.house._id)
                      .then(response => {
                        window.console.log(response);
                        this.houseComments = response.data;
                      })
                      .catch(error => {
                        window.console.log(error.response);
                      });
                  })
                  .catch(err => {
                    window.console.log(err);
                  });
              }
            })
            .catch(err => {
              window.console.log(err.response);
            });
        } else {
          alert("no house data to render");
          this.$router.push({ name: "search" });
        }
      } else {
        if (this.$store.getters.isLoggedIn) {
          let user_id = this.$store.getters.getUserId;
          this.$axios
            .get("/api/savelists/" + user_id + "/check/" + this.house._id)
            .then(response => {
              window.console.log(
                "has router params, fetch isSaved: ",
                response.data
              );
              this.isSaved = response.data;
              this.$axios
                .get("/api/comments/" + this.house._id)
                .then(response => {
                  window.console.log(response);
                  this.houseComments = response.data;
                })
                .catch(error => {
                  window.console.log(error.response);
                });
            })
            .catch(err => {
              window.console.log(err);
            });
        }
      }
    }
  },
  mounted() {}
};
</script>

<style>
.container {
  padding-top: 2rem;
  min-height: 500px;
  margin-bottom: 80px;
}

.card-img-top {
  width: 100%;
  height: 350px;
  object-fit: cover;
}

.sidebar {
  position: fixed;
  width: 20%;
}

a.list-group-item {
  color: #3c9d9b;
}

@media screen and (max-width: 991px) {
  .sidebar {
    display: none;
  }
}
@media screen and (min-width: 1040px) {
  .sidebar {
    width: 207px;
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

.condition-icon {
  font-size: 2rem;
  margin-left: 2rem;
  margin-right: 2rem;
}

.rating-text {
  font-weight: bold;
  border: 1px solid #cfcfcf;
  padding-left: 10px;
  padding-right: 10px;
  border-radius: 5px;
  color: #999;
  background: #fff;
}
</style>
