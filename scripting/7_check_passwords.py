import requests

url = 'https://api.pwnedpaswords.com/range/' + 'password123'
res = requests.get(url)
print(res)