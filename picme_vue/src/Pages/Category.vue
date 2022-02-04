<template>
  <div v-if="catDetails">
    <h3>{{catDetails.name}}</h3>
    <img :src="catDetails.img_url" alt="">
    <div>{{catDetails.description}}</div>
    <div :key="image.id" v-for="image in imageList">
      <h3>{{image.title}}</h3>
      <img :src="image.img" alt="">
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Category',
    components: {
      // ImageCard
    },
    data: () => ({
      catDetails: null,
      imageList: null
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
        this.imageList = res.data.image_list
      }
    }
}
</script>


<style scoped>
    h3 {
        color: #80cbc4;
    }
</style>