<template>
  <div class="hello">
    <div>
      <h1>{{ msg }}</h1>
      <ul>
        <li v-for="(user, index) in users" :key="index">
          {{ user.firstname }} {{ user.lastname }}
        </li>
      </ul>
    </div>
    <div>
      <input type="text" v-model="username">
    </div>
    <div>
      <span v-text="username"></span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      users: [
        {firstname: 'Carl', lastname: 'Luo'},
        {firstname: 'Rachel', lastname: 'Kang'},
        {firstname: 'Leo', lastname: 'Luo'}
      ],
      username: ''
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
