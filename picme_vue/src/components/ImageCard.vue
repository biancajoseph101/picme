<template>
  <div class="image_card_container">
    <h4>{{ image_card.title }}</h4>
    <img :src="image_card.img" alt="picture" class="picture" />
    <button @click="deleteImage">Delete</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ImageCard',
  props: {
    image_card: Object
  },
  methods: {
    async deleteImage() {
        await axios.delete(`http://localhost:8000/images/${this.image_card.id}`, {
          auth: {
            username: 'picmeuser',
            password: 'picme'
          }
        })
        this.$emit('handleDelete', this.image_card.id)
    }
  }
}
</script>

<style scoped>

img {
  max-height: 200px;
}


</style>