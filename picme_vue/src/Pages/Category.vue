<template>
  <div v-if="catDetails">
    <h3>{{catDetails.name}}</h3>
    <img :src="catDetails.img_url" alt="">
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Category',
    components: {
      // PictureCard
    },
    data: () => ({
      catDetails: null
    }),
    mounted: function(){
      this.getCatDetails()
    },
    methods: {
      async getCatDetails() {
        let id = parseInt(this.$route.params.cat_id)
        const res = await axios.get(
          `http://localhost:8000/categories/${id}`
        )
        console.log(res.data)
        this.catDetails = res.data
      }
    }
}
</script>


<style scoped>
    h3 {
        color: #80cbc4;
    }
</style>