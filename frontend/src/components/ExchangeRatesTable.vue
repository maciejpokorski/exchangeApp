<template>
    <div>
      <table class="table mt-4">
          <thead>
          <tr>
            <th v-for="(value, key) in exchangeRates[0]" :key="key">{{ key }}</th>
          </tr>
          </thead>
          <tbody>
              <tr v-for="rate in exchangeRates" :key="rate">
                <td v-for="(key, value) in rate" :key="key">
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