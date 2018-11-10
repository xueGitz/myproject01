import requests
import json

i = input('>')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

data = {
    "i": i,
    "doctype": "json",
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
}
proxies = {
    'https':'https://42.51.216.11:808'
}

resp = requests.post(url=url,data=data,headers=headers)

content = resp.content.decode()
content = json.loads(content)

print(content["translateResult"][0][0]['tgt'])
