from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator

# 使用redis缓存
from django.core.cache import cache
from redis import StrictRedis
# Create your views here.

from goods.models import *

class IndexView(View):
    def get(self,request):
        context = cache.get('index_cache')

        if context == None:

            types = GoodsType.objects.all()

            goods_banners = IndexGoodsBanner.objects.all().order_by('index')

            promotion_banners = IndexPromotionBanner.objects.all().order_by('index')

            for type in types:

                image_banners = IndexTypeGoodsBanner.objects.filter(type=type,display_type=1).order_by('index')
                title_banners = IndexTypeGoodsBanner.objects.filter(type=type,display_type=0).order_by('index')

                type.image_banners = image_banners
                type.title_banners = title_banners


            cart_count = 0

            context = {
                'types':types,
                'goods_banners':goods_banners,
                'promotion_banners':promotion_banners,
                'cart_count':cart_count
            }
            cache.set('index_cache',context,3600)

        return render(request,'goods/index.html',context)


def detail(request,sid):
    types = GoodsType.objects.all()
    goodSKU = GoodsSKU.objects.get(pk = sid)
    goodImage = GoodsImage.objects.get(sku_id=sid)
    goods_list = GoodsSKU.objects.filter(type_id=goodSKU.type_id).order_by('-create_time')[:2]
    same_list = GoodsSKU.objects.filter(goods_id=goodSKU.goods.id).exclude(pk = sid)

    user = request.user
    if user.is_authenticated():
        conn = StrictRedis('192.168.12.155')
        history_key = 'history_%d'%user.id
        conn.lrem(history_key,0,sid)
        conn.lpush(history_key,sid)
        conn.ltrim(history_key,0,4)

    context = {
        'types':types,
        'goodSKU':goodSKU,
        'goodImage':goodImage,
        'goods_list':goods_list,
        'same_list':same_list
    }
    return render(request,'goods/detail.html',context)

def goodslist(request,type_id,pn):
    sort = request.GET.get('sort')
    types = GoodsType.objects.all()
    type = GoodsType.objects.get(id = type_id)
    if sort == 'price':
        goodskus = GoodsSKU.objects.filter(type_id=type_id).order_by('price')
    elif sort == 'hot':
        goodskus = GoodsSKU.objects.filter(type_id=type_id).order_by('-sales')
    else:
        goodskus = GoodsSKU.objects.filter(type_id=type_id)
    goods_list = goodskus.order_by('-create_time')[:2]
    paginator = Paginator(goodskus,4)
    mypage = paginator.page(pn)

    currt_page_num = mypage.number
    range_page = []
    if currt_page_num <= 2:
        range_page = [1, 2, 3]
    elif currt_page_num >= paginator.num_pages - 1:
        range_page = [paginator.num_pages - 2, paginator.num_pages - 1, paginator.num_pages]
    else:
        range_page = list(range(max(currt_page_num - 1, 1), currt_page_num)) + list(
            range(currt_page_num, min(currt_page_num + 1, paginator.num_pages) + 1))

    context = {
        'type':type,
        'types':types,
        'goods_list':goods_list,
        'cart_count':0,
        'mypage':mypage,
        'range_page':range_page,
        'sort':sort
    }
    return render(request,'goods/list.html',context)