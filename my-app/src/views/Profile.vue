<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <navigation></navigation>
      </div>
    </div>
    <div class="row mt-5">
      <div class="col">
        <div class="jumbotron jumbotron">
          <div class="container">
            <h1 class="display-5">Hi {{ cityData }}!</h1>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navigation from "@/components/Navigation";
import { mapActions, mapGetters } from "vuex";
export default {
  components: {
    Navigation,
  },
  methods: {
    ...mapActions(["getCityData"]),
  },
  created() {
    this.getCityData().catch(() => {});
  },
  computed: {
    ...mapGetters(["cityData"]),
  },
};
</script>

<style></style>
