<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-6 col-md-12 grid-col-div">
        <!-- dynamic house info display start -->
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

          <!-- display text if no cover is selected -->
          <div class="house-cover-display" v-if="!displayData.cover">
            <p class="mt-3">House Cover</p>
          </div>

          <!-- house title & description -->
          <div class="card-body">
            <h4 class="card-title mt-2">{{ houseData.title ? houseData.title : "House Title" }}</h4>
            <p
              class="card-text mt-2 house-description-display"
              :class="{'text-left': houseData.description}"
            >{{ handleDescription(houseData.description) }}</p>
          </div>

          <!-- house suburb and price -->
          <div class="card-footer">
            <small class="text-muted">{{ houseData.suburb ? houseData.suburb : "Suburb" }}</small>
            <br />
            <small class="text-muted">${{ houseData.price ? houseData.price : "0" }}</small>
          </div>
        </div>
        <!-- dynamic house info display end -->
      </div>
      <div class="col-lg-6 col-md-12 grid-col-div">
        <!-- input title start -->
        <div class="row mt-2">
          <label class="input-label">Title:</label>
          <input type="text" class="form-control" placeholder="Title" v-model="houseData.title" />
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
            placeholder="House Description"
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
          <button class="my-btn form-control" @click="$refs.imagesInput.click()">Select Images</button>
        </div>
        <!-- input images end -->

        <!-- input suburb start -->
        <div class="row mt-2">
          <label class="input-label">Suburb:</label>
          <input type="text" class="form-control" placeholder="Suburb" v-model="houseData.suburb" />
        </div>
        <!-- input suburb end -->

        <!-- input price start -->
        <div class="row mt-2">
          <label class="input-label">Price:</label>
          <input
            type="text"
            class="form-control"
            placeholder="Price per night"
            v-model="houseData.price"
          />
        </div>
        <!-- input price end -->

        <!-- input size start -->
        <div class="row mt-2">
          <label class="input-label">
            Size (m
            <sup>2</sup>):
          </label>
          <input type="text" class="form-control" placeholder="Size" v-model="houseData.size" />
        </div>
        <!-- input size start -->
      </div>
    </div>
    <hr />
    <div class="row">
      <div class="col-lg-6 col-md-12 grid-col-div">
        <!-- input location start -->
        <div class="row mt-2">
          <label class="input-label">Location:</label>
          <input
            type="text"
            class="form-control"
            placeholder="Location (more detailed)"
            v-model="houseData.location"
          />
        </div>
        <!-- input location end -->

        <!-- input lat & lng start -->
        <div class="row mt-2">
          <label class="input-label">Google Map Location (Optional):</label>
          <input type="text" class="form-control" placeholder="Latitude" v-model="houseData.lat" />
          <input type="text" class="form-control" placeholder="Longitude" v-model="houseData.lng" />
        </div>
        <!-- input lat & lng end -->
      </div>
      <div class="col-lg-6 col-md-12 grid-col-div">
        <!-- input tenant number start -->
        <div class="row mt-2">
          <label class="input-label">Tenant Number:</label>
          <input
            type="text"
            class="form-control"
            placeholder="Tenant Number"
            v-model="houseData.tenant_num"
          />
        </div>
        <!-- input tenant number end -->

        <!-- input available facilities start -->
        <div class="row mt-2">
          <label class="input-label">Facility:</label>
          <div class="row w-100">
            <div class="col-6 m-auto text-left">
              <input type="checkbox" class="mx-2 mt-2" v-model="houseData.wifi" />
              <label for>
                <i class="fas fa-wifi facility-icon"></i>
                Wifi
              </label>
              <br />
              <input type="checkbox" class="mx-2" v-model="houseData.kitchen" />
              <label for>
                <i class="fas fa-utensils facility-icon"></i>
                Kitchen
              </label>
            </div>
            <div class="col-6 m-auto text-left">
              <input type="checkbox" class="mx-2" v-model="houseData.carpark" />
              <label for>
                <i class="fas fa-car facility-icon"></i>
                Car Park
              </label>
              <br />
              <input type="checkbox" class="mx-2" v-model="houseData.ac" />
              <label for>
                <i class="far fa-snowflake facility-icon"></i>
                Air Conditioning
              </label>
            </div>
          </div>
        </div>
        <!-- input available facilities end -->
      </div>
    </div>

    <!-- upload button -->
    <div class="row w-50 mx-auto mt-4">
      <button class="my-btn form-control" @click="uploadHouse">Upload House</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "uploadHouse",
  components: {},
  data() {
    return {
      displayData: {},
      houseData: {
        "title": "",
        "cover": "",
        "images": "",
        "description": "",
        "provider": "",
        "suburb": "",
        "location": "",
        "price": "",
        "size": "",
        "tenant_num": "",
        "wifi": false,
        "kitchen": false,
        "carpark": false,
        "ac": false,
        "lat": "",
        "lng": "",
      }
    };
  },
  methods: {
    selectCover(event) {
      window.console.log(event.target.files[0]);
      // when a cover is selected, assign it to displayData to show in house card
      if (event.target.files[0]) {
        this.houseData.cover = event.target.files[0];
        this.displayData.cover = URL.createObjectURL(this.houseData.cover);
        this.$forceUpdate();
      }
    },
    selectImages(event) {
      // need to select cover first (to display the carousel correctly)
      if (!this.displayData.cover) {
        this.$swal("Warning", "Please select cover first!", "warning");
        return;
      }

      // if there are images selected, assign them to display data's images
      if (Array.from(event.target.files)) {
        this.houseData.images = Array.from(event.target.files);
        window.console.log(this.houseData.images);

        this.displayData.images = [];
        for (let key in this.houseData.images) {
          this.displayData.images.push(
            URL.createObjectURL(this.houseData.images[key])
          );
        }
        this.$forceUpdate();
      }
    },

    // only display the first 150 characters of description
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

    // get url of image from imgBB API
    async imageToUrl(imageFile) {
      let KEY = "587e7ebff1f6ee9c2fc6501859d37864";
      let HOST = "https://api.imgbb.com/1/upload?key=" + KEY;
      let formData = new FormData();
      formData.append("image", imageFile);
      return await this.$axios.post(HOST, formData);
    },

    // upload house operation
    async uploadHouse() {
      // check if all required inputs are filled in
      for (let key in this.houseData) {
        if (key !== "lat" && key !== "lng") {
          if (this.houseData[key] === "") {
            window.console.log(key + " is empty!");
            this.$swal("Warning", key + " is empty!", "warning");
            return;
          }
        }
      }
      // get cover url
      let res = await this.imageToUrl(this.houseData.cover);
      this.houseData.cover = res.data.data.url;
      // get images urls
      let imageUrls = [];
      for (let idx in this.houseData.images) {
        let res = await this.imageToUrl(this.houseData.images[idx]);
        imageUrls.push(res.data.data.url);
      }
      this.houseData.images = imageUrls;
      window.console.log(this.houseData);

      // send uplaod request to backend
      this.$axios
        .post("/api/houses/", this.houseData)
        .then(response => {
          if (response.status == 201) {
            window.console.log("uploaded!");
            this.$swal("Success!", "House is uploaded!", "success");
            this.$router.push({ name: "myHouses" });
          }
        })
        .catch(err => {
          window.console.log(err.response.data);
        });
    }
  },

  created() {
    window.console.log("state.isProvider: " + this.$store.getters.isProvider);
    // only show this page to provider
    if (this.$store.getters.isProvider) {
      window.console.log("current user is provider.");
      this.houseData.provider = this.$store.getters.getUserId;
    } else {
      window.console.log("Require provider login!");
      this.$router.push({ name: "home" });
    }
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

.facility-icon {
  font-size: 1.25rem;
}
</style>