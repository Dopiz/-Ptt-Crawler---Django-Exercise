from django.urls import path

from . import views

app_name = 'pttCrawler'
urlpatterns = [
    path('', views.index, name='index'),
    path('parse/', views.parse, name='parse'),
    path('results/', views.results, name='results')
]
