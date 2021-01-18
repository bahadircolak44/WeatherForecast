<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <navigation></navigation>
      </div>
    </div>
    <div v-if="error.status" class="row mt-5">
      <div class="col d-flex justify-content-center">
        <div class="alert alert-danger">
          {{ error.message }}
        </div>
      </div>
    </div>
    <div class="row mt-5">
      <div class="col d-flex justify-content-center">
        <form @submit.prevent="register()">
          <div class="form-group">
            <label for="username">Username</label>
            <input
              type="text"
              class="form-control"
              id="username"
              aria-describedby="emailHelp"
              placeholder="Enter username"
              v-model="credentials.username"
            />
          </div>
          <div class="form-group">
            <label for="email">Email</label>
            <input
              type="email"
              class="form-control"
              id="email"
              placeholder="E-mail"
              v-model="credentials.email"
              required
            />
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input
              type="password"
              class="form-control"
              id="password"
              placeholder="Password"
              v-model="credentials.password"
              required
            />
          </div>
          <button
            type="submit"
            class="btn btn-primary btn-block">
            Register
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import Navigation from "@/components/Navigation";
export default {
  components: {
    Navigation,
  },
  data() {
    return {
      credentials: {
        username: "",
        email: "",
        password: ""
      },
      error: {
        status: false,
        message: "",
      },
    };
  },
  methods: {
    async register() {
      let payload = { ...this.credentials };
      try {
        await this.$store.dispatch("registerRequest", payload);
        this.$router.push({ name: "login" });
      } catch (error) {
        this.error.status = true;
        this.error.message =
          error.response.data.username[0] ||
          error.response.detail ||
          "Something went wrong!";
      }
    },
  },
  computed: {

  },
};
</script>

<style></style>
