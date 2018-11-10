import requests
import json
import urllib.request
# from lxml import etree


page = 1
page_size = int(input('每次响应条数>'))
infos = []
while True:
    print(page)
    try:
        url = 'https://api.live.bilibili.com/room/v1/area/getRoomList?'
        params={
            'parent_area_id': 1,
            'page':page,
            'page_size':page_size
        }
        resp = requests.get(url=url,params=params)
        print(resp.url)
        context = resp.text
        ret_json = json.loads(context)
        for i in range(page_size):
            info={}
            info['房间名称'] = ret_json['data'][i]['title']
            info['在线主播'] = ret_json['data'][i]['uname']
            info['观看人数'] = ret_json['data'][i]['online']
            info['房间编号'] = ret_json['data'][i]['roomid']
            infos.append(info)

            img_urls = []
            face_img_url = ret_json['data'][i]['face']
            cover_img_url = ret_json['data'][i]['user_cover']
            img_urls.append(face_img_url)
            img_urls.append(cover_img_url)
            for j in range(len(img_urls)):
                urllib.request.urlretrieve(img_urls[j],'./images/%s_%s.jpg'%(info['在线主播'],j))
        page+=1
    except Exception as ex:
        print(ex)
        break
    if page>5:
        break
with open('bilibili.json','a') as file:
    json.dump(infos,file,ensure_ascii=False,indent=4)