""" szam = input('Adjon meg egy szamot: ')

szam_jegyeinek_szama = len(szam)
szam_jegyeinek_osszege = 0
szam_forditott = ''
tukorszam = 'Nem tudjuk'
nincs_paros = ''

for char in szam:
    szam_jegyeinek_osszege += int(char)
    szam_forditott = char + szam_forditott
    if int(char) % 2 == 0:
        continue
    else:
        nincs_paros = nincs_paros + char

for x in range(round(len(szam)/2)):
    if szam[x] != szam[-(x+1)]:
        tukorszam = False
        break
    else:
        tukorszam = True



print(f'szam_jegyeinek_szama:{szam_jegyeinek_szama}, szam_jegyeinek_osszege:{szam_jegyeinek_osszege}, szam_forditott:{szam_forditott}, tukorszam: {tukorszam}, nincs_paros:{nincs_paros}')

# ****************Tömb adatszerkezet -> lista

dolgok = ['alma','eper', 'narancs', 'cica', 'koala', 'kutya', 'zsiráf',  'kalapács', 'matek', 'margaréta', 'narancs']
szamok=[1, 2, 3, 4, 5, 6, 4, 8, 9, 10]

# keressuk koala

keressuk_koala = 'koala'

koala_van_e = 'Van koala' if keressuk_koala in dolgok else 'Nincsen koala'
koala_helye = dolgok.index(keressuk_koala)

print(f'Koala van-e? {koala_van_e}. , A koala helye: {koala_helye}')

# masolat 3-7 index

allatok = dolgok[3:7]
print(f'Allatok: {allatok}')

# hany narancs van , töröljük az elsot ha több van

narancs_szama = dolgok.count('narancs')
if narancs_szama > 1:
    dolgok.remove('narancs')
print(f'Narancsok száma: {narancs_szama}, maradó dolgok: {dolgok}')

# fűzzünk össze egy lista elemeit egy stringgé, és fordítva.

strLanc = ''.join(map(str, szamok))
print(strLanc)

intLanc = int(strLanc)
print(intLanc)

# rendezze növekvő, majd csökkenő sorrendbe az előző lista elemeit

szamok.sort(reverse=True)
szamok.sort()
print(szamok)

# ************* Dictionary

#  Hozzunk létre egy dictionaryt, ami tárolja az egyed nevét, életkort és hogy féri (I/H)-e az illető. Írassuk ki, hogy: a felvitt nevét, korát, és h férfi-e, adjon választ a felvitt értékeke alapján. Pl. „A neve Nagy Géza, 30 eves és férfi? True”

personal_data = dict(name = input('Neve: '), age = input('Kora: '), gender = input('Az anyjával él?(I/H) : '))
print(f'A neve {personal_data['name']} , {personal_data['age']} éves és {'nem férfi' if (personal_data["gender"] == 'I' and int(personal_data['age']) > 30) else 'férfi vagy nő'}')

#  Hozzunk létre egy 1a, 1b, 2b, 3a osztályokat, adjuk meg a létszámukat. Írassuk ki, hogy mennyi osztálynak tudjuk a létszámát, mi ezen osztályoknak a neve?

class Osztaly:
    def __init__(self, nev, letszam):
        self.nev = nev
        self.letszam = letszam

    def myfunc(self):
        if self.nev == '1b':
            print('Tudjuk az 1b osztaly letszamat')
        if self.letszam == 25:
            print(f'Tudjuk az osztaly nevet : {self.nev} ahol a letszam pont 25')
        print(f"{self.nev} osztálynak {self.letszam} fő a létszáma.")


# Osztályok létrehozása és a létszámuk megadása
osztaly_1a = Osztaly("1a", 25)
osztaly_1b = Osztaly("1b", 28)
osztaly_2b = Osztaly("2b", 30)
osztaly_3a = Osztaly("3a", 27)

osztaly_1a.myfunc()
osztaly_1b.myfunc()
osztaly_2b.myfunc()
osztaly_3a.myfunc()

suli = {
    'osztaly_1a': 23,
    'osztaly_1b': 26,
    'osztaly_2a': 21,
    'osztaly_2b': 20,
    'osztaly_3a': 25
}

tuple_lista = [(kulcs, ertek) for kulcs, ertek in suli.items()]

print(tuple_lista) """

# 2 dimenziós tömb -> listák listája

import random

X = int(input("Adja meg az oszlopok számát: "))
Y = int(input("Adja meg a sorok számát: "))

def create_matrix(rows, columns):
    matrix = [[random.randint(-100, 100) for _ in range(columns)] for _ in range(rows)]
    return matrix

# random_numbers = list(map(lambda _: random.randint(-100, 100), range(columns)))

def print_matrix(matrix):
    for row in matrix:
        print(row)

matrix = create_matrix(Y, X)
print("A mátrix véletlen számokkal:")
print_matrix(matrix)

def create_2d_array(rows, columns):
    array = [[int(input(f"Adja meg az [{i+1}][{j+1}] elemet: ")) for j in range(columns)] for i in range(rows)]
    return array

def print_table(array):
    for row in array:
        print(" ".join(map(str, row)))

def find_min(array):
    flattened_array = [item for sublist in array for item in sublist]
    return min(flattened_array)

def sum_2d_array(array):
    return sum(map(sum, array))

def row_sums_and_averages(array):
    for row in array:
        row_sum = sum(row)
        row_average = row_sum / len(row)
        print(f"Sor összege: {row_sum}, Átlaga: {row_average}")

def min_max_per_row(array):
    for row in array:
        min_elem = min(row)
        max_elem = max(row)
        print(f"Sor legkisebb eleme: {min_elem}, Sor legnagyobb eleme: {max_elem}")

X = int(input("Adja meg az oszlopok számát: "))
Y = int(input("Adja meg a sorok számát: "))

array = create_2d_array(Y, X)
print("A kétdimenziós tömb:")
print_table(array)

# A) Legkisebb elem
print(f"A kétdimenziós tömb legkisebb eleme: {find_min(array)}")

# B) Tömb adatainak összege
print(f"A kétdimenziós tömb elemeinek összege: {sum_2d_array(array)}")

# C) Sorok összege és átlaga
print("Soronkénti összegek és átlagok:")
row_sums_and_averages(array)

# D) Soronkénti legkisebb és legnagyobb elem
print("Soronkénti legkisebb és legnagyobb elemek:")
min_max_per_row(array)

