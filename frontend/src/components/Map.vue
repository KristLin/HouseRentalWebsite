<template>
  <div>
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
</template>
<script>
export default {
  name: "Map",
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
      houses: [
        {
          price: "200",
          lat: "-33.918610",
          lng: "151.236246"
        },
        {
          price: "300",
          lat: "-33.918681",
          lng: "151.232416"
        }
      ]
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
      window.console.log(house);
      //   this.$router.push({
      //     name: "house",
      //     query: { houseId: house._id },
      //     params: { house: house }
      //   });
    }
  }
};
</script>

<style scoped>
</style>