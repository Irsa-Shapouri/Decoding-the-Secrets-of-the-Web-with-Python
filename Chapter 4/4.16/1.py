import requests

response = requests.get('http://httpbin.org/headers')

print(response.status_code)
print(response.text)