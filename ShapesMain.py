# NAME:

from turtle import *
from math import *


def equilateral_tri(t, size=100, rotate=0, lineColor=None, fillColor=None):
    print ("Equilateral Triangle, with Size:", size, "and Rotation:", rotate)
    t.lt(rotate)
    count = 0
    while count < 3:
        t.fd(size)
        t.lt(120)
        count += 1
    t.rt(rotate)

#--------------------------QUADRILATERALS-------------------------#

def para(t, width=100, height=100, big_angle=120, rotate=0, lineColor=None, fillColor=None):
    print ("Parallelogram, with Width:", width, "Height:", height, "Large Angle:", big_angle, "and Rotation:", rotate)
    count = 0
    while count < 2:
        t.fd(width)
        t.rt(120)
        t.fd(height)
        t.rt(60)
        count += 1
        
        
    

def rhom(t, size=100, big_angle=120, rotate=0, lineColor=None, fillColor=None):
    print ("Rhombus, with Size:", size, "Large Angle:", big_angle, "and Rotation:", rotate)
    count = 0
    while count < 2:
       t.rt(60)
       t.fd(size)
       t.rt(60)
       t.fd(size)
       t.rt(60)
       count += 1
       
  
def rect(t, width=100, height=100, rotate=0, lineColor=None, fillColor=None):
    print ("Rectangle, with Width:", width, "Height:", height, "and Rotation:", rotate)
    t.rt(rotate)
    count = 0
    while count < 2:
        t.fd(width)
        t.rt(90)
        t.fd(height)
        t.rt(90)
        count += 1
    
    
def square(t, size=100, rotate=0, lineColor=None, fillColor=None):
    print ("Sqaure, with Size:", size, "and Rotation:", rotate)
    t.lt(rotate)
    count = 0
    while count < 4:
        t.fd(size)
        t.lt(90)
        count += 1
    t.rt(rotate)
  
#-------------------------------POLYGONS--------------------------#

def poly(t, sides=5, size=100, rotate=0, lineColor=None, fillColor=None):
    print ("Polygon, with Sides:", sides, "Size:", size, "and Rotation:", rotate)
    count = 0
    while count < sides:
        t.fd(size)
        t.rt(360/sides)
        count += 1

def star(t, points=5, size=100.0, rotate=0, lineColor=None, fillColor=None):
    print ("Star, with Points:", points, "Size:", size, "and Rotation:", rotate)
    count = 0
   
    while count < points:
        t.fd(size)
        t.rt(180 - (180 - 2 * (360/points)))
        count += 1

#------------------------------MOVEMENT---------------------------#

def line(t, x=100, y=100, lineColor=None):
    print ("Line to a point X:", x, "over and Y:", y, "up")
    dist = sqrt(x ** 2 + y ** 2)
    angle = degrees(atan(y/x))
    t.lt(angle)
    t.fd(dist)
    t.rt(angle)
    


def move(t, x, y):
    print ("Move without marking a line to a point X:", x, "over and Y:", y, "up")
    t.pu()
    line(t,x,y)
    t.pd()


