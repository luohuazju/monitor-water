<template>
  <div class="container">
    <b-container fluid>

      <!-- navbar-1.vue -->
      <NavBar/>

      <!-- jumbotron -->
      <b-jumbotron header="Welcome to Console"></b-jumbotron>

      <div>
        <h1>{{ msg }}</h1>
        <ul>
          <li v-for="(user, index) in users" :key="index">
            {{ user.firstname }} {{ user.lastname }}
          </li>
        </ul>
      </div>
      <div>
        <g-signin-button
          :params="googleSignInParams"
          @success="onSignInSuccess"
          @error="onSignInError">
          Sign in with Google
        </g-signin-button>
      </div>
      <div>
        <input type="text" v-model="username">
      </div>
      <div>
        <span v-text="username"></span>
      </div>
    </b-container>
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
      username: '',
      googleSignInParams: {
        client_id: '442664569962-tvl04h7ej0pa8sb8nq2ic5qm6hj05oa7.apps.googleusercontent.com'
      }
    }
  },
  methods: {
    onSignInSuccess (googleUser) {
      // `googleUser` is the GoogleUser object that represents the just-signed-in user.
      // See https://developers.google.com/identity/sign-in/web/reference#users
      const profile = googleUser.getBasicProfile() // etc etc
      const authResponse = googleUser.getAuthResponse(false)
      console.log(profile)
      console.log(authResponse)
    },
    onSignInError (error) {
      // `error` contains any error occurred.
      console.log('OH NOES', error)
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
.g-signin-button {
  /* This is where you control how the button looks. Be creative! */
  display: inline-block;
  padding: 4px 8px;
  border-radius: 3px;
  background-color: #3c82f7;
  color: #fff;
  box-shadow: 0 3px 0 #0f69ff;
}
</style>
