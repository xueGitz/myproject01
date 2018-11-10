import requests
import re
from lxml import etree

pageindex=1
nextpage = '1'
while True:
    data = {
        "keyword":"python",
        "pageindex":pageindex,
        "maprange":"3",
        "workexperience":"0103",
        "education":"5",
        "salary":"0500108000",
        "islocation":"0",
        "order":"0",
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36'
    }
    url = 'https://m.zhaopin.com/zhengzhou-719/?'
    resp = requests.get(url=url,headers=headers,data=data)
    if nextpage:
        context = etree.HTML(resp.text)
        i = 0
        while True:
            try:
                job_name = context.xpath('//*[@id="r_content"]/div/div[1]/section[%s]/a/div[2]/div[1]/div[1]/text()'%(i+1))[0]
                job_money = context.xpath('//*[@id="r_content"]/div/div[1]/section[%s]/a/div[2]/div[1]/div[2]/div[1]/text()'%(i+1))[0]
                job_company = context.xpath('//*[@id="r_content"]/div/div[1]/section[%s]/a/div[2]/div[2]/div[1]/text()'%(i+1))[0]
                job_info = job_name+"---"+job_money+'---'+job_company
                with open('zhilian.txt','a',encoding='utf-8') as f:
                    f.write(job_info+'\n')
                i+=1
            except:
                break
        pageindex+=1
        nextpage = re.findall(r'class="nextpage">(.*?)', resp.text)
    else:
        break

