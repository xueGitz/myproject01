import requests


'''cookies'''
response = requests.get('http://www.baidu.com')

cookiesjar = response.cookies

cookiesdict = requests.utils.dict_from_cookiejar(cookiesjar)

print(cookiesjar)

print(cookiesdict)


print('*'*100)

# 1. 创建session对象，可以保存Cookie值
ssion = requests.session()

# 2. 处理 headers
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

# 3. 需要登录的用户名和密码
data = {"email":"18737572516", "password":"123456"}

# 4. 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里
ssion.post("http://www.renren.com/PLogin.do", data = data)

# 5. ssion包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
response = ssion.get("http://www.renren.com/profile")

# 6. 打印响应内容
with open('renren.html','w') as f:
    f.write(response.text)


