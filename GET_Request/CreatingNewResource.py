import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users"

# Read Input Json file
file = open('C:\\Users\\TestingWorld\\Desktop\\API\\CreateUser.json','r')
json_input = file.read()
request_json = json.loads(json_input)

# Make POST request with Json Input body

response= requests.post(url,request_json)

# Validating Response Code
assert  response.status_code ==201

# Fetch Header from Response
print(response.headers.get('Content-Length'))

# Parse response to Json Format
response_json = json.loads(response.text)

# Pick Id using Json Path
id = jsonpath.jsonpath(response_json,'id')
print(id[0])