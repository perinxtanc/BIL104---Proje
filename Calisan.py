from Insan import Insan

class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas
            
    def get_sektor(self):
        return self.__sektor
    
    def set_sektor(self, sektor):
        self.__sektor = sektor
            
    def get_tecrube(self):
        return self.__tecrube
    
    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube
    
    def get_maas(self):
        return self.__maas
    
    def set_maas(self, maas):
        self.__maas = maas
    
    def __str__(self):
        return f"{super().__str__()}\nSektör: {self.__sektor}\nTecrübe: {self.__tecrube} yıl\nMaaş: {self.__maas}"
