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
      <!-- <div class="col-lg-3 col-md-6 form-group">
        <label class="filter-label">Check in:</label>
        <input type="date" class="form-control" v-model="searchData.startDate" />
      </div>
      <div class="col-lg-3 col-md-6 form-group">
        <label class="filter-label">Check out:</label>
        <input type="date" class="form-control" v-model="searchData.endDate" />
      </div>-->
      <div class="col-lg-3 col-md-6 form-group">
        <label class="filter-label">Tenant Number:</label>
        <input
          type="text"
          class="form-control"
          placeholder="Tenant Number"
          v-model="searchData.tenant_num"
        />
      </div>
      <div class="col-lg-3 col-md-6 form-group">
        <label class="filter-label">House Facility:</label>
        <br />
        <div class="mt-2">
          <input type="checkbox" class="search-facility-input" v-model="searchData.wifi" />
          <i class="fas fa-wifi search-facility-icon"></i>
          <input type="checkbox" class="search-facility-input" v-model="searchData.kitchen" />
          <i class="fas fa-utensils search-facility-icon"></i>
          <br class="facility-input-layout-br">
          <input type="checkbox" class="search-facility-input" v-model="searchData.carpark" />
          <i class="fas fa-car search-facility-icon"></i>
          <input type="checkbox" class="search-facility-input" v-model="searchData.ac" />
          <i class="fas fa-snowflake search-facility-icon"></i>
        </div>
      </div>
      <div class="col-lg-3 col-md-6 form-group">
        <label class="filter-label">Sort by:</label>
        <select v-model="searchData.order_type" class="form-control">
          <option value="default">Default</option>
          <option value="price_asc">Lowest Price</option>
          <option value="price_desc">Highest Price</option>
          <option value="rating_asc">Lowest Rating</option>
          <option value="rating_desc">Highest Rating</option>
          <option value="rating_num_asc">Less Rating Number</option>
          <option value="rating_num_desc">Most Rating Number</option>
        </select>
      </div>
      <div class="col-lg-3 col-md-6 form-group">
        <label class="filter-label">Search House:</label>
        <button @click="searchHouse" class="my-btn form-control">Search</button>
      </div>
    </div>
    <div class="row w-50 m-auto"></div>
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
  },
  created() {
    if(!this.searchData.order_type) {
      this.searchData.order_type="default"
    }
  },
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

.search-facility-input {
  margin-right: 5px;
}
.search-facility-icon {
  margin-right: 12px;
}

.facility-input-layout-br {
  display: none;
}

@media screen and (max-width: 991px) {
  .search-facility-input {
    height: 1rem;
    margin-right: 8px;
  }
  .search-facility-icon {
    font-size: 1.2rem;
    margin-right: 25px;
  }
}

@media screen and (max-width: 767px) {
  .search-facility-input {
    height: 1.2rem;
    margin-right: 12px;
  }
  .search-facility-icon {
    font-size: 1.6rem;
    margin-right: 50px;
  }
}

@media screen and (max-width: 510px) {
  .search-facility-icon {
    font-size: 1.2rem;
    margin-right: 35px;
  }
}
@media screen and (max-width: 421px) {
  .search-facility-icon {
    font-size: 1rem;
    margin-right: 18px;
  }
}

@media screen and (max-width: 336px) {
  .search-facility-icon {
    font-size: 1rem;
    margin-right: 10px;
  }
}
</style>