from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
#按发布时间逆序返回新闻列表
def newsList( req ):
    output = {'code':200}
    res = JsonResponse(output,safe=False)
    res['Access-Control-Allow-Origin'] = '*',
    return res

#根据新闻ID返回新闻详情
def newsDetail( req ):
    output = {'code':200}
    res = JsonResponse(output,safe=False)
    res['Access-Control-Allow-Origin'] = '*',
    return res

