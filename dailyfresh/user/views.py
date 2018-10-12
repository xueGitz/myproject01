from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core.urlresolvers import reverse
#   序列化
from django.core.serializers import serialize
#   发送邮件
from django.core.mail import send_mail
# 导入setting
from django.conf import settings
# 基于类的视图
from django.views.generic import View
# python自带的加密解密包 itsdangerous
from itsdangerous import TimedJSONWebSignatureSerializer as tjss,SignatureExpired,BadSignature
# 使用认证系统登录
from django.contrib.auth import authenticate,login
# Create your views here.
from user.models import *
from utils.myutil import my_md5

class RegisterView(View):
    def get(self,request):
        return render(request, 'user/register.html')
    def post(self,request):
        #接收注册信息
        user_name = request.POST.get('user_name')
        user_pwd = request.POST.get('pwd')
        user_cpwd = request.POST.get('cpwd')
        user_email = request.POST.get('email')
        user_allow = request.POST.get('allow')
        verifycode = request.POST.get('verifycode','')

        #判断验证码是否正确
        if verifycode != request.session['verifycode']:
            errors = {}
            errors['err_veri'] = '验证码错误'
            return render(request, 'user/register.html', {'error': errors})
        #验证是否可以注册
        user = User.objects.filter(username=user_name)
        if user:
            error = {}
            error['err_2name'] = '用户已存在'
            return render(request,'user/register.html',{'error':error})
        if user_pwd == user_cpwd:
            user_pwd = my_md5(user_pwd)
            print(user_pwd)
            user = User.objects.create_user(username=user_name, password=user_pwd, email=user_email)
            user.is_active = 0
            user.save()

            '''验证邮箱'''
            # 加密用户身份信息，生成激活token
            tjs1 = tjss(settings.SECRET_KEY,1000)
            info = {'confirm':user.id}
            token = tjs1.dumps(info).decode('utf-8')
            encryption_url = 'http://192.168.12.155:8080/active/%s'%token
            # 发邮件
            subject = '天天生鲜欢迎您'
            message = '点击激活'
            sender = settings.EMAIL_FROM
            receiver = [user_email]
            html_message = '<h1>%s,欢迎您成为天天生鲜注册会员</h1>请点击下面的链接激活账户</br><a href="%s">%s</a>'%(user_name,encryption_url,encryption_url)

            send_mail(subject,message,sender,receiver,html_message=html_message)

            # 注册成功反馈
            reci = '<h1>%s,恭喜您，注册成功,请查看邮箱激活成为天天生鲜会员</br>'%(user_name)
            return HttpResponse(reci)
        else:
            return redirect(reverse('user:register'))


class ActiveView(View):
    def get(self,request,token):
        """进行用户激活"""
        #解密，获取需要激活的用户信息
        tjs2 = tjss(settings.SECRET_KEY,1000)

        # 检查邮箱
        try:
            info = tjs2.loads(token)
            user_id = info['confirm']

            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()

            return redirect(reverse('user:login'))
        except SignatureExpired as e:
            return HttpResponse('此链接已过期')
        except BadSignature as e:
            return  HttpResponse('此链接不可用')

def index(request):
    return render(request,'index.html')

def check_name(request):
    hname = request.GET.get('hname')
    count = User.objects.filter(username=hname).count()
    users_list = User.objects.filter(username=hname).values('pk')
    info = []
    for i in users_list:
        d = {}
        d['pk'] = i['pk']
        info.append(d)
    context = {
        'ret':info,
        'count':count
    }
    return JsonResponse(context)



def to_login(request):
    if request.method == 'GET':
        reme_name = request.COOKIES.get('reme_name','')
        return render(request,'user/login.html',{'reme_name':reme_name})
    else:
        user_name = request.POST.get('username')
        user_pwd = request.POST.get('pwd')
        remerber = request.POST.get('remerber')
        verifycode = request.POST.get('verifycode')
        if verifycode != request.session['verifycode']:
            errors = {}
            errors['err_verify'] = '验证码错误'
            return render(request, 'user/login.html', {'errors': errors})

        user = authenticate(username=user_name,password=user_pwd)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                print("用户通过")
                resp = redirect(reverse('user:index'))
                if remerber == '1':
                    resp.set_cookie('reme_name', user_name, 3600)
                else:
                    resp.set_cookie('reme_name', user_name, 0)
                return resp
            else:
                print("未激活")
                return HttpResponse('该用户尚未激活,如距离注册少于一小时，请去邮箱激活，否则，请重新注册')
        else:
            # the authentication system was unable to verify the username and password
            regis = 'http://192.168.12.155:8080/register'
            logi = 'http://192.168.12.155:8080/login'
            ret = '<h2>登陆时遇到错误,您可能尚未注册或者用户名密码输入错误</h2></br>' \
            '<h3>1)<a href = %s>注册</a></h3></br><h3>2)<a href = %s>登录</a></h3></br>'%(regis,logi)
            print("不存在")
            return HttpResponse(ret)
            # error = {}
            # error['errors'] = '用户名或密码不正确'
            # return render(request, 'user/login.html', {'error': error})


def verifycode(request):
    #引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象
    font = ImageFont.truetype('FreeMono.ttf', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    from io import BytesIO
    buf = BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')