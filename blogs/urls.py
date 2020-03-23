from django.urls import path

from . import views

urlpatterns = [
    path('', views.blogs),
    path('blogs', views.blogs),
    path('blogs/new', views.blogsNew),
    path('blogs/create', views.blogsCreate),
    path('blogs/<int:number>', views.blogsShow),
    path('blogs/<int:number>/edit', views.blogsEdit),
    path('blogs/<int:number>/delete', views.blogsDestroy),
]
