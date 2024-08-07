"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from blog import views 
from blog.feeds import LatestEntriesFeed


app_name ="blog"

urlpatterns = [
    path('', views.blog_view, name='index'),
    path('post/<int:pid>',views.blog_single, name="single"),
    path('newsletter',views.newsletter_view, name='newsletter'),
    path('search/',views.blog_search, name='search' ),
    path('category/<str:cat_name>', views.blog_view, name="category"),
    path('author/<str:author_username>', views.blog_view, name='author'),
    path('tag/<str:tag_name>',views.blog_view, name="tag"),
    path("rss/feed/", LatestEntriesFeed()),


    
    
]