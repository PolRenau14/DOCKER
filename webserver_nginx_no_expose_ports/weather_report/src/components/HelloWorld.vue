<template>
  <div class="hello">
    <h1>Weather Report</h1>
    <div>
      Container's one name is: {{ container1_name }} 
      and container'2 two name is: {{container2_name}}!
    </div>
  </div>
</template>

<script>

  import axios from "axios";

  export default {
    name: 'HelloWorld',
    props: {
      msg: String
    },
    data() {
      return {
        container1_name: 'None',
        container2_name: 'None'
      };
    },
    async mounted() {
      await axios({ method: "GET", "url": "http://rfm-service:5000/" })
          .then(result => {
            this.container1_name = result.data['name'];
          }, error => {
            console.error(error);
          });

      await axios({ method: "GET", "url": "http://recomendation-service:5000/" })
          .then(result => {
            this.container2_name= result.data['name'];
          }, error => {
            console.error(error);
          });
    }
  }
  </script>

  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
</style>
