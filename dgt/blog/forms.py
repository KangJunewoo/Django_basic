from django import forms
from .models import Post

class PostForm(forms.ModelForm):
  #Meta 클래스는, 이 폼을 만들기 위해 어떤 모델이 쓰여야 하는지 알려주는 역할을 함.
  class Meta:
    model=Post
    fields=('title','text',)