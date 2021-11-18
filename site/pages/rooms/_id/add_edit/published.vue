<template>
<div>
      <div :key="room.id">
  <Room-Create-NavBar :room="room" :activestep="activestep" ></Room-Create-NavBar>
</div>
  <b-container>
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">Congratulazioni!</h2>
        <h2 class="mb-3 display-4 text-uppercase">Il tuo annuncio è completo!</h2>
            <button v-on:click="goToView" class="btn btn-primary btn-block mt-2" type="submit" id="btn-next" :href="'rooms/'+room.id" >Visualizza Annuncio</button>
      </div>     
    </div>
  </b-container>
</div>
</template>
<script>
import RoomCreateNavBar from "~/components/RoomCreateNavBar.vue";


export default {
  
  head() {
    return {
      title: "Annuncio: Fine!"
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
        id:0
      },
      activestep: 9
    };
  },
  methods: {
      async goToView() {
        try {
          var routerString = '/rooms/'+this.room.id
          this.$router.push(routerString);
        } catch (e) {
          console.log(e);
        }
      }
    }
};
</script>
<style scoped>
</style>