<template>
  <div id="navbar">
    <b-navbar toggleable="md" type="dark" variant="info">
      <b-nav-toggle target="nav_collapse"></b-nav-toggle>
      <img src="../assets/logo.png">
      <b-navbar-brand href="/">Home</b-navbar-brand>
      <b-collapse is-nav id="nav_collapse">
        <!-- Right aligned nav items -->
        <b-nav b-nav-bar class="ml-auto">
          <b-nav b-nav-bar>
            <b-nav-item href="#/product_list">Product List</b-nav-item>
            <b-nav-item href="#/product_add">Add Product</b-nav-item>
            <b-nav-item href="#/water_release">Water Release</b-nav-item>
          </b-nav>
        </b-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'NavBar'
}
</script>

<style>
img {
  height: 50px;
}
</style>
