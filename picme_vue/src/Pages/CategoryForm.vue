<template>
  <div id="categoryform">
    <div class="form-container">
      <form @submit="handleSubmit">
        <h5>Create a new category</h5>
        <input placeholder="Category Name" :value="name" name="name" type="name" v-on:input="handleFormChange"/>
        <input placeholder="Description" :value="description" name="description" type="description" v-on:input="handleFormChange"/>
        <input placeholder="Image URL" :value="img_url" name="img_url" type="img_url" v-on:input="handleFormChange"/>
        <button type="submit">Submit Category</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'CategoryForm',
    data: () => ({
      name: '',
      description: '',
      img_url: ''
    }),
    methods: {
      handleFormChange(e) {
        this[e.target.name] = e.target.value
      },
      async handleSubmit(e) {
        e.preventDefault()
        const res = await axios.post(`http://localhost:8000/categories/`, {
          "name": this.name,
          "description": this.description,
          "img_url": this.img_url
          
        }, {
          auth: {
            username: 'picmeuser',
            password: 'picme'
          }
        })
        console.log(res)
        // this.name = res.data.name
        // this.description = res.data.description
        // this.img_url = res.data.img_url
        // this.category.push()
      }
    }
}
</script>


<style scoped>
    h3 {
        color: #80cbc4;
    }
    input {
      width: 500px;
      height: 60px;
      margin: 10px;    
      }

</style>