from django.urls import path
from .api.basic import NoticeApi

urlpatterns = [
    path('notice/list/', NoticeApi.as_view()),
]
