import re

with open('./pre_change.txt','r',encoding='utf-8') as f:
    content = f.read()

ret = re.sub(r'(.*?): (.*)',r'"\1":"\2",',content)
print(ret)