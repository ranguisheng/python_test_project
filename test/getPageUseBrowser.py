#coding:utf-8
'''
Created on 2015年12月17日

@author: 201510260176
'''
from selenium import webdriver
URL="https://www.baidu.com/"  #定义全局url
browser = webdriver.Firefox()
def getPageInfo(url):    
    browser.get(url)
    html_source = browser.page_source
    print(html_source)
if __name__=='__main__':
    for i in range(20):
        getPageInfo(URL)
    browser.close()   
