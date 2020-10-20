from django.urls import path
from .api.basic import NoticeApi, BannerApi, BookApi

urlpatterns = [
    path('notice/list/', NoticeApi.as_view()),
    path('banner/list/', BannerApi.as_view()),
    path('book/list/', BookApi.as_view()),
]
