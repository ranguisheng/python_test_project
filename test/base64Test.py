import base64
from collections import namedtuple,deque,defaultdict,OrderedDict,Counter
aa=base64.b64encode(b'binary\x00string')
print(aa)
bb=base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(bb)

#url safe modle BASE64
cc=base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(cc)
dd=base64.urlsafe_b64encode(b'binary\x00string')
print('url safe encode:%s' % dd)
ee=base64.urlsafe_b64decode(b'YmluYXJ5AHN0cmluZw==')
print(ee)

#collections
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)
print(p.x)
print(p.y)
print(isinstance(p, Point))
#dequeue
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
#defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])
#OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3),('b',7)])
print(d)
od = OrderedDict([('c', 1), ('b', 2), ('a', 3)])#注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
print(od)
#Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)