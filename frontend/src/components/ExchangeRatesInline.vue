<template>
    <div>
      <div class="container">
          <div v-if="isLoading" class="d-inline-flex">
              <span class="list-item pe-3">Loading...</span>
          </div>
          <div v-else class="d-inline-flex">
              <template v-for="(rate, currency) in exchangeRate" :key="currency">
                  <span class="list-item pe-3">{{ currency }}: {{ rate }}</span>
              </template>
          </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      exchangeRate: Object,
      isLoading: Boolean,
    },
  };
  </script>