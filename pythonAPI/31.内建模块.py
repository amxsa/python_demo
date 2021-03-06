#coding:utf-8
from datetime import datetime
from collections import namedtuple
import base64
import hashlib
from urllib import request,parse

now=datetime.now()
print(now)
#自己设置时间
dt=datetime(2016,2,14,12,50)
print(dt)
#计算毫秒数，小数位表示毫秒数
ts=dt.timestamp()
print(ts)
#毫秒数转换成时间
dt=datetime.fromtimestamp(ts)
print(dt)
#str转为datetime
day=datetime.strptime("2016-8-1 12:12:30","%Y-%m-%d %H:%M:%S")
print(day)
#datetime转换成str
string=now.strftime("%a,%b %d %H:%M")
print(string)

#tuple直接表示坐标，很难看出来
point=namedtuple("point",["x","y"])
p=point(1,2)
print(p.x,p.y)

#base64编解码
b=base64.b64encode(b"f:/test/aa.txt")
print(b)
fb=base64.b64decode(b)
print(fb)

#MD5 是最常见的摘要算法，速度很快，生成结果是固定的 128 bit 字节
md5=hashlib.md5()
md5.update("我是帅哥".encode("utf-8"))
print(md5.hexdigest())

#get
with request.urlopen("https://www.baidu.com/") as f:
	data=f.read()
	print(f.status,f.reason)
	#获取请求头信息
	for k,v in f.getheaders():
		print("%s:%s" %(k,v))

#post