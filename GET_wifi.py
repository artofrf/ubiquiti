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
