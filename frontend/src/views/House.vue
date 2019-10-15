<template>
  <!-- Page Content -->
  <div class="container">
    <div class="row">
      <div class="col-lg-3">
        <div class="list-group my-4 sidebar">
          <a href="#intro" class="list-group-item active">Intro</a>
          <a href="#description" class="list-group-item">Description</a>
          <a href="#facility" class="list-group-item">Facility</a>
          <a href="#review" class="list-group-item">Review</a>
        </div>
      </div>
      <!-- /.col-lg-3 -->

      <div class="col-lg-9">
        <div id="intro" class="card mt-4">
          <img class="card-img-top img-fluid" :src="house.cover" alt="house cover" />
          <div class="card-body">
            <h3 class="card-title text-left">{{ house.title }}</h3>
            <h6 class="text-left">${{house.price}} per night</h6>
            <span class="text-warning">&#9733; &#9733; &#9733; &#9733; &#9734;</span>
            4.0 stars
          </div>
        </div>
        <!-- /.card -->

        <div id="description" class="card card-outline-secondary my-4">
          <div class="card-header">House Description</div>
          <div class="card-body">
            <p class="text-left">{{ house.description }}</p>
          </div>
        </div>

        <div id="facility" class="card card-outline-secondary my-4">
          <div class="card-header">House Facility</div>
          <div class="card-body">
            <p>something</p>
          </div>
        </div>

        <div id="review" class="card card-outline-secondary my-4">
          <div class="card-header">House Reviews</div>
          <div class="card-body">
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Omnis et enim aperiam inventore, similique necessitatibus neque non! Doloribus, modi sapiente laboriosam aperiam fugiat laborum. Sequi mollitia, necessitatibus quae sint natus.</p>
            <small class="text-muted">Posted by Anonymous on 3/1/17</small>
            <hr />
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Omnis et enim aperiam inventore, similique necessitatibus neque non! Doloribus, modi sapiente laboriosam aperiam fugiat laborum. Sequi mollitia, necessitatibus quae sint natus.</p>
            <small class="text-muted">Posted by Anonymous on 3/1/17</small>
            <hr />
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Omnis et enim aperiam inventore, similique necessitatibus neque non! Doloribus, modi sapiente laboriosam aperiam fugiat laborum. Sequi mollitia, necessitatibus quae sint natus.</p>
            <small class="text-muted">Posted by Anonymous on 3/1/17</small>
            <hr />
            <a href="#" class="btn btn-success">Leave a Review</a>
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
export default {
  name: "House",
  props: {},
  data() {
    return {
      houseId: this.$route.query.houseId,
      house: this.$route.params.house
    };
  },
  // check if the params are lost
  components: {},
  beforeRouteEnter: (to, from, next) => {
    // if the params is empty, call the backend to get the house data.
    if (Object.keys(to.params).length === 0) {
      to.params.house = {
        _id: 1,
        title: "Title 1",
        description:
          "Aliquam mi massa, finibus ut elementum sed, tincidunt ac erat. Sed sagittis consectetur velit at tempor. In non tempor diam, eget pretium purus. Aliquam vel dictum odio, et cursus urna. Fusce convallis sapien dui, blandit convallis enim malesuada aliquam. Maecenas vestibulum tortor ac odio fringilla, in feugiat risus pretium. Donec iaculis eros at bibendum sollicitudin. Proin ultrices est tristique finibus ullamcorper. Pellentesque eleifend, dolor nec viverra luctus, mauris massa maximus libero, quis feugiat dolor diam a dui. Ut pharetra, dui sit amet condimentum mattis, metus ipsum eleifend lorem, vitae varius velit risus nec ipsum. Maecenas vehicula vulputate urna ut pulvinar. Aliquam erat volutpat. Praesent sapien sapien, fringilla sit amet placerat et, gravida interdum nunc. Nullam id tincidunt augue, quis porttitor risus.",
        cover: "/house_images/1.jpg",
        suburb: "Zetland",
        price: "200"
      };
      // house = this.$axios
      //   .get("/api/houses/" + this.houseId)
      //   .then(res => window.console.log(res))
      //   .catch(err => window.console.log(err));
    }
    next();
  }
};
</script>

<style>
.sidebar {
  position: fixed;
  width: 20%;
}
@media screen and (max-width: 991px) {
  .sidebar {
    display: none;
  }
}
</style>
