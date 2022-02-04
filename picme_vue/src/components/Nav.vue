<template>
  <nav>
    <!-- Nav Links Go Here -->
    <router-link to="/" name="Home" class="nav-btn">Home</router-link>
    <router-link to="/categoryform" class="nav-btn">Add a Category</router-link>
    <div v-if="categories">
      <div :key="category.id" v-for="category in categories">
        <div @click="selectCategory(category.id)" class="nav-btn">
          {{category.name}}
        </div>
      </div>
    </div>
    

  </nav>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Nav',
  data: () => ({
    categories: null
  }),
  mounted: function(){
    this.getCategories()
  },
  methods: {
    async getCategories() {
      const res = await axios.get(
        `http://localhost:8000/categories/`
      )
      this.categories = res.data
    },
    selectCategory(id){
      this.$router.push(`/categories/${id}`)
      this.$router.go()
    }
  }
}
</script>

<style scoped>
  .nav-btn{
    cursor: pointer;
    text-decoration: none;
    color: grey;
  }
  .nav-btn:hover{
    color:black
  }
  nav{
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
  }
</style>