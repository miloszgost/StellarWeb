import http.client
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, ArticleForm, CommentForm
from .models import Article, Comment
import time
# Create your views here.


def wiki_main(request):
    return render(request, "wikipedia/main.html")


def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
    else:
        form = UserCreationForm()
    return render(response, "registration/register.html", {"form": form})


def custom_list(request):
    articles = Article.objects.filter(is_active=True)
    context = {'articles': articles}
    return render(request, "wikipedia/forum.html", context)


def custom_article(request, pk):
    article = Article.objects.get(id=pk)
    comments = Comment.objects.filter(article=article, is_active=True)
    article_form = ArticleForm(instance=article)
    comment_form = CommentForm()

    if request.method == "POST":
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
    context = {'article': article, 'comments': comments, 'article_form': article_form, 'comment_form': comment_form}
    return render(request, "wikipedia/users/user_template.html", context)


def add_comment(request, article, theuser):
    target = User.objects.get(username=theuser)
    target_art = Article.objects.get(id=article)
    comment_form = CommentForm()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        comment_form.cleaned_data['name'] = target
        comment_form.cleaned_data['article'] = target_art
        if comment_form.is_valid():
            comment_form.save()
    return custom_article(request, article)


def delete_comment(request, article, pk):
    thecomment = Comment.objects.get(id=pk)
    thecomment.is_active = False
    thecomment.save()
    return custom_article(request, article)


def create_article(request, theuser):
    target = User.objects.get(username=theuser)
    newarticle = Article.objects.create(title='Article ' + str(time.time()), text='Sample text', author=target)
    newarticle.save()
    return redirect('/forum')


def delete_article(request, article):
    thearticle = Article.objects.get(id=article)
    thearticle.is_active = False
    thearticle.save()
    return custom_list(request)


def mercury(request):
    return render(request, "wikipedia/planets/Merkury.html")


def venus(request):
    return render(request, "wikipedia/planets/Wenus.html")


def earth(request):
    return render(request, "wikipedia/planets/Ziemia.html")


def mars(request):
    return render(request, "wikipedia/planets/Mars.html")


def jupiter(request):
    return render(request, "wikipedia/planets/Jowisz.html")


def saturn(request):
    return render(request, "wikipedia/planets/Saturn.html")


def uranus(request):
    return render(request, "wikipedia/planets/Uran.html")


def neptune(request):
    return render(request, "wikipedia/planets/Neptun.html")
