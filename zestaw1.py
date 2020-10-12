# -*- coding: utf-8 -*-
"""
Piotr Pasich, Łukasz Wycisło
WSB, Informatyka, Niestacjonarne, Programowanie w jezyku Python
Zestaw 1, Zadanie 1
"""

print("Hello World.")

"""
Zestaw 1, Zadanie 2
"""

name = input("Podaj imie")
print('podales imie %s' % name)

"""
Zestaw 1, Zadanie 3
"""
name = input("Podaj imie")
print('podales imie {0}'.format(name))


"""
Zestaw 1, Zadanie 4
"""
nb = "      To jest tekst     "
print('len(zmienna) %d' % len(nb)) #dlugosc calego ciagu razem ze spacjami
print('zmienna.upper() %s' % nb.upper()) #zamiana malych liter na duze
print('zmienna.lower() %s' % nb.lower()) #zamiana duzych liter na male
print('zmienna.strip() %s' % nb.strip()) #usuniecie spacji po lewej i po prawej stronie zdania
nb = nb.strip() # nadpisanie zmiennej przez tekst bez spacji po lewej i prawej stronie
print('zmienna.split() %s' % nb.split("ciąg_znakow")) # rozbicie tekstu na tablice elementow rozdzielona parametrem
print('zmienna.split() %s' % nb.split("jest")) # rozbicie tekstu na tablice elementow rozdzielona parametrem
print('zmienna.startswith() %s' % nb.startswith("jest")) # sprawdza czy zmienna zaczyna sie od zadanego ciagu znakow
print('zmienna.startswith() %s' % nb.startswith("To")) # sprawdza czy zmienna zaczyna sie od zadanego ciagu znakow
print('zmienna.endswith() %s' % nb.endswith("st")) # sprawdza czy zmienna konczy sie zadanym ciagiem znakow
print('zmienna.count() %d' % nb.count('e')) # zlicza wystapienia ciagu znakow w tekscie
print('zmienna.index() %d' % nb.index('e')) # pokazuje indeks, na ktorym mozna znalezc danych ciag znakow w tekscie
print('zmienna[n] %s' % nb[3]) # pokazuje co znajduje sie w danym indeksie w ciagu znakow
print('zmienna[n:m] %s' % nb[3:10]) # pokazuje co znajduje sie miedzy danymi indeksami w ciagu znakow
print('tekst in zmienna %r' % ("tekst" in nb)) # sprawdza czy dany ciag znakow wystepuje w tekscie
print('zmienna.replace("tekst", "inaczej") %s' % nb.replace('tekst', 'inaczej')) # zastepuje ciag znakow nowym ciagiem
#print('zmienna + 2 %s' % (nb + 2)) # stara sie dodac wartosc int to strina - powinien wyrzucic blad
print('zmienna + str(2) %s' % nb + str(2)) # zmienia int 2 na stringa i dodaje na koncu zmiennej
print('zmienna * 2 %s' % (nb * 2)) # powtarza tekst dwukrotnie


"""
Zestaw 1, Zadanie 5
"""
lista = [
    "to jest lista",
    "lista napisow",
    "napisow lista"
    ]

print("To jest drugi element, bo zaczynamy liczyc od zera: %s" % lista[1]) 

print("'testowy'.join(lista) %s" % ('testowy'.join(lista)))
#do kazdego elementu dokleja na koncu ciag znakow testowy i skleja do stringa

lista.append("ciag znakow")
#dodaje jeden element na koncu listy
print('nowy element: %s' % lista[-1])

lista.remove("lista napisow")
#usuwa zadany element z listy 
print('lista: %s' % lista)

"""
Zestaw 1, Zadanie 6
"""

napis = "abcd"
liczba1 = 2
liczba2 = 2.3

print(type(napis)) #string
print(type(liczba1)) #int
print(type(liczba2)) #float

print(type(str(napis))) #string
print(type(str(liczba1))) #string
print(type(str(liczba2))) #string

# funkcja str mapuje typ z dowolnego na string  