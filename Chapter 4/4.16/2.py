import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

url = 'http://httpbin.org/headers'
response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)