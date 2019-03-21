实验结果：
file_path : E:\GitHubSpace\PythonBasicGrammer\项目开发技能\读取配置文件\读取conf文件\test.ini
获取配置文件所有的section ['logging', 'mysql']
获取指定section下所有option ['host', 'port', 'user', 'password']
获取指定section下所有的键值对 [('host', '127.0.0.1'), ('port', '3306'), ('user', 'root'), ('password', '123456')]
获取指定的section下的option <class 'str'> 127.0.0.1

在软件的读取配置文件中，特殊的配置文件格式会被封装成一个parser包，这个方法可以类似对HTML文档进行DOM选取一样读写内容。