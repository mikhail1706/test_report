<template>
  <v-card class="overflow-hidden">
    <v-app-bar
        color="#6A76AB"
        dark
        shrink-on-scroll
        prominent
        src="https://picsum.photos/1920/1080?random"
        fade-img-on-scroll
        scroll-target="#scrolling-techniques-3">
      <template v-slot:img="{ props }">
        <v-img
            v-bind="props"
            gradient="to top right, rgba(100,115,201,.7), rgba(25,32,72,.7)"
        ></v-img>
      </template>

      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Report Test Project</v-toolbar-title>
      <v-spacer></v-spacer>

      <v-btn outlined @click="logout">
        logout
      </v-btn>
      <!--      <v-btn icon>-->
      <!--        <v-icon>mdi-heart</v-icon>-->
      <!--      </v-btn>-->
      <!--      <v-btn icon>-->
      <!--        <v-icon>mdi-dots-vertical</v-icon>-->
      <!--      </v-btn>-->

      <template v-slot:extension>
        <v-tabs align-with-title>
          <template v-for="link in links">
            <v-tab :to="link.url">{{ link.title }}</v-tab>
          </template>
        </v-tabs>
      </template>
    </v-app-bar>
    <v-sheet
        id="scrolling-techniques-3"
        class="overflow-y-auto"
        max-height="600">
    </v-sheet>
  </v-card>
</template>

<script>
export default {
  name: "Navbar",
  data: () => ({
    links: [
      {title: 'Dashboard', url: '/', exact: true},
    ]
  }),
  methods: {
    logout() {
      this.$store.commit('removeToken')
      this.$store.commit('setAuthUser', {
        authUser: {},
        isAuthenticated: false
      })
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>

</style>