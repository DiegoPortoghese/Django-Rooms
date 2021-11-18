<template>
<div>

<div :key="room.id">
  <Room-Create-NavBar :room="room" :activestep="activestep" ></Room-Create-NavBar>
</div>

  <b-container>
    <b-row class="mt-4">
      <b-col sm="6" offset-sm="3">
        <h3>Descrivi il tuo spazio agli ospiti</h3>
        <form @submit.prevent="submitFuncion" autocomplete="on">
          <label >Scrivi il titolo che vuoi dare al tuo annuncio.</label>
          <b-col sm="6">
             <h6>Titolo Annuncio</h6>
          </b-col>
          <b-col sm="9">
            <b-form-input id="inputTitle" v-model="room.title" type="text" placeholder="Scrivi qui il titolo del tuo annuncio" ></b-form-input>
          </b-col>
          
          <br>
          <label >Scrivi maggiorni informazioni del tuo spazio per gli ospiti</label>
          <b-col sm="6">
             <h6>Descrizione Annuncio</h6>
          </b-col>
          
          <b-col sm="12">
            <b-form-textarea
              id="textarea"
              v-model="room.description"
              placeholder="Scrivi qui la descrizione del tuo annuncio..."
              rows="9"
              max-rows="10"
            ></b-form-textarea>
          </b-col>
          <br>
          <button class="btn btn-primary btn-block mt-2" v-if="(room.title != '' && room.description != '' )" type="submit" id="btn-next" > Avanti </button>
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
        if (room.title == 'Unknown'){
          room.title = ''
        }
        if (room.description == 'Unknown'){
          room.description = ''
        }
        return { room };
      } catch (e) {
        return { room: [] };
      }
    },
    data() {
      return {
        room: {
          title: '',
          description: '',
        },
        activestep: 7
      };
    },
    methods: {
      async submitFuncion() {
        this.room.creation_progress = 7
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
          let response = await this.$axios.$put(`api/rooms/${editedRoom.id}/`, editedRoom, config);
          this.$router.push("step8");
        } catch (e) {
          console.log(e);
        }
      }
    }

  };
</script>
