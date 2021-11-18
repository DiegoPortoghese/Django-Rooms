<template>
<div class="Room-Create-NavBar" >
  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-navbar-nav class="">
            <b-navbar-brand href="#" v-if="!room.published">Crea Annuncio</b-navbar-brand>
            <b-navbar-brand href="#" v-if="room.published">Modifica Annuncio</b-navbar-brand>
      </b-navbar-nav>
      <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav class="ml-auto navbar-center">

        <b-nav-item href="step1" v-if="activestep!=1" >Tipo di alloggio</b-nav-item>
        <b-nav-item href="step1" v-if="activestep==1" active>Tipo di alloggio</b-nav-item>

        <b-nav-item href="step2" v-if="room.creation_progress > 0 && activestep!=2">Camere da letto</b-nav-item>
        <b-nav-item href="step2" v-if="room.creation_progress > 0 && activestep==2" active>Camere da letto</b-nav-item>
        <b-nav-item href="step2" v-if="room.creation_progress < 1" disabled>Camere da letto</b-nav-item>

        <b-nav-item href="step3" v-if="room.creation_progress >= 2  && activestep!=3">Bagni</b-nav-item>
        <b-nav-item href="step3" v-if="room.creation_progress >= 2  && activestep==3" active>Bagni</b-nav-item>
        <b-nav-item href="step3" v-if="room.creation_progress <= 1" disabled>Bagni</b-nav-item>

        <b-nav-item href="step4" v-if="room.creation_progress >= 3 && activestep!=4">Posizione</b-nav-item>
        <b-nav-item href="step4" v-if="room.creation_progress >= 3 && activestep==4" active>Posizione</b-nav-item>
        <b-nav-item href="step4" v-if="room.creation_progress <= 2" disabled>Posizione</b-nav-item>
        
        <b-nav-item href="step5" v-if="room.creation_progress >= 4 && activestep!=5">Servizi</b-nav-item>
        <b-nav-item href="step5" v-if="room.creation_progress >= 4 && activestep==5" active>Servizi</b-nav-item>
        <b-nav-item href="step5" v-if="room.creation_progress <= 3" disabled>Servizi</b-nav-item>

        <b-nav-item href="step6" v-if="room.creation_progress >= 5 && activestep!=6">Prezzo</b-nav-item>
        <b-nav-item href="step6" v-if="room.creation_progress >= 5 && activestep==6" active>Prezzo</b-nav-item>
        <b-nav-item href="step6" v-if="room.creation_progress <= 4" disabled>Prezzo</b-nav-item>

        <b-nav-item href="step7" v-if="room.creation_progress >= 6 && activestep!=7">Descrizione</b-nav-item>
        <b-nav-item href="step7" v-if="room.creation_progress >= 6 && activestep==7" active>Descrizione</b-nav-item>
        <b-nav-item href="step7" v-if="room.creation_progress <= 5" disabled>Descrizione</b-nav-item>

        <b-nav-item href="step8" v-if="room.creation_progress >= 7 && activestep!=8">Foto</b-nav-item>
        <b-nav-item href="step8" v-if="room.creation_progress >= 7 && activestep==8" active>Foto</b-nav-item>
        <b-nav-item href="step8" v-if="room.creation_progress <= 6" disabled>Foto</b-nav-item>

      </b-navbar-nav>

      <b-navbar-nav class="ml-auto">

        <b-nav-item href="published" v-if="room.creation_progress >= 8 && activestep!=9">Pubblica</b-nav-item>
        <b-nav-item href="published" v-if="room.creation_progress >= 8 && activestep==9" active>Pubblica</b-nav-item>
        <b-nav-item href="published" v-if="room.creation_progress <= 7" disabled>Pubblica</b-nav-item>
      
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
  </div>
</template>
<script>
export default {
    props: ["room","activestep"]
};
</script>