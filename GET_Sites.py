import http.client
from pprint import pprint as pp

api_key = input("Enter the X-API-Key: ")
conn = http.client.HTTPSConnection("api.ui.com")
payload = ''
headers = {
  'Accept': 'application/json',
  'X-API-Key': api_key
}
conn.request("GET", "/v1/sites?pageSize=10&nextToken=602232A870250000000006C514FF00000000073DD8DB000000006369FDA2:1467082514", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
// The above code is a Python script that makes an HTTP GET request to the Ubiquiti API to retrieve a list of sites. It prompts the user to enter their API key, sets up the connection and headers, and then sends the request. The response is read and printed in JSON format.