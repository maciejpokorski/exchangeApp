<template>
  <div class="container mt-5">
      <div class="row pb-5">
        <div class="col"><button type="button" class="btn btn-primary" @click="fetchData">Reload data</button></div>
      </div>
      <div class="row">
        <div class="col d-flex align-items-center">
          <div>
            <Datepicker v-model="date" :enable-time-picker="false" :max-date="new Date()"/>
          </div>
          <div>
            <ExchangeRatesInline :exchangeRates="exchangeRates" :isLoading="isLoading"></ExchangeRatesInline>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
import { toValue } from 'vue';
import ExchangeRatesInline from './components/ExchangeRatesInline.vue'
import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';

export default {
  name: 'App',
  components: {
    ExchangeRatesInline,
    Datepicker
  },
  data() {
    return {
        date: null,
        exchangeRates: null,
        isLoading: true,
    };
  },
  mounted() {
    this.date = new Date()
    this.fetchData()
  },
  methods: {
    async fetchData() {
      this.isLoading = true;
      const url = toValue("http://localhost:8000/fetch_data/" + this.date.toISOString().slice(0, 10))

      fetch(toValue(url))
        .then((res) => res.json())
        .then((json) => (this.exchangeRates = json))
        .catch((err) => (console.error("Error fetching data: " + err)))
        .finally(() => (this.isLoading = false));
    }
  },
}
</script>