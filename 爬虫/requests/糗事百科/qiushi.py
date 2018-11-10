import requests
import csv
from lxml import etree
from queue import Queue
from threading import Thread

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

def spider(url):
    alljokes = []
    print(url)
    resp = requests.get(url=url,headers=headers)

    html = etree.HTML(resp.text)
    alljoke = html.xpath('(//div[@class="article block untagged mb15 typs_hot"])|(//div[@class="article block untagged mb15 typs_recent"])|(//div[@class="article block untagged mb15 typs_old"])|(//div[@class="article block untagged mb15 typs_long"])')

    for joke in alljoke:
        jokes = {}
        gold_comment = joke.xpath('./a[2]/div/div[1]/text()[1]')
        if gold_comment:
            jokes['gold_comment'] = ''.join(gold_comment).replace('\n','')
        else:
            jokes['gold_comment'] = None
        href = joke.xpath('./a[@class="contentHerf"]/@href')[0]

        in_url = 'https://www.qiushibaike.com'+href
        resp1 = requests.get(url=in_url,headers=headers)
        html1 = etree.HTML(resp1.text)
        name = html1.xpath('//div[@class="author clearfix"]/a[2]/@title')
        if name:
            jokes['author_name'] = name
        else:
            jokes['author_name'] = None
        age = html1.xpath('//div[@class="author clearfix"]/div/text()')
        if age:
            jokes['author_age'] = age[0]
        else:
            jokes['author_age'] = None
        sex = html1.xpath('//div[@class="author clearfix"]/div/@class')
        if sex:
            if sex == 'articleGender manIcon':
                jokes['author_sex'] = '男'
            elif sex == 'articleGender womanIcon':
                jokes['author_sex'] = '女'
            else:
                jokes['author_sex'] = None
        else:
            jokes['author_sex'] = None

        content = ''.join(html1.xpath('//div[@class="content"]/text()')).replace('\n','')
        jokes['author_content'] = content
        funny_num = html1.xpath('//div[@class="stats"]/span[1]/i/text()')
        if funny_num:
            jokes['funny_num'] = funny_num[0]
        else:
            jokes['funny_num'] = None
        num_comment = html1.xpath('//div[@class="stats"]/span[2]/i/text()')
        if num_comment:
            jokes['comment_num'] = num_comment[0]
        else:
            jokes['comment_num'] = None
        alljokes.append(jokes)
    jokes_list.put(alljokes)

if __name__ == '__main__':
    #队列存储
    jokes_list = Queue()

    thread_spiders = []
    for i in range(13):

        url = 'https://www.qiushibaike.com/8hr/page/%s/'%(i+1)
        thread_spider = Thread(target=spider,args=[url])
        thread_spiders.append(thread_spider)
        thread_spider.start()



    for i in thread_spiders:
        i.join()

    flag = True
    while not jokes_list.empty():
        comments = jokes_list.get()
        print(comments)
        keys = comments[0].keys()
        values = [i.values() for i in comments]
        with open('jokes.csv','a') as file:
            mycsv = csv.writer(file)
            if flag:
                mycsv.writerow(keys)
                flag = False
            mycsv.writerows(values)




