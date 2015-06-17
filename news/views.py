from django.shortcuts import render, render_to_response,RequestContext,get_object_or_404
from news.models import News
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from news.serializers import NewsSerializer
from pymongo import MongoClient

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def home(request):
    # news = News.objects.all()
    init_mongo('fc2_movie','movies')
    movies = collect.find()[1200:1300]
    return render_to_response('home.html',
                              locals(),
                              context_instance=RequestContext(request))

def init_mongo(database,collection):
    connect = MongoClient('localhost', 27017)#, max_pool_size=None)
    db = connect[database]
    global collect
    # collect = db.movie_list
    collect = db[collection]

@csrf_exempt
def news_list(request):
    """
    List all code news, or create a new news.
    """
    if request.method == 'GET':
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True,context={'request': request})
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NewsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def news_detail(request, pk):
    """
    Retrieve, update or delete a code news.
    """
    try:
        news = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NewsSerializer(news)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NewsSerializer(news, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        news.delete()
