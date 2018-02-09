import Vue from 'vue'
import Router from 'vue-router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap/dist/css/bootstrap.css'

import HelloWorld from '@/components/HelloWorld'
import ProductAdd from '@/components/ProductAdd'
import ProductList from '@/components/ProductList'
import NavBar from '@/components/NavBar'

Vue.use(Router)
Vue.use(BootstrapVue)
Vue.component('NavBar', NavBar)

const EventBus = new Vue()
Object.defineProperties(Vue.prototype, {
  $bus: {
    get: function () {
      return EventBus
    }
  }
})

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/product_list',
      name: 'ProductList',
      component: ProductList
    },
    {
      path: '/product_add',
      name: 'ProductAdd',
      component: ProductAdd
    }
  ]
})
