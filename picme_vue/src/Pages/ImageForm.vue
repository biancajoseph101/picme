<template>
  <div id="imageform">
    <div class="form-container">
      <!-- <form @submit="handleSubmit"> -->
      <form>
        <h5>Add an Image</h5>
        <input
          placeholder="Category"
          :value="category"
          name="category"
          type="text"
          v-on:input="handleFormChange"
        />
        <input
          placeholder="Title"
          :value="title"
          name="title"
          type="text"
          v-on:input="handleFormChange"
        />
        <input :value="img" name="img" type="file" @change="onFileChanged" />
        <button type="submit" @click="onUpload">Upload</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'ImageForm',
  data: () => ({
    category: '',
    title: '',
    img: ''
    // selectedFile: null
  }),
  methods: {
    handleFormChange(e) {
      this[e.target.name] = e.target.value;
    },
    onFileChanged(e) {
      this.img = e.target.files[0];
      console.log(this.img);
    },
    onUpload(e) {
      e.preventDefault();
      //   let formData = new FormData();
      //   console.log(formData);
      //   formData.append('img', this.selectedFile);
      //   formData.append('category', this.category);
      //   formData.append('title', this.title);
      const newImg = {
        img: this.img,
        category: this.category,
        title: this.title
      };
      console.log(newImg);
      axios.post(`https://localhost:8000/images/`, newImg, {
        auth: {
          username: 'picmeuser',
          password: 'picme'
        }
      });
    }
    // async handleSubmit(e) {
    //   e.preventDefault();
    //   const res = await axios.post(
    //     `http://localhost:8000/images/`,
    //     {
    //       category: 'nature',
    //       title: 'spring',
    //       img: '/Users/bianca/ga_seir/unit4/projects/picme/picme_django/Autumn_Image.jpeg'
    //     },
    //     {
    //       auth: {
    //         username: 'picmeuser',
    //         password: 'picme'
    //       }
    //     }
    //   );
    //   console.log(res);
    // }
  }
};
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
