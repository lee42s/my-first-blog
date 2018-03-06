from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

class HomeView(TemplateView):
    template_name = 'home.html'

class UserRegisterView(CreateView):#model을 쓸수있다.
    template_name = 'registration/register.html'#template_name은 파일명을자기가 원하는데로 수정할수있다.
    form_class = UserCreationForm
    # 타이밍 로딩 문제로 reverse를 사용시 에러가 발생
    success_url = reverse_lazy('register_done')

class UserRegisterDoneView(TemplateView):
    template_name = 'registration/register_done.html'
