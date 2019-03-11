import requests
import json
import jsonpath

def test_Add_new_data():
    App_URL="http://thetestingworldapi.com/api/studentsDetails"
    f = open('C:/Users/TestingWorld/Desktop/TASK_API/RequestJson.json','r')
    request_json = json.loads(f.read())
    response = requests.post(App_URL,request_json)
    id= jsonpath.jsonpath(response.json(),'id')
    print(id[0])

    tech_api_url = "http://thetestingworldapi.com/api/technicalskills"
    f = open('C:/Users/TestingWorld/Desktop/TASK_API/TechDetails.json','r')
    request_json = json.loads(f.read())
    request_json['id']=int(id[0])
    request_json['st_id'] = id[0]
    response = requests.post(tech_api_url, request_json)
    print(response.text)

    add_api_url = "http://thetestingworldapi.com/api/addresses"
    f = open('C:/Users/TestingWorld/Desktop/TASK_API/address.json', 'r')
    request_json = json.loads(f.read())
    request_json['stId'] = id[0]
    response = requests.post(add_api_url, request_json)

    final_details="http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(final_details)
    print(response.text)
    