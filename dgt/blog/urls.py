from django.urls import path
from . import views

urlpatterns=[
  #이걸로 post_list라는 view가 루트URL에 할당된거.
  #즉 localhost:8000 접속하면, views.post_list를 보여주게 됨.
  #뷰 이름은 post_list. views.py를 보면 알겠지?
  path('', views.post_list, name='post_list'),
  path('post/<int:pk>/', views.post_detail, name='post_detail'),
  path('post/new', views.post_new, name='post_new'),
  path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]