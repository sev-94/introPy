import requests

url = 'https://api.pwnedpaswords.com/range/' + 'CBFDAC6008F9CAB4083784CBD1874F76618D2A97'
res = requests.get(url)
print(res)