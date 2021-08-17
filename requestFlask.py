import requests

res=requests.post('http://127.0.0.1:5000/v1/sanitized/input/',{ 'payload': '/*'})
print(res.content)