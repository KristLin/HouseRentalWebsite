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
      <div class="col-lg-3 col-md-6 form-group">
        <label class="filter-label">Tenant Number:</label>
        <input type="text" class="form-control" placeholder="Tenant Number" v-model="searchData.tenant_num" />
      </div>
      <div class="col-lg-3 col-md-6 form-group">
        <label class="filter-label">House Conditions:</label>
        <br />
        <div class="mt-2">
          <input type="checkbox" class="condition-input" v-model="searchData.has_wifi" />
          <i class="fas fa-wifi condition-icon"></i>
          <input type="checkbox" class="condition-input" v-model="searchData.party_allowed" />
          <i class="fas fa-glass-cheers condition-icon"></i>
          <input type="checkbox" class="condition-input" v-model="searchData.pet_allowed" />
          <i class="fas fa-dog condition-icon"></i>
          <input type="checkbox" class="condition-input" v-model="searchData.smoke_allowed" />
          <i class="fas fa-smoking condition-icon"></i>
        </div>
      </div>
    </div>
    <div class="row w-50 m-auto">
      <button @click="searchHouse" class="my-btn form-control">Search</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchInput",
  components: {},
  props: {
    searchData: {}
  },
  methods: {
    searchHouse() {
      window.console.log(this.searchData);
      this.$emit("searchHouse", this.searchData);
    }
  }
};
</script>

<style scoped>
.btn-dark {
  border: none;
  background-color: #3c9d9b;
}

.my-btn {
  border: none;
  background-color: #3c9d9b;
  color: white;
}

.my-btn:hover {
  border: none;
  background-color: black;
  color: white;
}

.condition-input {
  margin-right: 5px;
}
.condition-icon {
  margin-right: 12px;
}

@media screen and (max-width: 991px) {
  .condition-input {
    height: 1rem;
    margin-right: 8px;
  }
  .condition-icon {
    font-size: 1.2rem;
    margin-right: 25px;
  }
}

@media screen and (max-width: 767px) {
  .condition-input {
    height: 1.2rem;
    margin-right: 12px;
  }
  .condition-icon {
    font-size: 1.6rem;
    margin-right: 50px;
  }
}
</style>