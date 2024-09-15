from django.shortcuts import render


def main(request):
    return render(request, 'main.html')


def about(request):
    return render(request, 'about.html')


def publication_detail(request):
    return render(request, 'blog_detail.html')


def profile(request):
    return render(request, 'profile.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')
