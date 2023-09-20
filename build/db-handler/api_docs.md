---
title: Lambda DB Handler v0.1.0
language_tabs:
  - python: Python
language_clients:
  - python: ""
toc_footers: []
includes: []
search: false
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="lambda-db-handler">Lambda DB Handler v0.1.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

<h1 id="lambda-db-handler-default">Default</h1>

## Default landing page which will redirect you to the docs

<a id="opIdmain__get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/', headers = headers)

print(r.json())

```

`GET /`

> Example responses

> 200 Response

```json
null
```

<h3 id="default-landing-page-which-will-redirect-you-to-the-docs-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="default-landing-page-which-will-redirect-you-to-the-docs-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Resets the state of the database

<a id="opIdreset_reset_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/reset', headers = headers)

print(r.json())

```

`GET /reset`

<h3 id="resets-the-state-of-the-database-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|reset|query|boolean|false|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="resets-the-state-of-the-database-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="resets-the-state-of-the-database-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## DUMPS THE MONGODB FOR TESTING

<a id="opIddump_dump_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/dump', headers = headers)

print(r.json())

```

`GET /dump`

> Example responses

> 200 Response

```json
null
```

<h3 id="dumps-the-mongodb-for-testing-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="dumps-the-mongodb-for-testing-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="lambda-db-handler-display">Display</h1>

All endpoints used by the family display

## Get User Hours

<a id="opIdget_user_hours_display_user_totals_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/display/user-totals', headers = headers)

print(r.json())

```

`GET /display/user-totals`

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

<h3 id="get-user-hours-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="get-user-hours-responseschema">Response Schema</h3>

Status Code **200**

*Response Get User Hours Display User Totals Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="success">
This operation does not require authentication
</aside>

## Get Family Timeslots

<a id="opIdget_family_timeslots_display_family_timeslots_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/display/family-timeslots', headers = headers)

print(r.json())

```

`GET /display/family-timeslots`

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

<h3 id="get-family-timeslots-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="get-family-timeslots-responseschema">Response Schema</h3>

Status Code **200**

*Response Get Family Timeslots Display Family Timeslots Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="success">
This operation does not require authentication
</aside>

## Gets the timeslots that have a certain number of free users. Each slot is sorted in descending order in terms of how many people are free during it

<a id="opIdget_free_timeslots_display_user_free_timeslots_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/display/user-free-timeslots', headers = headers)

print(r.json())

```

`GET /display/user-free-timeslots`

<h3 id="gets-the-timeslots-that-have-a-certain-number-of-free-users.-each-slot-is-sorted-in-descending-order-in-terms-of-how-many-people-are-free-during-it-parameters">Parameters</h3>

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

<h3 id="gets-the-timeslots-that-have-a-certain-number-of-free-users.-each-slot-is-sorted-in-descending-order-in-terms-of-how-many-people-are-free-during-it-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="gets-the-timeslots-that-have-a-certain-number-of-free-users.-each-slot-is-sorted-in-descending-order-in-terms-of-how-many-people-are-free-during-it-responseschema">Response Schema</h3>

Status Code **200**

*Response Get Free Timeslots Display User Free Timeslots Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="lambda-db-handler-figurines">Figurines</h1>

All endpoints used by the figurines display

## Gets map of all users and their availability for that timeslot. 1 represents busy, 0 represents free

<a id="opIdget_available_figurines_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/figurines', headers = headers)

print(r.json())

```

`GET /figurines`

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

<h3 id="gets-map-of-all-users-and-their-availability-for-that-timeslot.-1-represents-busy,-0-represents-free-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="gets-map-of-all-users-and-their-availability-for-that-timeslot.-1-represents-busy,-0-represents-free-responseschema">Response Schema</h3>

Status Code **200**

*Response Get Available Figurines Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="lambda-db-handler-whiteboard">Whiteboard</h1>

All endpoints used by the lambda board

## Modify Calendar

<a id="opIdmodify_calendar_whiteboard__user__post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/whiteboard/{user}', headers = headers)

print(r.json())

```

`POST /whiteboard/{user}`

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

<h3 id="modify-calendar-parameters">Parameters</h3>

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

<h3 id="modify-calendar-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="modify-calendar-responseschema">Response Schema</h3>

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

