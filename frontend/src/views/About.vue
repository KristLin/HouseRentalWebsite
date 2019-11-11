<template>
  <div>
    <div class="container">
      <div>
        <h1 style="margin-top: 30px; margin-bottom:30px">Let's get started.</h1>
        <h5 style="margin-bottom:30px">What do we offer?</h5>
      </div>
      <div class="row">
        <!-- tenant intro -->
        <div class="col-lg-6 col-sm-12" style="margin-top:20px">
          <div class="card mx-auto shadow" style="width:85%">
            <div class="card-header" style="background-color: black; color: #fff; font-size:1.5rem;"><b>I am a tenant.</b></div>
            <div class="card-body">
              <h4 class="mb-4"  style="color: #3c9d9b"><b>I can..</b></h4>
              <ul class="list-group">
                <li class="list-group-item"><b>Search houses with planty of options</b></li>
                <li class="list-group-item"><b>View houses on Google Map</b></li>
                <li class="list-group-item"><b>Save houses to my list</b></li>
                <li class="list-group-item"><b>Comment and rate houses</b></li>
              </ul>
            </div>
          </div>
        </div>

        <!-- provider intro -->
        <div class="col-lg-6 col-sm-12" style="margin-top:20px">
          <div class="card mx-auto shadow" style="width:85%">
            <div class="card-header" style="background-color: black; color: #fff; font-size:1.5rem;"><b>I am a provider.</b></div>
            <div class="card-body">
              <h4 class="mb-4"  style="color: #3c9d9b"><b>I can..</b></h4>
              <ul class="list-group">
                <li class="list-group-item"><b>Advertise my house</b></li>
                <li class="list-group-item"><b>Plot my house in Google Map</b></li>
                <li class="list-group-item"><b>Manage my house list</b></li>
                <li class="list-group-item"><b>View house comments and ratings</b></li>
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