# from django.shortcuts import render
# from django.views import View
from rest_framework import views, response
from .. import models
from ..serializers import basic
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import ListAPIView


# 消息通知api
class NoticeApi(views.APIView):
    def get(self, request):
        qs = models.Notice.objects.all()
        # 因为对象不止一个，序列化[obj,obj,obj]这种,要使用many=True
        serializer = basic.NoticeSerializer(qs, many=True)
        return response.Response({
            'status': 0,
            'data': serializer.data
        })


# banner api
class BannerApi(ListAPIView):
    queryset = models.Banner.objects.all()
    serializer_class = basic.BannerSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return response.Response({
            'status': 0,
            'data': serializer.data
        })
