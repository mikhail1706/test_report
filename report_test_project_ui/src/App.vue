<template>
  <div id="app">
    <v-app>
      <component :is="layout">
        <router-view/>
      </component>
    </v-app>

  </div>
</template>

<script>
import EmptyLayout from '@/layouts/EmptyLayout'
import MainLayout from "@/layouts/MainLayout";

export default {
  computed: {
    layout() {
      return (this.$route.meta.layout || 'empty') + '-layout'
    }
  },
  components: {
    EmptyLayout, MainLayout
  }
}
</script>

<style>
@import 'https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900';
@import 'https://cdn.jsdelivr.net/npm/@mdi/font@4.x/css/materialdesignicons.min.css';
@import 'https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css';
</style>