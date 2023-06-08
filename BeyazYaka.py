from Calisan import Calisan

class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi
    
    def get_tesvik_primi(self):
        return self.__tesvik_primi
    
    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi
    
    def zam_hakki(self):
        try:
            tecrube_sene = int(self.get_tecrube().split()[0])
            if tecrube_sene < 2:
                return self.__tesvik_primi
            elif tecrube_sene <= 4 and self.get_maas() < 15000:
                return (self.get_maas() % tecrube_sene) * 5 + self.__tesvik_primi
            elif tecrube_sene > 4 and self.get_maas() < 25000:
                return (self.get_maas() % tecrube_sene) * 4 + self.__tesvik_primi
            else:
                return 0
        except:
            return 0
