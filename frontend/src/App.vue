<template>
  <!-- Main App Component -->
  <div class="container mt-5">
    <!-- Header Row -->
    <div class="row pb-5">
      <div class="col">
        <!-- Reload Button -->
        <button
          type="button"
          class="btn btn-primary"
          :disabled="isLoading"
          @click="reloadTable()"
        >
          Reload data
        </button>
      </div>
    </div>
    <!-- Datepicker and Exchange Rate Display -->
    <div class="row">
      <div class="col d-md-flex align-items-center">
        <!-- Datepicker Component -->
        <div>
          <Datepicker
            v-model="date"
            :clearable="false"
            @update:model-value="fetchData"
            :enable-time-picker="false"
            :max-date="new Date()"
          />
        </div>
        <div class="flex-fill">
          <!-- ExchangeRatesInline Component -->
          <ExchangeRatesInline
            :exchangeRate="exchangeRate"
            :isLoading="isLoading"
          ></ExchangeRatesInline>
        </div>
      </div>
      <!-- ExchangeRatesTable Component -->
      <div>
        <ExchangeRatesTable
          :exchangeRates="exchangeRates"
          :isLoading="isLoading"
        ></ExchangeRatesTable>
      </div>
    </div>
    <!-- Currency List Component -->
    <div class="row">
      <div class="col-md-12">
        <CurrencyList @update-currency="updateCurrencyStatus"></CurrencyList>
      </div>
    </div>
  </div>
</template>

<script>
import ExchangeRatesInline from './components/ExchangeRatesInline.vue';
import ExchangeRatesTable from './components/ExchangeRatesTable.vue';
import CurrencyList from './components/CurrencyList.vue';
import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';
import { fetchRemoteData, fetchLocalData, updateCurrencyStatus } from './api.js'

export default {
  name: 'App',
  components: {
    ExchangeRatesInline,
    ExchangeRatesTable,
    CurrencyList,
    Datepicker,
  },
  data() {
    return {
      // Selected date for exchange rate data
      date: null,
      // Current exchange rate
      exchangeRate: null,
      // List of exchange rates
      exchangeRates: [],
      // Loading indicator
      isLoading: true,
    };
  },
  async mounted() {
    // Initialize date with the current date
    this.date = new Date();
    // Fetch exchange rate data on component mount
    await this.fetchData();
  },
  methods: {
    /**
     * Fetch exchange rate data for the selected date.
     */
    async fetchData() {
      this.isLoading = true;
      this.exchangeRate = await fetchRemoteData(this.date);
      this.isLoading = false;
    },
    /**
     * Reload the exchange rate table data.
     */
    async reloadTable() {
      this.fetchData();
      this.exchangeRates = [];
      this.exchangeRates = await fetchLocalData();
    },
    /**
     * Update the status of a currency.
     * @param {Object} currency - The currency object to update.
     */
    async updateCurrencyStatus(currency) {
      await updateCurrencyStatus(currency);
    },
  },
};
</script>
