# from django.shortcuts import render
# from django.views import View
from rest_framework import views, response
from .. import models
from ..serializers.basic import NoticeSerializer


# 消息通知api
class NoticeApi(views.APIView):
    def get(self, request):
        qs = models.Notice.objects.all()
        serializer = NoticeSerializer(qs, many=True)
        return response.Response({
            'status': 0,
            'data': serializer.data
        })
