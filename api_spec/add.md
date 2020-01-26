**Addition**
----
  Returns the sum of two numbers a and b.

* **URL**

  /add

* **Method:**

  `POST`
  
* **Data Params**

  ```json
    {
        "a": 1234,
        "b": 1234
    }
  ```

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ "result" : 2468.0 }`
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />

* **Sample Call:**

  ```bash
    curl --request POST \
        --url http://localhost:6543/add \
        --header 'content-type: application/json' \
        --data '{
            "a": 1234,
            "b": 345
        }'
  ```