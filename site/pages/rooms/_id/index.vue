
<template >
<!--Carousel Wrapper-->
<div class="container-fluid" >
<div class="row">
      <div class="container-nerd" v-show="isNotMobile">
        <div class="gallery">
            <figure class="gallery__item gallery__item--1">
                <img :src="$axios.defaults.baseURL+'media/'+room.pictures[1].file" alt="Gallery image 1" class="gallery__img">
            </figure>
            <figure class="gallery__item gallery__item--2">
                <img :src="$axios.defaults.baseURL+'media/'+room.pictures[2].file" alt="Gallery image 2" class="gallery__img">
            </figure>
            <figure class="gallery__item gallery__item--3">
                <img :src="$axios.defaults.baseURL+'media/'+room.pictures[0].file" alt="Gallery image 3" class="gallery__img">
            </figure>
            <figure class="gallery__item gallery__item--4">
                <img :src="$axios.defaults.baseURL+'media/'+room.pictures[3].file" alt="Gallery image 4" class="gallery__img">
            </figure>
            <figure class="gallery__item gallery__item--5">
                <img :src="$axios.defaults.baseURL+'media/'+room.pictures[4].file" alt="Gallery image 5" class="gallery__img">
            </figure>
        </div>
      </div>

        <div v-show="!isNotMobile">
    <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="4000"
      controls
      indicators
      background="#ababab"
      img-width="1024"
      img-height="480"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <!-- Slides with image only -->
      <b-carousel-slide :img-src="$axios.defaults.baseURL+'media/'+room.pictures[0].file"></b-carousel-slide>
      <b-carousel-slide :img-src="$axios.defaults.baseURL+'media/'+room.pictures[1].file"></b-carousel-slide>
      <b-carousel-slide :img-src="$axios.defaults.baseURL+'media/'+room.pictures[2].file"></b-carousel-slide>
      <b-carousel-slide :img-src="$axios.defaults.baseURL+'media/'+room.pictures[3].file"></b-carousel-slide>
      <b-carousel-slide :img-src="$axios.defaults.baseURL+'media/'+room.pictures[4].file"></b-carousel-slide>
    </b-carousel>
        </div>


</div>
  <div class="row mt-4">
      <div class="col-sm-3 text-left offset-sm-3">
        <h3><b>{{ room.title }}</b></h3>
        <p>{{room.position_city}}</p>
        <p>{{room.guests}} ospiti &nbsp; {{room.bedrooms}} Camere da letto &nbsp; {{room.beds}} letti &nbsp; {{room.bathrooms}} bagni</p>
        
      </div >
      <div class="offset-sm-3" v-bind:class="{'col-sm-3' : isNotMobile, 'col-sm-6' : !isNotMobile}"><hr></div>
      <div id="LeftBoxButton" class="col-sm-6" v-bind:class="{left_box_button_big : isNotMobile, 'offset-sm-3' : !isNotMobile}" >
        <div style="padding-top:20px;">
          <h3>Prezzo per notte: &nbsp; €{{room.price}}</h3>
          <br>
          <p><b>Annuncio di {{room.owner_first_name}}</b></p>
        </div>
        <div class="d-flex justify-content-center">
          <button class="btn btn-danger w-100" v-if="isAuthenticated" v-on:click="sendPrenotationMessage(room.title,room.owner,room.owner_first_name)" >Contatta l'Host per prenotare</button>
          <a href='/account/registration' class="btn btn-danger w-100" v-if="!isAuthenticated" >Contatta l'Host per prenotare</a>
        </div>
      </div>
      <hr>
  </div>
  <div class="row mt-4">
        <div class="col-sm-2 text-left offset-sm-3 my_custom_index">
          <b>Servizi della struttura</b>
          <ul>
              <li v-for="service in room.services_description"
                  v-show="service.category == 1"
                  :key="service.id">
                {{ service.title }}
              </li>
            </ul>
        </div>
        <div class="col-sm-2 text-left my_custom_index">
            <b>Servizi della camera</b>
            <ul>
              <li v-for="service in room.services_description"
                  v-show="service.category == 2"
                  :key="service.id">
                {{ service.title }}
              </li>
            </ul>
        </div>
  </div>
  <div class="row">
        <div class="col-sm-2 offset-sm-3 text-left my_custom_index">
            <b>Servizi di accessibilità</b>
            <ul>
              <li v-for="service in room.services_description"
                  v-show="service.category == 3"
                  :key="service.id">
                {{ service.title }}
              </li>
            </ul>
        </div>
        <div class="col-sm-2 text-left my_custom_index">
            <b>Servizi per bambini</b>
            <ul>
              <li v-for="service in room.services_description"
                  v-show="service.category == 4"
                  :key="service.id">
                {{ service.title }}
              </li>
            </ul>
        </div>
  </div>
  
  <div class="row">
    
      <div class="col-sm-6 offset-sm-3" >
        <br>
      <hr>
        <div class="" >
          <p>{{room.description}}</p>
        </div>
      </div>
    
    </div>
    <div class="row mt-4">
      <div class="col-sm-6 offset-sm-3">
        <h4>L'alloggio si trova in questa zona</h4>
          <gmap-map
            :center="center"
            :zoom="16"
            style="width:100%;  height: 400px;"
          >
            <gmap-circle
              
              :center="marker.position"
              :radius="300"
              :visible="true"
              :options="{fillColor:'rgba(0, 75, 187, 0.226)',fillOpacity:0.5}"
            ></gmap-circle>
            
          </gmap-map>
          
      </div>
    </div>
    <div class="row">
      <br><br>
      
    </div>

</div>

</template>

<style>
.my_custom_index *,*::after,*::before {
  margin: 0;
  padding: 0;
  box-sizing: inherit; 
}
  
.left_box_button_big{
position:absolute;
left:55vw;
border-style:solid;
border-width:1px;
border-color: rgb(185, 185, 185);
width:380px;
height:182px;
margin:0;
padding-left:10px;
padding-right:10px;
box-sizing: inherit; 
}

ul {
  list-style-type: none;
}



.container-nerd {
  width: 100%;
  margin: 0 auto;
  border:block;
}

figure{
  margin:0;
  border-style: solid;
  border-width: 1px;
}
.gallery {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: repeat(10, 3vw);
  grid-gap: 0rem;
}

.gallery__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block; 
}

.gallery__item--1 {
  grid-column-start: 1;
  grid-column-end: 4;
  grid-row-start: 1;
  grid-row-end: 6;

  /** Alternative Syntax **/
  /* grid-column: 1 / span 2;  */
  /* grid-row: 1 / span 2; */
}

.gallery__item--2 {
  grid-column-start: 4;
  grid-column-end: 7;
  grid-row-start: 1;
  grid-row-end: 6;

  /** Alternative Syntax **/
  /* grid-column: 3 / span 2;  */
  /* grid-row: 1 / span 2; */
}

.gallery__item--3 {
  grid-column-start: 7;
  grid-column-end: 13;
  grid-row-start: 1;
  grid-row-end: 11;

  /** Alternative Syntax **/
  /* grid-column: 5 / span 4;
  grid-row: 1 / span 5; */
}

.gallery__item--4 {
  grid-column-start: 1;
  grid-column-end: 4;
  grid-row-start: 6;
  grid-row-end: 11;

  /** Alternative Syntax **/
  /* grid-column: 1 / span 4;  */
  /* grid-row: 3 / span 3; */
}

.gallery__item--5 {
  grid-column-start: 4;
  grid-column-end: 7;
  grid-row-start: 6;
  grid-row-end: 11;

  /** Alternative Syntax **/
  /* grid-column: 1 / span 4; */
  /* grid-row: 6 / span 3; */
}

</style>
<script>
import { mapGetters } from 'vuex'

export default {
  head() {
    return {
      title: "Annuncio"
    };
  },
  async asyncData({ $axios, params }) {
    try {
      let room = await $axios.$get(`api/rooms/${params.id}/`);
      const marker_gen = {
              lat: parseFloat(room.position_geometry_lat),
              lng: parseFloat(room.position_geometry_lng)
            };
      let marker = {position: marker_gen};
      let center = marker_gen;
      
      return { room, marker ,center };
    } catch (e) {
      return { room: [] };
    }
  },
  data() {
    return {
      room: {
        title: "",
        owner: "",
        description: "",
        create_date: null,
        price: 0,
        category: 0,
        creation_step: 0,
      },
      
      isNotMobile: false,
      center: { lat: 0, lng: 0 },
      marker: { position: null },
      slide: 0,
      sliding: null
    };
  },
  computed: {
    ...mapGetters(['isAuthenticated', 'loggedInUser'])
  },
  mounted: function(){
    this.$nextTick(function () {
      this.onResize();
    })
    window.addEventListener('resize', this.onResize)
  },
  methods: {
    onResize() {
      this.isNotMobile = document.documentElement.clientWidth > 1600;
      console.log(document.documentElement.clientWidth)
    },
    onSlideStart(slide) {
      this.sliding = true
    },
    onSlideEnd(slide) {
      this.sliding = false
    },
    async sendPrenotationMessage(title,owner,owner_first_name){
       if(this.loggedInUser.profile[0].fields.user != owner){
            const config = {
                headers: { "content-type": "multipart/form-data" }
            };
              try {
                  
                  let PrenotationMessage = 'Ciao '+owner_first_name+' ti contatto in merito al annuncio "'+title+'"'
                  
                  let formData = new FormData();
                  formData.append('from_user',this.loggedInUser.profile[0].fields.user)
                  formData.append('to_user',owner)
                  formData.append('message',PrenotationMessage)

                  let response =  this.$axios.$post(`api/chatmessages/`, formData, config);                 
                  await this.selectChat(this.selectedChatUser)
              } catch (e) {
                  console.log(e);
            }
      window.location = '/chatmessages/'
      }
    }

  }
};
</script>
