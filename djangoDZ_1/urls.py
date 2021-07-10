"""djangoDZ_1 URL Configuration

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
from homework import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/<int:id>/', views.get_one_product),
    path('product/', views.get_all_product),
    path('add_product/',views.add_product),
    path('add/',views.add),
    path('', views.main_page),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('add_products/', views.add_products),
    path('products/', views.products),
]
