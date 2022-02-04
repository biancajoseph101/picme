<template>
  <div id="app">
    <Nav/>
    <CategoryNav/>
    <!-- <Upload/> -->
    <router-view header="Header"></router-view>
  </div>
</template>

<script>

import Nav from './components/Nav.vue'
import CategoryNav from './components/CategoryNav.vue'

export default {
  name: 'App',
  components: {
    Nav,
    CategoryNav
    // Upload
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 10px;

}

</style>
