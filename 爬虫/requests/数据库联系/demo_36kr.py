import requests
import json
import pymysql

#链接数据库
try:
    conn = pymysql.connect(host='192.168.12.155', user='root',
                           passwd='1234', port=3306, db='zhang')
    csr = conn.cursor()
except:
    print('连接失败')

# 爬取数据
bid = 1
per_page = int(input('输入每页显示条数'))
while True:
    url = 'https://36kr.com/api/newsflash?'
    params = {
        'b_id':bid,
        'per_page':per_page
    }
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "acw_tc=276aedee15414916882904115e7b4aa199591ea7145d03e28b8cddfddecc98; device-uid=18a13a40-e19b-11e8-bf0e-c35d0e195f7a; laravel_session=eyJpdiI6Iko0YkxyeXFJNlNUdGVWeGpRVkxlUFE9PSIsInZhbHVlIjoiVm8zTFZxbmJqeXVPSzREVENHSlwvTVwvT0JMMFkzVmpCazNDMVZ4WVFDVktySENSRll1ZTZscnZOSEZzeU9kQWlJOWlhcmEyUFVvUUYxKzRJSGlvVVpvUT09IiwibWFjIjoiMTA5NTFmNjdjNmE5ODA2YjE1ZWNlYmU5YmNkNWY4NGJhMTY1N2E0Mjg0YjZiY2M3NWEzYzMwMGNkZWM4OWMyNCJ9; krnewsfrontss=0ce377459c7bb444ee045d716f78c154; M-XSRF-TOKEN=648e23690bf2dc02cfcf7436eca20d8f2a71464ab038ad48b29bc79a4f748438; sajssdk_2015_cross_new_user=1; kr_stat_uuid=dcRjc25691528; Hm_lvt_713123c60a0e86982326bae1a51083e1=1541491690; Hm_lvt_1684191ccae0314c6254306a8333d090=1541491690; TY_SESSION_ID=29fe1fd1-6760-4471-9e45-1f2aa9231356; download_animation=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22dcRjc25691528%22%2C%22%24device_id%22%3A%22166e81088145a2-08c5cd30dd369b-594c2a16-2073600-166e8108815490%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22166e81088145a2-08c5cd30dd369b-594c2a16-2073600-166e8108815490%22%7D; Hm_lpvt_713123c60a0e86982326bae1a51083e1=1541497140; Hm_lpvt_1684191ccae0314c6254306a8333d090=1541497140; identity_id=4683842011267362",
        "Host": "36kr.com",
        "Referer": "https://36kr.com/newsflashes",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        "X-Tingyun-Id": "Dio1ZtdC5G4;r=497159722",
    }
    resp = requests.get(url=url,params=params,headers=headers)
    content = resp.content.decode()
    ret = json.loads(content)
    for i in range(per_page):
        re_id = ret['data']['items'][i]['id']
        re_title = ret['data']['items'][i]['title']
        re_description = ret['data']['items'][i]['description']
        try:
            sql = "insert into 36kr(k_id,k_title,k_decr) VALUES (%s,%s,%s)"
            usr = conn.cursor()
            usr.execute(sql, (re_id, re_title,re_description))
            conn.commit()
            print('添加成功')
        except:
            conn.rollback()
            print('添加失败')

    bid = re_id
