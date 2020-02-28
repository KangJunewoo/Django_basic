'''
model 들어가니까 새로운 개념들이 막 나오기 시작한다.
하나하나 보자면
CharField : 짧은 텍스트
TextField : 긴 텍스트
DateTimeField : 날짜와 시간
ForeignKey : 다른모델 링크
옵션들은 독스 참고.


'''


from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date=timezone.now()
    self.save()

  def __str__(self):
    return self.title