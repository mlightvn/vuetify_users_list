import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'

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
      title: process.env.VUE_APP_TITLE
    },
    component: () => import('@/views/users/List.vue')
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
    component: () => import(/* webpackChunkName: "about" */ '@/views/About.vue')
  },

  {
    path: "/blockchain",
    name: "blockchain",
    meta:{
      title: 'Blockchain'
    },

    component: () => import("@/views/blockchain/Index.vue"),
    children: [
      {
        path: "donate",
        name: "blockchain-donate",
        meta:{
          title: 'Donate coin'
        },
        component: () => import("@/views/blockchain/donate/Index.vue"),
      },
    ],
  },

  {
    path: "/administration",
    name: "administration",
    meta:{
      title: 'Administration'
    },

    component: () => import("@/views/administration/Index.vue"),
    children: [
      {
        path: "management",
        name: "administration-management",
        meta:{
          title: 'Management'
        },
        component: () => import("@/views/administration/management/Index.vue"),
      },
      {
        path: "setting",
        name: "administration-setting",
        meta:{
          title: 'Setting'
        },
        component: () => import("@/views/administration/setting/Index.vue"),
      },
    ],
  },

  {
    path: "/:pathMatch(.*)*",
    name: "error_404",
    component: () => import("@/views/errors/error-404.vue"),
  },
]

const router = new VueRouter({
  routes
})

router.beforeEach((toRoute, fromRoute, next) => {
  let title = (toRoute.meta && toRoute.meta.title) ? toRoute.meta.title : 'Homepage'
  window.document.title = title + ' | ' + process.env.VUE_APP_TITLE

  next()
})

export default router
