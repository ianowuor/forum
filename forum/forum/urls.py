"""
URL configuration for forum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from forum import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('add/', views.add_question, name='add_question'),
    path('questions/', views.get_questions),
    path('question/<int:question_id>', views.question, name='question'),
    path('post_comment/<int:question_id>', views.post_comment, name='post_comment'),
    path('upvote/<int:question_id>/<int:comment_id>', views.upvote_comment, name='upvote_comment')
]
