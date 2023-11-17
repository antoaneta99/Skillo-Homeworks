# Homework 11
# 0. Create a virtualenv called `venv`
# 1. Install the requests package in python
# 2. Make a request to `https://reqbin.com/echo/get/json`
# 3. Save the response as a json file called response.json
import requests

url = "https://reqbin.com/echo/get/json"
response = requests.get(url)

if response.status_code == 200:
    print("Request successful")
else:
    print(f"Request failed with status code {response.status_code}")

with open("response.json", "w") as json_file:
    json_file.write(response.text)
