from django.shortcuts import render
#뷰에서 db에 저장된 데이터를 context로 넘겨야 하니, import하자.
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  #render(요청, 보여줄 템플릿, 넘겨줄 컨텍스트)
  return render(request, 'blog/post_list.html', {'posts' : posts})
  