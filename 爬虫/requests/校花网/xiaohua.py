import re
import requests
import urllib.request


for i in range(44):
    url = 'http://www.xiaohuar.com/list-1-%s.html'%(i)

    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Connection":"keep-alive",
        "Cookie":"__51cke__=; Hm_lvt_0dfa94cc970f5368ddbe743609970944=1541388302; Hm_lpvt_0dfa94cc970f5368ddbe743609970944=1541388302; bdshare_firstime=1541388321642; __tins__17172513=%7B%22sid%22%3A%201541388301648%2C%20%22vd%22%3A%207%2C%20%22expires%22%3A%201541390750214%7D; __51laig__=7",
        "Host":"www.xiaohuar.com",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36ws NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    }
    resp = requests.get(url=url,headers=headers)
    content = resp.text
    url_list = re.findall(r'class="item masonry_brick".*?src="(.*?)"',content,re.S)
    image_urls = []
    for url0 in url_list:
        if not re.match(r'^https',url0):
            url0 = 'http://www.xiaohuar.com'+url0
        image_urls.append(url0)
    index = 1+25*i
    for url1 in image_urls:
        try:
            urllib.request.urlretrieve(url1,'./images/%s.jpg'%index)
            index+=1
        except:
            continue

