import pandas as pd
from Insan import Insan
from Calisan import Calisan
from BeyazYaka import BeyazYaka
from MaviYaka import MaviYaka
from Issiz import Issiz

insan1 = Insan('11111111111', 'Ahmet', 'Yılmaz', 30, 'Erkek', 'Türk')
insan2 = Insan('22222222222', 'Ayşe', 'Demir', 25, 'Kadın', 'Türk')

calisan1 = Calisan('33333333333', 'Mehmet', 'Aydın', 35, 'Erkek', 'Türk', 'teknoloji', 60, 20000)
calisan2 = Calisan('44444444444', 'Fatma', 'Kaya', 28, 'Kadın', 'Türk', 'muhasebe', 36, 15000)
calisan3 = Calisan('55555555555', 'Ali', 'Şahin', 32, 'Erkek', 'Türk', 'inşaat', 84, 25000)

maviyaka1 = MaviYaka('66666666666', 'Ayhan', 'Yıldız', 29, 'Erkek', 'Türk', 'teknoloji', 48, 18000, 0.2)
maviyaka2 = MaviYaka('77777777777', 'Deniz', 'Kara', 31, 'Kadın', 'Türk', 'muhasebe', 24, 16000, 0.5)
maviyaka3 = MaviYaka('88888888888', 'Can', 'Demir', 27, 'Erkek', 'Türk', 'diğer', 36, 22000, 0.7)

beyazyaka1 = BeyazYaka('99999999999', 'Elif', 'Akgün', 33, 'Kadın', 'Türk', 'inşaat', 60, 19000, 1000)
beyazyaka2 = BeyazYaka('10101010101', 'Hasan', 'Yılmaz', 26, 'Erkek', 'Türk', 'teknoloji', 36, 17000, 500)
beyazyaka3 = BeyazYaka('12121212121', 'Zeynep', 'Kaya', 30, 'Kadın', 'Türk', 'muhasebe', 48, 20000, 1500)

issiz1 = Issiz('13131313131', 'Ömer', 'Yılmaz', 24, 'Erkek', 'Türk', 12)
issiz2 = Issiz('14141414141', 'Ayşe', 'Demir', 27, 'Kadın', 'Türk', 24)
issiz3 = Issiz('15151515151', 'Mehmet', 'Aydın', 31, 'Erkek', 'Türk', 60)

data = {
    'Nesne': ['çalışan', 'çalışan', 'çalışan', 'mavi yaka', 'mavi yaka', 'mavi yaka',
              'beyaz yaka', 'beyaz yaka', 'beyaz yaka'],
    'TC No': [calisan1.get_tc_no(), calisan2.get_tc_no(),
              calisan3.get_tc_no(), maviyaka1.get_tc_no(), maviyaka2.get_tc_no(), maviyaka3.get_tc_no(),
              beyazyaka1.get_tc_no(), beyazyaka2.get_tc_no(), beyazyaka3.get_tc_no()],
    'Ad': [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(),
           maviyaka1.get_ad(), maviyaka2.get_ad(), maviyaka3.get_ad(), beyazyaka1.get_ad(), beyazyaka2.get_ad(),
           beyazyaka3.get_ad()],
    'Soyad': [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(),
              maviyaka1.get_soyad(), maviyaka2.get_soyad(), maviyaka3.get_soyad(), beyazyaka1.get_soyad(),
              beyazyaka2.get_soyad(), beyazyaka3.get_soyad()],
}
