<template>
  <v-app>
    <v-container>
      <v-row align-content="center" justify="center">
        <v-col cols="3">
          <div class="text-center text-h4 mb-5">Registration</div>
          <v-form @submit.prevent="register">
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
                v-model="email"
                :error-messages="emailErrors"
                label="Email"
                required
                outlined
                @input="$v.email.$touch()"
                @blur="$v.email.$touch()">
            </v-text-field>
            <v-text-field
                v-model="password"
                :error-messages="passwordErrors"
                label="Password"
                required
                outlined
                type="password"
                @input="$v.password.$touch()"
                @blur="$v.password.$touch()">
            </v-text-field>
            <v-text-field
                v-model="re_password"
                label="Password confirm"
                :error-messages="passwordConfirmErrors"
                required
                outlined
                type="password"
                @input="$v.re_password.$touch()"
                @blur="$v.re_password.$touch()"
            ></v-text-field>
            <v-btn color="success"
                   type="submit"
                   large block>
              Submit
            </v-btn>
          </v-form>
        </v-col>
      </v-row>
    </v-container>
  </v-app>

</template>

<script>
import {email, minLength, required, sameAs} from "vuelidate/lib/validators";

export default {
  name: 'Register',
  title: 'Register',
  data: () => ({
    email: '',
    username: '',
    password: '',
    re_password: '',
  }),
  validations: {
    username: {required},
    email: {
      required,
      email
    },
    password: {
      required,
      minLength: minLength(8)
    },
    re_password: {
      sameAsPassword: sameAs('password')
    },
  },
  methods: {
    register() {
      if (this.$v.invalid) {
        this.$v.touch()
        return
      }
      const userData = {
        username: this.username,
        email: this.email,
        password: this.password
      }

      this.$store.dispatch('registration', userData)
          .then(response => {
            this.$router.push('/login')
          }).catch(error => {
            alert(error)
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
    emailErrors() {
      const errors = []
      if (!this.$v.password.$dirty) return errors
      !this.$v.password.required && errors.push('Email is required.')
      return errors
    },
    passwordErrors() {
      const errors = []
      if (!this.$v.password.$dirty) return errors
      !this.$v.password.required && errors.push('Password is required.')
      return errors
    },
    passwordConfirmErrors() {
      const errors = []
      if (!this.$v.re_password.$dirty) return errors
      !this.$v.re_password.sameAsPassword && errors.push('Passwords must be identical')
      return errors
    }
  }
}
</script>
