<template>
  <v-app>
    <v-container style="height: 100%">
      <v-row align-content="center" justify="center" style="height: 100%">
        <v-col cols="3">
          <div class="text-center text-h4 mb-5">Please sign in</div>
          <v-form ref="form" @submit.prevent="login">
            <v-text-field
                v-model="username"
                :error-messages="usernameErrors"
                label="Username"
                required
                outlined
                @input="$v.username.$touch()"
                @blur="$v.username.$touch()">
            </v-text-field>
            <v-text-field
                v-model="password"
                :error-messages="passwordErrors"
                type="password"
                label="Password"
                required
                outlined
                @input="$v.password.$touch()"
                @blur="$v.password.$touch()">
            </v-text-field>
            <v-btn color="blue darken-2"
                   dark
                   min-width="100%"
                   large
                   type="submit"
                   class="">
              Sign in
            </v-btn>
            <v-btn color="success darken-2"
                   dark
                   min-width="100%"
                   large
                   to="/register"
                   class="mt-2">
              Registration
            </v-btn>
          </v-form>
        </v-col>
      </v-row>
    </v-container>
  </v-app>

</template>

<script>
import {required} from "vuelidate/lib/validators"
import axios from 'axios'

export default {
  name: "Login",
  title: "Login",
  data: () => ({
    username: '',
    password: '',
  }),
  validations: {
    username: {required},
    password: {required}
  },
  methods: {
    login() {
      if (this.$v.$invalid) {
        this.$v.$touch()
        return
      }
      const userData = {
        username: this.username,
        password: this.password,
      }
      this.$store.dispatch('login', userData)
          .then(response => {
            this.$store.commit('updateToken', response.data.access)

            axios.get(`${this.$store.state.baseUrl}/auth/users/me/`,
                {
                  headers: {
                    Authorization: `JWT ${this.$store.state.auth.jwt}`,
                    'Content-Type': 'application/json'
                  }
                }).then(response => {
              this.$store.commit('setAuthUser',
                  {
                    authUser: response.data,
                    isAuthenticated: true
                  })
              this.$router.push('/')
            })
          }).catch(error => {
        console.log(error)
      })
    }
  },
  computed: {
    usernameErrors() {
      const errors = []
      if (!this.$v.username.$dirty) return errors
      !this.$v.username.required && errors.push('Name is required.')
      return errors
    },
    passwordErrors() {
      const errors = []
      if (!this.$v.password.$dirty) return errors
      !this.$v.password.required && errors.push('Password is required.')
      return errors
    }
  }
}
</script>

<style scoped>

</style>