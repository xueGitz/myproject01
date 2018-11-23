import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyfresh.settings")
django.setup()

from celery import Celery

from django.core.mail import send_mail
from django.template import loader
from django.conf import settings

from goods.models import *

app = Celery('hello', broker='redis://192.168.12.155:6379/1')



@app.task
def send_email(subject, message, sender, receiver, html_message):
    send_mail(subject, message, sender, receiver, html_message = html_message)



@app.task
def task_generate_static_index():
    '''产生静态首页'''
    print('begin...')

    types = GoodsType.objects.all()

    goods_banners = IndexGoodsBanner.objects.all().order_by('index')

    promotion_banners = IndexPromotionBanner.objects.all().order_by('index')

    for type in types:
        image_banners = IndexTypeGoodsBanner.objects.filter(type=type,display_type=1).order_by('index')
        title_banners = IndexTypeGoodsBanner.objects.filter(type=type,display_type=0).order_by('index')

        type.title_banners = title_banners
        type.image_banners = image_banners

    context = {
        'types':types,
        'goods_banners':goods_banners,
        'promotion_banners':promotion_banners
    }

    temp = loader.get_template('goods/static_index.html')

    static_index_html = temp.render(context)

    save_path = os.path.join(settings.BASE_DIR,'static/html/index.html')

    with open(save_path,'w') as f:
        f.write(static_index_html)

    print('end...')