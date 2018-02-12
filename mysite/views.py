from blog.models import Post
from board.models import Board
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView

def home(request):
    post = Post.objects.order_by("-created_date")[:5]
    board = Board.objects.order_by("-created_date")[:5]
    return render(request, "home.html", {'post': post, 'board': board})

class UserRegister(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserRegisterDone(TemplateView):
    template_name = 'registration/register_done.html'