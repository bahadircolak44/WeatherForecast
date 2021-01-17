import Vue from "vue";
import App from "./App.vue";
import store from "./store";
import VModal from 'vue-js-modal'
import router from "./router";
import vSelect from 'vue-select'
Vue.component('v-select', vSelect)
import 'vue-select/dist/vue-select.css';
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";

Vue.config.productionTip = false;
Vue.use(VModal)

new Vue({
  render: (h) => h(App),
  store,
  router,
}).$mount("#app");