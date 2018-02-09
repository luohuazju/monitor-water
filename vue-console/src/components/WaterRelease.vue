<template>
  <div class="container">
    <b-container fluid>

      <!-- navbar-1.vue -->
      <NavBar/>
      <line-example></line-example>
    </b-container>
  </div>
</template>

<script>
import LineExample from '../components/LineChart.js'
export default {
  name: 'app',
  components: {
    LineExample
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
  width: 80%;
}
h1, h2 {
  font-weight: normal;
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
