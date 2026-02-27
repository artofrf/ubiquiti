import http.client
from pprint import pprint as pp
import json

api_key = input("Enter the X-API-Key: ")
conn = http.client.HTTPSConnection("api.ui.com")
