from django.urls import path
from . import views

urlpatterns=[
  #3개를 꼭 정의해주자. 주소, 참조할 뷰, URL을 부를 이름(고유해야함.)
  #가능하면 뒤 2개는 같은 이름으로.

  path('', views.post_list, name='post_list'),
  path('post/<int:pk>/', views.post_detail, name='post_detail'),
  path('post/new', views.post_new, name='post_new'),
  path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]