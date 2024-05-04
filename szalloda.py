class Szoba :
    def __init__ (self,szoba_szam,szoba_ar,szoba_tipus):
        self.szoba_szam = szoba_szam
        self.szoba_ar = szoba_ar
        self.szoba_tipus = szoba_tipus

    def __str__(self):
        return f"Szobaszám: {self.szoba_szam}, Ár: {self.szoba_ar} Ft Tipus: {self.szoba_tipus}"

class EgyagyasSzoba(Szoba):
    def __init__(self, szoba_szam):
        super().__init__(szoba_ar=10000, szoba_szam=szoba_szam ,szoba_tipus='egyágyas szoba')

class KetagyasSzoba(Szoba):  
    def __init__(self, szoba_szam):
        super().__init__(szoba_ar=20000, szoba_szam=szoba_szam ,szoba_tipus='kétágyas szoba')

class Szalloda :
    group_name = 'GDE PROJECT EVENT GROUP'
    def __init__(self,hotel_name,hotel_szobak):
        self.hotel_name = hotel_name
        self.hotel_szobak = hotel_szobak

    def add (self,szoba):
        self.hotel_szobak.append(szoba)
    
    def delete (self,szoba_szam_torles):        
        for szoba in self.hotel_szobak:
            if szoba.szoba_szam == szoba_szam_torles :
                self.hotel_szobak.remove(szoba)
            else:
                continue

    def show(self):
        print('*********************************')
        for szoba in self.hotel_szobak:            
            print(szoba)
        print('*********************************')
            

def sys_initialization():
    szalloda_kek_hexagon = Szalloda('Kék Hexagon',[])
    szalloda_kek_hexagon.add(EgyagyasSzoba(1))
    szalloda_kek_hexagon.add(KetagyasSzoba(3))
    szalloda_kek_hexagon.add(KetagyasSzoba(6))
    return szalloda_kek_hexagon

def main(inOrOut):
    szalloda_kek_hexagon = sys_initialization()

    print(f"\n1. Foglalás\n2. Lemondás\n3. Foglalások listázása\n4. {inOrOut}")
    choice = int(input("Válassz egy műveletet: "))

    def please_sign_in():
        print('Kérlek lépj be a rendszerbe')
        main('Belépés')

    if choice == 1:
        if inOrOut == 'Belépés':
            please_sign_in()
        else:
            print('UC')
            main('Kilépés')
    elif choice == 2:
        if inOrOut == 'Belépés':
            please_sign_in()
        else:
            print('UC')
            main('Kilépés')
    elif choice == 3:
        if inOrOut == 'Belépés':
            please_sign_in()
        else:
            szalloda_kek_hexagon.show()
            main('Kilépés')
    else:
        print('Köszönjük! Viszontlátásra!' if inOrOut == 'Kilépés' else 'Isten Hozott!')
        main('Belépés' if inOrOut == 'Kilépés' else 'Kilépés')

if __name__ == "__main__":
    main('Kilépés')

