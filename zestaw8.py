#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Piotr Pasich, Łukasz Wycisło
WSB, Informatyka, Niestacjonarne, Programowanie w jezyku Python
Zestaw 8
"""

"""
Zadanie 1.
Napisz program zawierający instrukcję rysowania trójkąta równobocznego .
"""

import turtle

def zadanie1():
    t = turtle.Turtle()
    
    for i in range(3):
        t.left((360/3))
        t.forward(100)
 

"""
Zadanie 2.
Napisz program pozwalający na narysowanie poniżej przedstawionego fraktala:
"""        
import math
def square(t, side=100, iteration = 30):
    print(side, iteration)
    for i in range(4):
        t.forward(side)
        t.left(90)
    if (iteration != 0):
        newSide = math.floor(side * 0.9)
        square(t, newSide, iteration-1)
        
def zadanie2():
    t = turtle.Turtle()
    t.speed('fastest')
    square(t)
     
    
"""
Zadanie 3*.
Napisz program pozwalający na narysowanie fraktala przedstawionego na następnej stronie.
"""
points = [[-175,-125],[0,175],[175,-125]] #size of triangle


def getMidPoint(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2) #find midpoint

def triangle(t, points, iteration):

    t.up()
    t.goto(points[0][0],points[0][1])
    t.down()
    t.goto(points[1][0],points[1][1])
    t.goto(points[2][0],points[2][1])
    t.goto(points[0][0],points[0][1])

    if iteration>0:
        triangle(t, [points[0],
                        getMidPoint(points[0], points[1]),
                        getMidPoint(points[0], points[2])],
                   iteration-1)
        triangle(t, [points[1],
                        getMidPoint(points[0], points[1]),
                        getMidPoint(points[1], points[2])],
                   iteration-1)
        triangle(t, [points[2],
                         getMidPoint(points[2], points[1]),
                         getMidPoint(points[0], points[2])],
                   iteration-1)

def zadanie3():
    t = turtle.Turtle()
    t.ht()
    t.speed(9)
    iterations = 5
    triangle(t, points, iterations)
    
                
x = int(input("Podaj numer zadania: "))
#x = 3
if (x==1):
    zadanie1()
elif (x==2):
    zadanie2()
elif (x==3):
    zadanie3()