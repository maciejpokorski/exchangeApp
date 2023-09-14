/**
 * Fetch data from a remote API endpoint.
 * @param {string} url - The API endpoint URL.
 * @param {string} [method="GET"] - The HTTP method for the request (default is "GET").
 * @returns {Promise} A promise that resolves to the JSON response from the API.
 * @throws {Error} If the network response is not successful.
 */
async function fetchData(url, method = "GET") {
    const baseUrl = process.env.VUE_APP_API_BASE;
    const response = await fetch(baseUrl + url, { method });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return await response.json();
}

/**
 * Fetch remote data for a specific date.
 * @param {Date} date - The date for which to fetch data.
 * @returns {Promise} A promise that resolves to the fetched data.
 */
export async function fetchRemoteData(date) {
    const url = `fetch_remote_data/${date.toISOString().slice(0, 10)}`;
    return fetchData(url);
}
  
/**
 * Fetch local data from a specific API endpoint.
 * @returns {Promise} A promise that resolves to the fetched local data.
 */
export async function fetchLocalData() {
    const url = 'fetch_local_data/';
    return fetchData(url);
}

/**
 * Fetch a list of currencies.
 * @returns {Promise} A promise that resolves to a list of currencies.
 */
export async function fetchCurrencies() {
    const url = "get_currencies/";
    return fetchData(url);
}
  
/**
 * Update the status of a currency (enabled or disabled).
 * @param {Object} currency - The currency object to update.
 * @returns {Promise} A promise that resolves to the updated currency object.
 * @throws {Error} If there is an error during the update.
 */
export async function updateCurrencyStatus(currency) {
    currency.enabled = !currency.enabled;
    const url = `update_currency/${currency.id}?enabled=${currency.enabled}`;
    try {
        return fetchData(url, "PATCH");
    }
    catch (error) {
        // Rollback the status change if there's an error
        currency.enabled = !currency.enabled;
        throw error;
    }
}
