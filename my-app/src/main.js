import Vue from "vue";
import App from "./App.vue";
import store from "./store";
import router from "./router";
import vSelect from "vue-select";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import 'vue-select/dist/vue-select.css';
Vue.component("v-select", vSelect);
Vue.config.productionTip = false;

new Vue({
  render: (h) => h(App),
  store,
  router,
}).$mount("#app");