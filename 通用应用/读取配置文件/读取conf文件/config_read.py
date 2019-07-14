import configparser 

conf = configparser.ConfigParser()
file_path = "YourPath\\test.ini"
print('file_path :',file_path)
conf.read(file_path)

sections = conf.sections()
print('获取配置文件所有的section', sections)

options = conf.options('mysql')
print('获取指定section下所有option', options)


items = conf.items('mysql')
print('获取指定section下所有的键值对', items)


value = conf.get('mysql', 'host')
print('获取指定的section下的option', type(value), value)