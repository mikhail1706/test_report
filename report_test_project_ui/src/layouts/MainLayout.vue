<template>
  <div>
    <Navbar />
    <router-view/>
  </div>

</template>

<script>
import Navbar from '@/components/app/Navbar'

export default {
  name: 'main-layout',
  data: () => ({}),
  mounted() {
  },
  components: {
    Navbar
  }
}
</script>
