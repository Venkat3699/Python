# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://nagasekharreddy7.atlassian.net/rest/api/3/project"

API_Token = os.getenv("Api_token")

auth = HTTPBasicAuth("nagasekharreddy7@gmail.com", API_Token)

headers = {
  "Accept": "application/json"
}

query = {
  'query': 'query'
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query,
   auth=auth
)

output = json.loads(response.text)
for project in output:
    print("The project name is:", project["name"])
