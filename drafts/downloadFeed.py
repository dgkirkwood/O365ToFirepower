import requests
import json

url = "https://endpoints.office.com/endpoints/worldwide"

querystring = {"ClientRequestId":"ecf5c07e56a0478aba0c543382d5bf70"}

headers = {
    'cache-control': "no-cache",
    'Postman-Token': "b936853f-e38a-4d6d-b3cc-0070af7c4ea5"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)

respList = json.loads(response.text)

#print (respDict)

for entry in respList:
	if (entry["serviceArea"] == 'Exchange') or (entry["serviceArea"] == 'Common'):
		