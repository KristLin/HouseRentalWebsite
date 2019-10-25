<template>
  <div class="map-page">
    <div class="row">
      <div class="col-lg-6 col-md-12 overflow-auto">
        <HouseFromMap :house="house" />
      </div>
      <div class="col-lg-6 col-md-12">
        <div class="google-map">
          <GmapMap
            :options="options"
            :center="{lat:-33.912495, lng:151.230854}"
            :zoom="14"
            style="width: 100%; height: 500px;"
            map-type-id="roadmap"
          >
            <GmapMarker
              :key="index"
              v-for="(house, index) in houses"
              :position="getHousePosition(house)"
              :clickable="true"
              :draggable="true"
              :label="{text: '$' + house.price ,color: '#fff',fontSize: '12px',fontWeight: 'bold'}"
              :icon="{url:'https://vectr.com/kristlin/afhuGVy8p.png?width=45&height=35&select=afhuGVy8ppage0'}"
              @click="clickHouseMarker(house)"
            />
          </GmapMap>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HouseFromMap from "@/components/HouseFromMap.vue";

export default {
  name: "Map",
  components: {
    HouseFromMap
  },
  props: {
    // houses: Array
  },
  data() {
    return {
      options: {
        zoomControl: true,
        mapTypeControl: false,
        scaleControl: true,
        streetViewControl: false,
        rotateControl: false,
        fullscreenControl: true,
        disableDefaultUi: false
      },
      house: "",
      houses: []
    };
  },
  methods: {
    getHousePosition(house) {
      return {
        lat: parseFloat(house.lat),
        lng: parseFloat(house.lng)
      };
    },
    clickHouseMarker(house) {
      this.house = house;
      window.console.log(house);
      //   this.$router.push({
      //     name: "house",
      //     query: { houseId: house._id },
      //     params: { house: house }
      //   });
    }
  },
  created() {
    this.$axios
      .get("/api/houses/")
      .then(response => {
        // JSON responses are automatically parsed.
        this.houses = response.data;
        window.console.log(this.houses);
        // this.$forceUpdate();
      })
      .catch(err => {
        window.console.log(err.response);
      });
  }
};
</script>

<style scoped>
.map-page {
  margin: auto;
  margin-top: 30px;
  margin-bottom: 50px;
  width: 90%;
}
</style>