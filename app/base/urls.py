"""movie browser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

import browser.views
import users.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", users.views.home, name="home"),
    path("login/", users.views.login_user, name="login"),
    path("logout/", users.views.logout_user, name="logout"),
    path("signup/", users.views.sign_up, name="sign_up"),
    path("search/", browser.views.omdb_search, name="search"),
    path("favourite/", browser.views.favourites, name="favourite"),
]
