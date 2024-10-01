from shapes_new import *

def house (t, size = 10, color=None):
  square(t, size*3, 0, None, color)
  move(t, size*-1, size*3)
  equilateral_tri(t, size*5, 0, None, "red")
  move(t, size*3, size*-3)
  para(t, size*.7, size*1.5, 90, 0, None, "brown")
  move(t, size*-1.5, size*1)
  square(t, size*1, 0, None, "blue")
  car(t, 10, "blue")


 
def car (t, size = 10, color=None):
    
    move(t, size*15, size*0)
    rect(t, size*3, size*2, 0, None, "red")
    move(t, size*2, size*1)
    square(t, size*1, 0, None, color)
    move(t, size*.5, size*-2)
    poly(t, 10, 3, 0, None, "black")
    move(t, size*-2, size*0)
    poly(t, 10, 3, 0, None, "black")
    ground(t, 1, None)
   
def ground (t, size = 1, color=None):
    move(t, size*-300, size*-100)
    rect(t, size*500, size*100, 0, None, "green")
   
def tree (t, size = 1, color=None):
    move(t, size*400, size*100)
    rect(t, size*10, size*35, 0, None, "brown")
    move(t, size*0, size*35)
    poly(t, 10, 15, 0, None, "green")

def sun (t, size = 15, color=None):
    move(t, size*-200, size*150)
    star(t, 9, 50, 0, "yellow", "yellow")
