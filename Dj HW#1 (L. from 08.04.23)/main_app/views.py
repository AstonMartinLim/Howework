from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth import logout
from main_app.models import Post, Topic
from main_app.forms import AuthenticationForm, AddPostForm, AddCommentForm  # , CreateUserForm
from django.contrib.auth.forms import UserCreationForm


@login_required(login_url='login/')
def main(request):
    search_text = request.GET.get('search_text')
    if search_text:
        posts = Post.objects.filter(content__icontains=search_text)
    else:
        posts = Post.objects.all()
    return render(request, 'main.html', {'posts': Post.objects.all(), 'topics': Topic.objects.all()})


def about(request):
    return render(request, 'about.html')


def topic_post(request):
    get_id = request.GET.get("id")
    posts = Post.objects.all()

    query = Post.objects.filter(topic__id=get_id)
    return render(request, 'topic.html', {'topics': query, 'posts': posts})


def post_detail(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    context = {
        'post': post
    }
    return render(request, 'post_detail.html', context)


def add_comment(request):
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AddCommentForm()
    return render(request, 'add_comment.html', {'form': form})


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AddPostForm()
    return render(request, 'add_post.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def my_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def my_logout(request):
    logout(request)
    return HttpResponseRedirect('login')
