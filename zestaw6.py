#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Piotr Pasich, Łukasz Wycisło
WSB, Informatyka, Niestacjonarne, Programowanie w jezyku Python
Zestaw 6
"""

"""
Zadanie 1
Zaimportuj pakiet numpy, następnie przy użyciu funkcji array utwórz dwa 3-elementowe
wektory i wykonaj na nich podane niżej operacje, zinterpretuj wyniki:
a) +
b) -
c) *
d) /
e) **
f) %
"""

import numpy as np
a = np.array([[1,2,3],[4,5,6]])  

print('+', np.add(a[0], a[1]))
print('-', np.subtract(a[0], a[1]))
print('*', np.multiply(a[0], a[1]))
print('/', np.divide(a[0], a[1]))
print('**', np.power(a[0], a[1]))
print('%', np.mod(a[0], a[1]))

"""
Zadanie 2.
Przy użyciu funkcji matrix utwórz dwie tablice o wymiarach 3x3 i wykonaj na nich podane
niżej operacje, zinterpretuj wyniki:
a) +
b) -
c) *
d) /
e) **
f) %
g) mnożenie i dzielenie przez skalar
"""

matrixA = np.matrix(((1,1,1), (2,2,2), (3,3,3)))
matrixB = np.matrix(((3,3,3), (2,2,2), (4,4,3)))
print('+', np.add(matrixA, matrixB))
print('-', np.subtract(matrixA, matrixB))
print('*', np.multiply(matrixA, matrixB))
print('/', np.divide(matrixA, matrixB))
print('**', np.power(matrixA, matrixB))
print('%', np.fmod(matrixA, matrixB))
print('* scalar', np.multiply(matrixA, [1,2,3]))
print('/ scalar', np.divide(matrixA, [1,2,3]))

"""
Zadanie 3.
Napisz program obsługujący wyjątek spowodowany:
a) dzieleniem przez 0,
b) próbą otwarcia nieistniejącego pliku.
"""

print("Zadanie 3")

try:
    a = 1/0
except ZeroDivisionError:
    print("Dzielenie przez zero")
    

try:
    open('aaaa', 'r')
except FileNotFoundError:
    print("Plik nie istnieje")
    
"""
Zadanie 4
Napisz funkcję, która zgłosi wyjątek podczas jej użycia i obsłuż go w głównej części programu.
"""

def example(number):
    if (0 <= number <= 10) == False:
        raise IOError
    return number

try:
    number = int(input("Podaj liczbe: "))
    number = example(number)
except IOError:
    print("Liczba powinna byc z zakresu [0,10]")
except ValueError:
    print("To nie jest liczba")
else: 
    print("Liczba jest ok")