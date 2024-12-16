"""trustchain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
urlpatterns = [
    path('', views.main),
    path('login', views.login),
    path('admin_home', views.admin_home),
    path('manage_university', views.manage_university),
    path('reply_complaint', views.reply_complaint),
    path('view_complaints', views.view_complaints),
    path('view_employers', views.view_employers),
    path('view_feedback', views.view_feedback),


    path('generate_certificate', views.generate_certificate),
    path('sendComplaint', views.sendComplaint),
    path('sendFeedback', views.sendFeedback),
    path('universityHomepage', views.universityHomepage),
    path('uploadHistory', views.uploadHistory),
    path('uploadTemplate', views.uploadTemplate),

]
