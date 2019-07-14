# 该程序旨在测试本机和指定IP的连接和请求，探测信息
#please use GBK as Encoding
import socket, os, struct
import IPy
#This model is used to scan IP address
import os
import sys
#This model is used to show the error
import traceback


# 通过StringVar()的get()和set()函数可以读取和输出相应内容
def Scan(IP):
    version = IPy.IP(IP).version()
    backinfo = os.system('ping %s' % IP)  # 实现pingIP地址的功能，-c1指发送报文一次，-w1指等待1秒
    if backinfo == 1:
        print("The IP can not reach.")
    else:
        print("Ping success.")


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        print("Hello,What is the IP address?")
        IPaddress = input("Enter the IP address here:")
        Scan(IPaddress)
    except Exception as e:
        print(e)
        traceback.print_exc()
        return 0
    else:
        print('No Error')  # 当没有错误的时候才执行
    finally:  # 不管出不出错一定会执行
        print('Program Finished')

if __name__ == '__main__':
    main()