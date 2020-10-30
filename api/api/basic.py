from rest_framework.response import Response
from rest_framework import pagination
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


# book api
class BookApi(ListAPIView):
    """
    Python入门推荐用书API
    """
    """
    queryset = models.Book.objects.all()
    serializer_class = basic.BookSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return response.Response({
            'status': 0,
            'data': serializer.data
        })
    """
    queryset = models.Book.objects.all()
    serializer_class = basic.BookSerializer
    pagination_class = pagination.LimitOffsetPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return response.Response({
            'status': 0,
            'data': serializer.data
        })

    def get_paginated_response(self, data):
        """
        自定义分页显示的数据
        """
        return Response({
            'status': 0,
            'data': data,
            'total': self.paginator.count
        })
