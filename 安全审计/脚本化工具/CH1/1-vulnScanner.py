#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import os
import sys
""" 
    脚本功能：检查目标端口是否打开通信，并返回端口服务进程，检查该进程是否存在漏洞
    适用范围：快速安全监测，网络管理员
    备注：需要准备一份存在漏洞的filename列表
"""



# 端口扫描
# 返回结果返回端口通信结果
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return

# 检查危险端口返回的信息
def checkVulns(banner, filename):

    f = open(filename, 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print '[+] Server is vulnerable: ' +\
                banner.strip('\n')

# 主进程
def main():



    # 接受文件作为参数
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        # 检查文件是否存在
        if not os.path.isfile(filename):
            print '[-] ' + filename +\
                ' does not exist.'
            exit(0)
        # 检查读取权限
        if not os.access(filename, os.R_OK):
            print '[-] ' + filename +\
                ' access denied.'
            exit(0)
    else:   
        print '[-] Usage: ' + str(sys.argv[0]) +\
            ' <vuln filename>'
        exit(0)

    # 端口检查列表
    portList = [21,22,25,80,110,443]
    for x in range(147, 150):
        # 拼装待检测的IP 
        ip = '192.168.95.' + str(x)
        for port in portList:
            banner = retBanner(ip, port)
            # 如果检测到危险点
            if banner:
                print '[+] ' + ip + ' : ' + banner
                checkVulns(banner, filename)


if __name__ == '__main__':
    main()
