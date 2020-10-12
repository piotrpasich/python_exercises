#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Piotr Pasich, Łukasz Wycisło
WSB, Informatyka, Niestacjonarne, Programowanie w jezyku Python
Zestaw 4
"""


"""
Zadanie 1
Napisz program, w którym zostanie zdefiniowana i użyta funkcja wyświetlająca napis.
"""
def show(text):
    print(text)
    
show("Sample text")

"""
Zadanie 2
Zmodyfikuj funkcję z zadania 1, tak aby napis był podawany w argumencie. 
"""

# jak wyzej - udalo się od razu zrobic jako argument

"""
Zadanie 3
Napisz funkcję obliczającą i zwracającą wynik sumy a + b, gdzie a i b są argumentami funkcji. 
"""

def sum(a, b):
    return a + b

show(sum(2,3))

"""
Zadanie 4
Napisz program pobierający dwie liczby od użytkownika i wyświetlający wynik zwrócony
przez funkcję z zadania 3.
"""

try:
    a = int(input("Podaj liczbe a"))
    b = int(input("Podaj liczbe b"))
except ValueError:
    print('To nie jest liczba')
else: 
    show(sum(a, b))
    
"""
Zadanie 5
Załaduj pakiet random, służy do tego polecenie import. Następnie użyj funkcji random z
tego pakietu do wyświetlenia liczb z zakresu:
a) [0.0 ; 1.0)
b) [1; 10)
c) [5; 15]
W podpunktach: b i c mają to być liczby całkowite.
"""

import random

# [0.0, 1.0]
show(random.random())

# [1, 10]
show(random.randint(1,10))

# [5, 15]
show(random.randint(5, 15))

"""
Zadanie 6
Napisz program losujący 6 liczb i zapisujący je w liście.
"""

list = []
for i in range(0, 6):
    list.append(random.randint(0,100))
    
print(list)

"""
Zadanie 7
Napisz program losujący jedną liczbę całkowitą z zakresu [0; 100] i pobierający drugą od
użytkownika. Program ma wyświetlić komunikat: ”wylosowana liczba jest
mniejsza/większa/równa podanej”.
"""
minNumber = 0
maxNumber = 100
randomNumber = random.randint(minNumber, maxNumber)
try:
    userNumber = int(input("Podaj dowolną liczbę z zakresu od %d do %d: " % (minNumber, maxNumber)))
    if (0 <= userNumber <= 100) == False:
        raise IOError
except ValueError:
    print('To nie jest liczba')
except IOError: 
    print('Liczba musi byc z zakresu od %d do %d' % (minNumber, maxNumber))
else:
    if userNumber < randomNumber:
        show('wylosowana liczba jest mniejsza podanej')
    elif userNumber == randomNumber:
        show('wylosowana liczba jest rowna podanej')
    else:
        show('wylosowana liczba jest większa podanej')

"""
Zadanie 8
Napisz program imitujący grę w totka. Gracz podaje 6 liczb z puli 49, po czym ma nastąpić
wylosowanie 6 liczb i wyświetlenie liczby trafień gracza.
"""

print('Zadanie 8 Totolotek')

def getUserNumber():
    return input("Podaj liczbę z przedziału 1-49: ")

def getRandomNumber():
    return random.randint(1,49)

def parseNumbers(f):
    numbers = []
    while len(numbers) < 6:
        try:
            passedNumber = f()
            number = int(passedNumber)
            
            if (1 <= number <= 49) == False:
                raise IOError
                
            numbers.append(number)
        except ValueError:
            print('To nie jest liczba')
        except IOError:
            print('Liczba z poza zakresu')
        else:
            numbers = sorted(set(numbers))
            numbers =  [*numbers]
    return numbers

userNumbers = parseNumbers(getUserNumber)
print('liczby podane przez uzytkownika',  userNumbers)

randomNumbers = parseNumbers(getRandomNumber)
print('wylosowane liczby',  randomNumbers)

print('Pokrywające się liczby', sorted(set(userNumbers) & set(randomNumbers)))

