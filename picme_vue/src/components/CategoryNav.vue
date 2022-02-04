<template>
  <div class="category-nav">
    <div v-if="categories" class="flex-div">
      <div :key="category.id" v-for="category in categories">
        <div @click="selectCategory(category.id)" class="nav-btn">
          {{ category.name }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Nav',
  data: () => ({
    categories: null
  }),
  mounted: function () {
    this.getCategories();
  },
  methods: {
    async getCategories() {
      const res = await axios.get(`http://localhost:8000/categories/`);
      this.categories = res.data;
    },
    selectCategory(id) {
      this.$router.push(`/categories/${id}`);
      this.$router.go();
    }
  }
};
</script>

<style scoped>
.nav-btn {
  cursor: pointer;
  text-decoration: none;
  color: grey;
  display: flex;
  /* position: absolute; */
  justify-content: space-between;
  color: white;
}
.nav-btn:hover {
  color: white;
  font-weight: bolder;
}
.category-nav {
  background-color: gray;
  opacity: 50%;
  text-align: end;
  margin-bottom: 10px;
}
.flex-div {
  display: flex;
  justify-content: space-around;
}
</style>
