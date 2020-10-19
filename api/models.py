from django.db import models


class Notice(models.Model):
    '''消息通知表'''
    content = models.CharField(max_length=100, null=False, unique=True, verbose_name='消息内容')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='通知时间')

    class Meta:
        verbose_name_plural = '消息通知管理'

    def __str__(self):
        return self.content
