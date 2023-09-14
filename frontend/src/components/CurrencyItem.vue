<template>
  <!-- Currency Card Component -->
  <div class="p-2 col-sm-2 col-6 border">
    <div class="card-body">
      <!-- Currency Code -->
      <h5 class="card-title">{{ currency.code }}</h5>
      <!-- Currency Status -->
      <p
        :class="{
          'text-success': currency.enabled,
          'text-danger': !currency.enabled
        }">
        Status: {{ currency.enabled ? 'Enabled' : 'Disabled' }}
      </p>
      <!-- Toggle Status Button -->
      <button @click="toggleStatus" class="btn btn-primary">
        {{ currency.enabled ? 'Disable' : 'Enable' }}
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    /**
     * The currency object to be displayed and modified.
     * @type {Object}
     */
    currency: Object,
  },
  methods: {
    /**
     * Toggles the status of the currency and emits an event.
     */
    toggleStatus() {
      this.$emit('toggle-status', this.currency)
    },
  },
};
</script>
