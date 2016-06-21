#!/usr/bin/python
#encoding:utf-8
import urllib.request
import os
from datetime import datetime,timedelta
# url = 'http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2'
url = 'http://watchdog.creditease.corp/hdfs/log/download?token=tm_apf_10.130.98.31_1_1&clnm=投米&csnm=投米APP前台&file=2016-01-13_log.txt.gz'

################urlretrieve耗时三分钟########################
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
# local = os.path.join('E:/私人/downTest','Python-2.7.5.tar.bz2')
# print('urlretrieve begin:%s' % str(datetime.now()))
# urllib.request.urlretrieve(url,local,None)
# print('urlretrieve end:%s' % str(datetime.now()))

#####################urlopen耗时1分钟#####################
print('urlopen begin:%s' % str(datetime.now()))
f = urllib.request.urlopen(url) 
data = f.read() 
print('文件大小:',len(data)/1024/1024,'mb')
with open("E:/私人/downTest/demo.txt.gz", "wb") as code:     
    code.write(data)
print('urlopen end:%s' % str(datetime.now()))