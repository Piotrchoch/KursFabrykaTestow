# Lekcja 2:

print("Hello_world")

# ------------------------------------------

import random

liczba = random.randint(1, 10)
print("Wylosowana liczba to: ", liczba)


# Lekcja 5:

zmienna = 'Ala ma kota'

print(5==0)

print(5==5)

number = 1
number1 = 2

print(number + number1)

list = [1,2]

print(list)

list = [1,2,3]

print(list[0])

list = ['Ala','ma','kota',9]

print(list[0:3])

text = 'test'

text1 = 'czesc, jestem "Pawel"'

print(text1)

cities = {'city':['Warszawa', 'Gdansk', 'Bratyslawa']}

print(cities['city'][2])


# Lekcja 6:

suma = 1 + 2

print(suma)

odejmowanie = 1 - 2

print(odejmowanie)

reszta = 11 % 3

print(reszta)

kwadrat = 2 ** 2

print(kwadrat)

szescian = 10 ** 3

print(szescian)

print('zmienna ' + 'jest ' + 'super')

zmienna = 'no siema ' * 10

print(zmienna)

parzyste = [2,4,6,8]

nieparzyste = [1,3,5,7]

naturalne = parzyste + nieparzyste

print(naturalne)

print(1>2)

print(1 != 2)


# Lekcja 7:

imie = 'Paweł'
nazwisko = 'Zwierzchowski'
wiek = 30

if nazwisko == 'Zwierzchowski' and wiek == 30:
    print('Czesc Zwierzchowski, masz 30 lat')
else:
    print('to nie ty!')


if imie in ['Paweł', 'Krzysztof'] and wiek == 30:
    print('Czesc Paweł/Krzysztof, masz 30 lat')
else:
    print('nie jestes Paweł ani Krzysztof!')


zmienna1 = 1
zmienna2 = 2
zmienna3 = 3

if zmienna1 > 0:
    print('1')
elif zmienna2 < 0:
    print('2')
else:
    print('same falsy')

# Lekcja 8:


liczby = [1,2,3,4,5]

for i in liczby:
    print(i)

for i in liczby:
    print(liczby)

for i in range(10):
    print(i)

for i in range(15,18):
    print(i)

licznik = 0

while licznik < 10:
    print(licznik)
    licznik += 1

while True:
    print(licznik)
    licznik += 1
    if licznik >= 5:
        break

for x in range(20):
    if x % 2 == 0:
        continue
    print(x)