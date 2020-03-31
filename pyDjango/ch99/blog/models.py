from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils.text import slugify

#모델 클래스
class Post(models.Model):
  #⭐모델 속성. 필수로 들어가야 함.⭐
  #필드명=필드타입(필드옵션)
  title=models.CharField(verbose_name='TITLE', max_length=50)
  slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias')
  description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text')
  content=models.TextField('CONTENT')
  create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
  modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
  tags=TaggableManager(blank=True)
  owner=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)

  #meta 내부클래스. 각각의 레코드가 아닌 테이블 전체에 관한 정보를 다룸.
  class Meta:
    #meta 내부클래스 속성
    # 사용자에게 보여지는 모델이름.
    # 단수와 복수 지정가능.
    # 예를들어 FavoritePost보다는 my favorite post와 같이 보여지는게 낫지.
    verbose_name = 'post'
    verbose_name_plural = 'posts'
    #말그대로 db 이름. 기본값은 앱이름_모델클래스이름
    db_table = 'blog_posts'
    #정렬기준
    ordering = ('-modify_dt',)

  #모델 메소드. 각각의 레코드에 대한 함수다.
  #⭐객체의 문자열 표현을 리턴. 항상 정의해주는 게 좋다.⭐
  def __str__(self):
    return self.title

  #⭐자신이 정의된 url 변환. DetailView하고 찰떡궁합이다. 항상 정의해주는게 좋다.⭐
  def get_absolute_url(self):
    #여기서의 reverse는..?
    return reverse('blog:post_detail', args=(self.slug,))

  def get_previous(self):
    return self.get_previous_by_modify_dt()

  def get_next(self):
    return self.get_next_by_modify_dt()
    #return self.get_next()
    #return self.get_next_by_modify_dt()
  
  def save(self, *args, **kwargs):
    self.slug = slugify(self.title, allow_unicode=True)
    super().save(*args, **kwargs)