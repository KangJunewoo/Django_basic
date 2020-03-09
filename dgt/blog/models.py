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
  #User를 참조해야 하니 ForeignKey.
  #독스를 보니, on_delete=models.CASCADE는 Post가 지워질때 author 입장에서의 Post도 지워지는 느낌인듯.
  #독스를 항상 보는 습관을 들이자. 잘되어있다.
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  #짧으면 CharField
  title = models.CharField(max_length=200)
  #길면 TextField
  text = models.TextField()
  #생성된 시각이니까 만들어진 그 시점이 기본값.
  created_date = models.DateTimeField(default=timezone.now)
  #post요청하는 그때그때 반영.
  published_date = models.DateTimeField(blank=True, null=True)


  #메서드 또한 정의가능. self 인자 넣어주는거 잊지 말고.
  def publish(self):
    self.published_date=timezone.now()
    #save로 db에 저장하는건가보다.
    self.save()

  #표시방법을 title로 함. 웬만하면 정의해주자!!
  def __str__(self):
    return self.title