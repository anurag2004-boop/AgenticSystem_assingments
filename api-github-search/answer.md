

### 1. Role of Query Parameters

Query parameters are used to customize the API request and control the data returned by the server.

In this example:

* `q=python` → searches for repositories related to Python
* `sort=stars` → sorts repositories based on the number of stars
* `order=desc` → returns results in descending order (highest stars first)
* `per_page=5` → limits the number of results to 5

Without query parameters, the API would return default or unfiltered results.

---

### 2. Why use response.json() instead of response.text?

* `response.json()` converts the API response directly into a Python dictionary.
* This makes it easy to access data using keys like `data["items"]`.

On the other hand:

* `response.text` returns the raw response as a string (JSON format).
* You would then need to manually parse it using `json.loads()`.

So, `response.json()` is more convenient and efficient when working with APIs that return JSON data.
