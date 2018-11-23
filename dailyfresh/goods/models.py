from django.db import models
from tinymce.models import HTMLField

# Create your models here.
from db.base_model import BaseModel

class GoodsType(BaseModel):
    tittle = models.CharField(max_length=20,verbose_name='种类名称')
    logo = models.CharField(max_length=20,verbose_name='标识')
    image = models.ImageField(upload_to = 'type',verbose_name='商品类型图片')

    class Meta:
        db_table = 'df_goods_type'
        verbose_name = '商品种类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tittle


class GoodsSKU(BaseModel):
    status_chioces = (
        (0,'下架'),
        (1,'上架'),
    )
    type = models.ForeignKey('GoodsType',verbose_name='商品种类')
    goods = models.ForeignKey('Goods',verbose_name='商品SPU')
    tittle = models.CharField(max_length=20,verbose_name='商品名称')
    desc = models.CharField(max_length=256,verbose_name='商品简介')
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='商品单价')
    unite = models.CharField(max_length=20,verbose_name='商品单位')
    image = models.ImageField(upload_to='goods',verbose_name='商品图片')
    stock = models.IntegerField(default=1,verbose_name='商品库存')
    sales = models.IntegerField(default=0,verbose_name='商品销量')
    status = models.SmallIntegerField(default=1,choices=status_chioces,verbose_name='商品状态')

    class Meta:
        db_table = 'df_goods_sku'
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tittle



class Goods(BaseModel):
    tittle = models.CharField(max_length=20,verbose_name='商品SPU名称')
    detail = HTMLField(blank=True,verbose_name='商品详情')
    type = models.ForeignKey('GoodsType',verbose_name='商品种类')

    class Meta:
        db_table = 'df_goods'
        verbose_name = '商品SPU'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tittle


class GoodsImage(BaseModel):
    sku = models.ForeignKey('GoodsSKU',verbose_name='商品')
    image = models.ImageField(upload_to='goods',verbose_name='图片路径')

    class Meta:
        db_table = 'db_goods_image'
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sku.tittle


class IndexGoodsBanner(BaseModel):
    '''首页轮播商品展示模型类'''
    sku = models.ForeignKey('GoodsSKU',verbose_name='商品')
    image = models.ImageField(upload_to='banner',verbose_name='图片')
    index = models.SmallIntegerField(default=0,verbose_name='展示顺序')

    class Meta:
        db_table = 'df_index_banner'
        verbose_name = '首页轮播顺序'
        verbose_name_plural = verbose_name

class IndexTypeGoodsBanner(BaseModel):
    '''首页分类商品展示模型类'''
    DISPLAY_TYPE_CHOICES = (
        (0,'标题'),
        (1,'图片')
    )

    type = models.ForeignKey('GoodsType',verbose_name='商品类型')
    sku = models.ForeignKey('GoodsSKU',verbose_name='商品SKU')
    display_type = models.SmallIntegerField(default=1,choices=DISPLAY_TYPE_CHOICES)
    index = models.SmallIntegerField(default=0,verbose_name='展示顺序')

    class Meta:
        db_table = 'df_index_type_goods'
        verbose_name = '主页分类展示商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sku.tittle

class IndexPromotionBanner(BaseModel):
    '''首页促销活动模型类'''
    title = models.CharField(max_length=20,verbose_name='活动名称')
    url = models.CharField(max_length=256,verbose_name='活动链接')
    image = models.ImageField(upload_to='banner',verbose_name='活动图片')
    index = models.SmallIntegerField(default=0,verbose_name='展示顺序')

    class Meta:
        db_table = 'df_index_promotion'
        verbose_name = '主页促销活动'
        verbose_name_plural = verbose_name