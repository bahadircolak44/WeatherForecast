<template lang="pug">
div
  b \#{{item.id}}
  span  {{ item.city_name }}
</template>

<script>
export default {
  props: {
    item: { required: true }
  }
}
</script>
