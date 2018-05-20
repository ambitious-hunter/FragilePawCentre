from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PawPostForm


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "paw_blog.html", {'posts': posts})


def latest_post_list(request):
    posts = Post.objects.filter(published=True).order_by('-published_date')[0:2]
    return render(request, "index.html", {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "postdetail.html", {'post': post})


def index(request):
    return render(request, "index.html")


def new_blog(request):
    if request.method == "POST":
        form = PawPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)

    else:
        form = PawPostForm()
    return render(request, 'pawblogform.html', {'form': form})
