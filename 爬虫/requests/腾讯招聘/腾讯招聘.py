import requests
from lxml import etree
import json


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
pn = 0
ping_lists = []
while True:
    url = 'https://hr.tencent.com/position.php?lid=&tid=&keywords=%E8%AF%B7%E8%BE%93%E5%85%A5%E5%85%B3%E9%94%AE%E8%AF%8D&start={}#a'.format(10*pn)
    print(url)
    resp = requests.get(url=url,headers=headers)
    html = etree.HTML(resp.text)

    trs = html.xpath('(//tr[@class="even"])|(//tr[@class="odd"])')


    for i in range(len(trs)):
        ping={}
        ping['pname'] = trs[i].xpath('./td[1]/a/text()')[0]
        ping['ptype'] = trs[i].xpath('./td[2]/text()')[0]
        ping['pnum'] = trs[i].xpath('./td[3]/text()')[0]
        ping['pplace'] = trs[i].xpath('./td[4]/text()')[0]
        ping['ptime'] = trs[i].xpath('./td[5]/text()')[0]

        phref = trs[i].xpath('./td[1]/a/@href')[0]
        in_url = 'https://hr.tencent.com/'+phref
        in_resp = requests.get(url=in_url,headers=headers)
        in_html = etree.HTML(in_resp.text)

        uls = in_html.xpath('//ul[@class="squareli"]')
        ping['pcensure'] = "".join(uls[0].xpath('./li/text()'))
        ping['prequire'] = "".join(uls[1].xpath('./li/text()'))
        ping_lists.append(ping)
        print('添加%s'%i)
    pn += 1

    with open('tencent.json','a',encoding='utf-8') as file:
        json.dump(ping_lists,file,ensure_ascii=False,indent=4)




