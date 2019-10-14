<template>
  <div>
    <div class="card-group">
      <div class="card" v-bind:key="house._id" v-for="house in houses">
        <img src class="card-img-top" alt="house-cover" />
        <div class="card-body">
          <h5 class="card-title">{{house.title}}</h5>
          <p class="card-text">{{house.description}}</p>
        </div>
        <div class="card-footer">
          <small class="text-muted">{{house.suburb}}</small>
          <br />
          <small class="text-muted">{{house.price}}</small>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HouseCards",
  props: ["houses"]
};
</script>

<style scoped>
</style>