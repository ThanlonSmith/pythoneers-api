from django.urls import path
from .views import NoticeApi

urlpatterns = [
    path('notice/', NoticeApi.as_view()),
]
