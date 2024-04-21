""" def kisebb_osztok_osszege(szam):
    osszeg = 0
    for i in range(1, szam):
        if szam % i == 0:
            osszeg += i
    return osszeg

def spec_szamok():
    spec_szamok_10000 = []
    for szam in range(1, 10001):
        if kisebb_osztok_osszege(szam) == szam:
            spec_szamok_10000.append(szam)
    return spec_szamok_10000

bekert_szam = int(input("Adj meg egy számot, hogy megtudd az osztóinak az összegét: "))
print(f"{bekert_szam} osztóinak az összege: {kisebb_osztok_osszege(bekert_szam)}")

print("Az első 10 000 számban, melyeknek a tőle kisebb osztóinak az összege megegyezik a számmal:")
print(spec_szamok()) """

def talal_pitagoraszi_harmas(n):
    harmas = []
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c = (a ** 2 + b ** 2) ** 0.5
            if c.is_integer() and c <= n:
                harmas.append([a, b, int(c)])
    return harmas

def megoldas():
    num = int(input("Adjon meg egy pozitiv egesz szamot: "))
    harmas = talal_pitagoraszi_harmas(num)
    print("Pitagorszi hármasok a", num, "-es számig :")
    for szam in harmas:
        print(szam)

megoldas()