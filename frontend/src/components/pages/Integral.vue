<template>
<b-container class="pt-4">
  <b-form @submit="onSubmit">
    <b-form-group label="Fill in the following fields to calculate integral" class="pt-2">
      <b-input-group prepend="function">
        <b-input
          v-model="integratingFunction"
          required
          placeholder="a function to integrate"
        />
      </b-input-group>
      <b-input-group prepend="differential" class="pt-1">
        <b-input
          v-model="independentVariable"
          required
          placeholder="an independent variable"
        />
      </b-input-group>
      <b-input-group prepend="from" class="pt-1">
        <b-input
          v-model="fromNumber"
          placeholder="an optional field"
        />
      </b-input-group>
      <b-input-group prepend="to" class="pt-1">
        <b-input
          v-model="toNumber"
          placeholder="an optional field"
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

  <AnswerImage v-else-if="answer" :answer="answer" />

  <b-row align-h="center" class="p-2" v-else-if="error">
    Something went wrong...
  </b-row>
</b-container>
</template>

<script>
import AnswerImage from '@/components/common/AnswerImage'
import {makeSimpleRequest} from '@/utils'

export default {
  components: {AnswerImage},
  methods: {
    async onSubmit (event) {
      event.preventDefault()
      let requestString = `integrate ${this.integratingFunction} d${this.independentVariable}`
      if (this.fromNumber.length > 0) {
        requestString += ` from ${this.fromNumber}`
      }
      if (this.toNumber.length > 0) {
        requestString += ` to ${this.toNumber}`
      }
      this.fetching = true
      try {
        const response = await makeSimpleRequest(requestString)
        this.answer = response
        this.error = Boolean(response)
      } catch (error) {
        console.log(error)
        this.error = true
      }
      this.fetching = false
    }
  },
  data () {
    return {
      integratingFunction: '',
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
</style>
