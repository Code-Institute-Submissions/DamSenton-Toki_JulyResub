from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles, name='articles'),
    path('<slug:slug>/', views.individual_article, name='individual_article'),
]
