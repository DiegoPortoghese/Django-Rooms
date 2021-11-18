<template>
  <main class="container mt-4">
    <div class="row">
      <div class="col-12 text-right mb-4">
        <div class="d-flex justify-content-between">
          <h4>Risultati per: {{this.$route.query.search}}</h4>
        </div>
      </div>
      {{ searchChange }}
      <template v-for="room in rooms">
          <div :key="room.id" class="col-12 mb-4">
            <Room-card :room="room"></Room-card>
          </div>
      </template>
    </div>
  </main>
</template>
<script>
import RoomCard from "~/components/RoomCard.vue";

export default {
  head() {
    return {
      title: "Cerca Camere: "+this.$route.query.search
    };
  },
  components: {
    RoomCard
  },
  data() {
    return {
      rooms: [],
    };
  },
  mounted() {
    this.asyncData()
  },
  computed: {
    searchChange: function() {
      if(this.$route.query.search){
        this.asyncData()
      }
    }
  },
  methods: {
    async asyncData() {
      var self = this;
        try {
          await self.$axios.$get("api/rooms/search/?search=" + self.$route.query.search ).then(function(data){
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