from django.contrib import admin
from django.core.cache import cache


# Register your models here.
from goods.models import *

class GoodsSKUAdmin(admin.ModelAdmin):
    '''存静态网页信息'''
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj,form,change)
        from celery_tasks.tasks import task_generate_static_index
        task_generate_static_index.delay()
        cache.delete('index_cache')
    # 删除信息
    def delete_model(self, request, obj):

        super().delete_model(request,obj)
        from celery_tasks.tasks import task_generate_static_index
        task_generate_static_index.delay()
        print('delete')

admin.site.register(GoodsType)
admin.site.register(Goods)
admin.site.register(GoodsImage)
admin.site.register(GoodsSKU,GoodsSKUAdmin)
admin.site.register(IndexGoodsBanner)
admin.site.register(IndexPromotionBanner)
admin.site.register(IndexTypeGoodsBanner)