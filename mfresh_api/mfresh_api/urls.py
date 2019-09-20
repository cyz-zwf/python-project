"""mfresh_api URL Configuration

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
from django.urls import path
from user import views as uv  #导入用户
from news import views as nv  #导入新闻
from product import views as pv  #导入商品
from cart import views as cv  #导入购物车

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/login',uv.userLogin),
    path('user/register',uv.userRegister),
    path('user/check/uname',uv.userCheckUname),
    path('user/check/phone',uv.userCheckPhone),
    path('news/list',nv.newsList),
    path('news/detail',nv.newsDetail),
    path('product/list',pv.productList),
    path('product/detail',pv.productDetail)
    
]
