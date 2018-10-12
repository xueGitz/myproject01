from django.test import TestCase

# Create your tests here.
from itsdangerous import TimedJSONWebSignatureSerializer as tjss

s1 = tjss('abc',1000)
ret = s1.dumps('a').decode('utf-8')
print(ret)

s2 = tjss('abc',1000)
ret1 = s2.loads(ret)
print(ret1)

