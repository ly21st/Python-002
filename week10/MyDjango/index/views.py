from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from .form import LoginForm
from django.contrib.auth import authenticate, login

from django.contrib import messages

def index(request):
    return HttpResponse("Hello Django!")

###  从models取数据传给template  ###

# def login2(request):
#     if request.method == 'POST':
#         login_form = LoginForm(request.POST)
#         if login_form.is_valid():
#             # 读取表单的返回值
#             cd = login_form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user:
#                 # 登陆用户
#                 login(request, user)
#                 return HttpResponse('登录成功')
#             else:
#                 messages.add_message(request, messages.ERROR, 'User or Credentials Invalid')
#                 return render(request, 'form2.html', {'form': login_form})
#     # GET
#     if request.method == "GET":
#         login_form = LoginForm()
#         return render(request, 'form2.html', {'form': login_form})


def login2(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                return redirect('/index')
            else:
                return HttpResponse('用户名或密码错误')

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'form2.html', {'form': login_form})
