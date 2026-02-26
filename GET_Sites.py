import http.client

input = input("Enter the X-API-Key: ")
conn = http.client.HTTPSConnection("api.ui.com")
payload = ''
headers = {
  'Accept': 'application/json',
  'X-API-Key': '<X-API-Key>'
}
conn.request("GET", "/v1/sites?pageSize=10&nextToken=602232A870250000000006C514FF00000000073DD8DB000000006369FDA2:1467082514", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))