# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://nagasekharreddy7.atlassian.net/rest/api/3/issue"

API_Token = os.getenv("Api_token")

auth = HTTPBasicAuth("nagasekharreddy7@gmail.com", API_Token)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps({
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "Github Jira integration.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10009"
    },
    "project": {
      "key": "NAG"  # Fixed from "Key" to "key"
    },
    "summary": "First JIRA ticket"
  },
  "update": {}
})

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

# Use print instead of return to display the response
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


