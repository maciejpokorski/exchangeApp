<template>
    <div>
      <div class="px-md-3 ps-1 mt-md-0 mt-3">
          <div v-if="isLoading" class="d-inline-flex">
              <span class="list-item pe-3">Loading...</span>
          </div>
          <div v-else class="row">
              <template v-for="(rate, currency) in exchangeRate" :key="currency">
                  <span class="col-md-3 col-lg-2 col-6 py-2 list-item pe-md-3 pe-1">{{ currency }}: {{ rate }}</span>
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