import http.client

api_key = input("Enter the X-API-Key: ")
siteId = '66f8ae939850083bacc3c97e'
consoleId = 'UCGU-LAB01'
conn = http.client.HTTPSConnection("api.ui.com")
payload = ''
headers = {
  'Accept': 'application/json',
  'X-API-Key': api_key
}
conn.request("GET", f"/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/wifi/broadcasts?offset=%7Boffset%7D&limit=%7Blimit%7D&filter=%7Bfilter%7D", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))