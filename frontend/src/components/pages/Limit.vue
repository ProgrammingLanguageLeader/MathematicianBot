<template>
<b-container class="pt-4">
  <b-form @submit="onSubmit">
    <b-form-group label="Fill in the following fields to calculate limit" class="pt-2">
      <b-input-group prepend="function">
        <b-input
          v-model="limitFunction"
          required
          placeholder="a function to calculate limit"
        />
      </b-input-group>
      <b-input-group prepend="variable" class="pt-1">
        <b-input
          v-model="independentVariable"
          required
          placeholder="an independent variable"
        />
      </b-input-group>
      <b-input-group prepend="tends to" class="pt-1">
        <b-input
          v-model="tendingNumber"
          required
          placeholder="variable -> <this number>"
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
      const requestString = `limit ${this.limitFunction} when ${this.independentVariable} -> ${this.tendingNumber}`
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
      limitFunction: '',
      independentVariable: 'x',
      tendingNumber: 'infinity',
      answer: null,
      fetching: false,
      error: false
    }
  }
}
</script>

<style scoped>
</style>
