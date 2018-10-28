from flask import Flask
from flask import render_template
import requests
import json

url = "https://endpoints.office.com/endpoints/worldwide"

querystring = {"ClientRequestId":"ecf5c07e56a0478aba0c543382d5bf70"}

headers = {
    'cache-control': "no-cache",
    'Postman-Token': "b936853f-e38a-4d6d-b3cc-0070af7c4ea5"
    }


app = Flask(__name__)

@app.route('/iprange')
def ip_range():
	response = requests.request("GET", url, headers=headers, params=querystring)

	#print(response.text)

	respList = json.loads(response.text)

	#print (respDict)

	ipRange = []

	for entry in respList:
		if (entry["serviceArea"] == 'Exchange') or (entry["serviceArea"] == 'Common'):
			if "ips" in entry:
				ipRange.extend(entry["ips"])

	return render_template('ipaddresses.html', ipRange = ipRange)

@app.route('/urls')
def urls():
	response = requests.request("GET", url, headers=headers, params=querystring)

	#print(response.text)

	respList = json.loads(response.text)

	#print (respDict)

	urls = []

	for entry in respList:
		if (entry["serviceArea"] == 'Exchange') or (entry["serviceArea"] == 'Common'):
			if "urls" in entry:
				urls.extend(entry["urls"])

	return render_template('URLs.html', urls = urls)	
		