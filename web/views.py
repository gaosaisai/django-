from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
import json
# Create your views here.

# def Login(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         return HttpResponse(username)
#     else:
#         return render_to_response('login.html')
# def Login(request):
#     if request.method=='GET':
#         username=request.GET.get('username')
#         mobile = request.GET.get('mobile')
#         return HttpResponse(username+mobile)
#     else:
#         return render_to_response('login.html')

# def Login(request):
#     if request.method=='GET':
#         result={}
#         username=request.GET.get('username')
#         mobile = request.GET.get('mobile')
#         data=request.GET.get('data')
#         result['user']=username
#         result['mobileNum'] = mobile
#         result['data'] = data
#         result=json.dumps(result)
#         return HttpResponse(result,content_type='application/json;charset=utf-8')
#     else:
#         return render_to_response('login.html')

def Login(request):
    if request.method=='POST':
        result={}
        username=request.POST.get('username')
        mobile = request.POST.get('password')
        result['user']=username
        result['mobileNUM'] =mobile
        result=json.dumps(result)
        return HttpResponse(result)
    else:
        return render_to_response('login.html')
