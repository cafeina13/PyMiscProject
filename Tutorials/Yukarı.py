import random

sozluk = {0:"süper Şanslı",1:"çok şanslısın",2:"Şanslı tahmin",3:"Şanslı",4:"İyisin heee",5:"Fena değil",6:"idare edersin",7:"iyi diyelim iyi ol",8:"bilmeseydin",9:"Yarına kadar beklerdik devam etseydin"}
rastgele = random.randrange(1,99)

sayi = int(input("Lütfen bir sayı giriniz... "))

sayac = 0
denYukari = 0
denAsagi = 100
while sayi != rastgele:
    sayac += 1
    if sayi > rastgele:
        if sayi < denAsagi:
            denAsagi = sayi
        sayi = int(input(f"{denAsagi}'den aşağı {denYukari}'den yukarı\nAşağı... "))
    else:
        if sayi > denYukari:
            denYukari = sayi
        sayi = int(input(f"{denAsagi}'den aşağı {denYukari}'den yukarı\nyukarı... "))


if sayac in sozluk:
    print(f"{sozluk[sayac]}\n{sayac} Kerede bildin")
else:
    print("Kaç kerede bildin saysını unuttum daha çok çalış")