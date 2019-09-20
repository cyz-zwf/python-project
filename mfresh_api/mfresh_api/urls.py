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


from user.models import MfUser 
from django.http import JsonResponse

#测试:向数据库中添加一条记录
def testAdd(req):
    u = MfUser.objects.create(uname='ding',upwd='9999',phone='13189956435')
    print(u,type(u))
    return JsonResponse({})

#测试:向数据库中删除一条记录
def testdelete(req):
    r = MfUser.objects.filter(uid=2).delete()
    print(r,type(r))
    return JsonResponse({})


#测试:向数据库中修改一条记录
def testupdate(req):
    upda = MfUser.objects.filter(uid=3).update(uname='yaya',upwd='22')
    print(upda,type(upda))
    return JsonResponse({})


#测试:查询所有记录
def testAll(req):
    all = MfUser.objects.values('uid','uname','upwd')
    #all = all[5:10] 可以对下标进行分页
    print(all,type(all))  #返回值是: QuerySet  对象
    #把QuerySet强制转换为dict或则list  就可以使用json转换
    all = list(all)
    return JsonResponse(all,safe=False )

#测试:查询一行记录
def testone(req):
    one = MfUser.objects.filter(uname='yaya').values('uid','uname','upwd')
    one = one[0]   #<class 'dict'>
    print(one,type(one))  #返回值是: QuerySet  对象
    return JsonResponse(one,safe=False)


urlpatterns = [
    path('test/add',testAdd), #测试
    path('test/testdelete',testdelete),
    path('test/testupdate',testupdate),
    path('test/testAll',testAll),
    path('test/testone',testone), 

    path('admin/', admin.site.urls),
    path('user/login',uv.userLogin), #用户模块
    path('user/register',uv.userRegister),
    path('user/check/uname',uv.userCheckUname),
    path('user/check/phone',uv.userCheckPhone),
    path('news/list',nv.newsList), #新闻模块
    path('news/detail',nv.newsDetail),
    path('product/list',pv.productList), #商品模块
    path('product/detail',pv.productDetail),
    path('cart/detail/add',cv.cartDetailAdd),#购物车模块
    path('cart/detail/list',cv.cartDetailList),
    path('cart/detail/delete',cv.cartDetailDelete),
    path('cart/detail/update',cv.cartDetailUpdate),

    
]
