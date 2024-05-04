class Konyv:
    def __init__(self,konyv_cim,konyv_ar):
        self.konyv_cim=konyv_cim
        self.konyv_ar=konyv_ar
    def write_my_name(self):
        print(f'{self.konyv_cim}')
        
    def raise_price(self):
        self.konyv_ar += 200
        print(f'{self.konyv_ar}')


my_konyv_1 = Konyv(konyv_cim='Háború és Béke',konyv_ar=4000)
my_konyv_2 = Konyv(konyv_cim='Vörös és Fekete',konyv_ar=5000)

my_konyv_1.write_my_name()
my_konyv_2.write_my_name()

my_konyv_2.raise_price()
my_konyv_2.raise_price()
my_konyv_2.raise_price()