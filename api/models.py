from django.db import models


class Notice(models.Model):
    '''消息通知表'''
    content = models.CharField(max_length=100, null=False, verbose_name='消息内容')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='通知时间')

    class Meta:
        verbose_name_plural = '消息通知'

    def __str__(self):
        return self.content


class Banner(models.Model):
    """Banner表"""
    image = models.ImageField(upload_to='media/banner/', max_length=200, verbose_name="图片")  # 要安装Pillow模块
    resource = models.CharField(max_length=100, null=True, verbose_name="链接到的url")
    title = models.CharField(max_length=50, null=True, verbose_name='标题')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name_plural = '轮播图'

    def __str__(self):
        return str(self.image)


class Book(models.Model):
    title = models.CharField(max_length=80, null=True, verbose_name='书名')
    image = models.ImageField(upload_to='media/book/', null=True, max_length=200, verbose_name="图书封面")
    order_address = models.CharField(max_length=100, null=True, verbose_name="下单地址")
    coupon_address = models.CharField(max_length=100, null=True, verbose_name="领券地址")
    is_coupon = models.BooleanField(default=False, null=True, verbose_name='是否有优惠券')
    current_price = models.FloatField(null=True, verbose_name='现价')
    current_face_price = models.IntegerField(default=0, null=True, verbose_name='优惠券面值')
    monthly_sale = models.IntegerField(null=True, verbose_name='月销')
    book_store = models.CharField(max_length=20, null=True, verbose_name='书店')
    flag = models.CharField(max_length=3, null=True, verbose_name='位置标记')  # 前端用不到

    class Meta:
        verbose_name_plural = '参考用书'

    def __str__(self):
        return self.title
