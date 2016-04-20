#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
iter test
@author: Micahel Ran
'''
import itertools
import struct
import hashlib
# na=itertools.count(1)
# na=itertools.cycle('ABC')
na=itertools.repeat('A',10)
for n in na:
    print(n)
natuals = itertools.count(1)
ns=itertools.takewhile(lambda x:x<=10,natuals)
print(list(ns))
for c in itertools.chain('ABC', 'XYZ'):
    print(c)
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key,list(group))
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))
#测试md5摘要算法
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
#分多次计算摘要
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
#sha1测试
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
#sha256测试
sha1 = hashlib.sha256()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
#sha512测试
sha1 = hashlib.sha512()
sha1.update('13426314653'.encode('utf-8'))
print(sha1.hexdigest())

#struct测试
aa=struct.pack('>I', 10240099)
print(aa)

bb=struct.unpack('>I', b'\x00\x9c@c')
print(bb)