import axios from "axios";
import router from "./router";
import store from "./store";

const client = axios.create({
  baseURL: "http://127.0.0.1:8000/",
  headers: {
    "Content-Type": "application/json"
  },
});

client.interceptors.request.use(
  (config) => {
    let token = localStorage.getItem("accessToken") || "";
    config.headers["Authorization"] = `JWT ${token}`;
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

client.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    if (error.response.status == 401) {
      store.commit("logout");
      if (router.currentRoute.name === "login") {
        return Promise.reject(error);
      }
      router.push({ name: "login" });
    }
    return Promise.reject(error);
  }
);

export default client;