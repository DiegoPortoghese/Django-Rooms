<template>
  <main class="container mt-4">
    <div class="row">
      <div class="col-12 text-right mb-4">
        <div class="d-flex justify-content-between">
          <h4>Le tue inserzioni</h4>
        </div>
      </div>
      
      <template v-for="room in rooms">
          <div :key="room.id" class="col-12 mb-4">
            <Room-card-edit-delete :room="room"></Room-card-edit-delete>
          </div>
      </template>
    </div>
  </main>
</template>
<script>
import RoomCardEditDelete from "~/components/RoomCardEditDelete.vue";

export default {
  head() {
    return {
      title: "Le tue inserzioni"
    };
  },
  components: {
    RoomCardEditDelete
  },
  data() {
    return {
      rooms: [],
    };
  },
  mounted() {
    this.asyncData()
  },
  
  methods: {
    async asyncData() {
      var self = this;
        try {
          await self.$axios.$get("api/rooms/my").then(function(data){
            self.rooms = data;
          });
        } 
        catch (error) {
          // TODO: migliorare la segnalazione errori
          console.log(error)
        }
    },
    /*
    async deleteRoom(room_id) {
      console.log(11111)
      try {
        await this.$axios.$delete(`api/rooms/${room_id}/`); // delete room
        let newRooms = await this.$axios.$get("api/rooms/search/?search="); // get new list of rooms
        this.rooms = newRooms; // update list of s
      } catch (e) {
        console.log(e);
      }
    }*/
  }
};
</script>