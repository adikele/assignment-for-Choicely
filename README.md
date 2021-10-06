# assignment-for-Choicely
Assignment for Choicely

Author: Aditya Kelekar

Title: Programming assignment for Choicely

Description of the Program:
This program written in Python 3.7.3 uses Python's Flask library to create a server with endpoints for taking in data with a key-value pair 
and for returning the value associated with a key. 
Program uses PostgreSQL 13.0

Endpoints:

GET Endpoint: /load/<string:key>
Returns: A number 
Example Resource URL: 
http://127.0.0.1:5000/load?text=i4 Example Response: 1000
Parameters Name: text Description: A string Required: yes Default: none

POST Endpoint: /save/“key”: ”<string:key>”,“value”: <number> Example Resource URL: 
http://127.0.0.1:5000/save?key=v&value=100

NOTES:

1. The POST endpoint (/save) works when used via an API testing tool like Postman. However, on attempting to save data via a URL parameter, 
the endpoint displays a message: Method not allowed.
 
2. An additional POST endpoint (/save2) has been created for saving data via the Webpage: /form.
