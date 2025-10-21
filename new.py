import requests

response = requests.get('')

output = response.json()

print(output)

def darkmode():
    return 'darkmode'

darkmode()