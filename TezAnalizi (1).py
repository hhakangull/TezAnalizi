# içindekiler
# şekiller
# tablolar
# denklemler
# referanslar
# giriş
# içerik
class Icindekiler:
    icindekiler_listesi = {}

    def eleman_ekle(self, eleman_yazisi, tez_baslangic_sayfasi):
        eleman_yazisi = eleman_yazisi.split(" ")
        sayfa_numarasi = int(eleman_yazisi[-1]) - 1 + tez_baslangic_sayfasi
        baslik = ""
        for i in range(len(eleman_yazisi) - 1):
            baslik = baslik + eleman_yazisi[i] + " "
        icerik = baslik.strip()
        self.icindekiler_listesi[icerik] = sayfa_numarasi


class Sekiller:
    sekiller_listesi = {}

    def eleman_ekle(self, eleman_yazisi, tez_baslangic_sayfasi):
        eleman_yazisi = eleman_yazisi.split(" ")
        sayfa_numarasi = int(eleman_yazisi[-1]) - 1 + tez_baslangic_sayfasi
        baslik = ""
        for i in range(len(eleman_yazisi) - 1):
            baslik = baslik + eleman_yazisi[i] + " "
        icerik = baslik.strip()
        self.sekiller_listesi[icerik] = sayfa_numarasi


class Tablolar:
    tablolar_listesi = {}

    def eleman_ekle(self, eleman_yazisi, tez_baslangic_sayfasi):
        eleman_yazisi = eleman_yazisi.split(" ")
        sayfa_numarasi = int(eleman_yazisi[-1]) - 1 + tez_baslangic_sayfasi
        baslik = ""
        for i in range(len(eleman_yazisi) - 1):
            baslik = baslik + eleman_yazisi[i] + " "
        icerik = baslik.strip()
        self.tablolar_listesi[icerik] = sayfa_numarasi


class Denklemler:
    denklemler_listesi = {}

    def eleman_ekle(self, eleman_yazisi, tez_baslangic_sayfasi):
        eleman_yazisi = eleman_yazisi.split(" ")
        sayfa_numarasi = int(eleman_yazisi[-1]) - 1 + tez_baslangic_sayfasi
        baslik = ""
        for i in range(len(eleman_yazisi) - 1):
            baslik = baslik + eleman_yazisi[i] + " "
        icerik = baslik.strip()
        self.denklemler_listesi[icerik] = sayfa_numarasi


class Referanslar:
    referanslar_listesi = []

    def eleman_ekle(self, eleman_yazisi):
        if (eleman_yazisi != "KAYNAKÇA"):
            self.referanslar_listesi.append(eleman_yazisi[0:7])


class Cizelgeler:
    cizelgeler_listesi = {}

    def eleman_ekle(self, eleman_yazisi, tez_baslangic_sayfasi):
        eleman_yazisi = eleman_yazisi.split(" ")
        sayfa_numarasi = int(eleman_yazisi[-1]) - 1 + tez_baslangic_sayfasi
        baslik = ""
        for i in range(len(eleman_yazisi) - 1):
            baslik = baslik + eleman_yazisi[i] + " "
        icerik = baslik.strip()
        self.cizelgeler_listesi[icerik] = sayfa_numarasi


class Giris:
    giris_yazisi = ""

    def eleman_ekle(self, eleman_yazisi):
        self.giris_yazisi = self.giris_yazisi + " \n " + eleman_yazisi


# indisler 0 dan başlıyor fakat 0 = sayfa 1 anlamına gelmektedir
class Icerik:
    sayfalar_listesi = []

    def icerigi_guncelle(self, icerik_baslangic_sayfasi, icerik_bitis_sayfasi):
        for i in range(icerik_baslangic_sayfasi, icerik_bitis_sayfasi):
            self.sayfalar_listesi.append(i)


class Tez:
    icindekiler_nesnesi = ""
    sekiller_nesnesi = ""
    tablolar_nesnesi = ""
    cizelgeler_nesnesi = ""
    denklemler_nesnesi = ""
    referanslar_nesnesi = ""
    giris_nesnesi = ""
    icerik_nesnesi = ""
    tez_basligi = ""

    def __init__(self, tez_basligi, icindekiler_nesnesi, sekiller_nesnesi, tablolar_nesnesi, denklemler_nesnesi,
                 cizelgeler_nesnesi, referanslar_nesnesi, giris_nesnesi, icerik_nesnesi):
        self.icindekiler_nesnesi = icindekiler_nesnesi
        self.sekiller_nesnesi = sekiller_nesnesi
        self.tablolar_nesnesi = tablolar_nesnesi
        self.denklemler_nesnesi = denklemler_nesnesi
        self.referanslar_nesnesi = referanslar_nesnesi
        self.giris_nesnesi = giris_nesnesi
        self.icerik_nesnesi = icerik_nesnesi
        self.cizelgeler_nesnesi = cizelgeler_nesnesi
        self.tez_basligi = tez_basligi


import fitz


class PdfIslemleri:
    # Değişken tanımlamaları
    tez_yolu = ""
    tez_okuyucu = ""
    tez_nesnesi = ""
    icindekiler_listesi_sayfa_numaralari = []
    sekiller_listesi_sayfa_numaralari = []
    tablolar_listesi_sayfa_numaralari = []
    denklemler_listesi_sayfa_numaralari = []
    referanslar_listesi_sayfa_numaralari = []
    giris_sayfa_numaralari = []
    cizelgeler_sayfa_numaralari = []
    tez_baslangic_sayfasi = 0
    baslik_sayfa_numarasi = 0
    baslik = ""

    # Nesne tanımlamaları
    icindekiler_nesnesi = Icindekiler()
    sekiller_nesnesi = Sekiller()
    tablolar_nesnesi = Tablolar()
    denklemler_nesnesi = Denklemler()
    referanslar_nesnesi = Referanslar()
    giris_nesnesi = Giris()
    cizelgeler_nesnesi = Cizelgeler()
    icerik_nesnesi = Icerik()

    def __init__(self, tez_baslik_sayfa_numarasi, pdf_tez_yolu, icindekiler_sayfalari, sekiller_sayfalari,
                 tablolar_sayfalari, denklemler_sayfalari, cizelgeler_sayfalari, referanslar_sayfalari, giris_sayfalari,
                 tez_baslangic_sayfasi):
        self.tez_yolu = pdf_tez_yolu
        self.icindekiler_listesi_sayfa_numaralari = icindekiler_sayfalari
        self.sekiller_listesi_sayfa_numaralari = sekiller_sayfalari
        self.tablolar_listesi_sayfa_numaralari = tablolar_sayfalari
        self.denklemler_listesi_sayfa_numaralari = denklemler_sayfalari
        self.referanslar_listesi_sayfa_numaralari = referanslar_sayfalari
        self.giris_sayfa_numaralari = giris_sayfalari
        self.cizelgeler_listesi_sayfa_numaralari = cizelgeler_sayfalari
        self.tez_baslangic_sayfasi = tez_baslangic_sayfasi - 1
        self.baslik_sayfa_numarasi = tez_baslik_sayfa_numarasi - 1
        self.messageBox = []
        self.Tezi_Ac()

    def Tezi_Ac(self):
        self.tez_nesnesi = fitz.open(tez_yolu)
        self.Tezi_Parcala()

    def Tezi_Parcala(self):
        en_buyuk_giris_sayfasi = 0
        if (len(self.icindekiler_listesi_sayfa_numaralari) > 0):
            for sayfa_numarasi in self.icindekiler_listesi_sayfa_numaralari:
                sayfa_nesnesi = self.tez_nesnesi.loadPage(sayfa_numarasi - 1)
                sayfa_yazisi = sayfa_nesnesi.getText()
                sayfa_satirlari = sayfa_yazisi.splitlines()
                baslik = ""
                numara = ""
                for satir in sayfa_satirlari:
                    guncel_satir = satir.strip()

                    if (baslik != "" and len(guncel_satir) > 0 and guncel_satir.isdigit()):
                        numara = guncel_satir
                        self.icindekiler_nesnesi.eleman_ekle(baslik + " " + numara, tez_baslangic_sayfasi)
                        numara = ""
                        baslik = ""

                    elif (baslik != "" and len(guncel_satir) > 0):
                        baslik = baslik + " " + guncel_satir

                    if (len(guncel_satir) > 4):
                        if (guncel_satir[0].isdigit() and (guncel_satir[1] == '.' or guncel_satir[2] == '.')):
                            baslik = guncel_satir
                if (en_buyuk_giris_sayfasi < sayfa_numarasi):
                    en_buyuk_giris_sayfasi = sayfa_numarasi
            # print(self.icindekiler_nesnesi.icindekiler_listesi)
            print("İçerik Kısmı Derlendi...")
            self.messageBox.append("İçerik Kısmı Derlendi...")

        if (len(self.sekiller_listesi_sayfa_numaralari) > 0):
            for sayfa_numarasi in self.sekiller_listesi_sayfa_numaralari:
                sayfa_nesnesi = self.tez_nesnesi.loadPage(sayfa_numarasi - 1)
                sayfa_yazisi = sayfa_nesnesi.getText()
                sayfa_satirlari = sayfa_yazisi.splitlines()
                baslik = ""
                numara = ""
                for satir in sayfa_satirlari:
                    guncel_satir = satir.strip()

                    if (baslik != "" and len(guncel_satir) > 0 and guncel_satir.isdigit()):
                        numara = guncel_satir
                        self.sekiller_nesnesi.eleman_ekle(baslik + " " + numara, tez_baslangic_sayfasi)
                        numara = ""
                        baslik = ""

                    elif (baslik != "" and len(guncel_satir) > 0):
                        baslik = baslik + " " + guncel_satir

                    if (len(guncel_satir) > 4):
                        if (guncel_satir.split(" ")[0] == "Şekil"):
                            baslik = guncel_satir
                if (en_buyuk_giris_sayfasi < sayfa_numarasi):
                    en_buyuk_giris_sayfasi = sayfa_numarasi
            # print(self.sekiller_nesnesi.sekiller_listesi)
            print("Şekiller Listesi Derlendi...")
            self.messageBox.append("Şekiller Listesi Derlendi...")

        if (len(self.tablolar_listesi_sayfa_numaralari) > 0):
            for sayfa_numarasi in self.tablolar_listesi_sayfa_numaralari:
                sayfa_nesnesi = self.tez_nesnesi.loadPage(sayfa_numarasi - 1)
                sayfa_yazisi = sayfa_nesnesi.getText()
                sayfa_satirlari = sayfa_yazisi.splitlines()
                baslik = ""
                numara = ""
                for satir in sayfa_satirlari:
                    guncel_satir = satir.strip()

                    if (baslik != "" and len(guncel_satir) > 0 and guncel_satir.isdigit()):
                        numara = guncel_satir
                        self.tablolar_nesnesi.eleman_ekle(baslik + " " + numara, tez_baslangic_sayfasi)
                        numara = ""
                        baslik = ""

                    elif (baslik != "" and len(guncel_satir) > 0):
                        baslik = baslik + " " + guncel_satir

                    if (len(guncel_satir) > 4):
                        if (guncel_satir.split(" ")[0] == "Tablo"):
                            baslik = guncel_satir
                if (en_buyuk_giris_sayfasi < sayfa_numarasi):
                    en_buyuk_giris_sayfasi = sayfa_numarasi
            # print(self.tablolar_nesnesi.tablolar_listesi)
            print("Tablolar Listesi Derlendi...")

        if (len(self.denklemler_listesi_sayfa_numaralari) > 0):
            for sayfa_numarasi in self.denklemler_listesi_sayfa_numaralari:
                sayfa_nesnesi = self.tez_nesnesi.loadPage(sayfa_numarasi - 1)
                sayfa_yazisi = sayfa_nesnesi.getText()
                sayfa_satirlari = sayfa_yazisi.splitlines()
                baslik = ""
                numara = ""
                for satir in sayfa_satirlari:
                    guncel_satir = satir.strip()

                    if (baslik != "" and len(guncel_satir) > 0 and guncel_satir.isdigit()):
                        numara = guncel_satir
                        self.denklemler_nesnesi.eleman_ekle(baslik + " " + numara, tez_baslangic_sayfasi)
                        numara = ""
                        baslik = ""

                    elif (baslik != "" and len(guncel_satir) > 0):
                        baslik = baslik + " " + guncel_satir

                    if (len(guncel_satir) > 4):
                        if (guncel_satir.split(" ")[0] == "Denklem"):
                            baslik = guncel_satir
                if (en_buyuk_giris_sayfasi < sayfa_numarasi):
                    en_buyuk_giris_sayfasi = sayfa_numarasi
            # print(self.denklemler_nesnesi.denklemler_listesi)
            print("Denklemler Listesi Derlendi...")

        if len(self.cizelgeler_listesi_sayfa_numaralari) > 0:
            for sayfa_numarasi in self.cizelgeler_listesi_sayfa_numaralari:
                sayfa_nesnesi = self.tez_nesnesi.loadPage(sayfa_numarasi - 1)
                sayfa_yazisi = sayfa_nesnesi.getText()
                sayfa_satirlari = sayfa_yazisi.splitlines()
                baslik = ""
                numara = ""
                for satir in sayfa_satirlari:
                    guncel_satir = satir.strip()

                    if (baslik != "" and len(guncel_satir) > 0 and guncel_satir.isdigit()):
                        numara = guncel_satir
                        self.cizelgeler_nesnesi.eleman_ekle(baslik + " " + numara, tez_baslangic_sayfasi)
                        numara = ""
                        baslik = ""

                    elif (baslik != "" and len(guncel_satir) > 0):
                        baslik = baslik + " " + guncel_satir

                    if (len(guncel_satir) > 4):
                        if (guncel_satir.split(" ")[0] == "Çizelge"):
                            baslik = guncel_satir
                if (en_buyuk_giris_sayfasi < sayfa_numarasi):
                    en_buyuk_giris_sayfasi = sayfa_numarasi
            # print(self.cizelgeler_nesnesi.cizelgeler_listesi)
            print("Çizelgeler Listesi Derlendi...")
            self.messageBox.append("Çizelgeler Listesi...")

        if len(self.referanslar_listesi_sayfa_numaralari) > 0:
            for sayfa_numarasi in self.referanslar_listesi_sayfa_numaralari:
                sayfa_nesnesi = self.tez_nesnesi.loadPage(sayfa_numarasi - 1)
                sayfa_yazisi = sayfa_nesnesi.getText()
                sayfa_satirlari = sayfa_yazisi.splitlines()
                baslik = ""
                numara = ""
                onceki_satir = ""
                for satir in sayfa_satirlari:
                    guncel_satir = satir.strip()
                    if (len(guncel_satir) > 4 and len(onceki_satir) <= 4):
                        baslik = guncel_satir
                        self.referanslar_nesnesi.eleman_ekle(baslik)
                    onceki_satir = satir
            # print(self.referanslar_nesnesi.referanslar_listesi)
            print("Referanslar Listesi Derlendi...")
            self.messageBox.append("Referanslar Listesi...")

        if len(self.giris_sayfa_numaralari) > 0:
            for sayfa_numarasi in self.giris_sayfa_numaralari:
                sayfa_nesnesi = self.tez_nesnesi.loadPage(sayfa_numarasi - 1)
                sayfa_yazisi = sayfa_nesnesi.getText()
                self.giris_nesnesi.eleman_ekle(sayfa_yazisi)
            # print(str(len(self.giris_nesnesi.giris_yazisi)) + " adet harf içeriyor")
            print("Giriş Yazısı Derlendi...")
            self.messageBox.append("Giriş Yazısı...")

        self.icerik_nesnesi.icerigi_guncelle(en_buyuk_giris_sayfasi + 1,
                                             self.referanslar_listesi_sayfa_numaralari[0] - 1)
        # print(self.icerik_nesnesi.sayfalar_listesi)
        print("İçerik Kısmının Sayfa Numaraları Güncellendi...")
        self.messageBox.append("İçerik Kısmının Sayfa Numaraları Güncellendi...")

        sayfa_nesnesi = self.tez_nesnesi.loadPage(self.baslik_sayfa_numarasi)
        sayfa_yazisi = sayfa_nesnesi.getText()
        sayfa_satirlari = sayfa_yazisi.splitlines()
        bos_satir_sayisi = 0
        baslik_satiri_baslangici = 0
        for i in range(len(sayfa_satirlari)):
            if len(sayfa_satirlari[i]) < 2:
                bos_satir_sayisi = bos_satir_sayisi + 1
            if len(sayfa_satirlari[i]) >= 5 and bos_satir_sayisi >= 3:
                baslik_satiri_baslangici = i
                break

        while baslik_satiri_baslangici < len(sayfa_satirlari) and len(sayfa_satirlari[baslik_satiri_baslangici]) >= 5:
            self.baslik = self.baslik + sayfa_satirlari[baslik_satiri_baslangici] + " "
            baslik_satiri_baslangici = baslik_satiri_baslangici + 1
        # print(self.baslik)
        print("Başlık Kısmı Başarı İle Derlendi...")
        self.messageBox.append("Başlık Kısmı Başarı İle Derlendi...")

    def Tez_Nesnesi_Olustur(self):
        return Tez(self.baslik,
                   self.icindekiler_nesnesi,
                   self.sekiller_nesnesi,
                   self.tablolar_nesnesi,
                   self.denklemler_nesnesi,
                   self.cizelgeler_nesnesi,
                   self.referanslar_nesnesi,
                   self.giris_nesnesi,
                   self.icerik_nesnesi)


class HataKontrolleri:

    def __init__(self, tez_nesnesi, tez_yolu):
        self.tez_nesnesi = tez_nesnesi
        self.tez_yolu = tez_yolu
        self.Tezi_Ac()

    def Kontrol_Baslat(self):
        islem_numarasi = 11
        message = []
        if (self.Baslik_Kontrolu(self.tez_nesnesi.tez_basligi) == False):
            islem_numarasi = 1
            message.append("Başlıktaki Her Kelimenin Baş Harfi Büyük Değil")

        if (self.Giris_Yazisi_Kontrolu(self.tez_nesnesi.giris_nesnesi.giris_yazisi) == False):
            islem_numarasi = 7
            message.append("Giriş Sayfasının İlk Paragrafında Teşekkür İbaresi Yer Alıyor")

        if (self.Sekil_Sayfa_Uyum_Kontrolu(self.tez_nesnesi.sekiller_nesnesi) == False):
            islem_numarasi = 2
            message.append("Şekiller Listesindeki Şekil Tanımlaması Numarası İle Uyuşmuyor")

        if (self.Cizelge_Sayfa_Uyum_Kontrolu(self.tez_nesnesi.cizelgeler_nesnesi) == False):
            islem_numarasi = 5
            message.append("Çizelgeler Listesindeki Çizelge Tanımalaması Numarası İle Uyuşmuyor")

        if (self.Denklem_Sayfa_Uyum_Kontrolu(self.tez_nesnesi.denklemler_nesnesi) == False):
            islem_numarasi = 4
            message.append("Denklemler Listesindeki Denklem Tanımalaması Numarası İle Uyuşmuyor")

        if (self.Tablo_Sayfa_Uyum_Kontrolu(self.tez_nesnesi.tablolar_nesnesi) == False):
            islem_numarasi = 3
            message.append("Tablolar Listesindeki Tablo Tanımlaması Numarası İle Uyuşmuyor")

        if (self.Referans_Kontrolu(self.tez_nesnesi.referanslar_nesnesi.referanslar_listesi,
                                   self.tez_nesnesi.icerik_nesnesi.sayfalar_listesi) == False):
            islem_numarasi = 6
            message.append("Referanslarda Tanımalanan Referans Tez İçerisinde Kullanılmamış")

        if (self.Icindekiler_Kontrolu(self.tez_nesnesi.icindekiler_nesnesi) == False):
            islem_numarasi = 10
            message.append("İçindekiler Kısmındaki Sayfa Numaraları Doğru Değil")

        if (self.Cift_Tirnak_Kontrolu(self.tez_nesnesi.icerik_nesnesi.sayfalar_listesi) == False):
            islem_numarasi = 8
            message.append("İki Adet Çift Tırnak Arasında 50 Kelimeden Fazla Kelime Kullanılmış")

        if (self.Paragraf_Satir_Kontrolu(self.tez_nesnesi.icerik_nesnesi.sayfalar_listesi) == False):
            islem_numarasi = 9
            message.append("Paragraf İki Satır ve/veya İki Satırdan Daha Az Satırdan Oluşuyor")
        if len(message) < 1:
            message.append("Herhangi bir sorun bulunamadı.")
        return islem_numarasi, message

    def Baslik_Kontrolu(self, baslik_yazisi):
        baslik_yazisi = baslik_yazisi.split(" ")
        for kelime in baslik_yazisi:
            if (len(kelime) > 0 and kelime[0].islower()):
                return False
        return True

    def Giris_Yazisi_Kontrolu(self, giris_yazisi):
        ilk_paragraf = ""
        satirlar = giris_yazisi.splitlines()
        i = 0
        while (i < len(satirlar) and len(satirlar[i]) >= 5):
            ilk_paragraf = ilk_paragraf + satirlar[i]
            i = i + 1

        if ("Teşekkür" in ilk_paragraf or "teşekkür" in ilk_paragraf):
            return False
        return True

    def Sekil_Sayfa_Uyum_Kontrolu(self, sekiller_nesnesi):
        sekiller_listesi = sekiller_nesnesi.sekiller_listesi

        for sekil in sekiller_listesi:
            sayfa_nesnesi = self.pdf_nesnesi.loadPage(sekiller_listesi[sekil])
            sayfa_yazisi = sayfa_nesnesi.getText()
            if (sekil not in sayfa_yazisi):
                return False
        return True

    def Cizelge_Sayfa_Uyum_Kontrolu(self, cizelgeler_nesnesi):
        cizelgeler_listesi = cizelgeler_nesnesi.cizelgeler_listesi

        for cizelge in cizelgeler_listesi:
            sayfa_nesnesi = self.pdf_nesnesi.loadPage(cizelgeler_listesi[cizelge])
            sayfa_yazisi = sayfa_nesnesi.getText()
            if (cizelge not in sayfa_yazisi):
                return False
        return True

    def Denklem_Sayfa_Uyum_Kontrolu(self, denklemler_nesnesi):
        denklemler_listesi = denklemler_nesnesi.denklemler_listesi

        for denklem in denklemler_listesi:
            sayfa_nesnesi = self.pdf_nesnesi.loadPage(denklemler_listesi[denklem])
            sayfa_yazisi = sayfa_nesnesi.getText()
            if (denklem not in sayfa_yazisi):
                return False
        return True

    def Tablo_Sayfa_Uyum_Kontrolu(self, tablolar_nesnesi):
        tablolar_listesi = tablolar_nesnesi.tablolar_listesi

        for tablo in tablolar_listesi:
            sayfa_nesnesi = self.pdf_nesnesi.loadPage(tablolar_listesi[tablo])
            sayfa_yazisi = sayfa_nesnesi.getText()
            if (tablo not in sayfa_yazisi):
                return False
        return True

    def Referans_Kontrolu(self, referanslar_listesi, icerik_sayfa_numaralari):
        for referans in referanslar_listesi:
            is_find = False
            for sayfa_numarasi in icerik_sayfa_numaralari:
                sayfa_nesnesi = self.pdf_nesnesi.loadPage(sayfa_numarasi)
                sayfa_yazisi = sayfa_nesnesi.getText()
                if (referans in sayfa_yazisi):
                    is_find = True
                    break
            if (is_find == False):
                return False
        return True

    def Icindekiler_Kontrolu(self, icindekiler_nesnesi):
        icindekiler_listesi = icindekiler_nesnesi.icindekiler_listesi
        for icindeki in icindekiler_listesi:
            sayfa_nesnesi = self.pdf_nesnesi.loadPage(icindekiler_listesi[icindeki])
            sayfa_yazisi = sayfa_nesnesi.getText()
            if (icindeki not in sayfa_yazisi):
                return False
        return True

    def Cift_Tirnak_Kontrolu(self, icerik_sayfa_numaralari):
        for sayfa_numarasi in icerik_sayfa_numaralari:
            sayfa_nesnesi = self.pdf_nesnesi.loadPage(sayfa_numarasi)
            sayfa_yazisi = sayfa_nesnesi.getText()
            sayfa_yazisi = sayfa_yazisi.split("“")
            if (len(sayfa_yazisi) > 2):
                if (len(sayfa_yazisi[1].split(" ")) >= 50):
                    return False
        return True

    def Paragraf_Satir_Kontrolu(self, icerik_sayfa_numaralari):
        for sayfa_numarasi in icerik_sayfa_numaralari:
            sayfa_nesnesi = self.pdf_nesnesi.loadPage(sayfa_numarasi)
            sayfa_yazisi = sayfa_nesnesi.getText()
            sayfa_satirlari = sayfa_yazisi.splitlines()
            satir_sayaci = 0
            for i in range(len(sayfa_satirlari) - 1):
                if (len(sayfa_satirlari[i]) >= 5):
                    satir_sayaci = satir_sayaci + 1
                else:
                    satir_sayaci = 0

                if (len(sayfa_satirlari[i + 1]) < 5 and satir_sayaci <= 2):
                    return False
        return True

    def Tezi_Ac(self):
        self.pdf_nesnesi = fitz.open(self.tez_yolu)


tez_yolu = "TezOrnegi.pdf"
icindekiler_listesi_sayfa_numaralari = [7, 8]
sekiller_listesi_sayfa_numaralari = [11]
tablolar_listesi_sayfa_numaralari = []
denklemler_listesi_sayfa_numaralari = []
referanslar_listesi_sayfa_numaralari = [105, 106, 107, 108, 109, 110, 111, 112]
cizelgeler_listesi_sayfa_numaralari = [9, 10]
giris_sayfa_numaralari = [12, 13, 14]
tez_baslangic_sayfasi = 12
baslik_sayfasi = 1

pdf_islemleri = PdfIslemleri(baslik_sayfasi,
                             tez_yolu,
                             icindekiler_listesi_sayfa_numaralari,
                             sekiller_listesi_sayfa_numaralari,
                             tablolar_listesi_sayfa_numaralari,
                             denklemler_listesi_sayfa_numaralari,
                             cizelgeler_listesi_sayfa_numaralari,
                             referanslar_listesi_sayfa_numaralari,
                             giris_sayfa_numaralari,
                             tez_baslangic_sayfasi)

tez = pdf_islemleri.Tez_Nesnesi_Olustur()

hata_kontrol_nesnesi = HataKontrolleri(tez, tez_yolu)
result, message = (hata_kontrol_nesnesi.Kontrol_Baslat())
print(message)
