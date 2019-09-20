from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

#分页获取产品信息，按商品编号逆序排列
def productList( req ):
    output = {'code':200}
    res = JsonResponse(output , safe=False)
    res['Access-Control-Allow-Origin'] = '*'
    return res

#根据产品ID返回产品详情
def productDetail( req ):
    output = {'code':200}
    res = JsonResponse(output , safe=False)
    res['Access-Control-Allow-Origin'] = '*'
    return res