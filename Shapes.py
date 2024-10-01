from ShapesMain import *

dan = Turtle()
dan.speed(1)

def spiral():
    count = 0
    while count < 100:
        dan.fd(count)
        dan.rt(65)
        count = count + 1
        
def square():
    count = 0
    while count < 4:
        dan.fd(100)
        dan.rt(90)
        count = count + 1

def triangle():
    count = 0
    while count < 3:
        dan.fd(100)
        dan.rt(120)
        count = count + 1

move(dan,10,100)

done()
