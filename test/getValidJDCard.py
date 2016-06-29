#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
# from datetime import datetime
# import urllib.request
import logging
import traceback
import os
# import pytesseract
from PIL import Image
import random
import loginJd
from bs4 import BeautifulSoup
import BloomFilter
import downloadVerifyCodePic

#每个位置可供选择的单词或数字
wordList=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#获取新的验证码图片的接口url
verifyCodeUrl='http://mygiftcard.jd.com/giftcard/JDVerification.aspx?uid=%s&t=0.3688577947670343'
#通过如下url获取新的uuid
uuidUrl='http://mygiftcard.jd.com/giftcard/index.action'
#检查一个pwd是否可用的url
checkPwdUrl="http://mygiftcard.jd.com/giftcard/queryBindGiftCard.action?t="
#待初始化的uuid
UUID=''
#本地验证码临时存放目录
imgPath='E:/private/image/'
cardPath='E:/private/card/'
bf=None
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
#     UUID=loginJd.UUID
    print('UUID is : %s' % UUID)
    global verifyCodeUrl
    verifyCodeUrl = verifyCodeUrl % UUID
    global bf
    bf = BloomFilter.BloomFilter(0.001, 100000000)
    seedElement='1234-2234-3234-4234'
    bf.insert_element(seedElement)
#获取新的uuid
def getNewUUID():
    try:
        source_code = loginJd.Navigate(uuidUrl)
        print('get new uuid:')
        print(source_code)
        soup = BeautifulSoup(source_code,"html.parser")
#         uuid = soup.find('img', {'id':'verifyImg'})
        uuid = soup.find_all('img',{'id':'verifyImg'})[0]['src'].split("?uid=")[1].split("&")[0]
        if uuid == None:
            print("鬼知道什么原因，居然没有uuid!")
        else:
            print("获取到的uuid为：%s" % uuid)
            return uuid
    except Exception as e:
        print("Error",e)
        logging.exception(e)
        traceback.print_exc()
#保存验证码图片&&获取文本的验证码
def getNewVerifyCode(verifyCodeUrl):
    #下载验证码图片
    print('开始获取验证码：%s' % verifyCodeUrl)
    try:
        codeLocalPath = downloadVerifyCodePic.downCode(verifyCodeUrl)
        print('验证码识别中.......')
        image = Image.open(codeLocalPath)
        image.show()
        vcode = input("请输入弹出图片中的验证码：") 
#         vcode = pytesseract.image_to_string(image)
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
    return pwd
def get16RandomNum():
    #使用表理解(list comprehension)一次性生成多个随机数,range函数输入不同的值，可以设置需要生成随机数的个数
    return [random.randint(0,35) for _ in range(16)]
#检查密码是否有效
def checkIfPassValid(url,uuid,pwd,verifyCode):
    url = url+str(random.random())
    print('check pass url: %s' % url)
    postData = {
      'actionType':'query',
      'uuid':uuid,
      'giftCardId':'undefined',
      'giftCardPwd':pwd,
      'verifyCode':verifyCode
    }
    print('check pass post data: %s' % postData)
    checkRes = loginJd.Navigate(url,postData)
    print('check pwd:%s' % pwd)
    print('check response: %s' % checkRes)
if __name__=='__main__':
    init()
    verifyCode = getNewVerifyCode(verifyCodeUrl)
    randPwd = getNewRandPwd()
    #如果已经存在就重新生成随机密码
    while(bf.is_element_exist(randPwd)):
        randPwd = getNewRandPwd()
    checkIfPassValid(checkPwdUrl,UUID,randPwd,verifyCode)
    
        
    
