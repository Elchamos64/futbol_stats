import requests

# Define the URL with placeholders for username and token
url = "https://api.soccersapi.com/v2.2/stats/?user={{USERNAME}}&token={{TOKEN}}&t=player&id=13185&season_id=406"

# Replace placeholders with actual username and token
username = "oscar.ramos.andres"
token = "a56c6e90a4d381e47167d0ac3083db0d"
url = url.replace("{{USERNAME}}", username).replace("{{TOKEN}}", token)

# Make the GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content (JSON data)
    print(response.json())
else:
    # Print an error message if the request was not successful
    print("Failed to fetch data. Status code:", response.status_code)

