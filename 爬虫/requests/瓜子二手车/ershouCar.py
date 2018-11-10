import requests
import urllib.request
from lxml import etree
import csv

headers = {
    'Cookie':'clueSourceCode=10103000312%2300; uuid=7ab5e0b8-f911-43d6-8913-d30fb0539129; antipas=31B83K837x597958k117F97; ganji_uuid=7538878526334185901890; sessionid=53e0ad5c-0e23-4119-ad31-550ef952e979; lg=1; cainfo=%7B%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22tbmkbturl%22%2C%22ca_i%22%3A%22-%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22scode%22%3A%2210103000312%22%2C%22ca_transid%22%3Anull%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22ca_b%22%3A%22-%22%2C%22ca_a%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%227ab5e0b8-f911-43d6-8913-d30fb0539129%22%2C%22sessionid%22%3A%2253e0ad5c-0e23-4119-ad31-550ef952e979%22%7D; close_finance_popup=2018-11-08; cityDomain=zz; preTime=%7B%22last%22%3A1541641724%2C%22this%22%3A1541639967%2C%22pre%22%3A1541639967%7D',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
}
pn =1
flag = True
while True:
    cars = []
    url = 'https://www.guazi.com/zz/bmw/o%di7/'%pn
    print(url)
    resp = requests.get(url=url,headers=headers)
    html = etree.HTML(resp.text)

    lis = html.xpath('//ul[@class="carlist clearfix js-top"]/li')
    for li in lis:
        car = {}
        car['title'] = li.xpath('./a/h2/text()')[0]
        car['year'] = li.xpath('./a/div[@class="t-i"]/text()[1]')[0]
        car['totals'] = li.xpath('./a/div[@class="t-i"]/text()[2]')[0]
        car['price'] = li.xpath('./a/div[@class="t-price"]/p/text()')[0]

        car_news = li.xpath('(./a/div/i[@class="i-red"])/text()|(./a/div/i[@class="i-green"])/text()')
        print(car_news)
        if car_news:
            car['icon'] = ' '.join(car_news)
        else:
            car['icon'] = None

        car_url = 'https://www.guazi.com'+li.xpath('./a/@href')[0]
        print(car_url)
        resp1 = requests.get(url=car_url, headers=headers)

        html1 = etree.HTML(resp1.text)

        car_imgs = html1.xpath('//li[@class="js-bigpic"]/img/@data-src')
        car['pailiang'] = html1.xpath('//ul[@class="assort clearfix"]/li[last()-1]/span/text()')[0]+'排量'
        car['change_speed'] = html1.xpath('//ul[@class="assort clearfix"]/li[last()]/span/text()')[0]

        index = 1
        for car_img in car_imgs:
            urllib.request.urlretrieve(car_img,'images/%s_%s.jpg'%(car['title'].split(' ')[0],index))
            print('成功')
            index+=1
        cars.append(car)
        keys = cars[0].keys()
        values = [i.values() for i in cars]
        with open('cars.csv', 'a', encoding='utf-8') as f:
            print('1...')
            mycsv = csv.writer(f)
            if flag:
                mycsv.writerow(keys)
                flag = False
            mycsv.writerows(values)
    pn+=1
