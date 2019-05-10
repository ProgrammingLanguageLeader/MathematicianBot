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
        <b-input
          v-model="fromNumber"
          placeholder="optional"
        />
      </b-input-group>
      <b-input-group prepend="to" class="pt-1">
        <b-input
          v-model="toNumber"
          placeholder="optional"
        />
      </b-input-group>
    </b-form-group>

    <b-row align-h="center">
      <b-col md="6" sm="12">
        <b-button block type="submit" variant="primary">
          Submit
        </b-button>
      </b-col>
    </b-row>
  </b-form>

  <b-row align-h="center" class="pt-4" v-if="fetching">
    <b-spinner />
  </b-row>

  <b-container class="mt-2 mb-2" v-else-if="answer">
    <b-row align-h="center">
      <h4>Answer</h4>
    </b-row>
    <b-row align-h="center">
      <b-img id="answer-img" :src="answer" />
    </b-row>
  </b-container>

  <b-row align-h="center" class="p-2" v-else-if="error">
    Something went wrong...
  </b-row>
</b-container>
</template>

<script>
export default {
  methods: {
    async onSubmit (event) {
      event.preventDefault()
      const apiRoot = process.env.API_ROOT
      const apiEndpointUrl = new URL(`${apiRoot}/simple`)
      let requestString = `integrate ${this.integratingFunction} d${this.independentVariable}`
      if (this.fromNumber.length > 0) {
        requestString += ` from ${this.fromNumber}`
      }
      if (this.toNumber.length > 0) {
        requestString += ` to ${this.toNumber}`
      }
      const params = {
        'request': requestString
      }
      apiEndpointUrl.search = new URLSearchParams(params)
      this.fetching = true
      const response = await fetch(apiEndpointUrl)
      if (response.status !== 200) {
        this.error = true
        this.answer = null
      } else {
        this.error = false
        const reader = new FileReader()
        reader.onload = e => {
          this.answer = e.target.result
        }
        reader.readAsDataURL(await response.blob())
      }
      this.fetching = false
    }
  },
  data () {
    return {
      integratingFunction: 'x^2',
      independentVariable: 'x',
      fromNumber: '',
      toNumber: '',
      answer: null,
      fetching: false,
      error: false
    }
  }
}
</script>

<style scoped>
.input-group-text {
  width: 110px;
}

#answer-img {
  max-width: 100%;
  width: auto;
}
</style>
