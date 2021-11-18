<template>
  <b-container>
    <b-row class="mt-4">
      <b-col sm="6" offset-sm="3">
        <h3> Modifica profilo </h3>
        <form @submit.prevent="user" autocomplete="on">
          <b-alert fade dismissible variant="danger" :show="formErrorMessageGeneric">
            Attenzione: Si è verificato un errore durante il salvataggio dati.
          </b-alert>
          <b-alert fade dismissible variant="success" :show="formSuccessMessage">
            Salvataggio dati effettuato con successo. 
          </b-alert>
          <!-- username -->
          <label for="username" class="mt-2">Username:</label>
          <b-form-input id="username" type="text" v-model="formUsername" readonly></b-form-input>
          <!-- email -->
          <label for="email" class="mt-2">Email:</label>
          <b-form-input id="email" type="email" v-model="formEmail" readonly></b-form-input>
          <!-- first_name -->
          <label for="first-name" class="mt-2">Nome:</label>
          <b-form-input id="first-name" type="text" autocomplete="given-name" v-model="formFirstName" ></b-form-input>
          <!-- last_name -->
          <label for="last-name" class="mt-2">Cognome:</label>
          <b-form-input id="last-name" type="text" autocomplete="family-name" v-model="formLastName" ></b-form-input>
          <button class="btn btn-primary btn-block mt-2" type="submit"> 
            <i class="fa fa-edit"></i>
            Modifica 
          </button>
        </form> 
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  data() {
    return {
      formUsername: '',
      formEmail: '',
      formFirstName: '',
      formLastName: '',
      formSuccessMessage: false,
      formErrorMessageGeneric: false
    }
  },
  middleware: 'auth',
  layout: 'no-footer',
  computed: {
    ...mapGetters(['isAuthenticated', 'loggedInUser'])
  },
  mounted() {
    var self = this;
    self.formUsername = self.loggedInUser.username || '';
    self.formEmail = self.loggedInUser.email || '';
    self.formFirstName = self.loggedInUser.first_name || '';
    self.formLastName = self.loggedInUser.last_name || '';
  },
  methods: {
    async user() {
      var self = this;
      try {
        await self.$axios.put('rest-auth/user/', {
            pk: self.loggedInUser.pk,
            email: self.formEmail,
            username: self.formUsername,
            password: self.formPassword,
            first_name: self.formFirstName,
            last_name: self.formLastName
        }).then(function(data){
          self.formSuccessMessage = true;
          self.formErrorMessageGeneric = false;
        });
      } 
      catch (error) {
        // TODO: migliorare la segnalazione errori
        console.log(response.response.data);
        self.formSuccessMessage = false;
        self.formErrorMessageGeneric = true;
      }
    }
  }
}
</script>