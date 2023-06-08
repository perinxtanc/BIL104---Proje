from Insan import Insan

class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrube = tecrube
        self.__statu = self.__statu_bul(tecrube)
    
    def get_tecrube(self):
        return self.__tecrube
        
    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube
        self.__statu = self.__statu_bul(tecrube)
    
    def get_statu(self):
        return self.__statu
    
    def __statu_bul(self, tecrube):
        statuler = {
            'mavi yaka': 0.2,
            'beyaz yaka': 0.35,
            'yönetici': 0.45
        }
        
        max_etkisi = max(statuler.values())
        max_statu = [k for k, v in statuler.items() if v == max_etkisi]
        
        return max_statu[0]
