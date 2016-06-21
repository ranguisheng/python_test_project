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

#获取新的验证码图片的接口url
verifyCodeUrl='http://mygiftcard.jd.com/giftcard/JDVerification.aspx?uid=7f30cdf4-3f2f-4471-8c14-5a94533955d2&t=0.3688577947670343'
#本地验证码临时存放目录
imgPath='E:/private/image/'
cardPath='E:/private/card/'
#获取下一个不重复的随机数
def getNextTryPwd():
    res=''
    #生成下一个随机密码的代码
    return res
#做初始化操作
def init():
    #创建验证码目录
    if os.path.exists(imgPath) != True: #目录不存在就创建
        os.makedirs(imgPath)
    #创建card目录
    if os.path.exists(cardPath) != True: #目录不存在就创建
        os.makedirs(cardPath)
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
    except Exception as e:
        print('Error:',e)
        traceback.print_exc()
        logging.exception(e)
    print('下载验证码图片成功,保存路径：%s' % imgPath+tempFileName)
    #利用python开源库识别验证码文字
    print('验证码识别中.......')
    image = Image.open(imgPath+tempFileName)
#     image.show()
    vcode = pytesseract.image_to_string(image)
    print('识别出的验证码：%s' % vcode)
    return vcode
#获取下一个随机不重复的密码
def getNewRandPwd():
    pwd=12
    return pwd
if __name__=='__main__':
    init()
    getNewVerifyCode(verifyCodeUrl)
    
