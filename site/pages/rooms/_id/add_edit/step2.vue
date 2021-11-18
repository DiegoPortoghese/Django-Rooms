<template>
<div>

<div :key="room.id">
  <Room-Create-NavBar :room="room" :activestep="activestep" ></Room-Create-NavBar>
</div>

  <b-container>
    <b-row class="mt-4">
      <b-col sm="6" offset-sm="3">
        <h3>Quante persone può ospitare il tuo alloggio?</h3>
        <form @submit.prevent="submitFuncion" autocomplete="on">
          <label >Verifica di disporre di letti sufficienti per far dormire comodamente tutti gli ospiti.</label>
          <b-col sm="4">
            <h5 for="inputGuests">Ospiti:</h5>
          </b-col>
          <b-col sm="5">
            <b-form-input id="inputGuests" v-model="room.guests" type="number"></b-form-input>
          </b-col>
          <br>
          <label>Quante camere da letto possono utilizzare gli ospiti?</label>
          <b-col sm="4">
            <h5 for="inputBedrooms">Camere da letto:</h5>
          </b-col>
          <b-col sm="5">
            <b-form-input id="inputBedrooms" v-model="room.bedrooms" type="number"></b-form-input>
          </b-col>
          <br>
          <label>Quanti letti possono utilizzare gli ospiti?</label>
          <b-col sm="4">
            <h5 for="inputBeds">Letti:</h5>
          </b-col>
          <b-col sm="5">
            <b-form-input id="inputBeds" v-model="room.beds" type="number"></b-form-input>
          </b-col>

          <br>
          <button class="btn btn-primary btn-block mt-2" v-if="(room.guests > 0 && room.bedrooms > 0 && room.beds > 0 )" type="submit" id="btn-next" > Avanti </button>
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
        title: "Crea Annuncio: Camere da letto"
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
          guests: 0,
          bedrooms: 0,
          beds: 0,
          creation_progress: 0
        },
        activestep: 2
      };
    },
    methods: {
      async submitFuncion() {
        this.room.creation_progress = 2
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
          this.$router.push("step3");
        } catch (e) {
          console.log(e);
        }
      }
    }



  };
</script>
