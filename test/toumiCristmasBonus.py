#coding:utf-8
'''
Created on 2015年12月17日

@author: 201510260176
'''

from splinter import  Browser
import time
import urllib.request
from builtins import range
from bs4 import BeautifulSoup
with Browser() as browser:
    count=100
    sleeop=1
    #vist url
    url = "http://10.100.138.14:8383/active/toChristmasActivity.shtml?userId=100184881177"
    browser.visit(url)
    #browser.fill('wd', 'splinter - python acceptance testing for web applications')
    # Find and click the 'search' button
    button = browser.find_by_id('btn_lottery')
    for i in range(1,count):
        try:
            req = urllib.request.Request(url)
            response = urllib.request.urlopen(req)
            source_code = response.read()
            #print(source_code)
            soup = BeautifulSoup(source_code,"html.parser")
            num = soup.find('span', {'id':'number'}).string.strip() #<span id="number">0</span>
            if num == None:
                print("没找到对应的span")
            if num == '0':
                print("你没有抽奖机会了...........T_T")
                break
            else:
                print("你还有%s次抽奖机会"%num)
                print("第次%s抽奖"%i)
                button.click()
                
                time.sleep(sleeop)
        except Exception as e:
            print("看起来出现了问题%s"%e)
    browser.quit()
if __name__ == '__main__':
    browser
    pass