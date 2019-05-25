from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article, ArticleCategory, ArticleSeries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.
def directory(request, category):
    #check if url a category
    """
    categories = [c.category_directory for c in ArticleCategory.objects.all()] #all the categories
    if directory in categories: #check if directory reffers to a category
        matching_series = ArticleSeries.objects.filter(series_category__category_directory=directory) #find the series that match the category
        series_urls = {}

        for m in matching_series.all():
            part_one = Article.objects.filter(article_series__series=m.series).earliest("article_published") #find articles that match the series
            series_urls[m] = part_one.article_directory #link for the series

        return render(request,
                      'main/series.html',
                      {"part_ones":series_urls})
    articles = [a.article_directory for a in Article.objects.all()]
    if directory in articles:
        return HttpResponse(f"{directory} an article")
    return HttpResponse("huh?")
    """
    matching_series = ArticleSeries.objects.filter(series_category__category_directory=category)
    return render(request=request,
                  template_name="main/series.html",
                  context={"series":matching_series})

def subdirectory(request, category, series):
    matching_articles = Article.objects.filter(article_series__series=series)
    return render(request=request,
                  template_name="main/home.html",
                  context={"articles":matching_articles})

def homepage(request):
    return render(request=request,
                  template_name="main/categories.html",
                  context={"categories":ArticleCategory.objects.all})

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
                messages.success(request, f"congrats on logging in {username}!")
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