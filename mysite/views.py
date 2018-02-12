from blog.models import Post

from board.models import Board

from django.shortcuts import render

def home(request):
    post = Post.objects.order_by("-created_date")[:5]
    board = Board.objects.order_by("-created_date")[:5]
    return render(request, "home.html", {'post': post, 'board': board})