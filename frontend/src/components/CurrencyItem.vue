<template>
    <div class="p-2 col-sm-2 col-6 border">
      <div class="card-body">
        <h5 class="card-title">{{ currency.code }}</h5>
        <p  
        :class="{
          'text-success': currency.enabled,
          'text-danger': !currency.enabled
        }">
            Status: {{ currency.enabled ? 'Enabled' : 'Disabled' }}</p>
        <button @click="toggleStatus" class="btn btn-primary">{{ currency.enabled ? 'Disable' : 'Enable' }}</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      currency: Object,
    },
    methods: {
      toggleStatus() {
        this.$emit('toggle-status', this.currency)
      },
    },
  };
  </script>