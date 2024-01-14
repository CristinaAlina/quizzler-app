import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

# Get json data from Open Trivia Database API
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
all_data = response.json()

question_data = all_data["results"]
