class Insan:
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk):
        self.__tc_no = tc_no
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk
            
    def get_tc_no(self):
        return self.__tc_no
        
    def set_tc_no(self, tc_no):
        self.__tc_no = tc_no
            
    def get_ad(self):
        return self.__ad
