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
    'Yaş': [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(),
            maviyaka1.get_yas(), maviyaka2.get_yas(), maviyaka3.get_yas(), beyazyaka1.get_yas(), beyazyaka2.get_yas(),
            beyazyaka3.get_yas()],
    'Cinsiyet': [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(),
                 calisan3.get_cinsiyet(), maviyaka1.get_cinsiyet(), maviyaka2.get_cinsiyet(), maviyaka3.get_cinsiyet(),
                 beyazyaka1.get_cinsiyet(), beyazyaka2.get_cinsiyet(), beyazyaka3.get_cinsiyet()],
    'Uyruk': [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(),
              maviyaka1.get_uyruk(), maviyaka2.get_uyruk(), maviyaka3.get_uyruk(), beyazyaka1.get_uyruk(),
              beyazyaka2.get_uyruk(), beyazyaka3.get_uyruk()],
    'Sektör': [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), maviyaka1.get_sektor(),
               maviyaka2.get_sektor(), maviyaka3.get_sektor(), beyazyaka1.get_sektor(), beyazyaka2.get_sektor(),
               beyazyaka3.get_sektor()],
    'Tecrübe': [calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube(), maviyaka1.get_tecrube(),
                maviyaka2.get_tecrube(), maviyaka3.get_tecrube(), beyazyaka1.get_tecrube(), beyazyaka2.get_tecrube(),
                beyazyaka3.get_tecrube()],
    'Maaş': [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), maviyaka1.get_maas(),
             maviyaka2.get_maas(), maviyaka3.get_maas(), beyazyaka1.get_maas(), beyazyaka2.get_maas(),
             beyazyaka3.get_maas()],
    'Yıpranma Payı': [0, 0, 0, maviyaka1.get_yipranma_payi(), maviyaka2.get_yipranma_payi(),
                     maviyaka3.get_yipranma_payi(),0, 0, 0],
    'Teşvik Primi': [0, 0, 0, 0, 0, 0,beyazyaka1.get_tesvik_primi(),
                     beyazyaka2.get_tesvik_primi(), beyazyaka3.get_tesvik_primi()],
    'Yeni Maaş': [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), int(maviyaka1.get_maas()) + int(maviyaka1.zam_hakki()),
              int(maviyaka2.get_maas()) + int(maviyaka2.zam_hakki()), int(maviyaka3.get_maas()) + int(maviyaka3.zam_hakki()),
              int(beyazyaka1.get_maas()) + int(beyazyaka1.zam_hakki()), int(beyazyaka2.get_maas()) + int(beyazyaka2.zam_hakki()),
              int(beyazyaka3.get_maas()) + int(beyazyaka3.zam_hakki())],
}

df = pd.DataFrame(data)

df.fillna(0, inplace=True)

gruplu_df = df[["Nesne", "Tecrübe", "Yeni Maaş"]].groupby(['Nesne']).mean()
print("Tecrübe ve Yeni Maaş Ortalamaları:")
print(gruplu_df)

maas_ust_limit_sayisi = len(df[df['Maaş'] > 15000])
print("Maaşı 15000 TL üzerinde olanların toplam sayısı:", maas_ust_limit_sayisi)

siralama_df = df.sort_values('Yeni Maaş', ascending=True)
print("Yeni Maaşa Göre Sıralama:")
print(siralama_df)

tecrube_limit = 3
beyaz_yakalar = df[(df['Nesne'] == 'beyaz yaka') & (df['Tecrübe'] > tecrube_limit)]
print("Tecrübesi 3 seneden fazla olan Beyaz yakalılar:")
print(beyaz_yakalar)

maas_limit = 10000
satir_secimi_df = df[(df['Yeni Maaş'] > maas_limit)].iloc[1:6, [1, 12]]
print("Yeni Maaşı 10000 TL üzerinde olanların 2-5 satırları:")
print(satir_secimi_df)

yeni_df = df[['Ad', 'Soyad', 'Sektör', 'Yeni Maaş']]
print("Yeni DataFrame:")
print(yeni_df)
