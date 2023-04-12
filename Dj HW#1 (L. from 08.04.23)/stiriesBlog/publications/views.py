from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return HttpResponse("This is HOME PAGE! It's containe a list of blogs")


def about(request):
    return HttpResponse("Give a text about SITE FUNCTIONS")


def publication_form(request):
    return HttpResponse("Page to CREATE FORM of publication")


def publication_detaile(request, slug):
    return HttpResponse(f"This is page show DETAILE Publication of blog #{slug}")


def comment(request, slug):
    return HttpResponse(f"Page to ADD Comments from blog #{slug}")


def publication_update(request, slug):
    return HttpResponse(f"Page to watch and UPDATE publication of blog #{slug}")


def publication_delete(request, slug):
    return HttpResponse(f"Page to watch and DELETE publication of blog #{slug}")


def profile(request, username):
    return HttpResponse(f"This is PERSONAL PAGE of user {username}")


def change_password(request):
    return HttpResponse("This is page used to CHANGE personal data of user")


def register(request):
    return HttpResponse("This is page to REGISTER of new user")


def login(request):
    return HttpResponse("This is page with Login forms")
