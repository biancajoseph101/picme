<template>
  <div class="upload">
      <div class="l">
      <label>File
        <input type="file" @change="handleFileUpload"/>
      </label>
      <button @click="submitFile">Submit</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Upload',
  data: () => ({
    file: null
  }),
  methods: {
    submitFile() {
        console.log(this.file)
        let formData = new FormData();
        formData.append('category', [2,3])
        formData.append('title', 'uploaded image')
        formData.append('img', this.file, this.file.name);

        console.log(formData)
        axios.post( 'http://localhost:8000/upload/',
          formData,
          {
            auth: {
              username: 'picmeuser',
              password: 'picme'
            }
          },
          {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          }
        ).then(function(){
          console.log('SUCCESS!!');
        })
        .catch(function(){
          console.log('FAILURE!!');
        });
    },
      handleFileUpload(event){
        console.log(event)
        this.file = event.target.files[0]
      }
  }
}
</script>

<style scoped>

  .upload {
    border: 2px solid black;
    border-radius: 5px;
  }

</style>