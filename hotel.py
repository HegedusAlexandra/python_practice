from datetime import datetime, timedelta

class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=5000, szobaszam=szobaszam)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=8000, szobaszam=szobaszam)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas["szobaszam"] == szobaszam and foglalas["datum"] == datum:
                print("A szoba már foglalt ezen a napon.")
                return
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                self.foglalasok.append({"szobaszam": szobaszam, "datum": datum})
                print("Sikeres foglalás!")
                return
        print("A megadott szobaszám nem létezik a szállodában.")

    def lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas["szobaszam"] == szobaszam and foglalas["datum"] == datum:
                self.foglalasok.remove(foglalas)
                print("Sikeres lemondás!")
                return
        print("Nincs ilyen foglalás a megadott szobaszámmal és dátummal.")

    def listaz_foglalasok(self):
        if self.foglalasok:
            print("Foglalások:")
            for foglalas in self.foglalasok:
                print(f"Szobaszám: {foglalas['szobaszam']}, Dátum: {foglalas['datum']}")
        else:
            print("Nincs foglalás.")

def initialize_system():
    hotel = Szalloda("Hotel Example")
    hotel.add_szoba(EgyagyasSzoba(101))
    hotel.add_szoba(EgyagyasSzoba(102))
    hotel.add_szoba(KetagyasSzoba(201))
    hotel.add_szoba(KetagyasSzoba(202))
    hotel.add_szoba(KetagyasSzoba(203))

    today = datetime.today().date()
    for i in range(5):
        datum = today + timedelta(days=i)
        if i % 2 == 0:
            hotel.foglalas(101, datum)
        else:
            hotel.foglalas(201, datum)

    return hotel

def main():
    hotel = initialize_system()

    while True:
        print("\n1. Foglalás\n2. Lemondás\n3. Foglalások listázása\n4. Kilépés")
        choice = input("Válassz egy műveletet: ")

        if choice == "1":
            szobaszam = int(input("Add meg a szobaszámot: "))
            datum_str = input("Add meg a dátumot (YYYY-MM-DD formátumban): ")
            try:
                datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
                if datum < datetime.today().date():
                    print("A foglalás dátuma nem lehet a múltban.")
                    continue
                hotel.foglalas(szobaszam, datum)
            except ValueError:
                print("Hibás dátum formátum.")
        elif choice == "2":
            szobaszam = int(input("Add meg a szobaszámot: "))
            datum_str = input("Add meg a dátumot (YYYY-MM-DD formátumban): ")
            try:
                datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
                hotel.lemondas(szobaszam, datum)
            except ValueError:
                print("Hibás dátum formátum.")
        elif choice == "3":
            hotel.listaz_foglalasok()
        elif choice == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()