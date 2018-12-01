#正则表达式是高级的文本匹配，抽取，与或文本形式的搜索和替换提供了基础。
#regax英文写法
#python  re模块 支持remax
#一个概念 搜索和匹配是不同的概念 
#分别使w用两个函数来实现 search()和match()
#[A-Za-z]/w+ #含义从开头是字母的尾部是任意的
#grep, expr, sed , awk. 或 Vi 中经常会使用到正则表达式
#grep命令，使用正则表达式来搜索查找指定文本 Global Regular Expression Print
#这个命令没有用户的权限限制
#expr命令，这是一个偏向于操作数据的命令，可以用于字符串匹配
#sed命令，关键字，流操作，可以结合正则表达式
#awk命令，grep的查找，sed的编辑，awk在其对数据分析并生成报告时显得尤为强大简单来说awk就是把文件逐行的读入，以空格为默认分隔符将每行切片，切开的部分再进行各种分析处理。
#一句话 为了实现shell编程的强大威力，需要配合正则表达式


import re
 
line = "Cats are smarter than dogs"
 
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")
