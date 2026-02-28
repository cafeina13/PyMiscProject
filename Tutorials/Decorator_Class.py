class kisim:
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad

    @property
    def adsoyad(self):
        return f"{self.ad} {self.soyad}"

    @adsoyad.setter
    def adsoyad(self,isim:str):
        self.ad, self.soyad = isim.split(" ")

    @property
    def email(self):
        return f"{self.ad}{self.soyad}@example.com"


    @adsoyad.deleter
    def adsoyad(self):
        self.ad = None
        self.soyad = None

    @adsoyad.deleter
    def adsoyad(self):
        self.ad = "silindi"
        self.soyad = "silindi"


kisi1 = kisim("umay","kayra")
print(kisi1.email)

kisi1.adsoyad = "Luna Cynthia"
print(kisi1.email)

del kisi1.adsoyad
print(kisi1.email)
kisi1.ad = "Khonshu"
print(kisi1.ad)
print(kisi1.email)