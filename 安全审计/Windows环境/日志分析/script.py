#coding=utf-8
import mmap
import contextlib
from Evtx.Evtx import FileHeader
from Evtx.Views import evtx_file_xml_view
from xml.dom import minidom

def MyFun():
    #要操作的指定日志文件路径
    EvtxPath = "C:\Windows\System32\winevt\Logs\Security.evtx"
    #打开指定文件
    with open(EvtxPath,'r') as f:
        with contextlib.closing(mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)) as buf:
            #FileHeader是Evtx模块的一个方法
            fh = FileHeader(buf, 0)
            # 测试
            #help(FileHeader)

            # Evtx库解析文件，返回的结果由两个元素构成
            for xml, record in evtx_file_xml_view(fh):
                #只输出EventID为1102的Event
                InterestEvent(xml, 4672)
            print("完成。")

# 过滤掉不需要的事件，输出感兴趣的事件
def InterestEvent(xml, EventID):
    #parse()获取DOM对象
    xmldoc = minidom.parseString(xml)
    #minidom类方法 通过dom对象或根元素，再根据标签名获取元素节点，是个列表
    eventID = xmldoc.getElementsByTagName('EventID')[0]
    #这是一个序列,所有的指定ID值集合
    ID_node = eventID.childNodes[0]
    #打印所有序列值
    print(ID_node.data)
    #打印所有对象
    #print(eventID)

if __name__ == '__main__':
    MyFun()