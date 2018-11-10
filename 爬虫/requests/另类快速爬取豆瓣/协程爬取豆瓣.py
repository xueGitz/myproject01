'''协程'''
import requests
from gevent import monkey
import gevent
from queue import Queue
from lxml import etree
import urllib.request
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
# gevent 让我们可以按同步的方式来写异步程序
# monkey.patch_all() 会在Python程序执行时动态的将网络库（socket,select,thread)
# 替换掉，变成异步的库，让我们的程序可以异步的方式处理网络相关的任务
monkey.patch_all()
def spider(url):
    movies = []
    print(url)
    resp = requests.get(url=url,headers=headers)

    html = etree.HTML(resp.text)
    infos = html.xpath('//div[@class="item"]')
    for i in infos:
        movie = {}
        movie['排名'] = i.xpath('./div[1]/em/text()')[0]
        movie['电影名'] = i.xpath('.//div[1]/a/img/@alt')[0]
        movie['评分'] = i.xpath('//span[@class="rating_num"]/text()')[0]
        movies.append(movie)
        try:
            urllib.request.urlretrieve(i.xpath('.//div[1]/a/img/@src')[0],'./movie_images/%s.jpg'%movie['电影名'])
        except:
            pass

    movies_list.put(movies)

if __name__ == '__main__':
    #队列存储
    movies_list = Queue()

    gevent_spiders = []
    for i in range(10):
        url = 'https://movie.douban.com/top250?start=%s'%(i*25)
        gevent_spider = gevent.spawn(spider,url)
        gevent_spiders.append(gevent_spider)
        gevent_spider.start()

    gevent.joinall(gevent_spiders)

    flag = True
    while not movies_list.empty():
        movies = movies_list.get()
        print(movies)
        keys = movies[0].keys()
        values = [i.values() for i in movies]
        with open('movies_协程.csv','a') as file:
            print('1...')
            mycsv = csv.writer(file)
            if flag:
                mycsv.writerow(keys)
                flag = False
            mycsv.writerows(values)