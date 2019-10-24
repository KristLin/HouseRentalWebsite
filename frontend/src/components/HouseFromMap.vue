<template>
  <!-- Page Content -->
  <div>
    <div id="house-display" v-if="house">
      <div id="intro" class="card">
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
              v-for="(index, idx) in house.images"
              :data-slide-to="idx+1"
            ></li>
          </ol>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img class="card-img-top house-cover-display" :src="house.cover" />
            </div>
            <div class="carousel-item" :key="idx" v-for="(index, idx) in house.images">
              <img class="card-img-top house-cover-display" :src="house.images[idx]" />
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
        <div class="house-cover-display" v-if="!house.cover">
          <p class>House Cover</p>
        </div>
        <div class="card-body">
          <h3 class="card-title text-left">{{ house.title }}</h3>
          <h6 class="text-left">${{house.price}} per night</h6>
          <span class="text-warning">&#9733; &#9733; &#9733; &#9733; &#9734;</span>
          4.0 stars
        </div>
      </div>
      <div id="learnMore" class="card card-outline-secondary my-2">
        <button class="my-btn form-control" @click="goToHousePage">More Info</button>
      </div>
      <!-- /.card -->
      <div id="description" class="card card-outline-secondary my-2">
        <div class="card-header">House Description</div>
        <div class="card-body">
          <p class="text-left">{{ house.description }}</p>
        </div>
      </div>

      <div id="facility" class="card card-outline-secondary my-2">
        <div class="card-header">House Facility</div>
        <div class="card-body">
          <p>something</p>
        </div>
      </div>
    </div>
    <div class="house-display-hint" v-if="!house">
      <p>Click marker in the map to see house detail.</p>
    </div>
  </div>

  <!-- /.container -->
</template>

<script>
export default {
  name: "HouseFromMap",
  props: {
    house: {}
  },
  // check if the params are lost
  methods: {
    goToHousePage() {
      this.$router.push({
        name: "house",
        query: { houseId: this.house._id },
        params: { house: this.house }
      });
    }
  },
  components: {},
  created() {}
};
</script>

<style>
#house-display {
  max-height: 500px;
  overflow: auto;
}

#description {
  max-height: 400px;
  overflow: auto;
}

.card-img-top {
  width: 100%;
  height: 300px;
  object-fit: cover;
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

.house-display-hint {
  margin-top: 100px;
  margin-bottom: 100px;
}
</style>
