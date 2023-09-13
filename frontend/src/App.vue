<template>
  <div class="container mt-5">
      <div class="row pb-5">
        <div class="col"><button type="button" class="btn btn-primary" :disabled="isLoading" @click="reloadTable()">Reload data</button></div>
      </div>
      <div class="row">
        <div class="col d-md-flex align-items-center">
          <div>
            <Datepicker v-model="date" :clearable="false" @update:model-value="fetchData" :enable-time-picker="false" :max-date="new Date()"/>
          </div>
          <div>
            <ExchangeRatesInline :exchangeRate="exchangeRate" :isLoading="isLoading"></ExchangeRatesInline>
          </div>
        </div>
        <div>
          <ExchangeRatesTable :exchangeRates="exchangeRates" :isLoading="isLoading"></ExchangeRatesTable>
        </div>
      </div>
      <div class="row">
        <div class="col-12 col-sm-10">
          <CurrencyList @update-currency="updateCurrencyStatus"></CurrencyList>
        </div>
      </div>
  </div>
</template>

<script>
import { toValue } from 'vue';
import ExchangeRatesInline from './components/ExchangeRatesInline.vue'
import ExchangeRatesTable from './components/ExchangeRatesTable.vue'
import CurrencyList from './components/CurrencyList.vue'
import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';

export default {
  name: 'App',
  components: {
    ExchangeRatesInline,
    ExchangeRatesTable,
    CurrencyList,
    Datepicker
  },
  data() {
    return {
        date: null,
        exchangeRate: null,
        exchangeRates: [],
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
      const url = toValue("http://localhost:8000/fetch_remote_data/" + this.date.toISOString().slice(0, 10))

      return fetch(toValue(url))
        .then((res) => res.json())
        .then((json) => (this.exchangeRate = json))
        .catch((err) => (console.error("Error fetching data: " + err)))
        .finally(() => (this.isLoading = false));
    },
    reloadTable() {
      this.fetchData()
      this.exchangeRates = []
      const url = "http://localhost:8000/fetch_local_data/"
      fetch(url).then((res) => res.json()).then((json) => (this.exchangeRates = json)).catch((err) => (console.error("Error fetching data: " + err)))
    },
    updateCurrencyStatus(currency) {
      currency.enabled = !currency.enabled;
      // Send a PATCH request to update the enabled status using fetch
      fetch(`http://localhost:8000/update_currency/${currency.id}?enabled=${currency.enabled}`, {
        method: 'PATCH',
      })
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .catch(error => {
          console.error('Error updating currency:', error);
          // Rollback the status change if there's an error
          currency.enabled = !currency.enabled;
        });
    },
  },
}
</script>