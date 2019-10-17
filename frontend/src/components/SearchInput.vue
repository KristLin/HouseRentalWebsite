<template>
  <div>
    <div class="row">
      <div class="col-lg-3 col-md-6 form-group">
        <label class="filter-label">Keyword:</label>
        <input type="text" class="form-control" placeholder="Keyword" v-model="searchData.keyword" />
      </div>
      <div class="col-lg-3 col-md-6 form-group">
        <label class="filter-label">Suburb:</label>
        <input type="text" class="form-control" placeholder="Suburb" v-model="searchData.suburb" />
      </div>
      <div class="col-lg-3 col-md-6 form-group">
        <label class="filter-label">Price from:</label>
        <input
          type="input"
          class="form-control"
          name="input"
          placeholder="Min Price"
          v-model="searchData.minPrice"
        />
      </div>
      <div class="col-lg-3 col-md-6 form-group">
        <label class="filter-label">to:</label>
        <input
          type="input"
          class="form-control"
          name="input"
          placeholder="Max Price"
          v-model="searchData.maxPrice"
        />
      </div>
    </div>
    <div class="row">
      <div class="col-lg-3 col-md-6 form-group">
        <label class="filter-label">Check in:</label>
        <input type="date" class="form-control" v-model="searchData.startDate" />
      </div>
      <div class="col-lg-3 col-md-6 form-group">
        <label class="filter-label">Check out:</label>
        <input type="date" class="form-control" v-model="searchData.endDate" />
      </div>
      <div class="col-lg-6 col-md-12 form-group">
        <label class="filter-label">Search</label>
        <button @click="searchHouse" class="btn btn-primary form-control">Search</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchInput",
  components: {},
  props: {
    searchData: {
      keyword: "",
      suburb: "",
      min_price: "",
      max_price: "",
      start_date: "",
      end_date: ""
    }
  },
  methods: {
    searchHouse() {
      this.$emit("searchHouse", this.searchData);
    }
  }
};
</script>

<style scoped>
</style>