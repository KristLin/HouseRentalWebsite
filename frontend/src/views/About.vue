<template>
  <div>
    <div class="container">
      <div>
        <h1 style="margin-top: 30px; margin-bottom:30px">Let's get started.</h1>
        <h5 style="margin-bottom:30px">What do we offer?</h5>
      </div>
      <div class="row">
        <div class="col-lg-6 col-sm-12" style="margin-top:20px">
          <div class="card mx-auto" style="width:85%">
            <div class="card-header" style="background-color: #3c9d9b; color: #fff; font-size:1.5rem;">I am a tenant.</div>
            <div class="card-body">
              <h4 class="mb-4">I can..</h4>
              <ul class="list-group">
                <li class="list-group-item">Search houses with planty of options</li>
                <li class="list-group-item">View houses on Google Map</li>
                <li class="list-group-item">Save houses to my list</li>
                <li class="list-group-item">Comment and rate houses</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="col-lg-6 col-sm-12" style="margin-top:20px">
          <div class="card mx-auto" style="width:85%">
            <div class="card-header" style="background-color: #3c9d9b; color: #fff; font-size:1.5rem;">I am a provider.</div>
            <div class="card-body">
              <h4 class="mb-4">I can..</h4>
              <ul class="list-group">
                <li class="list-group-item">Advertise my house</li>
                <li class="list-group-item">Plot my house in Google Map</li>
                <li class="list-group-item">Manage my house list</li>
                <li class="list-group-item">View house comments and ratings</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "about",
  components: {}
};
</script>

<style scoped>
.container {
  padding-top: 2rem;
  min-height: 500px;
  margin-top: 100px;
  margin-bottom: 80px;
}

.jumbotron {
  padding-top: 0;
  padding-bottom: 0;
}
</style>