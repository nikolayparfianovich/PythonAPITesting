import requests


param={'name':"testingworld",'email':'testingworldindia@gmail.com','number':'+91-8743-913121'}
response = requests.get('https://httpbin.org/get',params=param)
print(response.text)