from django.contrib import admin

# Register your models here.
from goods.models import *

admin.site.register(GoodsType)
admin.site.register(Goods)
admin.site.register(GoodsImage)
admin.site.register(GoodsSKU)