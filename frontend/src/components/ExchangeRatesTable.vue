<template>
  <!-- Exchange Rate Table Component -->
  <div class="table-responsive">
    <!-- Loading Indicator -->
    <div v-if="isLoading" class="d-inline-flex">
      <span class="list-item pe-3 my-4">Loading...</span>
    </div>
    <!-- Display Exchange Rate Table -->
    <table v-else class="table table-responsive table-striped mt-4">
      <thead>
        <tr>
          <!-- Table Header -->
          <th v-for="(value, key) in exchangeRates[0]" :key="value">{{ key }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="rate in exchangeRates" :key="rate">
          <!-- Table Data -->
          <td v-for="(key, value) in rate" :key="value">{{ key }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    /**
     * The exchange rate data as an array of objects, where each object represents a row of exchange rates.
     * @type {Object[]}
     */
    exchangeRates: Array,
    /**
     * A boolean indicating whether the data is currently loading.
     * @type {Boolean}
     */
    isLoading: Boolean,
  },
};
</script>
