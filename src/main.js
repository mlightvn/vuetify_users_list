import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import Notifications from 'vue-notification'
import VueConfirmDialog from 'vue-confirm-dialog'

Vue.config.productionTip = false

Vue.use(Notifications)
Vue.use(VueConfirmDialog)

Vue.component('vue-confirm-dialog', VueConfirmDialog.default)

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
