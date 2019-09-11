# 由于MD5模块在python3中被移除，在python3中使用hashlib模块进行md5操作
import hashlib

# 待加密信息
str = '这是一个测试'

# 创建md5对象
hl = hashlib.md5()

# 此处必须声明encode
# 若写法为hl.update(str)  
# 报错为： Unicode-objects must be encoded before hashing
hl.update(str.encode(encoding='utf-8'))

print('MD5加密前为 ：' + str)
print('MD5加密后为 ：' + hl.hexdigest())


""" 
运行结果
MD5加密前为 ：这是一个测试
MD5加密后为 ：cfca700b9e09cf664f3ae80733274d9f
md5的长度，默认为128bit，也就是128个0和1的二进制串。这样表达是很不友好的。
所以将二进制转成了16进制，每4个bit表示一个16进制，所以128/4 = 32 换成16进制表示后，为32位了。
 """