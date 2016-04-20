from urllib import request,parse

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))

req = request.Request('https://mm.taobao.com/920543925.htm')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0')
# req.add_header('Host', 'mm.taobao.com')
# req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
# req.add_header('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
# req.add_header('Accept-Encoding', 'gzip, deflate')
# req.add_header('Cookie', 't=1548d7940c1b8c46f35b18a3d2a438dd; thw=cn; cna=UOi0Dmb+qgACAWX+tiIBck7A; l=Ap2dqhXvH4NTnfIHD7eeMDFqjXeXu9EM; tracknick=tb_6314653; _cc_=Vq8l%2BKCLiw%3D%3D; tg=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; miid=7213732822385296513; mt=np=&ci=5_1&cyk=1_0; uc3=sg2=BxeMKy7pGqVfzoS1aBJ6LhGt3k2PYLbDvlbiyc7XSl4%3D&nk2=F5QqboZDKdQlKg%3D%3D&id2=VWeT38cFzXnj&vt3=F8dASm%2BwcXEuAu4hEFM%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; uss=V3%2Ffq775MhvzUk5m4qJCDRnynO2Hxk3%2BdWL5rdIJJRWncTqha%2FwyW6hn2g%3D%3D; lgc=tb_6314653; CNZZDATA30064598=cnzz_eid%3D678753897-1460536864-%26ntime%3D1460536864; CNZZDATA30063600=cnzz_eid%3D576421839-1460536864-%26ntime%3D1460536864; CNZZDATA30063598=cnzz_eid%3D1539375435-1460538734-%26ntime%3D1460538734; JSESSIONID=99EEAF0E39DEF9AE61DB9277DBF373C4; v=0; cookie2=1094cacb09e99ad450717953ea66c7fb; _tb_token_=T2Y3wkBFUG8SWP8; uc1=cookie14=UoWxMc65eD6ROA%3D%3D&existShop=false&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie21=UtASsssme%2BBq&tag=7&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&pas=0; existShop=MTQ2MDk3MDA4MA%3D%3D; sg=323; cookie1=BYAPnFSrd4MIHz8xx4k60szKXHScJakJbMSQTAWLelY%3D; unb=682057002; skt=04e972d415da2029; _l_g_=Ug%3D%3D; _nk_=tb_6314653; cookie17=VWeT38cFzXnj')
# req.add_header('Connection', 'keep-alive')
data='';
content='mm-aixiu-content'
flag=False
with request.urlopen(req) as f:
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
    data=f.read().decode('gbk')
    f=open('page.html','w+')
    f.write(str(data))
    f.close()
    
with open('page.html','r') as f:
    for line in f.readlines():
        if content in line:
            print('找到了')
            flag=True
            break
if flag:
    print('YES............')
else:
    print('No.............')
    
    
# print('Login to weibo.cn...')
# email = input('Email: ')
# passwd = input('Password: ')
# login_data = parse.urlencode([
#     ('username', email),
#     ('password', passwd),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])
# 
# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
# 
# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))
