from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

#用户登录验证
def userLogin( req ):
    output = {'code':200}
    res = JsonResponse(output,safe=False)
    res['Access-Control-Allow-Origin'] = '*'
    return res

#注册新用户
def userRegister( req ):
    output = {'code':200}
    res = JsonResponse(output,safe=False)
    res['Access-Control-Allow-Origin'] = '*'
    return res

#验证用户名是否已经存在
def userCheckUname( req ):
    output = {'code':200}
    res = JsonResponse(output,safe=False)
    res['Access-Control-Allow-Origin'] = '*'
    return res

#验证电话号码是否已经存在
def userCheckPhone( req ):
    output = {'code':200}
    res = JsonResponse(output,safe=False)
    res['Access-Control-Allow-Origin'] = '*'
    return res

