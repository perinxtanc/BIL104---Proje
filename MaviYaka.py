from Calisan import Calisan

class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranma_payi = yipranma_payi
            
    def get_yipranma_payi(self):
        return self.__yipranma_payi
    
    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi
    
    def zam_hakki(self):
        try:
            tecrube_sene = int(self.get_tecrube().split()[0])
            if tecrube_sene < 2:
                return self.__yipranma_payi * 10
            elif tecrube_sene <= 4 and self.get_maas() < 15000:
                return (self.get_maas() % tecrube_sene) / 2 + self.__yipranma_payi * 10
            elif tecrube_sene > 4 and self.get_maas() < 25000:
                return (self.get_maas() % tecrube_sene) / 3 + self.__yipranma_payi * 10
            else:
                return 0
        except:
            return 0
    
    def __str__(self):
        yeni_maas = self.get_maas() + self.zam_hakki()
        return f"{super().__str__()}\nYıpranma Payı: {self.__yipranma_payi}\nYeni Maaş: {yeni_maas}"
    
