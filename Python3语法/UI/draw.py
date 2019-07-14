import turtle #调用模块turtle

def DRAWSquare(x,y,radius):
    t=turtle.Pen()  #创建画布
    t.forward(radius)   #移动50个像素
    t.left(90)
    t.forward(radius)
    t.left(90)
    t.forward(radius)
    t.left(90)
    t.forward(radius)
    t.left(90)   #画出了一个正方形

def DRAWTriangle(x,y,radius):
    t=turtle.Pen()
    for i in range(3):
        turtle.seth(i*120)
        turtle.fd(radius)

def DRAWStar(x,y,radius):
    t=turtle.Pen()
    t.up()
    t.goto(x,y)
    t.left(36)
    t.down()
    for i in range(5):
        t.forward(radius)
        t.left(144)


def main():
    radius = float(input('Radius:'))
    x = float(input('x:'))
    y = float(input('y:'))
    Choose = input('Input shape (s - square ,t -truanqle ,st -start) : ')
    if Choose == 's':
        DRAWSquare(x,y,radius)
    elif Choose == 't':
        DRAWTriangle(x,y,radius)
    elif Choose == 'st':
        DRAWStar(x,y,radius)

main()

