#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
from datetime import datetime,timedelta
import urllib.request
import threading
import logging
import traceback
import os
#修改 2016-06-18  解决部分日志是txt结尾的bug
#下载文件的url  带ip和时间参数
url='http://watchdog.creditease.corp/hdfs/log/download?token=tm_apf_%s_1_1&clnm=投米&csnm=投米APP前台&file=%s_log.txt'
#ip列表
ipList=['10.130.96.234','10.130.96.238','10.130.98.88','10.130.96.230','10.130.96.237','10.130.98.30','10.130.98.31']
#下载保存路径
filePath='E:/private/Log/'
#获取日志开始日期
startDateStr='2016-06-06'
#获取日志结束日期
endDateStr='2016-06-17'
#下载资源大小计数
downDataSize=0
#获取日期列表  yyyy-MM-dd
def getDateList(begin,end):
    dateList=[]
    beginDay = datetime.strptime(begin, '%Y-%m-%d')
    print('下载日志的开始日期%s' % beginDay)
    endDay = datetime.strptime(end, '%Y-%m-%d')
    print('下载日志的结束日期%s' % endDay)
    #得到日期列表
    for i in range((endDay - beginDay).days+1):
        dateStr=(beginDay+timedelta(days=i)).strftime('%Y-%m-%d')
        dateList.append(dateStr)
#         print(dateStr)
    return dateList
#显示下载进度
def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print('%.2f%%' % per)
#获取所有日志
def getAllLog():
    global downDataSize
    downBegin = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #记录下载开始时间
    #下载日志个数计数
    downCount=0
    if os.path.exists(filePath) != True:  #目录不存在就创建
                os.makedirs(filePath)
    dateList=getDateList(startDateStr,endDateStr)
    for ip in ipList:
        #创建ip子目录
        if os.path.isdir(filePath):
            if os.path.exists(filePath+ip) != True:  #如果子目录不存在就创建
                os.mkdir(os.path.join(filePath, ip))
        for date in dateList:
            if(os.path.exists(filePath+ip+'/'+ip+'_'+date+'_log.txt') == False) and (os.path.exists(filePath+ip+'/'+ip+'_'+date+'_log.txt.gz') == False): #只下载还没下载过的文件
                downCount+=1 #下载计数器加1
                t = threading.Thread(target=getOneDayLog(ip,date), name='DownLoadThread_'+ip+'_'+date)
                t.start()
    downEnd = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #记录下载开始时间
    print('------------------------下载报告----------------------')
    if(downCount == 0):
        print('没有下载任何数据!')
    else:
        print('下载开始时间：%s' % downBegin)
        print('下载结束时间：%s' % downEnd)
        print('全部资源下载完成，共下载了%s个资源文件.' % downCount)
        print('下载资源大小：%sGB(%sMB)' %(round(downDataSize/1024,2),round(downDataSize,2)))
#以urlopen的方式下载
def downloadUseOpen(ip,date,tempUrl):
    global downDataSize
    print('获取文件的url:',tempUrl)
    f = urllib.request.urlopen(tempUrl)
    data = f.read() 
    dataSize=len(data)/1024/1024
    if(dataSize > 0):
        print('文件大小:%smb' % round(dataSize,2))
        tempFileName = ip+'_'+date+'_log.txt'
        with open(filePath+ip+'/'+tempFileName, "wb") as code:
            code.write(data)
        print('获取完成  [%s]' % tempUrl)
        downDataSize+=dataSize
    else:
        print('未获取到文件内容，尝试获取%s文件' % tempUrl+'.gz')
        f = urllib.request.urlopen(tempUrl+'.gz')
        data = f.read() 
        dataSize=len(data)/1024/1024
        print('文件大小:%smb' % round(dataSize,2))
        tempFileName = ip+'_'+date+'_log.txt.gz'
        with open(filePath+ip+'/'+tempFileName, "wb") as code:
            code.write(data)
        print('获取完成  [%s]' % tempUrl+'.gz')
        downDataSize+=dataSize
#下载某个ip某天的日志
def getOneDayLog(ip,date):
    try:
        print('-----------------开始获取如下url的日志------------------')
        tempUrl=url %(ip,date)
        print(tempUrl)
        #执行下载操作
        downloadUseOpen(ip,date,tempUrl)
    except Exception as e:
        print('Error:',e)
        traceback.print_exc()
        logging.exception(e)
if __name__=='__main__':
    getAllLog()