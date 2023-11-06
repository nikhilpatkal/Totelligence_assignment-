"""
URL configuration for Ecommerce project.

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
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
     
     path('home/', views.hello),
     path('home1/', views.hello1),
     path('search/', views.search),
     path('all_product/',views.all_product),
     path('', views.login),
     path('login_view/', views.login_view),
     path('regestartion/', views.regestartion),
     path('Bye_page/<int:arg1>/', views.Bye_page),
     path('address/', views.address),
     path('succesfull/', views.succesfull),
     path('Feedback/', views.Feedback),






    
]
