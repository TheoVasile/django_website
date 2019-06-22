from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article, ArticleCategory
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
from mysite import settings
from django.http import HttpResponse, Http404
import os

# Create your views here.
def directory(request, directory):
    categories = [c.category_directory for c in ArticleCategory.objects.all()]
    if directory in categories:
        matching_articles = Article.objects.filter(article_category__category_directory=directory)
        if len(matching_articles) > 0:
            return render(request=request,
                template_name="main/home.html",
                context={"articles":matching_articles})
        else:
            return render(request=request,
                          template_name="main/blank.html")


def subdirectory(request, category, series):
    matching_articles = Article.objects.filter(article_series__series=series)
    return render(request=request,
                  template_name="main/home.html",
                  context={"articles":matching_articles})

def homepage(request):
    return render(request=request,
                  template_name="main/categories.html",
                  context={"categories":ArticleCategory.objects.all})

def account(request):
    return render(request=request,
                  template_name="main/account.html")

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"congrats {username}!")
            login(request, user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    return render(request,
                  "main/register.html",
                  context={"form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "logged in")
                return redirect("main:homepage")
        else:
            messages.error(request, "invalid username or password")

    form = AuthenticationForm()
    return render(request,
                  "main/login.html",
                  {"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "logged out")
    return redirect("main:homepage")