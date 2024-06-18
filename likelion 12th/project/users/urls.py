from django.urls import path
from .views import mypage, follow, mypage_redirect

app_name = "users"
urlpatterns = [
    path('mypage/<int:id>', mypage, name="mypage"),
    path('follow/<int:id>', follow, name="follow"),
    path('user/<int:user_id>', mypage_redirect, name="mypage_redirect"),  # 유저 이름 클릭 시 마이페이지로 리다이렉트할 url 패턴
]