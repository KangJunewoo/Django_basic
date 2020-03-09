#get_object_or_404를 import해서, 404 페이지처리 가능.
from django.shortcuts import render, get_object_or_404
#뷰에서 db에 저장된 데이터를 template으로 넘겨야 하니, import하자.
from .models import Post
#이 PostForm은 원래 있는게 아닌, 우리가 정의한거다. post요청시 사용됨.
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
  #모델.objects하면 다 튀어나오는듯하고, filter랑 order_by 등으로 상세정렬 가능한듯.
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  #render(request, template, context)
  return render(request, 'blog/post_list.html', {'posts' : posts})

#url에서 <int:pk>로 처리한 부분이 pk로 넘어옴.
def post_detail(request, pk):
  #그 pk가 유효하지 않으면 저절로 빠꾸.
  post=get_object_or_404(Post, pk=pk)
  return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
  #post일경우, 해당 postform이 valid하다면 추가정보 붙여서 save.
  if request.method=='POST':
    form=PostForm()
    if form.is_valid():
      post=form.save(commit=False)
      post.author=request.user
      post.published_date=timezone.now()
      post.save()
      return redirect('post_detail', pk=post.pk)
  #get일경우, 그냥 postform 출력
  else:
    form=PostForm()
  
  return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
  #pk로 해당 post를 읽어온 담에
  post=get_object_or_404(Post, pk=pk)
  #post면 instance를 post로 해서 valid하다면 update
  if request.method=='POST':
    form=PostForm(request.POST, instance=post)
    if form.is_valid():
      post=form.save(commit=False)
      post.author=request.user
      post.published_date=timezone.now()
      post.save()
      return redirect('post_detail', pk=post.pk)
  #get이면 instance를 post로 띄워주기
  else:
    form=PostForm(instance=post)
  return render(request, 'blog/post_edit.html', {'form':form})
