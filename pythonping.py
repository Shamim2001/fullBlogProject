import requests

response = requests.get('https://linkedin.com')

print(response)
print(response.url)