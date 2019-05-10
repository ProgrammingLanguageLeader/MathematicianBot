<template>
<b-container class="mt-2 mb-2" v-if="answer">
  <b-row align-h="center">
    <b-img id="answer-img" :src="answer" />
  </b-row>
</b-container>
</template>

<script>
export default {
  props: ['answer'],
  name: 'StyledInputGroup'
}
</script>

<style scoped>
#answer-img {
  max-width: 100%;
  width: auto;
}
</style>
