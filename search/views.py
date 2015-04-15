from django.shortcuts import render, render_to_response,RequestContext,get_object_or_404
from django.core.urlresolvers import reverse
from .Bing import Bing
from .extract_content import ExtractContent
# from django.template import Context, loader
from django.http import HttpResponse,Http404,HttpResponseRedirect
# Create your views here.
import requests

def home(request):

    if request.method == 'POST':
        query = request.POST['query']
        bing = Bing()
        results = bing.web_search(query, 5, ['Url','Title'])
        # results = [{"Url":'http://google.com','Title':'Google'},
        #            {"Url":'http://yahoo.com','Title':'Yahoo'},
        #            {"Url":'http://d.hatena.ne.jp/echizen_tm/20140929/1412004395#seemore','Title':'ほいーるだっく'},
        #            ]
        extractor = ExtractContent()
        # オプション値を指定する
        opt = {"threshold":50}
        extractor.set_option(opt)

        url = results[0]["Url"]
        resp=requests.get(url)
        html=resp.text

        # html = open("yono python-extractcontent.html").read() # 解析対象HTML
        extractor.analyse(html)
        text, title = extractor.as_text()

    return render_to_response('home.html',   # 使用するテンプレート
                              locals(),       # テンプレートに渡すデータ
                              context_instance=RequestContext(request)) # その他標準のコンテキスト

