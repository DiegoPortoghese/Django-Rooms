<template>
<div>

<div :key="room.id">
  <Room-Create-NavBar :room="room" :activestep="activestep" ></Room-Create-NavBar>
</div>

  <b-container>
    <b-row class="mt-4">
      <b-col sm="6" offset-sm="3">
        <h3>Aggiungi le foto del tuo spazio</h3>
        <form @submit.prevent="submitFuncion" autocomplete="on">
          <label>Carica la foto che verra visualizzata per prima nel tuo annuncio.</label>
          <b-col sm="11">
            <div class="shadow-lg p-3 mb-5 rounded">
            <b-img
              v-if="preview[0]"
              :src="preview[0]"
              fluid
            ></b-img>
            <h6>Foto Principale</h6>
            <input type="file" name="file" @change="onFileChange($event,0)">
            </div>
          </b-col>
          <br>
          <h6>Aggiungi altre foto fino a un massimo di 4.</h6>
          <b-col sm="11">
            <div class="shadow-lg p-3 mb-3 rounded">
              <b-img
                v-if="preview[1]"
                :src="preview[1]"
                fluid
              ></b-img>
              <input type="file" name="file" @change="onFileChange($event,1)">
            </div>
            <div class="shadow-lg p-3 mb-3 rounded">
              <b-img
                v-if="preview[2]"
                :src="preview[2]"
                fluid
              ></b-img>
              <input type="file" name="file" @change="onFileChange($event,2)">
            </div>
            <div class="shadow-lg p-3 mb-3 rounded">
              <b-img
                v-if="preview[3]"
                :src="preview[3]"
                fluid
              ></b-img>
              <input type="file" name="file" @change="onFileChange($event,3)">
            </div>
            <div class="shadow-lg p-3 mb-3 rounded">
              <b-img
                v-if="preview[4]"
                :src="preview[4]"
                fluid
              ></b-img>
              <input type="file" name="file" @change="onFileChange($event,4)">
            </div>
          </b-col>
         
          <br>
          <button class="btn btn-primary btn-block mt-2" v-if="(preview[0]!=''&&preview[1]!=''&&preview[2]!=''&&preview[3]!=''&&preview[4]!='' )" type="submit" id="btn-next" > Avanti </button>
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
        let preview= {0:"",1:"",2:"",3:"",4:""}

        return { room ,preview};
      } catch (e) {console.log(e)
        return { room: [] };
      }
    },
    data() {
      return {
        room: {
          title: '',
          description: '',
          pictures: [
            {id: 0, file:''},
            {id: 0, file:''},
            {id: 0, file:''},
            {id: 0, file:''},
            {id: 0, file:''},
          ]
        },
        preview:{0:"",1:"",2:"",3:"",4:""},
        activestep: 8
      };
    },
    methods: {
      onFileChange: function(event,nfile) {
        let files = event.target.files || event.dataTransfer.files;
        if (!files.length) {
          return;
        }
        let reader = new FileReader();
        let vm = this;
        reader.onload = e => {
          vm.preview[nfile] = e.target.result;
        };
        reader.readAsDataURL(files[0]);
      },
      async submitFuncion() {
        this.room.creation_progress = 8
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
          
          // CLEAR PREVIEW
          if (this.preview[0]!= ''){
            for (let key in this.room.pictures){
              var obj = this.room.pictures[key]
              try{
                await this.$axios.$delete(`api/rooms/upload/${obj.id}`);
              }catch(e){}
            }
            
            for (let key in this.preview){
              var obj = this.preview[key]
              const configUploadFile = {
                headers: { "content-type": "multipart/form-data" }
              };
              let imageData = {
                room: this.room.id,
                file: obj
              }
              let formData = new FormData();
              formData.append('file',obj)
              formData.append('room',this.room.id)

              let response = await this.$axios.$post("api/rooms/upload/", formData, configUploadFile);
            }
          }
          
        } catch (e) {
          console.log(e);
        }
        try{
          this.room.creation_progress = 8
          this.room.published = true
          let response = await this.$axios.$patch(`api/rooms/${editedRoom.id}/`, editedRoom, config);
          this.$router.push("published");
        }catch(e){}
      }
    }



  };
</script>
