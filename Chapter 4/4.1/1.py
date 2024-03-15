import requests

response = requests.get('https://google.com')
html = response.text


data = { 'username': 'example_user', 'password': 'example_password' }
response = requests.post( 'https://www.example.com/login', data = data)


response = requests.get('https://www.example.com')
html_content = response.content


response = requests.get('https://realpython.github.io/fake-jobs/')

status = response.status_code

if status == 200:
    print('Request was successful!')

else:
    print('Request failed with status code: ', status)

