<template>
<div>

<div :key="room.id">
  <Room-Create-NavBar :room="room" :activestep="activestep" ></Room-Create-NavBar>
</div>

  <b-container>
    <b-row class="mt-4">
      <b-col sm="6" offset-sm="3">
        <h3>Dove si trova il tuo alloggio?</h3>
        <form @submit.prevent="submitFuncion" autocomplete="on">
          <label >Gli ospiti riceveranno il tuo indirizzo completo solo dopo aver effettuato una prenotazione.</label>
          <br><br>
          <label >Scrivi l'indirizzo e seleziona quello corretto dal suggerimento</label>
          <label style="width: 100%">
            <gmap-autocomplete @place_changed="setPlace" style="width: 100%" placeholder="Scrivi l'indrizzo qui" v-if="room.position_full_address != 'Unknown'" :value="room.position_full_address">
            </gmap-autocomplete>
            <gmap-autocomplete @place_changed="setPlace" style="width: 100%" placeholder="Scrivi l'indrizzo qui" v-else="">
            </gmap-autocomplete>
          </label>
          <br/>
          <h5>Puoi controllare sulla mappa che l'indirizzo sia corretto</h5>
          <gmap-map
            :center="center"
            :zoom="12"
            style="width:100%;  height: 400px;"
          >
            <gmap-marker
              :key="marker"
              v-model="marker"
              :position="marker.position"
              @click="center=marker.position"
            ></gmap-marker>
          </gmap-map>
          <br/>
          <button class="btn btn-primary btn-block mt-2" v-if="room.position_full_address != 'Unknown'" type="submit" id="btn-next" > Avanti </button>
          <button class="btn btn-primary btn-block mt-2" v-else="" type="submit" id="btn-next" disabled> Avanti </button>
        </form> 
      </b-col>
    </b-row>
    </b-container>


</div>
</template>
<script>
    import RoomCreateNavBar from "~/components/RoomCreateNavBar.vue";
    // on click next execute query
    export default {
      layout: 'no-footer',
    head() {
      return {
        title: "Crea Annuncio: Posizione"
      };
    },
    components: {
      RoomCreateNavBar
    },
  
    async asyncData({ $axios, params }) {
      try {
        let room = await $axios.$get(`api/rooms/${params.id}/`);
        return { room };
      } catch (e) {
        return { room: [] };
      }
    },
    data() {
      return {
        room: {
              position_full_address : 'Unknown',
              position_country: 'Unknown',
              position_city: 'Unknown',
              position_locality_regione: 'Unknown',
              position_locality_provincia: 'Unknown',
              position_locality_comune: 'Unknown',
              position_street: 'Unknown',
              position_street_number: 'Unknown',
              position_zipcode: 'Unknown',
              position_geometry_lat: 0,
              position_geometry_lng: 0,
          creation_progress: 0
        },
        activestep: 4,
        center: { lat: 41.87194, lng: 12.56737999 },
        marker: { position:null },
        currentPlace: null,
      };
    },
    methods: {
      // ARRAY GOOGLE MAPS API: https://developers.google.com/places/web-service/autocomplete https://developers.google.com/places/web-service/details
      // receives a place object via the autocomplete component
      setPlace(place) {
        try{
            this.currentPlace = place;
            const marker_gen = {
              lat: this.currentPlace.geometry.location.lat(),
              lng: this.currentPlace.geometry.location.lng()
            };
            //this.m = marker;
            this.marker = {position: marker_gen};
            this.center = marker_gen;
            console.log(this.marker) // 3 comune
            console.log('formatted_address'+this.currentPlace.formatted_address) // full address
            console.log(this.currentPlace.address_components) // 6 Country
            console.log(this.currentPlace.address_components.length)
            if (this.currentPlace.address_components.length === 6){
              this.room.position_full_address = this.currentPlace.formatted_address
              this.room.position_country = this.currentPlace.address_components[5].long_name
              this.room.position_city = this.currentPlace.address_components[2].long_name
              this.room.position_locality_regione = this.currentPlace.address_components[4].long_name
              this.room.position_locality_provincia = this.currentPlace.address_components[3].short_name
              this.room.position_locality_comune = this.currentPlace.address_components[2].long_name
              this.room.position_street = this.currentPlace.address_components[0].long_name
              this.room.position_street_number = ''
              this.room.position_zipcode = this.currentPlace.address_components[6].long_name
              this.room.position_geometry_lat = this.currentPlace.geometry.location.lat()
              this.room.position_geometry_lng = this.currentPlace.geometry.location.lng()
              }
            if (this.currentPlace.address_components.length === 8){
              this.room.position_full_address = this.currentPlace.formatted_address
              this.room.position_country = this.currentPlace.address_components[6].long_name
              this.room.position_city = this.currentPlace.address_components[3].long_name
              this.room.position_locality_regione = this.currentPlace.address_components[5].long_name
              this.room.position_locality_provincia = this.currentPlace.address_components[4].short_name
              this.room.position_locality_comune = this.currentPlace.address_components[3].long_name
              this.room.position_street = this.currentPlace.address_components[1].long_name
              this.room.position_street_number = this.currentPlace.address_components[0].long_name
              this.room.position_zipcode = this.currentPlace.address_components[7].long_name
              this.room.position_geometry_lat = this.currentPlace.geometry.location.lat()
              this.room.position_geometry_lng = this.currentPlace.geometry.location.lng()
            }
            //this.currentPlace = null;
            
        }catch (e){
          console.log(e)
        }
      },
      addMarker() {
      },
      geolocate: function() {
        navigator.geolocation.getCurrentPosition(position => {
          this.center = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
          };
        });
      },
      async submitFuncion() {
        this.room.creation_progress = 4
        let editedRoom = this.room
        const config = {
          headers: { "content-type": "application/json" }
        };
        /*let formData = new FormData();
        for (let data in editedRoom) {
          formData.append(data, editedRoom[data]);
        }*/
        //console.log(formData);
        try {
          let response = await this.$axios.$patch(`api/rooms/${editedRoom.id}/`, editedRoom, config);
          this.$router.push("step5");
        } catch (e) {
          console.log(e);
        }
      }
    }



  };
</script>
