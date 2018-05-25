# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from models import PatientBasicInfo,BingLi,DiagHistoryBasic,Photo,Login
from rest_framework import viewsets
from serializers import PatientBasicInfoSerializer,BingLiSerializer,DiagHistoryBasicSerializer,PhotoSerializer

from django.shortcuts import render, redirect, reverse  
from django.contrib.auth.decorators import login_required  
from django.contrib.auth import authenticate, login 

@login_required(login_url='/login/do_login')  
def show(request):  
    return render(request,  
                  'show.html',  
                  {'username': request.user.username})  

def do_login(request):  
    if request.method == 'GET':  
        return render(request, 'login.html')  
  
    username = request.POST.get('username', '')  
    password = request.POST.get('password', '')  
  
    user = authenticate(request, username=username, password=password)  
    if user is not None:  
        login(request, user)  
        return redirect(reverse('zscg:show'))  
    else:  
        return render(request, 'login.html', {  
            'username': username,  
            'password': password,  
        })  

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")

# Create your views here.
#def login():
#    return render(request,'login.html')
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class PatientBasicInfoViewSet(viewsets.ModelViewSet):
    queryset = PatientBasicInfo.objects.all()
    serializer_class = PatientBasicInfoSerializer

    # 使用过滤器 
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter,)
    # 定义需要使用过滤器的字段
    filter_fields = ('gender', 'name','marriage')
    ordering_fields = ('id',)

class BingLiViewSet(viewsets.ModelViewSet):
    queryset = BingLi.objects.all()
    serializer_class = BingLiSerializer

    filter_backends = (DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('binglihao','xingming', 'xingbie')
    ordering_fields = ('id',)

class DiagHistoryBasicViewSet(viewsets.ModelViewSet):
    queryset = DiagHistoryBasic.objects.all()
    serializer_class = DiagHistoryBasicSerializer

    filter_backends = (DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('sign','id')
    ordering_fields = ('id',)

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    filter_backends = (DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('id','phototype','identifyid')
    ordering_fields = ('id',)
#   def get_queryset(self):
 #       """
 #       This view should return a list of all the purchases for
 #       the user as determined by the username portion of the URL.
 #       """
  #      name = self.kwargs['name']
   #     return PatientBasicInfo.objects.filter(PatientBasicInfo__name=name)

#from django.http import HttpResponse
#import json
#def get_patient(request):
#    queryset = PatientBasicInfo.objects.get(id=0)
    #resp = {'errorcode': 100, 'detail': 'Get success'}    
#    resp = {'id': queryset.id, 'name': queryset.name}
#    return HttpResponse(json.dumps(resp), content_type="application/json")
