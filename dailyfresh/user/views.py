from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.
from user.models import *


def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'user/register.html')

def register_headle(request):
    user_name = request.POST.get('user_name')
    user_pwd = request.POST.get('pwd')
    user_cpwd = request.POST.get('cpwd')
    user_email = request.POST.get('email')
    if user_pwd == user_cpwd:
        User.objects.create(uname = user_name,upwd = user_pwd,uemail= user_email)
        return redirect(reverse('user:login'))
    else:
        return redirect(reverse('user:register'))

def login(request):
    reme_name = request.COOKIES.get('reme_name','')
    return render(request,'user/login.html',{'reme_name':reme_name})

def login_headle(request):
    user_name = request.POST.get('username')
    user_pwd = request.POST.get('pwd')
    remerber = request.POST.get('remerber')
    verifycode = request.POST.get('verifycode')
    if verifycode != request.session['verifycode']:
        errors = {}
        errors['err_verify'] = '验证码错误'
        return render(request,'user/login.html',{'errors':errors})
    users = User.objects.filter(uname=user_name)
    resp = redirect(reverse('user:index'))
    if users:
        if user_pwd == users[0].upwd:
            if remerber == '1':
                resp.set_cookie('reme_name',user_name,3600)
            else:
                resp.set_cookie('reme_name', user_name, 0)
            return resp

    else:
        error = {}
        error['errors'] = '用户名或密码不正确'
        return render(request,'user/login.html',{'error':error})


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

