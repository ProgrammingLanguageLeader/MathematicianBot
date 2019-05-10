<template>
<b-container class="pt-4">
  <h3>Choose an option to start</h3>
  <b-list-group>
    <b-list-group-item to="/integral">
      Integral
    </b-list-group-item>
    <b-list-group-item to="/derivative">
      Derivative
    </b-list-group-item>
    <b-list-group-item to="/limit">
      Limit
    </b-list-group-item>
    <b-list-group-item to="/sum">
      Sum
    </b-list-group-item>
    <b-list-group-item to="/plot">
      Plot
    </b-list-group-item>
    <b-list-group-item to="/equation">
      Equation
    </b-list-group-item>
    <b-list-group-item to="/extrema">
      Extrema
    </b-list-group-item>
    <b-list-group-item to="/taylor-series">
      Taylor series
    </b-list-group-item>
    <b-list-group-item to="/manual-query">
      Manual query
    </b-list-group-item>
  </b-list-group>
</b-container>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped>
  h3 {
    padding: 10px;
  }
</style>
