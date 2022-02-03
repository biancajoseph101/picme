<template>
  <div>
    <h4>{{ image_card.title }}</h4>
  </div>
</template>

<script>
export default {
  name: 'ImageCard',
  props: {
    image_card: Object
  }
}
</script>

<style scoped>

</style>