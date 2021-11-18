<template>
<div class="card room-card mb-3 border border-info shadow" v-on:click="viewRoom(room.id)">
  <div class="row no-gutters">
    <div class="col-md-4">
      <img :src="$axios.defaults.baseURL+'media/'+room.pictures[0].file" class="card-img" :href="`/rooms/${room.id}/`" >
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <h5 class="card-title">{{room.title}}</h5>
        <p class="card-text">{{room.position_city}}</p>
        <p class="card-text">{{room.description | truncate(190) }}</p>
        <p class="card-text"><small class="text-muted">Prezzo per notte {{ room.price }}€</small></p>
        <p class="card-text text-right"><small class="text-muted">Creato il {{ room.creation_date.substring(0, 10) }}</small></p>
      </div>
    </div>
  </div>
</div>

<!--
  <div class="card room-card" style="max-height: 270px;">
     <div class="row no-gutters">
      <div class="col-md-4 thumb-post">
        <img :src="$axios.defaults.baseURL+'media/'+room.pictures[0].file" class="thumb-post" :alt="room.title" v-if="room.pictures.length > 0">
      </div>
      <div class="col-md-8">
        <div class="card-body">
          <a :href="`/rooms/${room.id}/`" ><h5 class="card-title">{{room.title}}</h5></a>
          <h6 style="margin-top:-1vh;">{{room.position_city}}</h6>
          <p class="card-text">{{room.description | truncate(200) }}.</p>
          <p class="card-text room-card-datetime"><span class="text-muted">{{ room.create_date }}</span></p>
        </div>        
      </div>
    </div>
  </div> -->
</template>
<style>
.card-img{
   width: 100%!important;
   height: 280px!important;
   object-fit: cover;
}
/*
.room-card {
    box-shadow: 0 0.1rem 0.3rem rgba(0,0,0,.6);
}*/
</style>
<script>
export default {
    props: ["room"],
    filters:{
      truncate(string, value) {
        return (string || '').substring(0, value) + '…'
      }
    },
    methods:{
      viewRoom(roomId){
        window.location = '/rooms/'+roomId
        
      }

    }
};
</script>

