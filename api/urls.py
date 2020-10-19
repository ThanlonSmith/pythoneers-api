from django.urls import path
from .api.basic import NoticeApi, BannerApi

urlpatterns = [
    path('notice/list/', NoticeApi.as_view()),
    path('banner/list/', BannerApi.as_view()),
]
