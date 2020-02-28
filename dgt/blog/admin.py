from django.contrib import admin
from .models import Post

# Register your models here.
# models.py에 정의한 post 모델을 등록한거임.
admin.site.register(Post)