<template>
  <div class="container">
    <!-- row start -->
    <div class="row">
      <!-- house info display start -->
      <div class="col-lg-5 col-md-5 my-auto">
        <div class="card h-100">
          <img
            class="card-img-top house-cover-display"
            v-if="houseData.cover"
            :src="houseData.cover"
            alt="house-cover"
          />
          <div class="house-cover-display" v-if="!houseData.cover">
            <p class="mt-3">House Cover</p>
          </div>
          <div class="card-body">
            <h4 class="card-title mt-2">{{ houseData.title ? houseData.title : "House Title" }}</h4>
            <p
              class="card-text mt-2 house-description-display"
              :class="{'text-left': houseData.description}"
            >{{ handleDescription(houseData.description) }}</p>
          </div>
          <div class="card-footer">
            <small class="text-muted">{{ houseData.suburb ? houseData.suburb : "Suburb" }}</small>
            <br />
            <small class="text-muted">${{ houseData.price ? houseData.price : "0" }}</small>
          </div>
        </div>
      </div>
      <!-- house info display end -->

      <!-- spacing start -->
      <div class="col-lg-1 col-md-1"></div>
      <!-- spacing end -->

      <!-- input part start -->
      <div class="col-lg-6 col-md-6">
        <!-- input title start -->
        <div class="row mt-2">
          <label class="input-label">Title:</label>
          <input type="text" class="form-control" placeholder="Title" v-model="houseData.title" />
        </div>
        <!-- input title end -->

        <!-- input cover start -->
        <div class="row mt-2">
          <label class="input-label">Cover Url:</label>
          <input type="text" class="form-control" placeholder="Cover Url" v-model="houseData.cover" />
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
          <label class="input-label">Image Urls (Please separate Urls with return):</label>
          <textarea
            cols="30"
            rows="3"
            class="form-control"
            placeholder="Image Urls"
            v-model="houseData.images"
          ></textarea>
        </div>
        <!-- input images end -->

        <!-- input suburb start -->
        <div class="row mt-2">
          <label class="input-label">Suburb:</label>
          <input type="text" class="form-control" placeholder="Suburb" v-model="houseData.suburb" />
        </div>
        <!-- input title end -->

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
        <div class="row my-4">
          <label class="input-label">Upload House:</label>
          <button class="my-btn form-control" @click="uploadHouse">Upload House</button>
        </div>
        <!-- input title end -->
      </div>
      <!-- input part end -->
    </div>
    <!-- row end -->

    <!-- inputs with file picker -->
    <!-- <div class="row">
      <div class="col-lg-3 col-md-6 form-group">
        <label class="filter-label">Title:</label>
        <input type="text" class="form-control" placeholder="Title" v-model="houseData.title" />
      </div>
      <div class="col-lg-3 col-md-6 form-group">
        <label class="filter-label">Description:</label>
        <textarea
          type="text"
          class="form-control"
          placeholder="Description"
          v-model="houseData.description"
        />
      </div>
      <div class="col-lg-3 col-md-6 form-group">
        <label class="filter-label">Cover:</label>
        <input
          type="file"
          class="form-control"
          placeholder="Cover Url"
          @change="uploadCover"
          accept="image/png, image/jpeg, image/jpg"
        />
      </div>
      <div class="col-lg-3 col-md-6 form-group">
        <label class="filter-label">Images:</label>
        <input
          type="file"
          class="form-control"
          placeholder="Image Url"
          @change="uploadImages"
          accept="image/png, image/jpeg, image/jpg"
          multiple
        />
      </div>
    </div>
    <div class="row">
      <div class="col-lg-3 col-md-6 form-group">
        <label class="filter-label">Suburb:</label>
        <input type="text" class="form-control" placeholder="Suburb" v-model="houseData.suburb" />
      </div>
      <div class="col-lg-3 col-md-6 form-group">
        <label class="filter-label">Price per night:</label>
        <input type="text" class="form-control" placeholder="Price" v-model="houseData.price" />
      </div>

      <div class="col-lg-3 col-md-6 form-group">
        <label class="filter-label">Provider ID:</label>
        <input
          type="text"
          class="form-control"
          placeholder="Provider ID"
          v-model="houseData.provider"
        />
      </div>
      <div class="col-lg-3 col-md-6 orm-group">
        <label class="filter-label">Upload House:</label>
        <button class="btn btn-dark form-control" @click="uploadHouse">Upload House</button>
      </div>
    </div>-->
  </div>
</template>

<script>
export default {
  name: "login",
  components: {},
  data() {
    return {
      houseData: {
        title: "",
        cover: "",
        description: "",
        price: "",
        images: []
      }
    };
  },
  methods: {
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
    uploadCover(event) {
      this.houseData.cover = event.target.files[0];
      window.console.log(this.houseData.cover);
    },
    uploadImages(event) {
      this.houseData.images = event.target.files;
      //   window.console.log(this.houseData.images[0]);
    },
    uploadHouse() {
      // convert imageUrls from text to list
      this.houseData.images = this.parseImagesUrls(this.houseData.images);
      // window.console.log(this.houseData);

      // upload images in url form to backend
      this.$axios
        .post("/api/houses/", this.houseData)
        .then(response => {
          // JSON responses are automatically parsed.
          if (response.status == 200) {
            window.console.log("uploaded!");
          }
        })
        .catch(err => {
          window.console.log(err.response);
        });

      // upload images in file form to backend (failed)
      // let formData = new FormData();
      // formData.append("title", this.houseData.title);
      // formData.append("description", this.houseData.description);
      // formData.append("cover", this.houseData.cover);
      // formData.append("images", this.houseData.images);
      // formData.append("suburb", this.houseData.suburb);
      // formData.append("price", this.houseData.price);
      // formData.append("provider", this.houseData.provider);
      // let config = {
      //   headers: { "Content-Type": "multipart/form-data" }
      // };
      // this.$axios
      //   .post("/api/houses/", formData, config)
      //   .then(response => {
      //     // JSON responses are automatically parsed.
      //     if (response.status == 200) {
      //       window.console.log("uploaded!");
      //     }
      //   })
      //   .catch(err => {
      //     window.console.log(err.response);
      //   });
    },
    parseImagesUrls(imagesUrlText) {
      let imageUrls = imagesUrlText.split("\n");
      return imageUrls;
    }
  }
};
</script>

<style scoped>
.container {
  padding-top: 2rem;
  min-height: 500px;
}

.house-cover-display {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.card-body {
  padding: 1rem;
}

.house-description-display {
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
</style>