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
        <label class="filter-label">House Conditions:</label>
        <br />
        <div class="mt-2">
          <input type="checkbox" class="search-condition-input" v-model="searchData.has_wifi" />
          <i class="fas fa-wifi search-condition-icon"></i>
          <input type="checkbox" class="search-condition-input" v-model="searchData.party_allowed" />
          <i class="fas fa-glass-cheers search-condition-icon"></i>
          <input type="checkbox" class="search-condition-input" v-model="searchData.pet_allowed" />
          <i class="fas fa-dog search-condition-icon"></i>
          <input type="checkbox" class="search-condition-input" v-model="searchData.smoke_allowed" />
          <i class="fas fa-smoking search-condition-icon"></i>
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

.search-condition-input {
  margin-right: 5px;
}
.search-condition-icon {
  margin-right: 12px;
}

@media screen and (max-width: 991px) {
  .search-condition-input {
    height: 1rem;
    margin-right: 8px;
  }
  .search-condition-icon {
    font-size: 1.2rem;
    margin-right: 25px;
  }
}

@media screen and (max-width: 767px) {
  .search-condition-input {
    height: 1.2rem;
    margin-right: 12px;
  }
  .search-condition-icon {
    font-size: 1.6rem;
    margin-right: 50px;
  }
}

@media screen and (max-width: 510px) {
  .search-condition-icon {
    font-size: 1.2rem;
    margin-right: 35px;
  }
}
</style>