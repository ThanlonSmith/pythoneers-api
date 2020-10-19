from rest_framework import serializers
from .. import models


class NoticeSerializer(serializers.ModelSerializer):
    # 对时间格式化
    add_time = serializers.DateTimeField(format='%Y-%m-%d %X')

    class Meta:
        model = models.Notice
        fields = '__all__'
