from django.urls import path
from .views import *

app_name = "users"
urlpatterns = [
    path('mypage/', mypage, name="mypage"),
    path('<int:id>', detail, name="detail"),
]