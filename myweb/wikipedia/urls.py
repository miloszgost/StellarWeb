from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.wiki_main),
    path('forum', views.custom_list),
    path('forum/<str:pk>', views.custom_article, name='article'),
    path('forum/<str:article>/new/<str:theuser>', views.add_comment, name='add_comment'),
    path('forum/new/<str:theuser>', views.create_article, name='create_article'),
    path('forum/<str:article>/<str:pk>', views.delete_comment, name='delete_comment'),
    path('forum/<str:article>/delete', views.delete_article, name='delete_article'),
    path('register', views.register, name='register'),
    path('mercury', views.mercury),
    path('venus', views.venus),
    path('earth', views.earth),
    path('mars', views.mars),
    path('jupiter', views.jupiter),
    path('saturn', views.saturn),
    path('uranus', views.uranus),
    path('neptune', views.neptune),
]