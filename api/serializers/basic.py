from rest_framework import serializers
from .. import models


class NoticeSerializer(serializers.ModelSerializer):
    # 对时间格式化
    add_time = serializers.DateTimeField(format='%Y-%m-%d %X')

    class Meta:
        model = models.Notice
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = (
            'id',
            'image',
            'resource',
            'title'
        )


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = (
            'title',
            'image',
            'order_address',
            'coupon_address',
            'is_coupon',
            'current_price',
            'current_face_price',
            'monthly_sale',
            'book_store'
        )
