<template>
<div>

<div :key="room.id">
  <Room-Create-NavBar :room="room" :activestep="activestep" ></Room-Create-NavBar>
</div>

  <b-container>
    <b-row class="mt-4">
      <b-col sm="6" offset-sm="3">
        <h3>Definisci i prezzi del tuo spazio</h3>
        <form @submit.prevent="submitFuncion" autocomplete="on">
          <label >Imposta lo stesso prezzo standard per ogni notte.</label>
          <b-col sm="3">
             <h6>Euro</h6>
          </b-col>
          <b-col sm="3">
            <b-form-input id="inputPrice" v-model="room.price" type="decimal" placeholder="€" ></b-form-input>
          </b-col>
          <br>
          <br>
          <button class="btn btn-primary btn-block mt-2" v-if="(room.price > 0 )" type="submit" id="btn-next" > Avanti </button>
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
        title: "Crea Annuncio: Prezzo"
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
          price: 0,
        },
        activestep: 6
      };
    },
    methods: {
      async submitFuncion() {
        this.room.creation_progress = 6
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
          this.$router.push("step7");
        } catch (e) {
          console.log(e);
        }
      }
    }



  };
</script>
