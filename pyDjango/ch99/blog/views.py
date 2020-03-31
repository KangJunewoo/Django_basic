from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from django.conf import settings

from .models import Post

from django.views.generic import FormView
from .forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin
'''
1. 적당한 제네릭뷰를 선택한다
2. 필요한 속성과 메소드들을 마구 오버라이드한다.

파일 하단에 test용 view 만들어볼테니 거기서 자세히 설명.
'''
#--- 리스트뷰
class PostLV(ListView):
  model=Post
  template_name='blog/post_all.html'
  context_object_name='posts'
  paginate_by=2

#--- 디테일뷰
class PostDV(DetailView):
  model=Post

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
    context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
    context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
    context['disqus_title'] = f"{self.object.slug}"
    return context

#--- 아카이브뷰
class PostAV(ArchiveIndexView):
  model=Post
  date_field='modify_dt'

class PostYAV(YearArchiveView):
  model=Post
  date_field='modify_dt'
  make_object_list = True

class PostMAV(MonthArchiveView):
  model=Post
  date_field='modify_dt'

class PostDAV(DayArchiveView):
  model=Post
  date_field='modify_dt'

class PostTAV(TodayArchiveView):
  model=Post
  date_field='modify_dt'

class TagCloudTV(TemplateView):
  template_name='taggit/taggit_cloud.html'

class TaggedObjectLV(ListView):
  template_name='taggit/taggit_post_list.html'
  model=Post

  def get_queryset(self):
    return Post.objects.filter(tags__name=self.kwargs.get('tag'))

  def get_context_data(self, **kwargs):
    context=super().get_context_data(**kwargs)
    context['tagname']=self.kwargs['tag']
    return context

#----폼뷰
class SearchFormView(FormView):
  form_class = PostSearchForm
  template_name = 'blog/post_search.html'

  def form_valid(self, form):
    searchWord = form.cleaned_data['search_word']
    post_list=Post.objects.filter(Q(title__icontains=searchWord) | Q(description__icontains=searchWord) | Q(content__icontains=searchWord)).distinct()

    context={}
    context['form']=form
    context['search_term'] = searchWord
    context['object_list'] = post_list

    return render(self.request, self.template_name, context)

class PostCreateView(LoginRequiredMixin, CreateView):
  model=Post
  fields=['title', 'slug', 'description', 'content', 'tags']
  initial={'slug':'auto-filling-do-not-input'}
  #fields=['title','description','content','tags']
  success_url=reverse_lazy('blog:index')

  def form_valid(self,form):
    form.instance.owner=self.request.user
    return super().form_valid(form)

class PostChangeLV(LoginRequiredMixin, ListView):
  template_name='blog/post_change_list.html'

  def get_queryset(self):
    return Post.objects.filter(owner=self.request.user)

class PostUpdateView(OwnerOnlyMixin, UpdateView):
  model=Post
  fields=['title', 'slug', 'description', 'content', 'tags']
  success_url=reverse_lazy('blog:index')

class PostDeleteView(OwnerOnlyMixin, DeleteView):
  model=Post
  success_url=reverse_lazy('blog:index')

class TestPostLV(ListView):
  '''
  # Post모델의 모든 레코드를 불러오겠다.
  model=Post

  # Post모델에서 처음 5개의 레코드만 불러오겠다
  queryset = Post.objects.all()[:5]
  '''
  #렌더링할 템플릿을 blog/post_test.html로 하겠다.
  template_name='blog/post_test.html'
  #템플릿에서 사용할 컨텍스트 변수명을 posts로 하겠다.
  context_object_name='posts'
  #한 페이지에 2개씩 보여주겠다.
  paginate_by=2

  #다음 함수에서 반환하는 걸 출력하는 객체로 하겠다.
  #model, queryset, get_queryset(self) 중 하나는 반드시 있어야함. 보통 models가 되겠지만..
  def get_queryset(self):
    '''
    기본값
    return super().get_queryset()
    '''
    #url에서 넘어온 word가 들어있는 Post만 참조하겠다.
    return Post.objects.filter(Q(content__icontains=self.kwargs['word'])).distinct()

  #다음 함수에서 반환하는 걸 context로 넘길 data로 하겠다.
  def get_context_data(self, **kwargs):
    #원래의 context_data를 받아서(get_queryset에서 넘어온 게 아닐까 추측)
    context = super().get_context_data(**kwargs)
    #
    context['SearchWord'] = self.kwargs['word']
    return context