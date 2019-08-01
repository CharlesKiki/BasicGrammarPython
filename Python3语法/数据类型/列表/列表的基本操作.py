# 指定字符编码格式
#-*- coding:utf-8 -*-

# 列表以中括号开始，逗号分隔元素
list1 = ['Google', 'Runoob', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
# 删除列表元素
del list1[2]

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5]) # 分片操作，从下标1开始，到下标5结束 

# 列表和元组统称为序列
# 几种操作 索引 分片 加 乘 迭代

# 构造一个列表
Charles = ['Charles',20]
Gimmy   = ['Gimmy',20]
# 列表可以是列表的元素
Student = [Charles,Gimmy]
# 构造一个字符串，由字符构成的序列
greeting = 'Hello'
# 访问索引
greeting[0]

Getnum = input('Year:')[3]
# input返回一个字符串，可以对这个字符串做索引访问
print(Getnum)

#数组
Fidnum = ['90','100','23','45','67']
Fidnum.index('90')
