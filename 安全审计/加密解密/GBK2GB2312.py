#-*- coding:utf-8 -*-
s = '安全实验'
s1=s.encode('utf-8')
print(s1,type(s1))      #utf-8编码
s2 = s1.decode("utf-8") # utf-8 转成 Unicode，decode(解码)需要注明当前编码格式
print(s2,type(s2))
s3 = s2.encode("gbk")   # unicode 转成 gbk，encode(编码)需要注明生成的编码格式
print(s3,type(s3))
s4 = s2.encode("utf-8") # unicode 转成 utf-8，encode(编码)注明生成的编码格式
print(s4,type(s4))


""" 在python中使用
函数encode（）进行编码，
使用decode（）进行解码。
函数decode（char_set）可以实现从其他编码到Unicode的转换，
函数encode(char_set)可以实现从Unicode到其他编码方式的转换。 """