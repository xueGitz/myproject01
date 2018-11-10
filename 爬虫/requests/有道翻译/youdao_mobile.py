import requests
import re

pre_trans = input('待翻译：')
url = 'http://m.youdao.com/translate'

data = {
    'inputtext': pre_trans,
    'type': 'AUTO'
}
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36",
}
proxies = {
    'https':'https://42.51.216.11:808'
}

resp = requests.post(url=url,data=data,headers=headers)

content = resp.content.decode()

ret = re.findall(r'<ul id="translateResult">\s+<li>(.*?)</li>\s+</ul>',content)[0]
print("结果："+ret)


