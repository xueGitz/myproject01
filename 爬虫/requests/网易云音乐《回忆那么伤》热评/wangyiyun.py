import requests
import json


url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_431080419?csrf_token='

data ={
    "params":"kfc66tWYD8STZ9Cs10/z9DMZ85G4tr1ofxganBTB/9ggPEo9X7Z4TVTYW+mgehewc8OdgIO0SdZ3VacbFuzDNx5C/xKgEOFGiXfA2TbHWJ6O8b7LktNWU9c1iHUh0zGgsO81qbyp/Kp6CG8TnxzXiCFBcytj9Hb/eYuXXUfm6cdsYA3ZTi+LcTZCstgk4f9S",
    "encSecKey":"7524df274f4191604b73a03ca27a1bb97fb9bc0358303bd01dc24c130eb4dc5bf94c1b85c02137334e10ccc9152e4a12b30ccc3b5abd6932e2be1aae8c7d8d37b4a76a4298f2ff06cfdecf370eb155e1dc3edf63c2e2057d81d7a96a03c34e33aba8229519f88120362b8659aec1a702e82e05820fdc71fb03b7ed42ee7c34e1",
}

headers = {
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Connection":"keep-alive",
    "Content-Length":"480",
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie":"_ntes_nnid=4e8e7f17f78da81d094357a1c4ad3069,1527077241482; _ntes_nuid=4e8e7f17f78da81d094357a1c4ad3069; __utmz=94650624.1527161490.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=187553192.1530442183.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __oc_uuid=761d7b40-7d1c-11e8-bcc5-8b423c009d33; __utma=187553192.1545365345.1530442183.1530442183.1530445617.2; __f_=1534225618885; UM_distinctid=1662021febf877-0d99549c7e6929-36664c08-1fa400-1662021fec068; vjuids=-e8d45aac9.16620387036.0.21b06e8303db6; __gads=ID=47c0cbf62edf5940:T=1538138864:S=ALNI_Ma3H8jQl_LCFD462knxLQGaprfF9g; mail_psc_fingerprint=affab0a58f1bf8976c09d1609db0eb17; _iuqxldmzr_=32; WM_TID=DJbXBdyoacZFABREFUd5fHx5dB5yoz53; usertrack=CrH+Y1vASetvU+LZAwNuAg==; P_INFO=m13523077502@163.com|1540292154|0|mail163|00&99|hen&1539329442&mail163#hen&410100#10#0#0|135502&1||13523077502@163.com; nts_mail_user=13523077502@163.com:-1:1; Province=0370; City=0371; vjlast=1538138862.1540991759.23; vinfo_n_f_l_n3=3f5fa1cdcbb73119.1.1.1538137391221.1538138923004.1540991763450; JSESSIONID-WYYY=ZgA4e%2BF1U5UKEFKXVwmOsH7MXwx66pyHE40PvCmsyu%5Cd8HX0vHcqdhgb%5C285mXgxSK4qIaAiveWa9cu%2BwEOQF3v9w1CHVSw86H8AtGVFo0j%2BvVQSdxklnt4vt6%2FR5yAXUm3wuvlUViYNIud2GZPCZ6OHZZBgqEc%2BAg%2FyrBE4Q80QHi3l%3A1541512713489; __utma=94650624.308500647.1527077242.1541166441.1541510914.4; __utmc=94650624; WM_NI=m59jw3M4ezXRDKFI3GCn9zUcc0Pst0h3SJBaFRObJTHMXJZLBmC4Jr2r9jOcsh%2F%2Fj60NqUbsrnIT9%2BOr1y0zrfCigrejlBB0z6M6XxFVJ6TwaOv39lsE6HTrARo6y%2F1sVlc%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee91d73db8e8fb8aee7eb4a88ea2c54b928e9a84f76ba7b798a5b26efc8e9f9bc22af0fea7c3b92aafebf78bf6398fecab9bdb5a88958aaab24d81b2f79bd869a1f0a094f73caced9dabc16b868e8183c9608c9398abd94882b38dd5c97af2aef78bce69b1b8e1d0e93ef492bfb6e179b2b287b5bc218daeff9ab372b2ba8d8ae67aa7b6a4a3c13cbaea83d7db74868a86d7d77da391bad4bc68b19bfaa9d77a838ea1d7fc25f3ad9a8de237e2a3; playerid=88561162; __utmb=94650624.12.10.1541510914",
    "Host":"music.163.com",
    "Origin":"https://music.163.com",
    "Referer":"https://music.163.com/song?id=431080419",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
}
resp = requests.post(url=url,data=data,headers=headers)
ret = json.loads(resp.text)
name = ret['hotComments'][0]['user']['nickname']
print(name)
i = 0
while True:
    try:
        name = ret['hotComments'][i]['user']['nickname']
        content = ret['hotComments'][i]['content']
        print(name,content)
        info = name+'---'+content+'\n'
        with open('comment.txt','r',encoding='utf-8') as file:
            infos = file.readlines()
        if info not in infos:
            with open('comment.txt','a') as file:
                file.write(info)
        i+=1
    except:
        break
