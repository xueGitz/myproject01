import requests
import re
import pymysql
from lxml import etree

for i in range(10):
    if i ==0:
        url = 'https://movie.douban.com/top250'
    else:
        url = 'https://movie.douban.com/top250?start=%s' % (25*i)
    print(url)

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": 'bid=cxDZtW7mSuU; ll="118237"; __yadk_uid=xGB70mpJ7ybucTrmSWVdhs68ETBgDA2m; _vwo_uuid_v2=D665E68035765ED527120A78E166A17F5|46984d28bd7fc6a61d14cd7ec6f3fdd2; __utma=30149280.409717640.1528853758.1540955229.1541380099.5; __utmc=30149280; __utmz=30149280.1541380099.5.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.1.10.1541380099; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1541380110%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DN7H3iUijNSl-IHpXczXBJoFbqhDnsmbCnp7L0AiN5QJE3NFGEUtygprCT37gu2IW%26wd%3D%26eqid%3D97eb867d000593bd000000045bdf9807%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.175305640.1539861348.1540955229.1541380110.4; __utmb=223695111.0.10.1541380110; __utmc=223695111; __utmz=223695111.1541380110.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_id.100001.4cf6=d6c5a4cb17a4c3f3.1539861348.4.1541380298.1540955229.',
        "Host": "movie.douban.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    }
    proxy = {
        'https':'https://106.75.169.71:3128'
    }
    resp = requests.get(url=url,headers=headers)
    content =  etree.HTML(resp.text)
    movie_hrefs = content.xpath('//div[@class="hd"]/a/@href')
    info_list = re.findall(r'<div class="bd">\s+<p class="">\s+(.*?)&nbsp;&nbsp;&nbsp;(.*?)<br>\s+(.*?)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;(.*?)\s+</p>',resp.text)

    # 链接数据库
    try:
        conn = pymysql.connect(host='192.168.12.155', user='root',
                               passwd='1234', port=3306, db='zhang')
    except:
        print('连接失败')

    try:
        for j in range(25):
            ranking_num = content.xpath('//*[@id="content"]/div/div[1]/ol/li[%s]/div/div[1]/em/text()'%(j+1))[0]
            movie_name = content.xpath('//*[@id="content"]/div/div[1]/ol/li[%s]/div/div[2]/div[1]/a/span[1]/text()'%(j+1))[0]
            dire = info_list[j][0].partition(':')[2]
            actors = info_list[j][1].partition(':')[2]
            show_year = info_list[j][2]
            country = info_list[j][3]
            show_type = info_list[j][4]
            sql = "insert into douban(rank_num,title,director,actors,showyear,country,type) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cur = conn.cursor()
            cur.execute(sql,(ranking_num,movie_name,dire,actors,show_year,country,show_type))
            conn.commit()
            print('插入成功')
    except:
        conn.rollback()
        print('数据回滚')


