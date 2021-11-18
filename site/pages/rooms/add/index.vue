<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">CREA IL TUO ANNUNCIO</h2>
        <p>Con {{appname}} potrai creare il tuo annuncio gratuitamente! cosa aspetti! Crea subito il tuo annuncio!!</p>
        <form @submit.prevent="submitRoom">
          <button type="submit" class="btn btn-primary">Crea il tuo annuncio adesso</button>
        </form>
      </div>
      <div class="col-md-4">
        
      </div>
    </div>
  </main>
</template>
<script>
export default {
  head() {
    return {
      title: "Crea Annuncio"
    };
  },
  data() {
    return {
      room: {
        title: "Unknown",
        description: "Unknown",
        price: 0,
        category: 0,
        guests: 0,
        bedrooms: 0,
        beds: 0,
        bathrooms: 0,
        bathrooms_isprivate: false,
      },
      appname: "Flybnb"

    };
  },
  methods: {
    onFileChange(e) {
      let files = e.target.files || e.dataTransfer.files;
      if (!files.length) {
        return;
      }
      this.room.picture = files[0];
      this.createImage(files[0]);
    },
    createImage(file) {
      // let image = new Image();
      let reader = new FileReader();
      let vm = this;
      reader.onload = e => {
        vm.preview = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    async submitRoom() {
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      for (let data in this.room) {
        formData.append(data, this.room[data]);
      }
      try {
        let response = await this.$axios.$post("/api/rooms/", formData, config);
        console.log(response.id)
        this.$router.push("/rooms/"+response.id+"/add_edit/step1");
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>
<style scoped>
</style>