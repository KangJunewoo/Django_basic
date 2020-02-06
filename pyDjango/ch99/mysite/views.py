from django.views.generic import TemplateView

#-- 템플릿뷰
class HomeView(TemplateView):
  template_name = 'home.html'