from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.conf import settings

from goods.models import *


class CartAddView(View):

    def post(self,request):
        user = request.user
        if not user.is_authenticated():
            return JsonResponse({'res':0,'errmsg':'请先登录'})
        sku_id = request.POST.get('sku_id')
        count = request.POST.get('count')

        if not all([sku_id,count]):
            return JsonResponse({'res':1,'errmsg':'数据不完整'})

        try:
            sku = GoodsSKU.objects.get(id=sku_id)
        except GoodsSKU.DoesNotExist:
            return JsonResponse({'res':2,'errmsg':'商品不存在'})

        try:
            count = int(count)
        except Exception as e:
            return JsonResponse({'res':3,'errmsg':'商品数目出错'})

        conn = settings.REDIS_CONN
        cart_key = 'cart_%d'%user.id

        cart_count = conn.hget(cart_key,sku_id)
        if cart_count:
            count+=int(cart_count)
        if count > sku.stock:
            return JsonResponse({'res':4,'errmsg':' 库存不足'})

        conn.hset(cart_key,sku_id,count)
        total_count = get_cart_count(user)
        context = {
            'res': 5,
            'total_count': total_count,
            'message':'添加成功'

        }

        return JsonResponse(context)

def get_cart_count(user):

    total_count = 0

    if user.is_authenticated():
        conn = settings.REDIS_CONN

        cart_key = 'cart_%d'%user.id
        cart_dirt = conn.hgetall(cart_key)

        for sku_id,count in cart_dirt.items():
            total_count += int(count)
    return total_count


def cart(request):
    user = request.user
    if user.is_authenticated():
        conn = settings.REDIS_CONN
        cart_dirt = conn.hgetall('cart_%d'%user.id)

        goodskus = []
        total_count=0
        total_price = 0
        for sku_id, count in cart_dirt.items():
            goodsku = GoodsSKU.objects.get(id = sku_id)
            count = int(count)
            goodsku.count = count
            amount = goodsku.price*count
            goodsku.total_price = amount
            goodskus.append(goodsku)

            total_count += count
            total_price += amount

        context = {
            'goodskus':goodskus,
            'total_count':total_count,
            'total_price':total_price

        }
    else:
        return JsonResponse({'res':0})
    return render(request,'goods/cart.html',context)

class CartUpdateView(View):

    def post(self,request):
        user = request.user
        if not user.is_authenticated():
            return JsonResponse({'res':0,'errmsg':'请先登录'})
        sku_id = request.POST.get('sku_id')
        count = request.POST.get('count')

        if not all([sku_id,count]):
            return JsonResponse({'res':1,'errmsg':'数据不完整'})

        try:
            sku = GoodsSKU.objects.get(id=sku_id)
        except GoodsSKU.DoesNotExist:
            return JsonResponse({'res':2,'errmsg':'商品不存在'})

        try:
            count = int(count)
        except Exception as e:
            return JsonResponse({'res':3,'errmsg':'商品数目出错'})

        conn = settings.REDIS_CONN
        cart_key = 'cart_%d'%user.id


        if count > sku.stock:
            return JsonResponse({'res':4,'errmsg':' 库存不足'})

        conn.hset(cart_key,sku_id,count)
        total_count = get_cart_count(user)
        context = {
            'res': 5,
            'total_count': total_count,
            'message':'更新成功'

        }

        return JsonResponse(context)

class CartDeleteView(View):

        def post(self, request):
            user = request.user
            if not user.is_authenticated():
                return JsonResponse({'res': 0, 'errmsg': '请先登录'})
            sku_id = request.POST.get('sku_id')

            if not all([sku_id]):
                return JsonResponse({'res': 1, 'errmsg': '数据不完整'})

            try:
                sku = GoodsSKU.objects.get(id=sku_id)
            except GoodsSKU.DoesNotExist:
                return JsonResponse({'res': 2, 'errmsg': '商品不存在'})

            conn = settings.REDIS_CONN
            cart_key = 'cart_%d' % user.id

            conn.hdel(cart_key, sku_id)
            total_count = get_cart_count(user)
            context = {
                'res': 3,
                'total_count': total_count,
                'message': '删除成功'

            }

            return JsonResponse(context)


