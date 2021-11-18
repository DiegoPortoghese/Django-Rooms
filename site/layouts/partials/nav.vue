<template>
  <header>
    <b-navbar toggleable="lg" type="light" variant="" class="shadow">
      <b-navbar-brand to="/">Flybnb</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-left">
          <b-nav-item-dropdown>
              <template v-slot:button-content>
              <i class="fa fa-map-marker" aria-hidden="true"></i>
              <span class="text-capitalize"> 
                {{locality}}
              </span>
            </template>
            <b-dropdown-item v-on:click="selectLocality('Località')">Località</b-dropdown-item>
            <b-dropdown-item v-on:click="selectLocality('Abruzzo')">Abruzzo</b-dropdown-item>
            <b-dropdown-item v-on:click="selectLocality('Basilicata')">Basilicata</b-dropdown-item>
            <b-dropdown-item v-on:click="selectLocality('Calabria')">Calabria</b-dropdown-item>
            <b-dropdown-item v-on:click="selectLocality('Campania')">Campania</b-dropdown-item>
            <b-dropdown-item v-on:click="selectLocality('Emilia-Romagna')">Emilia-Romagna</b-dropdown-item>
            <b-dropdown-item v-on:click="selectLocality('Friuli-Venezia Giulia')">Friuli-Venezia Giulia</b-dropdown-item>
            <b-dropdown-item v-on:click="selectLocality('Lazio')">Lazio</b-dropdown-item>
            <b-dropdown-item v-on:click="selectLocality('Liguria')">Liguria</b-dropdown-item>
            <b-dropdown-item v-on:click="selectLocality('Lombardia')">Lombardia</b-dropdown-item>
            <b-dropdown-item v-on:click="selectLocality('Marche')">Marche</b-dropdown-item>
            <b-dropdown-item v-on:click="selectLocality('Molise')">Molise</b-dropdown-item>
            <b-dropdown-item v-on:click="selectLocality('Piemonte')">Piemonte</b-dropdown-item>
            <b-dropdown-item v-on:click="selectLocality('Puglia')">Puglia</b-dropdown-item>
            <b-dropdown-item v-on:click="selectLocality('Sardegna')">Sardegna</b-dropdown-item>
            <b-dropdown-item v-on:click="selectLocality('Sicilia')">Sicilia</b-dropdown-item>
            <b-dropdown-item v-on:click="selectLocality('Toscana')">Toscana</b-dropdown-item>
            <b-dropdown-item v-on:click="selectLocality('Trentino-Alto Adige')">Trentino-Alto Adige</b-dropdown-item>
            <b-dropdown-item v-on:click="selectLocality('Umbria')">Umbria</b-dropdown-item>
            <b-dropdown-item v-on:click="selectLocality('Valle d\'Aosta')">Valle d'Aosta</b-dropdown-item>
            <b-dropdown-item v-on:click="selectLocality('Veneto')">Veneto</b-dropdown-item>
            </b-nav-item-dropdown>
          <b-nav-form @submit.stop.prevent="Search" role="search">
            <b-form-input v-model="searchText" aria-label="Input" placeholder="Cosa stai cercando? Esempio: bologna camera" class="input border-info" style="width:40vw;"></b-form-input>
            <!-- <b-button class="btn btn-info" type="submit"><i class="fa fa-search" aria-hidden="true"></i></b-button> -->
          </b-nav-form>
        </b-navbar-nav >
        <b-navbar-nav class="ml-auto">
          
          <b-nav-item v-show="isAuthenticated" to="/chatmessages/"><i v-if="newMessage" class="fa fa-bell" aria-hidden="true" style="color: orange;"></i> <i class="fa fa-lg fa-envelope-o" aria-hidden="true"></i> </b-nav-item>
          <b-nav-item-dropdown v-if="isAuthenticated">
            <template v-slot:button-content>
              <i class="fa fa-user"></i> 
              <span class="text-capitalize"> 
                {{ loggedInUser.username }}
              </span>
            </template>
            <b-dropdown-item to="/account/user/">Modifica Profilo</b-dropdown-item>
            <b-dropdown-item to="/account/password-change/">Modifica Password</b-dropdown-item>
            <b-dropdown-divider></b-dropdown-divider>
            <b-dropdown-item to="/rooms/my/">Le tue inserzioni</b-dropdown-item>
            <b-dropdown-divider></b-dropdown-divider>
            <b-dropdown-item @click="logout">Logout</b-dropdown-item>
          </b-nav-item-dropdown>
          
          <b-nav-item v-show="!isAuthenticated" to="/account/login/">Accedi</b-nav-item>
          <b-nav-item v-show="!isAuthenticated" to="/account/registration/">Registrati</b-nav-item>
          <b-nav-item v-show="isAuthenticated" to="/rooms/add/">
            <button type="button" class="btn btn-outline-success btn-sm" >Crea Annuncio</button>
          </b-nav-item>
          <b-nav-item v-show="!isAuthenticated" to="/account/registration/">
            <button type="button" class="btn btn-outline-success btn-sm" >Crea Annuncio</button>
          </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </header>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  data(){
    return{
      searchText: '',
      newMessage: false,
      locality:'Località'
    }
  },
  computed: {
    ...mapGetters(['isAuthenticated', 'loggedInUser'])
  },
  mounted() {
    if (this.isAuthenticated){
        this.CheckNewMessage()
      }
    },
  methods: {
    async logout() {
      await this.$auth.logout();
    },
    
    async Search() {
      if (this.searchText != ''){
        // forse qui sarebbe meglio fare una emit
        let region = ''
        if (this.locality != 'Località'){
          region = this.locality
        }
        this.$router.push({path: '/rooms', query: {search: region+' '+this.searchText }});
      }
    },
    async CheckNewMessage(){
      var self = this;
        try {
          if (this.isAuthenticated){
           let buff_mgs = []
            await self.$axios.$get("api/chatmessages/").then(function(data){
                buff_mgs = data;
            });
            for(let key in buff_mgs){
              if(buff_mgs[key].displayed === false && buff_mgs[key].from_user != this.loggedInUser.profile[0].fields.user){
                this.newMessage = true
                break;
              }
            }
            }
            }catch(error){
              console.log(error)
            }
        },
        async selectLocality(locality){
          this.locality = locality
        }
  },
}
</script>
