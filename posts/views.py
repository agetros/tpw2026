from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator


# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by("-created_at")
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)
    data = {"posts": posts}
    return render(request, "blog/post_list.html", data)


def create_post(request):
    form = PostForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect("post_list")
    data = {"form": form}
    return render(request, "blog/create_post.html", data)


def edit_post(request):
    data = {}
    return render(request, "blog/edit_post.html", data)


def delete_post(request):
    return render(request, "blog/delete_post.html")


def post_detail(request):
    data = {}
    return render(request, "blog/post_detail.html", data)
