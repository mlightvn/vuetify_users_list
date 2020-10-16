import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta:{
      title: 'Homepage'
    },
  },
  {
    path: '/users',
    name: 'Users',
    meta:{
      title: 'Users List'
    },
    component: () => import('../views/users/List.vue')
  },
  {
    path: '/about',
    name: 'About',
    meta:{
      title: 'About me'
    },
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  routes
})

router.beforeEach((toRoute, fromRoute, next) => {
  let title = (toRoute.meta && toRoute.meta.title) ? toRoute.meta.title : 'Users List'
  window.document.title = title + ' | VUE DEMO'

  next()
})

export default router
