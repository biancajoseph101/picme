<template>
  <div>
    <h3>This is home</h3>
      <section class="image container-grid">
        <div v-for="image_card in image_array" :key="image_card.id">
          <ImageCard v-bind:image_card="image_card" @handleDelete="handleDelete"/>
        </div>
      </section>
  </div>
</template>

<script>
import ImageCard from '../components/ImageCard.vue'
import axios from 'axios'
export default {
    name: 'HomePage',
    components: {
      ImageCard
    },
    data: () => ({
      image_array: []
    }),
    mounted() {
      this.getImages()
    },
    methods: {
      async getImages() {
        const res = await axios.get(`http://localhost:8000/images/`)
        this.image_array = res.data
      },
      handleDelete(id) {
        this.image_array = this.image_array.filter(image => image.id !== id)
      }
    }
}
</script>


<style scoped>
    h3 {
        color: #80cbc4;
    }
</style>