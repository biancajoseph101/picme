<template>
  <div v-if="catDetails">
    <div class="container">
      <img :src="catDetails.img_url" alt="" class="blur">
      <div class="center">{{catDetails.name}}</div>
    </div>


    <div>{{catDetails.description}}</div>
    <div class="cont">
      <div :key="image_card.id" v-for="image_card in imageList" >
        <ImageCard v-bind:image_card="image_card" @handleDelete="handleDelete"/>
     </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import ImageCard from '../components/ImageCard.vue'
export default {
    name: 'Category',
    components: {
      ImageCard
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
      },
      handleDelete(id) {
        this.imageList = this.imageList.filter(image => image.id !== id)
      }
    }
}
</script>


<style scoped>
    h3 {
      color: #80cbc4;
    }
    img {
      height: 200px;
    }
    .cont {
      display: flex;
      flex-wrap: wrap;
      flex-direction: row;
      justify-content: space-around;
    }
    .container {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

.center {
  position: absolute;
  text-align: center;
  font-size: 50px;
}

img { 
  width: 100%;
  height: 100px;
  border-radius: 7px;
}

.blur {
 opacity: 0.4;
}
</style>