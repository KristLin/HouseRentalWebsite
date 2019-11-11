<template>
  <div>
    <div class="row">
      <!-- left side is house info section -->
      <div class="col-lg-5 col-md-12 overflow-auto">
        <HouseFromMap :house="house" />
      </div>

      <!-- right side is the google map section -->
      <div class="col-lg-7 col-md-12">
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
              :draggable="false"
              :label="{text: '$' + house.price ,color: '#fff',fontSize: '12px',fontWeight: 'bold'}"
              
              :icon="{url: 'https://vectr.com/kristlin/afhuGVy8p.svg?width=45&height=35&select=afhuGVy8ppage0'}"
              @click="clickHouseMarker(house)"
            />
            <!-- 'https://vectr.com/kristlin/afhuGVy8p.png?width=45&height=35&select=afhuGVy8ppage0' -->
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
    houses: Array
  },
  data() {
    return {
      // google map options
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
    }
  },
};
</script>

<style scoped>
</style>