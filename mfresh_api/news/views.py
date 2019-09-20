from django.shortcuts import render
from django.http import JsonResponse
from user.models import MfNews
import math 

# Create your views here.
#按发布时间逆序返回新闻列表
def newsList( req ):
    #读取客户端提交的请求参数 --可能有可能没有
    # pageNum = req.GET['pageNum'] #有则读取,无则抛错
    n = req.GET.get('pagNum',1) #有则读取,无则使用默认值
    n = int(n) #请求数据默认都是str
#查询 创建带放给客户端
    output = {
        'totalRecord' :0,  #总记录数
        'pageSize':10 , #分页大小
        'pageCount':0, #页面数量
        'pageNum':n, #当前页号
        'data':[] #当前页中的数据
    }
    output['totaRecord'] = MfNews.objects.count()
    #计算总页数
    output['pageCount'] = math.ceil(output['totalRecord']/output['pageSize'])
    #获取指定页上的数据
    start = (pageNum-1)*output['pageSize'] #开始下标
    end = pageNum*output['pageSize'] #结束下标
    output['data'] = MfNews.objects.values('nid','title','pubtime')[start:end]
    output['data'] = list(output['data']) #把QuerSet转换为list 以方便json序列化
     '''
    1 0~9
    2 10~19
    3 20~29
    '''

    res = JsonResponse(output,safe=False)
    res['Access-Control-Allow-Origin'] = '*',
    return res

#测试http://127.0.0.1:8000/news/list?pageNum=3

#根据新闻ID返回新闻详情
def newsDetail( req ):
    #获取客户端提交的请求数据
    nid = req.GET['nid']
    #执行数据库查询 SELECT nid,title,pubtime,content FROM mf_news WHERE nid=?
    n= MfUser.objects.filter(nid=nid).values('nid','title','pubtime','content')
    print(n)
    if len(result)>0:
        output = result[0]
    else:
        output = {}
    res = JsonResponse(output,safe=False)
    res['Access-Control-Allow-Origin'] = '*',
    return res

#http://127.0.0.1:8000/news/detail?nid=2