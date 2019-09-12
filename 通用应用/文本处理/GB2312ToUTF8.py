#!/usr/bin/python
#encoding = utf-8
import os, sys
""" 
功能：批量将GB2312编码文件转换为UTF-8文件
环境：Windows
使用方法：命令行下 python GB2312_UTF8.py 目标文件夹地址
备注： 
如果想要知道原始文件的格式,使用notepad++打开文件,右下角有文件的编码格式
目标文件夹地址创建新文件夹
 """

# 转换函数，转换后的编码为utf-8
def convert_file(file_dir,new_dir,desc_type,previous_type):
    error_list = list()
    for root,dirs,files in os.walk(file_dir):
        for file in files:
            file_path = os.path.join(root,file)
            # try:
            #     df1 = pandas.read_csv(file_path,encoding=previous_type)
            #     new_path = os.path.join(new_dir,file)
            #     df1.to_csv(new_path,encoding=desc_type)
            # except Exception as e:
            #     print(e)
            #     print("file :{}  open is error and continue".format(file_path))
            #     error_list.append(file_path)
            #     continue
            try:
                with open(file_path, "rb") as f:
                    res = f.read().decode(previous_type)   # decode 是将二进制bytes编码转换为unicode,
                with open(os.path.join(new_dir,file),"w",encoding=desc_type) as f:  # encode 是将unicode编码转换为其他编码
                    f.write(res)
            except Exception as e:
                print("file :{} because error : [{}] continue".format(file,e))
                error_list.append(file)
        print(error_list)

def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print (path+' 创建成功')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print (path+' 目录已存在')
        return False


def main():
    file_dir = sys.argv[1]               # 存放原文件数据的目录
    new_dir = sys.argv[1] + "./new_data"   # 存放新数据的目录
    mkdir(new_dir)
    TargetFolder_list = os.listdir(file_dir)      # 列出文件夹下所有的目录与文件
    desc_type = "utf-8"         # 文件的格式
    previous_type = "GB2312"       # 文件的原格式
    convert_file(file_dir,new_dir,desc_type,previous_type)  
    print(TargetFolder_list)
    for i in range(0, len(TargetFolder_list)):
        path = os.path.join(file_dir, TargetFolder_list[i])
        if os.path.isfile(path):
            convert_file(file_dir,new_dir,desc_type,previous_type)
if __name__ == "__main__":
    main()