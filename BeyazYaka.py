from Calisan import Calisan

class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi
    
    def get_tesvik_primi(self):
        return self.__tesvik_primi
    
    def set_yipranma_payi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi
