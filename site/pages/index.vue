<template>
  <div class="container-fluid">
    <div class="row" v-bind:class="{'wrapper' : isNotMobile,'wrapper_2' : !isNotMobile}">
      <div class="col-md-6 offset-sm-1 d-flex align-items-center" style="">
        <div class="box_bax rounded-lg text-light" v-bind:class="{'box_bax' : isNotMobile,'box_bax_mobile' : !isNotMobile}" >
          <h1>Sei un affitta camere?</h1><h1>Crea il tuo annuncio su Flybnb!</h1><h1>È completamente gratuito!</h1><br>
          <a class="btn btn-lg btn-info btn-block " v-if="isAuthenticated" href="/rooms/add/">CREA IL TUO ANNUNCIO</a>
          <a class="btn btn-lg btn-info btn-block " v-if="!isAuthenticated" href="/account/registration/">CREA IL TUO ANNUNCIO</a>
        </div>
      </div>
      <div class="col-sm-5 text-light d-flex align-items-left" style="">
        <div class="box_bax_2 rounded-lg text-dark" style="" >
          <h2></h2>
          <h2></h2>
          <h1></h1><br>
          
        </div>
      </div>
    </div>
    <div class="row mt-4 justify-content-md-center">
      <div class="col-12 justify-content-md-center">
        <div class="text-center">
          <h4>Trova offerte su hotel, case e tanto altro...</h4>
          <label>Comodi appartamenti al mare, fantastici chalet in montagna e tanto altro</label>
        </div>
        <div class="col-12 d-flex justify-content-center mb-4">
            <b-form @submit.stop.prevent="Search" role="search" class="form-inline border-info shadow" >
              <b-form-select v-model="selected" :options="options" class="border-info rounded-0">Località</b-form-select>
              <b-form-input v-model="searchTextIndex" aria-label="Input" placeholder="Che tipo di alloggio stai cercando? Esempio: Camera vista mare" class="input-lg border-info rounded-0 mw-100" style="width:30vw" v-bind:class="{'w-100':!isNotMobile}"></b-form-input><span> </span>
              <button type="submit" class="input btn btn-primary border border-info rounded-0" v-bind:class="{'w-100':!isNotMobile}"> Cerca </button>
            </b-form>
        <br>
        </div>
        
    </div>
  </div>
  <div class="row mt-4 mx-auto" v-bind:class="{'w-75':isNotMobile}" >
    <div class="col-sm-12 mb-2">
    <h4>Scegli tra gli alloggi piu convenienti in tutta Italia</h4>
    </div>
        <template v-for="room in rooms">
            <div :key="room.id" class="col-sm-3 col-md-3">
              <Room-card-mini :room="room"></Room-card-mini>
            </div>
        </template>
    <!--
    <div class="" v-bind:class="{'col-9': isNotMobile,'col-12': !isNotMobile}">
    </div> -->
    <div class="col-sm-12 mb-4 mt-5" >
    <h4>I piu visitati delle ultime 24h</h4>
    </div>
        <template v-for="room in rooms">
            <div :key="room.id" class="col-sm-3 col-md-3">
              <Room-card-mini :room="room"></Room-card-mini>
            </div>
        </template>
  </div>
</div>
</template>

<!-- <span v-if="isAuthenticated">
  <p> Sei autenticato: </p>
  <code>
  {{ loggedInUser }}
  </code>
  </span> 
-->
<style>
.box_bax{
padding:2vh;
border-width:1px;
background-color:rgba(0, 0, 0, 0.411);
}
.box_bax_2{
padding:2vh;
border-width:1px;
/* background-color:rgba(0, 0, 0, 0.212); */
}


.box_bax_mobile{
padding:2vh;
margin:-2vh;
border-width:1px;
background-color:rgba(0, 0, 0, 0.411);
}

.wrapper{
  background-image: url('/homepage_cut_new.jpg');
  background-size: 100% 100%;
  background-repeat: no-repeat;
  margin-left: -15px;
  margin-right: -15px;
  /* Full height */
  min-height: 679px;
  /* Center and scale the image nicely */
  background-position: center;
}

.wrapper_2{
  background-image: url('/homepage_cut_new.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  margin-left: -15px;
  margin-right: -15px;
  /* Full height */
  min-height: 500px;
  /* Center and scale the image nicely */
  background-position: center;
}
</style>

<script>
import { mapGetters } from 'vuex'
import RoomCardMini from "~/components/RoomCardMini.vue";

export default {
  components: {
    RoomCardMini
  },
  data() {
    return {
      rooms: [],
      searchTextIndex: '',
      isNotMobile: false,
      selected: 'Località',
      options: [
          { value: 'Località', text: 'Località', disabled: true },
          { value: 'Abruzzo', text: 'Abruzzo' },
          { value: 'Basilicata', text: 'Basilicata' },
          { value: 'Calabria', text: 'Calabria' },
          { value: 'Campania', text: 'Campania' },
          { value: 'Emilia-Romagna', text: 'Emilia-Romagna' },
          { value: 'Friuli-Venezia Giulia', text: 'Friuli-Venezia Giulia' },
          { value: 'Lazio', text: 'Lazio' },
          { value: 'Liguria', text: 'Liguria' },
          { value: 'Lombardia', text: 'Lombardia' },
          { value: 'Marche', text: 'Marche' },
          { value: 'Molise', text: 'Molise' },
          { value: 'Piemonte', text: 'Piemonte' },
          { value: 'Puglia', text: 'Puglia' },
          { value: 'Sardegna', text: 'Sardegna' },
          { value: 'Sicilia', text: 'Sicilia' },
          { value: 'Toscana', text: 'Toscana' },
          { value: 'Trentino-Alto Adige', text: 'Trentino-Alto Adige' },
          { value: 'Umbria', text: 'Umbria' },
          { value: 'Valle d\'Aosta', text: 'Valle d\'Aosta' },
          { value: 'Veneto', text: 'Veneto' },
        ]
    };
  },
  
  mounted() {
    this.asyncData()
    this.$nextTick(function () {
      this.onResize();
    })
    window.addEventListener('resize', this.onResize)
  },
  computed: {
    ...mapGetters(['isAuthenticated', 'loggedInUser'])
  },
  methods: {
    async logout() {
      await this.$auth.logout();
    },
    async asyncData() {
      var self = this;
        try {
          await self.$axios.$get("api/rooms/").then(function(data){
            self.rooms = data;
          });
        } 
        catch (error) {
          // TODO: migliorare la segnalazione errori
          console.log(error)
        }
    },
    async Search() {
      if (this.searchTextIndex != ''){
        // forse qui sarebbe meglio fare una emit
        if (this.selected != 'Località'){
          this.searchTextIndex = this.selected +' '+ this.searchTextIndex
        }
        
        this.$router.push({path: '/rooms', query: {search: this.searchTextIndex }});
      }
    },
    onResize() {
      this.isNotMobile = document.documentElement.clientWidth > 1600;
      console.log(document.documentElement.clientWidth)
    }
  },
}
</script>