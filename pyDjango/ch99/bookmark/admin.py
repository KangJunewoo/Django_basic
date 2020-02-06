from django.contrib import admin

# Register your models here.
from bookmark.models import Bookmark

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
  list_display=('id', 'title','url')

'''
데코레이터 없이 하려면
admin.site.register(Bookmark, BookmarkAdmin)

이렇듯 테이블을 새로 만드려면
models.py랑 admin.py 둘 다 수정해야 함!
'''