from django.urls import path, re_path
from blog import views

app_name='blog'
urlpatterns=[
  #/blog/
  path('', views.PostLV.as_view(), name='index'),

  #/blog/post/
  path('post/', views.PostLV.as_view(), name='post_list'),

  #/blog/post/django-example/
  #한글 포함된 슬러그도 처리하기 위해서(아마 정규표현식이겠지?)
  #path('post/<slug:slug>/', views.PostDV.as_view(), name='post_detail') 대신에
  #아놔 정규표현식 \ 하나만 안넣어도 에러가 나는구나...
  re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),

  #/blog/archive/
  path('archive/', views.PostAV.as_view(), name='post_archive'),

  #/blog/archive/2019/
  path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),

  #/blog/archive/2019/nov/
  path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),

  #/blog/archive/2019/nov/10/
  path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),
  
  #여기서 연 4자리숫자 월 3자리소문자 일 한두자리숫자로 지정하고싶다면 re_path에 정규식 사용하면 됨.
  #re_path(r'archive/(?<year>\d{4})/(?P<month>[a-z]{3})/(<?P<day>\d{1,2})/$', views.PostDAV.as_view(), name='post_day_archive'),
  
  
  #/blog/archive/today/
  path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'),

  #/blog/tag/
  path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),

  #/blog/tag/tagname/
  path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),

  #/blog/search/
  path('search/', views.SearchFormView.as_view(), name='search'),

  #/blog/add/
  path('add/', views.PostCreateView.as_view(), name='add'),

  #/blog/change/
  path('change/', views.PostChangeLV.as_view(), name='change'),

  #/blog/99/update/
  path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),

  #/blog/99/delete/
  path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
] 