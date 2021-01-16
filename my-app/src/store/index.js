import Vue from "vue";
import Vuex from "vuex";
import userService from "../services/user-service";
import {CityList} from "@/model/Cities";

Vue.use(Vuex);

const initialUser = () => {
  let token = localStorage.getItem("accessToken");
  if (token)
    return { loggedIn: true, username: "", role: "", accessToken: token };
  else return { loggedIn: false, username: "", role: "", accessToken: null };
};


function initialCity () {
  return {
    city_list: new CityList(),
  }
}

export default new Vuex.Store({
  state: {
    user: initialUser(),
    city: initialCity()
  },
  getters: {
    isLoggedIn: (state) => state.user.loggedIn,
    userData: (state) => state.user,
    cityData: (state) => state.city.city_list,
  },
  mutations: {
    loginSuccessful(state, token) {
      state.user.loggedIn = true;
      state.user.accessToken = token;
      localStorage.setItem("accessToken", token);
    },
    logout(state) {
      console.log(state)
    },
    weather(state) {
      (state.user.loggedIn = false), localStorage.removeItem("accessToken");
    },
    city(state, city_list){
      for (let i = 0; i < city_list.length; i++) {
        state.city.city_list.addItem(city_list[i])
      }
    },
    setUserData(state, userInfo) {
      (state.user.city = userInfo.city);
    },
  },
  actions: {
    loginRequest(context, credentials) {
      return userService
        .login(credentials)
        .then((res) => {
          context.commit("loginSuccessful", res.data.token);
          return Promise.resolve(res.data);
        })
        .catch((err) => {
          return Promise.reject(err);
        });
    },
    registerRequest(context, payload) {
      return userService
        .register(payload)
        .then((res) => {
          return Promise.resolve(res.data);
        })
        .catch((err) => {
          return Promise.reject(err);
        });
    },
    getUserData(context) {
      return userService
        .userDetail()
        .then((res) => {
          context.commit("setUserData", res.data);
          return Promise.resolve(res.data);
        })
        .catch((err) => {
          return Promise.reject(err);
        });
    },
    getCityData(context) {
      return userService
        .cities()
        .then((res) => {
          console.log(res.data)
          context.commit("city", res.data);
          return Promise.resolve(res.data);
        })
        .catch((err) => {
          return Promise.reject(err);
        });
    },
    logoutRequest(context) {
      return userService
        .logout()
        .then((res) => {
          context.commit("logout");
          return Promise.resolve(res.data);
        })
        .catch((err) => {
          return Promise.reject(err);
        });
    },
    getWeatherByCityName(context, payload) {
      return userService
        .weather(payload)
        .then((res) => {
          context.commit("weather");
          return Promise.resolve(res.data);
        })
        .catch((err) => {
          return Promise.reject(err);
        });
    },
  },
});