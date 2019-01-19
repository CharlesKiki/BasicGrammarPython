'''
    commit:
    这个反例不好的原因在于所有的职责全部写入了一个类中。
    改进的方法是对多个方法进行分割称为单独的类，最后以多重继承的方法写Iphone类。
'''

class Iphone(object):
    def __init__(self):
        pass
    #拨号
    def _dial(self,phonenumber):
        pass
    #通话完挂机
    def _hangup():
        pass
    #通话过程
    def _chat(self,object):
        pass
