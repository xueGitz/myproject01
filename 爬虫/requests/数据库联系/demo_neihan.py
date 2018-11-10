import requests
import re
import pymysql
from lxml import etree

#链接数据库
try:
    conn = pymysql.connect(host='192.168.12.155', user='root',
                           passwd='1234', port=3306, db='zhang')
except:
    print('连接失败')

url = 'https://www.neihan8.com/e/action/ListInfo/?'
headers = {
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
}
page = 0
while True:
    params = {
        'classid': 11,
        'page': page,
    }
    resp = requests.get(url=url,params=params,headers=headers)
    context = etree.HTML(resp.text)
    i = 1
    while True:
        titles = context.xpath('/html/body/div[4]/div/div[1]/div[2]/div[%s]/h3/a/text()'%(i))
        if titles:
            try:
                title = titles[0]
                detail = context.xpath('/html/body/div[4]/div/div[1]/div[2]/div[%s]/div[1]/text()'%i)[0]
                detail=re.sub(r'\s+',r'',detail)
                detail=re.sub(r'<.*?>',r'',detail)
                detail=re.sub(r'&(.*?);',r'',detail)

                sql = "insert into neihan(title,detail) VALUES (%s,%s)"
                usr = conn.cursor()
                usr.execute(sql,(title,detail))
                conn.commit()
                print('添加成功')

            except:
                conn.rollback()
                print('添加失败')
            i+=1
        else:
            break
    page+=1
    if page>10:
        break

