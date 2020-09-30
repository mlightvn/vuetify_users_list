import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import Notifications from 'vue-notification'
import VueConfirmDialog from 'vue-confirm-dialog'
import router from './router'

Vue.config.productionTip = false

Vue.use(VueRouter)
Vue.use(Notifications)
Vue.use(VueConfirmDialog)

Vue.component('vue-confirm-dialog', VueConfirmDialog.default)

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
