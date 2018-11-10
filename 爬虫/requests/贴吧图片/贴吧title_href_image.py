import requests
import urllib.request
from lxml import etree


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
pn = 0
kw = input('>>')

while True:
    url = 'https://tieba.baidu.com/f?kw=%s&ie=utf-8&pn=%s'%(kw,50*pn)
    print(url)
    resp = requests.get(url=url,headers=headers)
    content = resp.text

    html_content = content.replace('<!--','').replace('-->','')

    html = etree.HTML(html_content)
    titles = html.xpath('//a[@class="j_th_tit "]/text()')
    print(titles)
    hrefs = html.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/@href')
    print(hrefs)
    try:
        for href in hrefs:
            in_url = 'https://tieba.baidu.com'+href
            resp1 = requests.get(url=in_url,headers=headers)
            content1 = resp1.text
            html_content1 = content1.replace('<!--','').replace('-->','')

            html1 = etree.HTML(html_content1)
            img_urls = html1.xpath('//div[@class="d_post_content j_d_post_content "]/img/@src')
            print(img_urls)

            for img_url in img_urls:
                image_name = img_url[img_url.rfind('/')+1:]
                urllib.request.urlretrieve(img_url,'./images/%s'%image_name)
        pn+=1
        nextpage = html.xpath('//a[@class="next pagination-item"]/text()')
        if not nextpage:
            break
    except:
        break




