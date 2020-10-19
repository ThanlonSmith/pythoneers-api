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
    image = models.ImageField(upload_to='media/banner/', max_length=200, verbose_name="图片链接")  # 要安装Pillow模块
    resource = models.CharField(max_length=100, null=True, verbose_name="链接到的url")
    title = models.CharField(max_length=50, null=True,  verbose_name='标题')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name_plural = 'Banner'

    def __str__(self):
        return str(self.image)
