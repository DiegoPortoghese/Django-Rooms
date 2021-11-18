<template>
<div>

<div :key="room.id">
  <Room-Create-NavBar :room="room" :activestep="activestep" ></Room-Create-NavBar>
</div>

  <b-container>
    <b-row class="mt-4">
      <b-col sm="6" offset-sm="3">
        <h3>Quali servizi metti a disposizione?</h3>
        <form @submit.prevent="submitFuncion" autocomplete="on">
          <label>Fai sapere ai tuoi ospiti quali servizi avranno a dispozione.</label>
          <br>
            <h6>Servizi della struttura:</h6>
            <b-form-group>
              <b-form-checkbox-group
                id="checkbox-group-1"
                v-model="room.services"
                :options="options_hotel"
                name="flavour-2a"
              stacked></b-form-checkbox-group>
            </b-form-group>
            <h6>Servizi della camera:</h6>
            <b-form-group>
              <b-form-checkbox-group
                id="checkbox-group-2"
                v-model="room.services"
                :options="options_camera"
                name="flavour-2a"
              stacked></b-form-checkbox-group>
            </b-form-group>
            <h6>Servizi di accessibilità:</h6>
            <b-form-group>
              <b-form-checkbox-group
                id="checkbox-group-3"
                v-model="room.services"
                :options="options_accessibilità"
                name="flavour-2a"
              stacked></b-form-checkbox-group>
            </b-form-group>
            <h6>Servizi per i bambini:</h6>
          <b-form-group>
              <b-form-checkbox-group
                id="checkbox-group-4"
                v-model="room.services"
                :options="options_bambini"
                name="flavour-2a"
              stacked></b-form-checkbox-group>
            </b-form-group>
          <br>
          <button class="btn btn-primary btn-block mt-2" v-if="(room.guests > 0 && room.bedrooms > 0 && room.beds > 0 )" type="submit" id="btn-next" > Avanti </button>
          <button class="btn btn-primary btn-block mt-2" v-else="" type="submit" id="btn-next" disabled> Avanti </button>
          <br><!-- da levare dopo che abbiamo sistemato il footer -->
          <br><!-- da levare dopo che abbiamo sistemato il footer -->
          <br><!-- da levare dopo che abbiamo sistemato il footer -->
          <br><!-- da levare dopo che abbiamo sistemato il footer -->
          <br><!-- da levare dopo che abbiamo sistemato il footer -->
          <br><!-- da levare dopo che abbiamo sistemato il footer -->

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
        title: "Crea Annuncio: Servizi"
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
        options_hotel: [
          { text: 'Ascensore', value: 1 },
          { text: 'Cassaforte', value: 2 },
          { text: 'Parcheggio', value: 3 },
          { text: 'PC con internet', value: 4 },
          { text: 'Reception 24 ore su 24', value: 5 },
          { text: 'Servizio in camera', value: 6 },
          { text: 'Stanze per non fumatori', value: 7 },
          { text: 'Terrazza', value: 8 },
          { text: 'Wi-Fi nella hall', value: 9 },
        ],
        options_camera: [
          { text: 'Aria Condizionata', value: 10 },
          { text: 'Asciugacapelli', value: 11 },
          { text: 'Cassaforte in camera', value: 12 },
          { text: 'Wi-Fi in camera', value: 13 },
          { text: 'Riscaldamento', value: 14 },
          { text: 'Scrivania', value: 15 },
          { text: 'Telefono', value: 16 },
          { text: 'TV', value: 17 },
          { text: 'TV satellitare', value: 18 },
        ],
        options_accessibilità: [
          { text: 'Accesso per sedia a rotelle', value: 19 },
        ],
        options_bambini: [
          { text: 'Lettini', value: 20 },
          { text: 'Culle', value: 21 },
        ],
        
        room: {
          guests: 0,
          bedrooms: 0,
          beds: 0,
          creation_progress: 0
        },
        activestep: 5,
        
      };
    },
    methods: {
      async submitFuncion() {
        this.room.creation_progress = 5
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
          this.$router.push("step6");
        } catch (e) {
          console.log(e);
        }
      }
    }



  };
</script>
