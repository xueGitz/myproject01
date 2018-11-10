import requests
import execjs
import re
import json


class BaiduFanyi:
    def __init__(self, query):
        self.query = query
        self.urls = [
            'https://fanyi.baidu.com/v2transapi',
            'https://fanyi.baidu.com/',
            'https://fanyi.baidu.com/langdetect'
        ]
        self.headers = {
            "Cookie": 'BIDUPSID=285082838AB7A9C9F620D4DEC3CAF58A; PSTM=1518533621; BAIDUID=EA702E381BC8A5869D7758EA3284423D:FG=1; __cfduid=dfa4025b76007dceb42735b7795cee2b01520239569; BD_UPN=12314753; BDUSS=xlOWFLZjJYT1V4d0VEVmN1N1EwZGpwWjFtQ2R6VE9EZUxldkFpQmhqYnhVcDliQVFBQUFBJCQAAAAAAAAAAAEAAACme8J~UVVFWFUxMjMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPHFd1vxxXdbTG; MCITY=-268%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; pgv_pvi=5358852096; BD_HOME=1; H_PS_PSSID=1441_21113_27400_27153; delPer=0; BD_CK_SAM=1; PSINO=5; locale=zh; H_PS_645EC=3e32LOyhgb17C9zBPUS8r91bEuE7HSYGlSdR3unFZenJMYhxipjvswo%2FgKw',
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        self.proxies = {
            'https':'https://119.29.119.64:8080'
        }

    def parse_url(self,url,params=None,data=None,headers=None,proxies=None,method='get'):
        if method=='get':
            resp = requests.get(url=url,params=params,headers=headers,proxies=proxies)
        else:
            resp = requests.post(url=url,data=data,headers=headers,proxies=proxies)
        return resp.content.decode('utf-8')

    def get_lang(self):

        data = {
            'query': self.query
        }
        context = self.parse_url(url=self.urls[2],data=data,method='post',headers=self.headers)
        context = json.loads(context)

        return context['lan']

    def get_sign_token(self):

        content = self.parse_url(url=self.urls[1],headers=self.headers)

        token = re.findall(r"token: '(.*?)',", content)[0]

        with open('baidu_fanyi.js', 'r', encoding='utf-8') as f:
            js = f.read()

        cxt = execjs.compile(js)
        sign = cxt.call('e', self.query)

        return sign, token


    def main(self):

        lang = self.get_lang()
        sign, token = self.get_sign_token()
        data = {
            "query": self.query,
            "simple_means_flag": '3',
            "sign": sign,
            "token": token
        }
        if lang == 'zh':
            data.update( {
                "from": 'zh',
                "to": 'en',
            })
        else:
            data.update( {
                "from": 'en',
                "to": 'zh',
            })


        content = self.parse_url(url=self.urls[0],data=data,headers=self.headers,method='post')


        content = json.loads(content)
        print('结果：'+content['trans_result']['data'][0]['dst'])




if __name__ == '__main__':
    query = input('待翻译：')
    bf = BaiduFanyi(query)
    bf.main()
