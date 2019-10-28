<template>
  <div class="container">
    <div class="row">
      <!-- house info display start -->
      <div class="col-lg-6 col-md-12 grid-col-div">
        <div class="row card house-display-card">
          <div
            id="carouselExampleIndicators"
            class="carousel slide"
            data-ride="carousel"
            v-if="displayData.cover"
          >
            <ol class="carousel-indicators active">
              <!-- cover image -->
              <li data-target="#carouselExampleIndicators" data-slide-to="0"></li>
              <!-- other images -->
              <li
                data-target="#carouselExampleIndicators"
                :key="idx"
                v-for="(index, idx) in displayData.images"
                :data-slide-to="idx+1"
              ></li>
            </ol>
            <div class="carousel-inner">
              <div class="carousel-item active">
                <img class="card-img-top house-cover-display" :src="displayData.cover" />
              </div>
              <div class="carousel-item" :key="idx" v-for="(index, idx) in displayData.images">
                <img class="card-img-top house-cover-display" :src="displayData.images[idx]" />
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

          <div class="house-cover-display" v-if="!displayData.cover">
            <p class="mt-3">House Cover</p>
          </div>
          <div class="card-body">
            <h4 class="card-title mt-2">{{ displayData.title ? displayData.title : "House Title" }}</h4>
            <p
              class="card-text mt-2 house-description-display"
              :class="{'text-left': displayData.description}"
            >{{ handleDescription(displayData.description) }}</p>
          </div>
          <div class="card-footer">
            <small class="text-muted">{{ displayData.suburb ? displayData.suburb : "Suburb" }}</small>
            <br />
            <small class="text-muted">${{ displayData.price ? displayData.price : "0" }}</small>
          </div>
        </div>
      </div>
      <!-- house info display end -->

      <div class="col-lg-6 col-md-12 grid-col-div">
        <!-- input title start -->
        <div class="row mt-2">
          <label class="input-label">Title:</label>
          <input
            type="text"
            class="form-control"
            :placeholder="displayData.title"
            v-model="houseData.title"
          />
        </div>
        <!-- input title end -->

        <!-- input cover start -->
        <div class="row mt-2">
          <input
            type="file"
            style="display: none"
            accept=".png, .jpg, .jpeg"
            ref="coverInput"
            @change="selectCover"
          />
          <button class="my-btn form-control" @click="$refs.coverInput.click()">Select Cover</button>
        </div>
        <!-- input cover end -->

        <!-- input description start -->
        <div class="row mt-2">
          <label class="input-label">Description:</label>
          <textarea
            cols="30"
            rows="8"
            class="form-control"
            :placeholder="displayData.description"
            v-model="houseData.description"
          ></textarea>
        </div>
        <!-- input description end -->

        <!-- input images start -->
        <div class="row mt-2">
          <input
            type="file"
            style="display: none"
            accept=".png, .jpg, .jpeg"
            ref="imagesInput"
            @change="selectImages"
            multiple
          />
          <button class="btn btn-dark form-control" @click="$refs.imagesInput.click()">Select Images</button>
        </div>
        <!-- input images end -->

        <!-- input suburb start -->
        <div class="row mt-2">
          <label class="input-label">Suburb:</label>
          <input
            type="text"
            class="form-control"
            :placeholder="displayData.suburb"
            v-model="houseData.suburb"
          />
        </div>
        <!-- input title end -->

        <!-- input price start -->
        <div class="row mt-2">
          <label class="input-label">Price:</label>
          <input
            type="text"
            class="form-control"
            :placeholder="displayData.price"
            v-model="houseData.price"
          />
        </div>
        <div class="row mt-2">
          <label class="input-label">
            Size (m
            <sup>2</sup>):
          </label>
          <input
            type="text"
            class="form-control"
            :placeholder="displayData.size"
            v-model="houseData.size"
          />
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-lg-6 col-md-12 grid-col-div">
        <div class="row mt-2">
          <label class="input-label">Location:</label>
          <input
            type="text"
            class="form-control"
            :placeholder="displayData.location"
            v-model="houseData.location"
          />
        </div>
        <div class="row mt-2">
          <label class="input-label">Google Map Location:</label>
          <input
            type="text"
            class="form-control"
            :placeholder="displayData.lat"
            v-model="houseData.lat"
          />
          <input
            type="text"
            class="form-control"
            :placeholder="displayData.lng"
            v-model="houseData.lng"
          />
        </div>
      </div>
      <div class="col-lg-6 col-md-12 grid-col-div">
        <div class="row mt-2">
          <label class="input-label">Tenant Number:</label>
          <input
            type="text"
            class="form-control"
            placeholder="Tenant Number"
            v-model="houseData.tenant_num"
          />
        </div>
        <div class="row mt-2">
          <label class="input-label">Conditions:</label>
          <div class="row w-100">
            <div class="col-6 m-auto text-left">
              <input type="checkbox" class="mx-2 mt-2" v-model="houseData.has_wifi" />
              <label for>
                <i class="fas fa-wifi condition-icon"></i>
                Has Wifi
              </label>
              <br />
              <input type="checkbox" class="mx-2" v-model="houseData.party_allowed" />
              <label for>
                <i class="fas fa-glass-cheers condition-icon"></i>
                Allow Party
              </label>
            </div>
            <div class="col-6 m-auto text-left">
              <input type="checkbox" class="mx-2" v-model="houseData.pet_allowed" />
              <label for>
                <i class="fas fa-dog condition-icon"></i>
                Allow Pet
              </label>
              <br />
              <input type="checkbox" class="mx-2" v-model="houseData.smoke_allowed" />
              <label for>
                <i class="fas fa-smoking condition-icon"></i>
                Allow Smoke
              </label>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row w-50 mx-auto mt-4">
      <button class="btn btn-dark form-control" @click="updateHouse">Update House</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "updateHouse",
  components: {},
  data() {
    return {
      houseId: this.$route.query.houseId,
      displayData: {},
      houseData: {}
    };
  },
  methods: {
    selectCover(event) {
      if (event.target.files[0]) {
        window.console.log(event.target.files[0]);
        this.houseData.cover = event.target.files[0];
        this.displayData.cover = URL.createObjectURL(this.houseData.cover);
        this.$forceUpdate();
      }
    },
    selectImages(event) {
      if (!this.displayData.cover) {
        alert("Please select cover first!");
        return;
      }
      if (Array.from(event.target.files)) {
        this.houseData.images = Array.from(event.target.files);

        this.displayData.images = [];
        for (let key in this.houseData.images) {
          this.displayData.images.push(
            URL.createObjectURL(this.houseData.images[key])
          );
        }
        this.$forceUpdate();
      }
    },
    handleDescription(description) {
      if (description) {
        return (
          description.substring(0, 150) +
          (description.length > 150 ? " ..." : "")
        );
      } else {
        return "House Description";
      }
    },
    async imageToUrl(imageFile) {
      let KEY = "587e7ebff1f6ee9c2fc6501859d37864";
      let HOST = "https://api.imgbb.com/1/upload?key=" + KEY;
      let formData = new FormData();
      formData.append("image", imageFile);
      return await this.$axios.post(HOST, formData);
    },
    async updateHouse() {
      let validData = 0;
      window.console.log(this.houseData);
      for (let key in this.houseData) {
        if (this.houseData[key] !== null && this.houseData[key] !== "") {
          if (this.houseData[key] !== this.displayData[key]) {
            validData += 1;
          }
        }
      }
      if (validData === 0) {
        alert("Nothing to update");
        return;
      }

      if (this.houseData.cover !== null && this.houseData.cover !== undefined) {
        // get cover url
        let res = await this.imageToUrl(this.houseData.cover);
        this.houseData.cover = res.data.data.url;
      }

      if (
        this.houseData.images !== null &&
        this.houseData.images !== undefined
      ) {
        // get images urls
        let imageUrls = [];
        for (let idx in this.houseData.images) {
          let res = await this.imageToUrl(this.houseData.images[idx]);
          imageUrls.push(res.data.data.url);
        }
        this.houseData.images = imageUrls;
      }

      this.$axios
        .patch(
          "/api/houses/" +
            this.$store.getters.getUserId +
            "/" +
            this.displayData._id,
          this.houseData
        )
        .then(response => {
          // JSON responses are automatically parsed.
          if (response.status == 200) {
            window.console.log("House is updated!");
            alert("House is updated!");
            this.$router.push({ name: "myHouses" });
          }
        })
        .catch(err => {
          window.console.log(err.response);
        });
    }
  },
  created() {
    this.$axios
      .get("/api/houses/" + this.$route.query.houseId)
      .then(response => {
        // JSON responses are automatically parsed.
        this.displayData = response.data;

        if (this.$store.getters.getUserId !== this.displayData.provider) {
          window.console.log("current user is not the provider.");
          alert("current user is not the provider.");
          this.$router.push({ name: "myHouses" });
        }
        this.houseData.has_wifi = this.displayData.has_wifi;
        this.houseData.party_allowed = this.displayData.party_allowed;
        this.houseData.pet_allowed = this.displayData.pet_allowed;
        this.houseData.smoke_allowed = this.displayData.smoke_allowed;
      })
      .catch(err => {
        window.console.log(err.response);
      });
    // house = this.$axios
    //   .get("/api/houses/" + this.houseId)
    //   .then(res => window.console.log(res))
    //   .catch(err => window.console.log(err));
  }
};
</script>

<style scoped>
.container {
  padding-top: 2rem;
  min-height: 500px;
  margin-top: 100px;
  margin-bottom: 80px;
}

.grid-col-div {
  padding-left: 40px;
  padding-right: 40px;
}

.house-display-card {
  margin-top: 15%;
}

@media screen and (max-width: 991px) {
  .house-display-card {
    margin-top: 0;
  }
}

.house-cover-display {
  width: 100%;
  height: 250px;
  object-fit: cover;
}

.card-body {
  padding: 1rem;
}

.house-description-display {
  padding-top: 1rem;
  padding-left: 2rem;
  padding-right: 2rem;
  word-wrap: break-word;
  min-height: 100px;
}

.input-label {
  font-size: 14px;
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
  font-size: 1.25rem;
}
</style>