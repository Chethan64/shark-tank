# Sharktank
Simple RESTful API backend where budding entrepreneurs can pitch ideas for a business or product they wish to develop by providing their name, title & idea for the business, investment amount they expect to be fulfilled and the percentage of equity they are ready to shed away to the potential investors. Investors must be able to retrieve the list of all pitches and share their feedback/comment with a counter offer as per their interests.

The implementation is done using Python, Flask and MongoDB. PyMongo distribution is used to interact with the MongoDB database using Python.

### How to get the server running

```
bash ./setup.sh
bash ./server_run.sh
```

- ```setup.sh``` has the shell commands to install the required packages for the setup from ```requirements.txt```. Recommended to run the script file in a dedicated python virtual environment
- ```server_run.sh``` starts the flask backend application at *localhost* and *port 8081*
- ```src/app.py``` is the flask application which has the routines for REST API endpoints
- ```src/database/db.py``` imports pymongo, sets up a client and creates a database called "xharktank"
- ```src/validate/validreq.py``` contains methods to validate offer and pitch requests

----

The interaction between the frontend and backend is based on a REST API with support for the below endpoints and specifications

### 1. Endpoint to post a pitch to the backend

`/pitches`

HTTP endpoint : `/pitches`

HTTP method : `POST`

**Request body**

```json
{
    "entrepreneur": "string",
    "pitchTitle" : "string",
    "pitchIdea" : "string",
    "askAmount": "float",
    "equity" : "float"
}
```

**Request example**

```json
{
    "entrepreneur": "Ashok kumar",
    "pitchTitle" : "Crio.Do - Work-experience based learning programs for developers",
    "pitchIdea" : "Build professional projects like the top 1% developers. Master the latest full stack and backend tech with real work-ex. Crack developer jobs at the best tech companies.",
    "askAmount": 10000000.25,
    "equity" : 12.5
}
```

**Success response**

Response code : `201 CREATED`

**Response body**

```json
{
    "id": "1"
}
```

**Error response**

Condition : Invalid request body

Response code : `400 BAD REQUEST`

----

### 2. Endpoint to make a counter offer for a pitch to the backend

`/pitches/<pitch_id>/makeOffer`

HTTP endpoint : `/pitches/<pitch_id>/makeOffer`

HTTP method : `POST`

**Request body**

```json
{
    "investor": "string",
    "amount" : "float",
    "equity" : "float",
    "comment": "string"
}
```

**Request example**

```json
{
    "investor": "Anupam Mittal",
    "amount" : 10000000.56,
    "equity" : 20.2,
    "comment": "A new concept in the ed-tech market. I can relate with the importance of the Learn By Doing philosophy. Keep up the Good Work! Definitely interested to work with you to scale the vision of the company!"
}
```

**Success response**

Response code : `201 CREATED`

**Response body**

```json
{
    "id": "1"
}
```

**Error response**

-   Condition : Invalid request body

    Response code : `400 BAD REQUEST`

-   Condition : Pitch not found

    Response code : `404 NOT FOUND`

----

### 3. Endpoint to fetch the all the pitches in the reverse chronological order ( i.e. last created one first ) from the backend

`/pitches`

HTTP endpoint : `/pitches`

HTTP method : `GET`

**Success Response**

Response code : `200 OK`

**Response body**

```json
[
    {
        "id": "string",
        "entrepreneur": "string",
        "pitchTitle" : "string",
        "pitchIdea" : "string",
        "askAmount": "float",
        "equity" : "float"
        "offers": [
            {
                "id": "string",
                "investor": "string",
                "amount" : "float",
                "equity" : "float",
                "comment": "string"
            }
        ]
    }
]
```

**Response example**

```json
[
    {
        "id": "2",
        "entrepreneur": "Sanjay kumar",
        "pitchTitle": "Lenskart - Sabo Chashma Pehnao",
        "pitchIdea": "Lenskart's aim is to help drop this number marginally in the coming years, which can be achieved by providing high quality eyewear to millions of Indians at affordable prices, giving free eye check ups at home and by extending our services to the remote corners of India.",
        "askAmount": 20000000.23,
        "equity": 15.23,
        "offers": []
    },
    {
        "id":"1",
        "entrepreneur": "Ashok kumar",
        "pitchTitle": "Crio.Do - Work-experience based learning programs for developers",
        "pitchIdea": "Build professional projects like the top 1% developers. Master the latest full stack and backend tech with real work-ex. Crack developer jobs at the best tech companies.",
        "askAmount": 10000000,
        "equity": 12.5,
        "offers": [
            {
                "id": "1",
                "investor": "Anupam Mittal",
                "amount": 10000000.23,
                "equity": 20.23,
                "comment": "A new concept in the ed-tech market. I can relate with the importance of the Learn By Doing philosophy. Keep up the Good Work! Definitely interested to work along with you"
            }
        ]
    }
]

```

----

### 4. Endpoint to specify a particular id (identifying the pitch) to fetch a single Pitch

`/pitches/<pitch_id>`

HTTP endpoint : `/pitches/<pitch_id>`

HTTP method : `GET`

**Success Response**

Response code : `200 OK`

**Response body**

```json
{
        "id": "string",
        "entrepreneur": "string",
        "pitchTitle" : "string",
        "pitchIdea" : "string",
        "askAmount": "float",
        "equity" : "float"
        "offers": [
            {
                "id": "string",
                "investor": "string",
                "amount" : "float",
                "equity" : "float",
                "comment": "string"
            }
        ]
}
```

**Response example**

```json
{
        "id": "1",
        "entrepreneur": "Ashok kumar",
        "pitchTitle": "Crio.Do - Work-experience based learning programs for developers",
        "pitchIdea": "Build professional projects like the top 1% developers. Master the latest full stack and backend tech with real work-ex. Crack developer jobs at the best tech companies.",
        "askAmount": 10000000,
        "equity": 12.5,
        "offers": [
            {
                "id":"1",
                "investor":"Anupam Mittal",
                "amount":10000000.23,
                "equity":20.23,
                "comment":"A new concept in the ed-tech market. I can relate with the importance of the Learn By Doing philosophy. Keep up the Good Work! Definitely interested to work along with you"
            }
        ]
}
```

**Error response**

Condition : Pitch not found

Response code : `404 NOT FOUND`

----
