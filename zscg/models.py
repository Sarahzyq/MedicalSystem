# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class PatientBasicInfo(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    name = models.CharField('姓名',db_column='Name', max_length=50, blank=True, null=True)
    birthday = models.DateField('生日',db_column='Birthday', blank=True, null=True)
    age = models.IntegerField('年龄',db_column='Age', blank=True, null=True)
    gender = models.IntegerField('性别',db_column='Gender', blank=True, null=True)
    marriage = models.IntegerField('婚否',db_column='Marriage', blank=True, null=True)
    hometown = models.CharField('籍贯',db_column='HomeTown', max_length=50, blank=True, null=True)
    address = models.CharField('住址',db_column='Address', max_length=100, blank=True, null=True)
    phone = models.IntegerField('电话',db_column='Phone', blank=True, null=True)
    inputdate = models.DateTimeField('输入日期',db_column='InputDate', blank=True, null=True)
    pifukebinglihao = models.IntegerField('皮肤科病历号',db_column='PiFuKeBingLiHao', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PatientBasicInfo'

class BingLi(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  
    patientid = models.ForeignKey('PatientBasicInfo', models.DO_NOTHING, db_column='PatientID')  
    songjianriqi = models.DateTimeField('送检日期',db_column='SongJianRiQi', blank=True, null=True)  
    xingming = models.CharField('姓名',db_column='XingMing', max_length=50, blank=True, null=True)  
    nianling = models.IntegerField('年龄',db_column='NianLing', blank=True, null=True)  
    xingbie = models.CharField('性别',db_column='XingBie', max_length=10, blank=True, null=True)  
    bumen = models.CharField('部门',db_column='BuMen', max_length=100, blank=True, null=True)  
    linchuangzhenduan = models.CharField('临床诊断',db_column='LinChuangZhenDuan', max_length=1000, blank=True, null=True)  
    qucaibuwei = models.CharField('取材部位',db_column='QuCaiBuWei', max_length=100, blank=True, null=True)  
    songjianyishi = models.CharField('送检医师',db_column='SongJianYiShi', max_length=100, blank=True, null=True)  
    baogaoyishi = models.CharField('报告医师',db_column='BaoGaoYiShi', max_length=100, blank=True, null=True)  
    operator = models.CharField('操作者',db_column='Operator', max_length=100, blank=True, null=True)  
    binglihao = models.IntegerField('病历号',db_column='BingLiHao', blank=True, null=True)  
    jingxiasuojian = models.CharField('镜下所见',db_column='JingXiaSuoJian', max_length=1000, blank=True, null=True)  
    binglizhenduan = models.CharField('病理诊断',db_column='BingLiZhenDuan', max_length=1000, blank=True, null=True)  
    baogaoriqi = models.DateTimeField('报告日期',db_column='BaoGaoRiQi', blank=True, null=True)  
    zhuyuanhao = models.IntegerField('住院号',db_column='ZhuYuanHao', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'BingLi'


class DiagHistoryBasic(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  
    patientid = models.ForeignKey('PatientBasicInfo', models.DO_NOTHING, db_column='PatientID')  
    xianbingshi = models.CharField('现病史',db_column='XianBingShi', max_length=1000, blank=True, null=True)  
    jiwangshi = models.CharField('既往史',db_column='JiWangShi', max_length=1000, blank=True, null=True)  
    jiazushi = models.CharField('家族史',db_column='JiaZuShi', max_length=1000, blank=True, null=True)  
    tigejiancha = models.CharField('体格检查',db_column='TiGeJianCha', max_length=1000, blank=True, null=True)  
    linchuangjiancha = models.CharField('临床检查',db_column='LinChuangJianCha', max_length=1000, blank=True, null=True)  
    zhiliao = models.CharField('治疗',db_column='ZhiLiao', max_length=1000, blank=True, null=True)  
    sign = models.CharField('注册医师',db_column='Sign', max_length=1000, blank=True, null=True)  
    photonum = models.IntegerField('图像数量',db_column='PhotoNum', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'DiagHistoryBasic'

class Photo(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  
    patientid = models.ForeignKey(PatientBasicInfo, models.DO_NOTHING, db_column='PatientID')  
    phototype = models.CharField('图像类型',db_column='PhotoType', max_length=100, blank=True, null=True)  
    photo = models.CharField('图像路径',db_column='Photo', max_length=100, blank=True, null=True)  
    identifyid = models.CharField('定义ID',db_column='IdentifyID', max_length=100, blank=True, null=True)  
    description = models.CharField('描述',db_column='Description', max_length=1000, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Photo'


class Login(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    user = models.CharField('用户名',db_column='User', max_length=100)  
    password = models.CharField('密码',db_column='Password', max_length=100)  

    class Meta:
        managed = False
        db_table = 'login'
