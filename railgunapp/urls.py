from django.urls import path
from railgunapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('bio/', views.bio, name='bio'),
    path('blog/<str:slug>/', views.blogDetail, name='detail'),
    path('project/', views.project, name='project'),
    path('project/dseictool/', views.dseictool, name='dseictool'),
]