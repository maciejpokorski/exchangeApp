<template>
    <div class="table-responsive">
      <div v-if="isLoading" class="d-inline-flex">
          <span class="list-item pe-3 my-4">Loading...</span>
      </div>
      <table v-else class="table table-responsive table-striped mt-4">
          <thead>
          <tr>
            <th v-for="(value, key) in exchangeRates[0]" :key="value">{{ key }}</th>
          </tr>
          </thead>
          <tbody>
              <tr v-for="rate in exchangeRates" :key="rate">
                <td v-for="(key, value) in rate" :key="value">
                  {{ key }}
                 </td>
                </tr>
          </tbody>
      </table>
    </div>
  </template>

<script>
export default {
  props: {
    exchangeRates: Object,
    isLoading: Boolean,
  },
};
</script>