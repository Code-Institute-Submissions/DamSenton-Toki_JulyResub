from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles, name='articles'),
    path('edit_article/<slug:slug>/', views.edit_article, name='edit_article'),
    path('new_article/', views.new_article, name='new_article'),
    path('delete_article/<slug:slug>/', views.delete_article, name='delete_article'),
    path('<slug:slug>/', views.individual_article, name='individual_article'),
]
