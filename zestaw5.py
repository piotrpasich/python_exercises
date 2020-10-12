#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Piotr Pasich, Łukasz Wycisło
WSB, Informatyka, Niestacjonarne, Programowanie w jezyku Python
Zestaw 5
"""

import math 

"""
Zadanie 1
"""


def getUserNumber():
    return input("Podaj liczbę: ")

def parseNumbers(f, n):
    numbers = []
    while len(numbers) < n:
        try:
            passedNumber = f()
            number = int(passedNumber)
                
            numbers.append(number)
        except ValueError:
            print('To nie jest liczba')
        else:
            numbers = sorted(set(numbers))
            numbers =  [*numbers]
    return numbers

def show(w, x, f):
    try:
        print(w, ': ', f(x))
    except ZeroDivisionError: 
        print(w, ' Obliczenie niemozliwe')
    except ValueError:
        print(w, ' Obliczenie niemozliwe')

x = parseNumbers(getUserNumber, 1)[0]

show('w1', x, lambda x: 4 * (math.sqrt((x + 6))))
show('w2', x, lambda x: (3 * math.pow(x, 3)) + (4 * math.pow(x, 2)) - (5 * x) + math.sqrt(7))
show('w3', x, lambda x: 1 / math.sqrt((2 * math.pow(x, 2)) + (3 * x) - 9))
show('w4', x, lambda x: abs(2 * x))
show('w5', x, lambda x: 1 / math.exp(x))
show('w6', x, lambda x: 6 * math.sin(x) - 5)


"""
Zadanie 2
Napisz program wyświetlający w postaci tabeli przebieg dowolnej funkcji wykorzystującej
funkcje np. sinus, cosinus.
"""

resolution = 0.01

result = [] # [[x,y]]
x = -math.pi
while x < math.pi:
    result.append([x,math.sin(x)])
    x += resolution
    
print (result)

"""
Zadanie 3
Zmodyfikuj program z zadania 2 tak, aby przebieg funkcji był wyświetlany w postaci wykresu.
Wykorzystaj do tego funkcje z modułu matplotlib.pyplot.
"""
import matplotlib.pyplot as plt

xAxis = [*map(lambda x: x[0], result)]
yAxis = [*map(lambda x: x[1], result)]
plt.plot(xAxis , yAxis )
plt.ylabel('y')
plt.xlabel('x')
plt.grid(True)
plt.title('sinus')


"""
Zadanie 4
Dodaj do wykresu otrzymanego w zadaniu 3:
a) tytuł wykresu,
b) opisy osi,
c) siatkę.
"""

#j/w


"""
Zadanie 5
Uzupełnij program z zadania 3 tak, aby obraz został automatycznie zapisany w pliku.
"""

import os
path = os.path.dirname(os.path.abspath(__file__))
plt.savefig(path + '/sinus.png')

plt.show()