from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Article, Comment
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField( widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Username'}) )
    password = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder': 'Password'}) )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body', 'article')
        widgets = {'name': forms.HiddenInput()}


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'text')

