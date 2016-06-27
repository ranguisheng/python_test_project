#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
from datetime import datetime,timedelta
import urllib.request
import threading
import logging
import traceback
import os
import pytesseract
from PIL import Image
import random
import loginJd
from bs4 import BeautifulSoup
from splinter import  Browser


#每个位置可供选择的单词或数字
wordList=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#获取新的验证码图片的接口url
verifyCodeUrl='http://mygiftcard.jd.com/giftcard/JDVerification.aspx?uid=7f30cdf4-3f2f-4471-8c14-5a94533955d2&t=0.3688577947670343'
#通过如下url获取新的uuid
uuidUrl='http://mygiftcard.jd.com/giftcard/index.action'
#待初始化的uuid
UUID=''
#本地验证码临时存放目录
imgPath='E:/private/image/'
cardPath='E:/private/card/'
#获取新的uuid
def getNewUUID():
    try:
#         browser = Browser()
#         browser.visit(uuidUrl)
#         imgTag = browser.find_by_id('verifyImg')
#         print('imgTag：%s' % imgTag)
        req = urllib.request.Request(uuidUrl)
        response = urllib.request.urlopen(req)
        source_code = response.read()
        print(source_code)
        soup = BeautifulSoup(source_code,"html.parser")
        uuid = soup.find('img', {'id':'verifyImg'}) #<span id="number">0</span>
        if uuid == None:
            print("鬼知道什么原因，居然没有uuid!")
        else:
            print("获取到的uuid为：%s" % uuid)
            return uuid
    except Exception as e:
        print("Error",e)
        logging.exception(e)
        traceback.print_exc()
#     finally:
#         browser.quit()
#做初始化操作
def init():
    #创建验证码目录
    if os.path.exists(imgPath) != True: #目录不存在就创建
        os.makedirs(imgPath)
    #创建card目录
    if os.path.exists(cardPath) != True: #目录不存在就创建
        os.makedirs(cardPath)
    #登录
    loginJd.processCookie()
    passportRes = loginJd.Navigate(loginJd.loginPostUrl,loginJd.packagePostData())
    print('login response: %s' % passportRes)
    global UUID
    #初始化UUID
    UUID=getNewUUID()
#保存验证码图片&&获取文本的验证码
def getNewVerifyCode(verifyCodeUrl):
    #下载验证码图片
    print('开始获取验证码：%s' % verifyCodeUrl)
    try:
        
        f = urllib.request.urlopen(verifyCodeUrl)
        data = f.read()
        tempFileName = datetime.now().strftime('%Y%m%d%H%M%S')+'.jpg'
        with open(imgPath+tempFileName, "wb") as code:
            code.write(data)
        print('下载验证码图片成功,保存路径：%s' % imgPath+tempFileName)
        #利用python开源库识别验证码文字
        print('验证码识别中.......')
        image = Image.open(imgPath+tempFileName)
        vcode = pytesseract.image_to_string(image)
        print('识别出的验证码：%s' % vcode)
        return vcode
    except Exception as e:
        print('Error:',e)
        traceback.print_exc()
        logging.exception(e)
#获取下一个随机不重复的密码
def getNewRandPwd():
    i=0
    pwd=''
    numList = get16RandomNum()
    for index in numList:
        pwd+=wordList[index]
        i+=1
        if( i>0 and i<16 and (i % 4==0) ):
            pwd+='-'
    print('新的随机密码为：%s' % pwd)
    return pwd
def get16RandomNum():
    #使用表理解(list comprehension)一次性生成多个随机数,range函数输入不同的值，可以设置需要生成随机数的个数
    return [random.randint(0,35) for _ in range(16)]
if __name__=='__main__':
    init()
    getNewVerifyCode(verifyCodeUrl)
    getNewRandPwd()
    
