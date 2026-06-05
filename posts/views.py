from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm, PostForm
from .models import Post


# Create your views here.
def post_list(request):
    query = request.GET.get("search")
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query)
            | Q(content__icontains=query)
            | Q(categories__icontains=query)
        ).order_by("-created_at")
    else:
        posts = Post.objects.all().order_by("-created_at")
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)
    data = {"posts": posts}
    return render(request, "blog/post_list.html", data)


@login_required
def create_post(request):
    form = PostForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        messages.success(request, "Publicación creada exitosamente.")
        return redirect("post_list")
    data = {"form": form}
    return render(request, "blog/create_post.html", data)


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance=post)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Publicación actualizada exitosamente.")
        return redirect("post_list")
    data = {"form": form, "post": post}
    return render(request, "blog/edit_post.html", data)


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Publicación eliminada exitosamente.")
        return redirect("post_list")
    data = {"post": post}
    return render(request, "blog/delete_post.html", data)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by("-created_at")
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, "Comentario agregado exitosamente.")
            return redirect("post_detail", post_id=post_id)
    else:
        comment_form = CommentForm()
    data = {"form": comment_form, "post": post, "comments": comments}
    return render(request, "blog/post_detail.html", data)
