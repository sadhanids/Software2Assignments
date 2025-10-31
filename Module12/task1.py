import json
import requests

chuk_norris_request_url = "https://api.chucknorris.io/jokes/random"
print("--------------Fetching Chuck Norris Jokes--------------")
print("-------------------------------------------------------")
try:
    response = requests.get(chuk_norris_request_url).json()
    joke_text = response.get("value")
    print(joke_text)

except requests.exceptions.RequestException:
    print("SERVER ERROR: Failed to get data due to network error")
