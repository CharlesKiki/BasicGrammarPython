'''
    功能：
        陆生动物类
        水生动物类
        针对不同的动作使用不同的类。
    Commit：
            单一职责的原则：一个类只负责同类的事务
            并且注意：往往一个负责处理逻辑的类不应该承担渲染的功能。
'''

class Terrestrialanimal(object):

    def __init__(self):
        pass

    def breathe(self, name):
        print('%s 呼吸空气' %name)


class Aquatic(object):

    def __init__(self):
        pass

    def breathe(self, name):
        print('%s 呼吸水' %name)


# caller
class Client(object):
    def __init__(self):
        pass

    def work(self):
        terrestrialanimal = Terrestrialanimal()
        terrestrialanimal.breathe('牛')
        terrestrialanimal.breathe('羊')
        terrestrialanimal.breathe('猪')

        aquatic = Aquatic()
        aquatic.breathe('鱼')


if __name__ == '__main__':
    client = Client()
    client.work()
