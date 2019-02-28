## seledium的功能
seledium作为前端的自动化测试软件，实际上也是可以当作爬虫使用的工具。它的Wevdriver模块可以用作获取网页的工具。

## seledium的在Windows下的配置

seledium本身可以支持多个语言，它在Github的项目中放出了执行文件。
地址：https://github.com/mozilla/geckodriver/releases
下载执行文件后解压到FireFox的根目录下。在Python调用该执行文件时需要指定这个Path。
    例子：webdriver.Firefox(executable_path='E:\FIREFOX\geckodriver')
如果不希望加入这一段代码，也可以在系统的环境变量PATH中添加执行文件的路径。

## 如何执行
在编写脚本之后应该给与脚本足够的权限。