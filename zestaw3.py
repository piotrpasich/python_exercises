#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Piotr Pasich, Łukasz Wycisło
WSB, Informatyka, Niestacjonarne, Programowanie w jezyku Python
Zestaw 3
"""
import os


"""
Zadanie 1
Napisz program otwierający plik Dane1.txt i wyświetlający jego zawartość. 
"""
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/Dane.txt'
file = open(filename, 'r')
print(file.read())
file.close()

"""
Zadanie 2
Napisz program otwierający plik Dane1.txt i odczytujący z niego dane linia po linii
"""

print('Zadanie 2')
file = open(filename, 'r')
for x in file:
  print(x)
  print('---')
  
file.close()
# or

file = open(filename, 'r')
lines = file.readlines() 
  
count = 0
# Strips the newline character 
for line in lines: 
    print("Line{}: {}".format(count, line.strip())) 
    count += 1
file.close()

"""
Zadanie 3
Napisz program odczytujący plik tekstowy Dane2.txt o podanym formacie:
1; 2; 3; 4; 5
i zapisujący znajdujące się w nim liczby w liście ([1,2,3,4,5]).
"""

print('Zadanie 3')
filename = path + '/Dane2.txt'
try:
    file = open(filename, 'r')
except:
    print("File not found")
else:
    result = []
    for line in file.read().splitlines():
        result.append(tuple(line.split(";")))
    print(result);
file.close()    

"""
Zadanie 4
Napisz program zapisujący dowolny ciąg znaków w pliku Wynik4.txt.
"""

print('Zadanie 4')
filename = path + '/Wynik4.txt'
try:
    file = open(filename, 'a')
except:
    print("File could not be created or updated")
else:
    file.write("whatever")
file.close()


"""
Zadanie 5
Napisz program zapisujący dowolną listę (napisów, liczb) w pliku Wynik5.txt, tak aby
każdy element był w osobnej linii.
"""

print('Zadanie 5')
filename = path + '/Wynik5.txt'
try:
    file = open(filename, 'w')
except:
    print("File could not be created or updated")
else:
    lines = [
        'linia1',
        'linia 2',
        'troszke dluzszy tekst do zapisania',
        'ale nie za dlugi'
        ]
    file.write('\n'.join(lines) + '\n')
file.close()


"""
Zadanie 6
Napisz program odczytujący plik tekstowy Dane3.txt o podanym formacie:
5; 2
3; 5
2; 10
i przepisz te liczby do pliku Wynik6.txt wraz z wynikiem potęgowania:
5; 2; 25
3; 5; 243
2; 10; 1024
"""


print('Zadanie 6')
import csv

filenameOut = path + '/Wynik6.txt'
filenameIn = path + '/Dane3.txt'

try:
    fileOut = open(filenameOut, 'w+')
except:
    print("File could not be created or updated")
else:     
    with open(filenameIn, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            row.append(pow(int(row[0]), int(row[1])))
            print(row)
            fileOut.write(';'.join(map(str, row)) + "\n")


"""
Zadanie 7
Napisz program wyszukujący w pliku Dane1.txt tekstowym liczbę:
a) spacji,
b) zadanego ciągu znaków,
c) znaków przejść do następnej linii.
"""


print('Zadanie 6')
filename = path + '/Dane.txt'
file = open(filename, 'r')
text = file.read()

print('Ilosc spacji %d' % text.count(' '))
print('Ciag znakow %d' % text.count('Lorem'))
print('Ilosc nowych linii %d' % text.count('\n'))