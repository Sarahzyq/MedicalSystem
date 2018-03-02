# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class Bingli(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  
    patientid = models.ForeignKey('Patientbasicinfo', models.DO_NOTHING, db_column='PatientID')  
    songjianriqi = models.DateTimeField(db_column='SongJianRiQi', blank=True, null=True)  
    xingming = models.CharField(db_column='XingMing', max_length=50, blank=True, null=True)  
    nianling = models.IntegerField(db_column='NianLing', blank=True, null=True)  
    xingbie = models.CharField(db_column='XingBie', max_length=10, blank=True, null=True)  
    bumen = models.CharField(db_column='BuMen', max_length=100, blank=True, null=True)  
    linchuangzhenduan = models.CharField(db_column='LinChuangZhenDuan', max_length=1000, blank=True, null=True)  
    qucaibuwei = models.CharField(db_column='QuCaiBuWei', max_length=100, blank=True, null=True)  
    songjianyishi = models.CharField(db_column='SongJianYiShi', max_length=100, blank=True, null=True)  
    baogaoyishi = models.CharField(db_column='BaoGaoYiShi', max_length=100, blank=True, null=True)  
    operator = models.CharField(db_column='Operator', max_length=100, blank=True, null=True)  
    binglihao = models.IntegerField(db_column='BingLiHao', blank=True, null=True)  
    jingxiasuojian = models.CharField(db_column='JingXiaSuoJian', max_length=1000, blank=True, null=True)  
    binglizhenduan = models.CharField(db_column='BingLiZhenDuan', max_length=1000, blank=True, null=True)  
    baogaoriqi = models.DateTimeField(db_column='BaoGaoRiQi', blank=True, null=True)  
    zhuyuanhao = models.IntegerField(db_column='ZhuYuanHao', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'BingLi'


class Diaghistorybasic(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  
    patientid = models.ForeignKey('Patientbasicinfo', models.DO_NOTHING, db_column='PatientID')  
    xianbingshi = models.CharField(db_column='XianBingShi', max_length=1000, blank=True, null=True)  
    jiwangshi = models.CharField(db_column='JiWangShi', max_length=1000, blank=True, null=True)  
    jiazushi = models.CharField(db_column='JiaZuShi', max_length=1000, blank=True, null=True)  
    tigejiancha = models.CharField(db_column='TiGeJianCha', max_length=1000, blank=True, null=True)  
    linchuangjiancha = models.CharField(db_column='LinChuangJianCha', max_length=1000, blank=True, null=True)  
    zhiliao = models.CharField(db_column='ZhiLiao', max_length=1000, blank=True, null=True)  
    sign = models.CharField(db_column='Sign', max_length=1000, blank=True, null=True)  
    photonum = models.IntegerField(db_column='PhotoNum', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'DiagHistoryBasic'


class Patientbasicinfo(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  
    birthday = models.DateField(db_column='Birthday', blank=True, null=True)  
    age = models.IntegerField(db_column='Age', blank=True, null=True)  
    gender = models.IntegerField(db_column='Gender', blank=True, null=True)  
    marriage = models.IntegerField(db_column='Marriage', blank=True, null=True)  
    hometown = models.CharField(db_column='HomeTown', max_length=50, blank=True, null=True)  
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  
    phone = models.IntegerField(db_column='Phone', blank=True, null=True)  
    inputdate = models.DateTimeField(db_column='InputDate', blank=True, null=True)  
    pifukebinglihao = models.IntegerField(db_column='PiFuKeBingLiHao', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'PatientBasicInfo'


class Photo(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  
    patientid = models.ForeignKey(Patientbasicinfo, models.DO_NOTHING, db_column='PatientID')  
    phototype = models.CharField(db_column='PhotoType', max_length=100, blank=True, null=True)  
    photo = models.CharField(db_column='Photo', max_length=100, blank=True, null=True)  
    identifyid = models.CharField(db_column='IdentifyID', max_length=100, blank=True, null=True)  
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Photo'


class Login(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    user = models.CharField(db_column='User', max_length=100)  
    password = models.CharField(db_column='Password', max_length=100)  

    class Meta:
        managed = False
        db_table = 'login'
