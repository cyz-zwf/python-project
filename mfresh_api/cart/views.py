from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

#向购物车中添加商品
def cartDetailAdd( req ):
    output = {'code':200}
    res = JsonResponse(output,safe=False)
    res['Access-Control-Allow-Origin'] = '*'
    return res


#查询指定用户的购物车内容
def cartDetailList( req ):
    output = {'code':200}
    res = JsonResponse(output,safe=False)
    res['Access-Control-Allow-Origin'] = '*'
    return res

#根据购物车详情记录编号删除该购买记录
def cartDetailDelete( req ):
    output = {'code':200}
    res = JsonResponse(output,safe=False)
    res['Access-Control-Allow-Origin'] = '*'
    return res

#根据购物车详情记录编号修改该商品购买数量
def cartDetailUpdate( req ):
    output = {'code':200}
    res = JsonResponse(output,safe=False)
    res['Access-Control-Allow-Origin'] = '*'
    return res