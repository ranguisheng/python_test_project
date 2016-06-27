import urllib
import http.cookiejar
import socket
from bs4 import BeautifulSoup
import traceback
import base64

RETRY_COUNT=5
loginPageUrl = "https://passport.jd.com/new/login.aspx"
loginPostUrl = "http://passport.jd.com/uc/loginService"
userName=''
password=''
#定义连接函数，有超时重连功能
def Navigate(url,data={}):           
    tryTimes = 0
    while True:
        if (tryTimes > RETRY_COUNT):
            print("尝试%s次之后仍无法链接网络，程序终止" % RETRY_COUNT)
            break
        try:
            print('data type: %s' % type(data))
            if (data=={}):
                req = urllib.request.Request(url)
            else:
                req = urllib.request.Request(url,urllib.parse.urlencode(data).encode('utf-8'))
            req = urllib.request.urlopen(req).read()
            tryTimes = tryTimes +1
        except socket.error:
            print("连接失败，尝试重新连接")
            traceback.print_exc()
        else:
            break
    return req   
#处理cookie
def processCookie():
    try:
        cookie = http.cookiejar.CookieJar()
        cookieProc = urllib.request.HTTPCookieProcessor(cookie)
        opener = urllib.request.build_opener(cookieProc)
        opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')]
        urllib.request.install_opener(opener)
    except Exception as e:
        print("Error",e)
        traceback.print_exc()
#获取和组装post请求数据
def packagePostData():
    login = Navigate(loginPageUrl)
    print('获取到登录页的内容：')
    print(login)
    loginSoup = BeautifulSoup(login,'html.parser')
    #查找登陆参数中的uuid
    uuid = loginSoup.find_all("form")[0].find_all("input")[0]['value']
    print('uuid: %s' % uuid)
     
    #查找登陆参数中的随机值，class为clr
#     clr = loginSoup.find_all("span","clr")[0]
#     clrName = clr.find_next_siblings("input")[0]['name']  
#     clrValue = clr.find_next_siblings("input")[0]['value']
    clrName = 'aaa'  
    clrValue = 'bbb'
    #print clrName,clrValue
     
    #print url
    postData = {
      'loginname':base64.b64decode(userName).decode('utf-8'),
      'nloginpwd':base64.b64decode(password).decode('utf-8'),
      'loginpwd':base64.b64decode(password).decode('utf-8'),
      'machineNet':'',
      'machineCpu':'',
      'machineDisk':'', 
       str(clrName):str(clrValue),
      'uuid':uuid,
      'authcode':''
    }
    print('postData')
    print(postData)
    return postData
if __name__=='__main__':
    processCookie()
    passportRes = Navigate(loginPostUrl,packagePostData())
    print('login response: %s' % passportRes)
    #\\u8bf7\\u5237\\u65b0\\u9875\\u9762\\u540e\\u91cd\\u65b0\\u63d0\\u4ea4   请刷新页面后重新提交
     
      
    