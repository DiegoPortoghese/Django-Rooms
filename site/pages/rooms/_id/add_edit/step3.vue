<template>
<div>

<div :key="room.id">
  <Room-Create-NavBar :room="room" :activestep="activestep" ></Room-Create-NavBar>
</div>

  <b-container>
    <b-row class="mt-4">
      <b-col sm="6" offset-sm="3">
        <h3>Quanti bagni?</h3>
        <form @submit.prevent="submitFuncion" autocomplete="on">
          <label >Considera i bagni che non hanno doccia o vasca come un bagno di servizio.</label>
          <b-col sm="4">
            <h5 >Bagni:</h5>
          </b-col>
          <b-col sm="5">
            <b-form-input v-model="room.bathrooms" type="number"></b-form-input>
          </b-col>
          <br>
          <h6>Qualcuno dei bagni è privato?</h6>
          <b-form-group onchange="document.getElementById('btn-next').disabled = false;">
            <b-form-radio v-model="room.bathrooms_isprivate" name="some-radios" v-bind:value="true"  >Si</b-form-radio>
            <b-form-radio v-model="room.bathrooms_isprivate" name="some-radios" v-bind:value="false" >No, sono condivisi</b-form-radio>
          </b-form-group>
          <br>
          <button class="btn btn-primary btn-block mt-2" v-if="(room.bathrooms_isprivate != null && room.bathrooms > 0)" type="submit" id="btn-next" > Avanti </button>
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
        title: "Crea Annuncio: Bagni"
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
          bathrooms: 0,
          bathrooms_isprivate: null,
          creation_progress: 0
        },
        activestep: 3
      };
    },
    methods: {
      async submitFuncion() {
        this.room.creation_progress = 3
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
          this.$router.push("step4");
        } catch (e) {
          console.log(e);
        }
      }
    }



  };
</script>
