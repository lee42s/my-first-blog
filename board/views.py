from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from board.models import Board,Category
from django.contrib.auth.decorators import login_required
from board.forms import BoardForm

# Create your views here.


def post_list(request):
    ctgry = request.GET['category']
    # ctgry =request.GET.get('category')
    if ctgry != '':
        posts = Board.objects.filter(category__name = ctgry)
    else:
        posts = Board.objects.all()

    category = Category.objects.all()
    return render(request, 'board/post_list.html', {'posts':posts, 'category':category})


def post_detail(request, pk):
    post = get_object_or_404(Board, pk=pk)
    category = Category.objects.all()
    return render(request, 'board/post_detail.html', {'post': post, 'category':category})

@login_required
def post_new(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        # PostForm(request.POST).is_valid()
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('board:post_detail', pk=post.pk)
    else:
        form = BoardForm()
    return render(request, 'board/post_edit.html', {'form': form})
