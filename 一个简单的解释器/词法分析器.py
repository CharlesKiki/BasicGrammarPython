# -*- coding: utf-8 -*-
def readfile(path):
    file_object = open(path) 
    try:
        return file_object.read()
    #源码被全部加载，直到解释器工作完毕释放内存
    except Exception as StandardError:
        print(StandardError)

def expression():
    return

def program():
    return 

def eval():
    return 

def main():
    while True:
        try:
            text = input('C source code path> ')
        except EOFError:
            break
        if not text:
            continue
        file_context = readfile(text)
        print(file_context)

if __name__ == '__main__':
    main()

#E:\GitHubSpace\PythonBasicGrammer\一个简单的解释器\Cinterapter.c