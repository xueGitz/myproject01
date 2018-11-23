from django.core.files.storage import Storage
from django.conf import settings
from fdfs_client.client import Fdfs_client

class FDFSStorage(Storage):
    '''fast_dfs文件存储类'''

    def __init__(self):
        '''初始化'''
        self.client_conf = settings.FDFS_CLIENT_CONF
        self.base_url = settings.FDFS_URL


    def _open(self,name,mode='rb'):
        '''打开文件使用'''
        pass

    def _save(self,name,content):
        '''保存文件时使用  name：你选择上传文件的名字     content：包含你上传文件内容的File对象'''

        #创建Fdfs_client对象
        client = Fdfs_client(self.client_conf)

        #上传文件到fast dfs系统中
        res = client.upload_by_buffer(content.read())

        print('res',res)
        if res.get('Status') != 'Upload successed.':
            #上传失败
            raise Exception('上传文件到FastDFS失败')

        #获取返回文件ID
        filename = res.get('Remote file_id')

        return filename.decode()

    def exists(self, name):
        return False

    def url(self, name):
        return self.base_url + name