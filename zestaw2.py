# -*- coding: utf-8 -*-
"""
Piotr Pasich, Łukasz Wycisło
WSB, Informatyka, Niestacjonarne, Programowanie w jezyku Python
Zestaw 2, Zadanie 1
"""
import calendar

print("napis\n" * 10)

for x in range(10):
    print("napis")
    
"""
Zestaw 2, Zadanie 2
"""

for x in range(1001):  # dodajemy 1 do zakresu, zeby wyswietlil 1000 
    if x % 50 == 0:
        print(x)
        
"""
Zestaw 2, Zadanie 3
"""
try:
   number = int(input('Podaj liczbe'))
   if (number > 5):
       print("Liczba %d jest wieksza od 5" % number)
   else:
       print("Liczba %d nie jest wieksza od 5" % number)
except ValueError:
    print('To nie jest liczba')
    
"""
Zestaw 2, Zadanie 4
"""

try:
   number = int(input('Podaj numer dnia tygodnia 0-7'))
   if (number > 7 or number < 1):
       raise IOError
except ValueError:
    print('To nie jest liczba')
except IOError: 
    print('Liczba musi byc z zakresu od 1 do 7')
else:
    weekdayMapper = [
        'Poniedziałek',
        'Wtorek',
        'Środa',
        'Czwartek',
        'Piątek',
        'Sobota',
        'Niedziela'
        ]
    print('Dzien tygodnia %s' % weekdayMapper[number - 1])
    
"""
Zestaw 2, Zadanie 5
"""

def sumToN(number):
    if number == 0:
        return 0
    
    return number + sumToN(number - 1)

try:
   number = int(input('Podaj liczbę do zsumowania'))
   if (number < 0):
       raise ValueError
except ValueError:
    print('To nie jest liczba większa od zera')
else:
    print('Suma: %d' % sumToN(number))
    
"""
Zestaw 2, Zadanie 6
"""

print('Napisz program pobierający liczby od użytkownika. Jeżeli zostanie podana liczba 4 to programma zakończyć swoje działanie. ')

exitNumber = 0
while (exitNumber != 4):
    try:
        exitNumber  = int(input('Wpisz liczbę'))
    except ValueError:
        print('To nie jest liczba')
    else: 
        print('Jesli chcesz przerwać wpisz 4')
        
# tutaj program konczy dzialanie

"""
Zestaw 2, Zadanie 7
"""

print('Napisz program pobierający liczby od użytkownika tak długo, aż zostanie podana liczba 0. Po odczytaniu 0 wyświetl sumę podanych przez użytkownika liczb.')

exitNumber = -1
sumNumbers = 0 
while (exitNumber != 0):
    try:
        exitNumber  = int(input('Wpisz liczbę'))
        sumNumbers += exitNumber
    except ValueError:
        print('To nie jest liczba')
    else: 
        print('Jesli chcesz przerwać wpisz 0')

print('Suma wszystkich podanych liczb to %d' % sumNumbers)
# tutaj program konczy dzialanie

"""
Zestaw 2, Zadanie 8
"""

print('Napisz program pobierający napis oraz znak od użytkownika i sprawdzający, czy w napisieznajduje się podany znak. Jeżeli tak – wyświetl indeksy występowania, jeżeli nie – stosownykomunikat.')

def find(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i

napis = input("Podaj napis: ")
znak = input("Podaj znak lub ciag znakow do sprawdzenia: ")

if znak in napis:
    print('%s wystepuje w tekscie %s %d razy na indeksach %s' % (znak, napis, napis.count(znak), list(find(napis, znak))))
else: 
    print('%s nie wystepuje w tekscie %s' % (znak, napis))