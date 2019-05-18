"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path#需增加
from student import views#需增加

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path("query",views.query),

    re_path("myhtml/",views.myhtml),
    re_path("add_data/",views.add_data),

    re_path("delete/",views.delete),
    re_path("delete_result/",views.delete_result),

    re_path("search/",views.search),
    re_path("find/",views.find),

    re_path("update/",views.update),
    re_path("update_result/",views.update_result),
]
