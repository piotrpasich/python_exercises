#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Piotr Pasich, Łukasz Wycisło
WSB, Informatyka, Niestacjonarne, Programowanie w jezyku Python
Zestaw 7
"""

"""
Zadanie 1.
Utwórz słownik i użyj go do przechowania danych osobowych (imię, nazwisko, wiek, pesel,
numer telefonu). Wskazówka: tylko wiek ma być liczbą, pozostałe wartości mają być
tekstami. Następnie podaj postać poleceń:
a) wyznaczenia wielkości słownika,
b) wyświetlenia wszystkich kluczy słownika, każdy w osobnym wierszu,
c) wyświetlenia wszystkich wartości słownika, każda w osobnym wierszu,
d) wszystkich elementów słownika, każdy w osobnym wierszu o formacie klucz:
wartość,
e) sprawdzenia, czy dany klucz istnieje w słowniku,
f) odwołania do wartości z kluczem 'Nazwisko',
g) zmiany wartości z kluczem 'Numer telefonu',
h) wstawienia nowego elementu słownika o kluczu 'Rok studiów', wartość ma być
liczbą,
i) usunięcia elementu o kluczu 'Rok studiów'.
"""

person = {
    'imie': 'Jan',
    'nazwisko': 'Kowalski',
    'wiek': 34,
    'pesel': '87010112213',
    'telefon': '515123123'
    }
print(person)
print('Wielkosc slownika', len(person))
print('Klucze', person.keys())
print('Wartosci', person.values())

print('d) wszystkich elementów słownika, każdy w osobnym wierszu o formacie klucz: wartość,')
for k, v in person.items():
    print(k, ": ", v)
    
if "imie" in person:
    print('Imie istnieje')
else: 
    print('Imie nie istnieje')
    
print("nazwisko: ", person['nazwisko'])

print("telefon: ", person['telefon'])
person['telefon'] = '123123123'
print("telefon: ", person['telefon'])

person['rok studiow'] = 2020
print(person)

del person['rok studiow']
print(person)


"""
Zadanie 2.
Jaki jest wynik działania metod: pop, popitem oraz clear dla słownika z zadania 1.
"""
person.pop('wiek') # usuwa pole
print(person) 

person.popitem() # usuwa ostatnie pole
print(person) 

person.clear() #usuwa wszystkie elementy
print(person) 

"""
Zadanie 3.
Utwórz słownik, w którym kluczami będą duże litery alfabetu łacińskiego, a wszystkie
wartości będą równe 100. Uwaga: słownika nie należy tworzyć przy użyciu pętli ani
wyrażenia listotwórczego!
"""

import string
keys = [*string.ascii_uppercase]
values = [100] * len(keys)
alphabet = dict(zip(keys, values))

print(alphabet)

"""
Zadanie 4.
Napisz funkcję zlicz_znaki_alfanumeryczne(tekst), która zwróci słownik, w
którym kluczami będą występujące w tekście znaki alfanumeryczne ('a' – 'z', 'A' – 'Z',
'0' – '9'), a wartościami liczba ich wystąpień. Wielkość liter nie powinna mieć znaczenia.
Jeżeli argument nie będzie tekstem to funkcja ma wyświetlić komunikat o błędzie i zwrócić
wartość None.
"""

def getAlphabet():
    keys = [*string.ascii_lowercase] + [*'0123456789']
    values = [0] * len(keys)
    alphabet = dict(zip(keys, values))
    
    return alphabet


def zlicz_znaki_alfanumeryczne(tekst): 
    if isinstance(tekst, str) == False :
        print('Tekst powinien byc stringiem')
        return None
    
    occurencies = getAlphabet()
    
    for char in tekst:
        lowChar = char.lower()
        if lowChar in occurencies:
            occurencies[lowChar] += 1
        
    return occurencies

print(zlicz_znaki_alfanumeryczne(input("Podaj tekst do zliczenia znakow: ")))

print(zlicz_znaki_alfanumeryczne(99))

"""
Zadanie 5.
Napisz program wczytujący dane z pliku Test.txt do słownika. Uwaga: klucze w pliku
mogą się powtarzać, zatem związanymi z nimi wartościami powinny być listy
"""

import os
import typing
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/Test.txt'

person = {}

with open(filename) as file:
  for row in file:
      (key, value) = row.split()
      if key in person: 
          if isinstance(person[key], typing.List):
              person[key].append(value)
          else:
              person[key] = [person[key], value]
      else: 
          person[key] = value
  
print(person)

"""
Zadanie 6.
Uzupełnij program z zadania 5 tak, aby zawartość słownika została zapisana w pliku
Test1.txt, przy czym klucze i wartości powinny być posortowane. Wskazówka:
wykorzystać funkcję sorted.
"""

filename = path + '/Test1.txt'
with open(filename, 'w+') as file: 
    personKeys = sorted(person)
    
    for key in personKeys:
        if isinstance(person[key], typing.List):
            for value in person[key]:
                file.write(key + ' ' + value + '\n')
        else:
            file.write(key + ' ' + person[key] + '\n')