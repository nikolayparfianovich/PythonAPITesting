import requests
import json
import jsonpath
import openpyxl
from DataDriven import Library

def test_add_multiple_students():
    # API
    api_url= "http://thetestingworldapi.com/api/studentsDetails"
    f = open('C:/Users/TestingWorld/Desktop/TASK_API/AddNewStudent.json')
    json_request = json.loads(f.read())

    obj = Library.Common("C:/Users/TestingWorld/Desktop/TASK_API/TestData.xlsx", "Sheet1")
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keyList = obj.fetch_key_names()


    for i in range(2,row+1):
        updated_json_request = obj.update_request_with_data(i,json_request,keyList)
        response = requests.post(api_url,updated_json_request)
        print(response)