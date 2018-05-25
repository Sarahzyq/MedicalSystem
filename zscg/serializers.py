#-*- coding: utf-8 -*-

from models import PatientBasicInfo
from models import BingLi
from models import DiagHistoryBasic
from models import Photo
from rest_framework import serializers

class PatientBasicInfoSerializer(serializers.HyperlinkedModelSerializer):
#    url = serializers.HyperlinkedIdentityField(view_name="patientbasicinfo-detail")

    class Meta:
        model = PatientBasicInfo
        fields = ('id', 'name', 'birthday', 'age', 'gender', 'marriage', 'hometown',
                  'address', 'phone', 'inputdate', 'pifukebinglihao')

class BingLiSerializer(serializers.HyperlinkedModelSerializer):
 #   url = serializers.HyperlinkedIdentityField(view_name="bingli-detail")
    #patientid = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name="patientbasicinfo-detail")
    class Meta:
        model = BingLi
        fields = ('id','patientid', 'songjianriqi', 'xingming', 'nianling', 'xingbie', 'bumen', 'linchuangzhenduan',
                  'qucaibuwei', 'songjianyishi', 'baogaoyishi','operator','binglihao','jingxiasuojian','binglizhenduan', 
                  'baogaoriqi','zhuyuanhao')

class DiagHistoryBasicSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="zscg:diaghistorybasic-detail")
    class Meta:
        model = DiagHistoryBasic
        fields = ('url','id','patientid','xianbingshi','jiwangshi','jiazushi','tigejiancha',
                  'linchuangjiancha','zhiliao','sign','photonum')

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
 #   url = serializers.HyperlinkedIdentityField(view_name="zscg:photo-detail")
    class Meta:
        model = Photo
        fields = ('id','patientid','phototype','photo','identifyid','description')
