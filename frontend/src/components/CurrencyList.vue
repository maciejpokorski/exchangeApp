<template>
  <div class="accordion" id="accordionExample">
    <div class="accordion-item">
      <h2 class="accordion-header" id="headingOne">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
          Configure currencies
        </button>
      </h2>
      <div id="collapseOne" class="accordion-collapse collapse" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
        <div class="accordion-body">
          <h1>Currency List</h1>
          <input
            v-model="search"
            class="form-control mb-3"
            placeholder="Search currencies"
          />
          <div class="container">
            <div class="d-flex flex-row row">
                <CurrencyItem
                  v-for="currency in filteredCurrencies"
                  :key="currency.id"
                  :currency="currency"
                  @toggle-status="updateCurrencyStatus"
                />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  </template>
  
  <script>
  import CurrencyItem from "./CurrencyItem.vue";
  
  export default {
    components: {
      CurrencyItem,
    },
    data() {
      return {
        currencies: [],
        search: '',
      };
    },
    mounted() {
      this.fetchData();
    },
    computed: {
      filteredCurrencies() {
        return this.currencies.filter(currency => {
          return currency.code.toLowerCase().includes(this.search.toLowerCase())
        })
      }
    },
    methods: {
        fetchData() {
            const url = "http://localhost:8000/get_currencies/";
            fetch(url).then((res) => res.json()).then((json) => (this.currencies = json)).catch((err) => (console.error("Error fetching data: " + err)))
        },
        updateCurrencyStatus(updatedCurrency) {
            // Find the index of the updated currency in the array
            const index = this.currencies.findIndex(currency => currency.id === updatedCurrency.id);
            if (index !== -1) {
                this.currencies[index].enabled = updatedCurrency.enabled;
                this.$emit('update-currency', updatedCurrency)
            }
      },
    },
  };
  </script>