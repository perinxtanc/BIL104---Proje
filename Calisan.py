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
