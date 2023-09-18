---
title: Lambda DB Handler v0.1.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="lambda-db-handler">Lambda DB Handler v0.1.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

<h1 id="lambda-db-handler-default">Default</h1>

## main__get

<a id="opIdmain__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET / \
  -H 'Accept: application/json'

```

```http
GET / HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /`

*Default landing page which will redirect you to the docs*

> Example responses

> 200 Response

```json
null
```

<h3 id="main__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="main__get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## reset_reset_get

<a id="opIdreset_reset_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /reset \
  -H 'Accept: application/json'

```

```http
GET /reset HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/reset',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/reset',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/reset', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/reset', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/reset");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/reset", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /reset`

*Resets the state of the database*

<h3 id="reset_reset_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|reset|query|boolean|false|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="reset_reset_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="reset_reset_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## dump_dump_get

<a id="opIddump_dump_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /dump \
  -H 'Accept: application/json'

```

```http
GET /dump HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/dump',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/dump',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/dump', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/dump', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/dump");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/dump", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /dump`

*DUMPS THE MONGODB FOR TESTING*

> Example responses

> 200 Response

```json
null
```

<h3 id="dump_dump_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="dump_dump_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="lambda-db-handler-display">Display</h1>

All endpoints used by the family display

## get_user_hours_display_user_totals_get

<a id="opIdget_user_hours_display_user_totals_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /display/user-totals \
  -H 'Accept: application/json'

```

```http
GET /display/user-totals HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/display/user-totals',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/display/user-totals',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/display/user-totals', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/display/user-totals', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/display/user-totals");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/display/user-totals", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /display/user-totals`

*Get User Hours*

> Example responses

> 200 Response

```json
{
  "user_1": 81.5,
  "user_2": 85.25,
  "user_3": 84.75,
  "user_4": 79
}
```

<h3 id="get_user_hours_display_user_totals_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="get_user_hours_display_user_totals_get-responseschema">Response Schema</h3>

Status Code **200**

*Response Get User Hours Display User Totals Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="success">
This operation does not require authentication
</aside>

## get_family_timeslots_display_family_timeslots_get

<a id="opIdget_family_timeslots_display_family_timeslots_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /display/family-timeslots \
  -H 'Accept: application/json'

```

```http
GET /display/family-timeslots HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/display/family-timeslots',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/display/family-timeslots',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/display/family-timeslots', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/display/family-timeslots', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/display/family-timeslots");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/display/family-timeslots", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /display/family-timeslots`

*Get Family Timeslots*

> Example responses

> 200 Response

```json
{
  "body": [
    {
      "day": "monday",
      "time": "14:00",
      "slot_num": 56,
      "booked_users": [
        "family",
        "user_2"
      ]
    },
    {
      "day": "monday",
      "time": "14:15",
      "slot_num": 57,
      "booked_users": [
        "family"
      ]
    },
    {
      "day": "monday",
      "time": "14:30",
      "slot_num": 58,
      "booked_users": [
        "family"
      ]
    },
    {
      "day": "monday",
      "time": "14:45",
      "slot_num": 59,
      "booked_users": [
        "family"
      ]
    },
    {
      "day": "tuesday",
      "time": "15:00",
      "slot_num": 60,
      "booked_users": [
        "family",
        "user_2"
      ]
    }
  ]
}
```

<h3 id="get_family_timeslots_display_family_timeslots_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="get_family_timeslots_display_family_timeslots_get-responseschema">Response Schema</h3>

Status Code **200**

*Response Get Family Timeslots Display Family Timeslots Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="success">
This operation does not require authentication
</aside>

## get_free_timeslots_display_user_free_timeslots_get

<a id="opIdget_free_timeslots_display_user_free_timeslots_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /display/user-free-timeslots \
  -H 'Accept: application/json'

```

```http
GET /display/user-free-timeslots HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/display/user-free-timeslots',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/display/user-free-timeslots',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/display/user-free-timeslots', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/display/user-free-timeslots', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/display/user-free-timeslots");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/display/user-free-timeslots", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /display/user-free-timeslots`

*Gets the timeslots that have a certain number of free users. Each slot is sorted in descending order in terms of how many people are free during it*

<h3 id="get_free_timeslots_display_user_free_timeslots_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|min_num_users|query|integer|false|none|

> Example responses

> 200 Response

```json
{
  "body": [
    {
      "day": "monday",
      "time": "08:00",
      "slot_num": 32,
      "booked_users": [],
      "num_free_users": 4
    },
    {
      "day": "monday",
      "time": "08:15",
      "slot_num": 33,
      "booked_users": [],
      "num_free_users": 4
    },
    {
      "day": "monday",
      "time": "08:30",
      "slot_num": 34,
      "booked_users": [],
      "num_free_users": 4
    },
    {
      "day": "tuesday",
      "time": "14:30",
      "slot_num": 58,
      "booked_users": [
        "user_1"
      ],
      "num_free_users": 3
    },
    {
      "day": "tuesday",
      "time": "14:45",
      "slot_num": 59,
      "booked_users": [
        "user_1"
      ],
      "num_free_users": 3
    }
  ]
}
```

<h3 id="get_free_timeslots_display_user_free_timeslots_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="get_free_timeslots_display_user_free_timeslots_get-responseschema">Response Schema</h3>

Status Code **200**

*Response Get Free Timeslots Display User Free Timeslots Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="lambda-db-handler-figurines">Figurines</h1>

All endpoints used by the figurines display

## get_available_figurines_get

<a id="opIdget_available_figurines_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /figurines \
  -H 'Accept: application/json'

```

```http
GET /figurines HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/figurines',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/figurines',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/figurines', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/figurines', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/figurines");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/figurines", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /figurines`

*Gets map of all users and their availability for that timeslot. 1 represents busy, 0 represents free*

> Example responses

> 200 Response

```json
{
  "user_1": 0,
  "user_2": 1,
  "user_3": 0,
  "user_4": 3
}
```

<h3 id="get_available_figurines_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="get_available_figurines_get-responseschema">Response Schema</h3>

Status Code **200**

*Response Get Available Figurines Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="lambda-db-handler-whiteboard">Whiteboard</h1>

All endpoints used by the lambda board

## modify_calendar_whiteboard__user__post

<a id="opIdmodify_calendar_whiteboard__user__post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /whiteboard/{user} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /whiteboard/{user} HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "body": [
    {
      "day": "monday",
      "time_slot": 0,
      "data": "captured text"
    },
    {
      "day": "tuesday",
      "time_slot": 0,
      "data": "text"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/whiteboard/{user}',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/whiteboard/{user}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/whiteboard/{user}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/whiteboard/{user}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/whiteboard/{user}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/whiteboard/{user}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /whiteboard/{user}`

*Modify Calendar*

> Body parameter

```json
{
  "body": [
    {
      "day": "monday",
      "time_slot": 0,
      "data": "captured text"
    },
    {
      "day": "tuesday",
      "time_slot": 0,
      "data": "text"
    }
  ]
}
```

<h3 id="modify_calendar_whiteboard__user__post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|user|path|string|true|none|
|body|body|any|true|none|

> Example responses

> 200 Response

```json
{
  "body": [
    {
      "day": "monday",
      "time": "00:00",
      "slot_num": 0,
      "booked_users": [
        "user_2",
        "user_3",
        "user_1"
      ]
    },
    {
      "day": "tuesday",
      "time": "00:00",
      "slot_num": 0,
      "booked_users": [
        "user_1"
      ]
    }
  ]
}
```

<h3 id="modify_calendar_whiteboard__user__post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="modify_calendar_whiteboard__user__post-responseschema">Response Schema</h3>

Status Code **200**

*Response Modify Calendar Whiteboard  User  Post*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

<h2 id="tocS_TimeSlot">TimeSlot</h2>
<!-- backwards compatibility -->
<a id="schematimeslot"></a>
<a id="schema_TimeSlot"></a>
<a id="tocStimeslot"></a>
<a id="tocstimeslot"></a>

```json
{
  "day": "monday",
  "time_slot": 0,
  "data": "string"
}

```

TimeSlot

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|day|string|true|none|none|
|time_slot|integer|true|none|none|
|data|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|day|monday|
|day|tuesday|
|day|wednesday|
|day|thursday|
|day|friday|
|day|saturday|
|day|sunday|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[anyOf]|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msg|string|true|none|none|
|type|string|true|none|none|

<h2 id="tocS_WhiteboardRequest">WhiteboardRequest</h2>
<!-- backwards compatibility -->
<a id="schemawhiteboardrequest"></a>
<a id="schema_WhiteboardRequest"></a>
<a id="tocSwhiteboardrequest"></a>
<a id="tocswhiteboardrequest"></a>

```json
{
  "body": [
    {
      "day": "monday",
      "time_slot": 0,
      "data": "string"
    }
  ]
}

```

WhiteboardRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|body|[[TimeSlot](#schematimeslot)]|true|none|none|

