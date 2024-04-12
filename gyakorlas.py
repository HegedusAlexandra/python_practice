szam = input('Adjon meg egy szamot: ')

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