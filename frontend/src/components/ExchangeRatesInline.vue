<template>
  <!-- Exchange Rate Display Component -->
  <div>
    <div class="px-md-3 ps-1 mt-md-0 mt-3">
      <!-- Loading Indicator -->
      <div v-if="isLoading" class="d-inline-flex">
        <span class="list-item pe-3">Loading...</span>
      </div>
      <!-- Exchange Rate Data -->
      <div v-else class="row">
        <template v-for="(rate, currency) in exchangeRate" :key="currency">
          <!-- Display Exchange Rate -->
          <span class="col-md-3 col-lg-2 col-6 py-2 list-item pe-md-3 pe-1">{{ currency }}: {{ rate }}</span>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    /**
     * The exchange rate data as an object where currency codes are keys and rates are values.
     * @type {Object}
     */
    exchangeRate: Object,
    /**
     * A boolean indicating whether the data is currently loading.
     * @type {Boolean}
     */
    isLoading: Boolean,
  },
};
</script>
