import { createApp } from 'vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle.js';

const app = createApp(App)

app.config.errorHandler = function (err) {
    console.error(err)
    alert("Sorry, something went wrong. Please try again later. Error details in the console.")
}
app.mount('#app')