<template>
<b-container class="pt-4">
  <b-form @submit="onSubmit">
    <b-form-group label="Enter the following fields to calculate integral" class="pt-2">
      <b-input-group prepend="function">
        <b-input
          id="integrating-function"
          v-model="integratingFunction"
          required
          placeholder="Enter the function"
        />
      </b-input-group>
      <b-input-group prepend="differential: " class="pt-1">
        <b-input
          v-model="independentVariable"
          required
          placeholder="Independent variable"
        />
      </b-input-group>
      <b-input-group prepend="from" class="pt-1">
        <b-input />
      </b-input-group>
      <b-input-group prepend="to" class="pt-1">
        <b-input />
      </b-input-group>
    </b-form-group>

    <b-button type="submit" variant="primary">
      Submit
    </b-button>
  </b-form>
</b-container>
</template>

<script>
export default {
  methods: {
    onSubmit (event) {
      event.preventDefault()
      console.log(this.integratingFunction)
    }
  },
  data () {
    return {
      integratingFunction: 'x^2',
      independentVariable: 'x'
    }
  }
}
</script>

<style scoped>
.input-group-text {
  width: 110px;
}
</style>
