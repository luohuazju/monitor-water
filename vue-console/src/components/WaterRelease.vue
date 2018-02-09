<template>
  <div class="container">
    <b-container fluid>
      <!-- navbar-1.vue -->
      <NavBar/>
      <LineChart :chart-data="datacollection"/>
      <button @click="fillData()">Fetch Data</button>
    </b-container>
  </div>
</template>

<script>
import LineChart from '../components/LineChart.js'
export default {
  components: {
    LineChart
  },
  data () {
    return {
      datacollection: { labels: [], datasets: [] }
    }
  },
  mounted () {
    // this.fillData()
  },
  methods: {
    fillData () {
      let result = {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#FC2525',
            data: [40, 39, 10, 40, 39, 80, 40]
          }, {
            label: 'Data Two',
            backgroundColor: '#05CBE1',
            data: [60, 55, 32, 10, 2, 12, 53]
          }
        ]
      }
      this.datacollection = result
    }
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
