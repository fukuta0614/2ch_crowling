from django.shortcuts import render, render_to_response,RequestContext,get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .forms import SignUpForm
# Create your views here.

def home(request):

    # form = SignUpForm(request.POST or None)
    #
    # if form.is_valid():
    #     save_it = form.save(commit=False)
    #     save_it.save()
    #     messages.success(request,'Thank you')

    if request.method == 'POST':
        query = request.POST['query']

    return render_to_response('home.html',   # 使用するテンプレート
                              locals(),       # テンプレートに渡すデータ
                              context_instance=RequestContext(request))  # その他標準のコンテキスト