from django.urls import path
from . import views

urlpatterns = [
    path('surveys', views.Surveys),
    path('surveys/new', views.surveysNew),
]