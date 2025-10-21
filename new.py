import requests

response = requests.get('')

output = response.json()

print(output)