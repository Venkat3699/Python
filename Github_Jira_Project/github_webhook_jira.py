from flask import Flask, request, jsonify
import requests
from requests.auth import HTTPBasicAuth
import json
import os

app = Flask(__name__)

# Jira API details
jira_url = "https://nagasekharreddy7.atlassian.net/rest/api/3/issue"
API_Token = os.getenv("Api_token")
auth = HTTPBasicAuth("nagasekharreddy7@gmail.com", API_Token)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Function to create a Jira ticket
def create_jira_ticket():
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
                "key": "NAG"
            },
            "summary": "First JIRA ticket"
        }
    })

    response = requests.post(jira_url, data=payload, headers=headers, auth=auth)
    print(f"Jira API response: {response.status_code}, {response.text}")  # Debug response
    return response

# Route to handle GitHub webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    comment = data.get("comment", {}).get("body", "").strip()

    # Simple if condition to check the comment body
    if comment == "/createJira":
        jira_response = create_jira_ticket()

        if jira_response.status_code == 201:  # Jira issue created successfully
            return jsonify({"message": "Jira ticket created successfully!"}), 201
        else:
            return jsonify({"error": "Failed to create Jira ticket", "details": jira_response.text}), 500
    else:
        return jsonify({"error": "Invalid command. Use /createJira to create a ticket."}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
