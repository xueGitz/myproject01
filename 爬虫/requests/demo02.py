import requests

formdata = {
    "type":"AUTO",
    "i":"i love python",
    "doctype":"json",
    "xmlVersion":"1.8",
    "keyfrom":"fanyi.web",
    "ue":"UTF-8",
    "action":"FY_BY_ENTER",
    "typoResult":"true"
}

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

# response = requests.get(url=url,headers=headers,data = formdata)

# print(response.text)

print('-'*100)


# 根据协议类型，选择不同的代理
proxies = {
    'https':'https://119.29.119.64:8080'
}

response = requests.get("https://www.baidu.com", proxies = proxies)

with open('baidu.html','wb') as f:
    f.write(response.content)

