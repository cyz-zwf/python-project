from django.shortcuts import render
from django.http import JsonResponse
from user.models import MfUser
# Create your views here.

#用户登录验证
def userLogin( req ):
    #获取查询字符串的请求参数
    n = req.GET['unameOrPhone']
    p = req.GET['upwd']
    #执行数据库查询
    #SELECT uid FROM mf_user
    #WHERE (uname=? AND upwd=?) OR (phone=? AND upwd=?)
    result = MfUser.objects.filter(uname=n,upwd=p) | MfUser.objects.filter(phone=n,upwd=p)
    if len(result)>0:  #查到了相关记录
        user = result[0]
        output = {'code':1,'uid':user.uid,'uname':user.uname,'phone':user.phone}
    else :              #没查到相关记录
        output = {'code':400}

    res = JsonResponse(output,safe=False)
    res['Access-Control-Allow-Origin'] = '*'
    return res

#注册新用户
def userRegister( req ):
    print("================================")
    print("用户在注册")
    print("================================")
    #读取客户端提交的请求数据
    n = req.POST['uname']
    p = req.POST['upwd']
    h = req.POST['phone']
    #执行数据库的添加操作
    MfUser.objects.create(uname=n,upwd=p,phone=h)
    if user:       #添加成功
        output = {'code':1,'uid':user.uid,'uname':user.uname}
    else :          #添加失败
        output = {'code':500}
    res = JsonResponse(output,safe=False)
    res['Access-Control-Allow-Origin'] = '*'
    return res

#验证用户名是否已经存在
def userCheckUname( req ):
    #接收客户端请求数据
    n = req.GET['uname']
    #执行数据库操作 SELECT * FROM mf_user WHERE uname=?
    result =  MfUser.objects.filter(uname=n)
    if len(result)>0: #查询到该用户对应记录
        output = {'code':1,'msg':'exists'}
    else:     #未查询到该用户记录
        output = {'code':2 , 'msg':'non-exisit'}
    res = JsonResponse(output,safe=False)
    res['Access-Control-Allow-Origin'] = '*'
    return res

#测试代码 : http://127.0.0.1:8000/user/check/uname?uname=admin 



#验证电话号码是否已经存在
def userCheckPhone( req ):
    p = req.GET['phone']
    result = MfUser.objects.filter(phone=p)
    if len(result)>0:
        output = {'code':1,'msg':'exisit'}
    else:
        output = {'code':2,'msg':'non-exisit'}
    res = JsonResponse(output,safe=False)
    res['Access-Control-Allow-Origin'] = '*'
    return res

#测试:http://127.0.0.1:8000/user/check/phone?phone=13501111111
