aylar:dict =     {"ocak":13,"şubat":14,"mart":3 ,"nisan":4 ,"mayıs":5 ,"haziran":6 ,"temmuz":7 ,"ağustos":8 ,"eylül":9,"ekim":10,"kasım":11,"aralık":12}
aylarGun:dict =  {"ocak":31,"şubat":28,"mart":31,"nisan":30,"mayıs":31,"haziran":30,"temmuz":31,"ağustos":31,"eylül":30,"ekim":31,"kasım":30,"aralık":31}
sayisalAy:dict = {"1":"ocak","2":"şubat","3":"mart","4":"nisan","5":"mayıs","6":"haziran","7":"temmuz","8":"ağustos","9":"eylül","10":"ekim","11":"kasım","12":"aralık"}

yil:int = -1
print("Lütfen ",end='')
while not (1582 < yil < 5000):
    yil = int(input("yıl giriniz:.. "))
    if not (1582 < yil < 5000):
        print("Lütfen geçerli bir ",end='')

if yil % 400 == 0 or (yil % 100 != 0 and yil % 4 == 0):
    aylarGun.update({"şubat":29})

ay:str = "yook"
print("Lütfen ",end='')
while ay not in aylar:
    ay = input("ay giriniz:.. ").lower()
    if ay in sayisalAy:
        ay = sayisalAy[ay]
    if ay not in aylar:
        print("Lütfen geçerli bir ",end='')



gun:int = 0 # q
print("Lütfen ",end='')
while not (1 <= gun <= aylarGun[ay]):
    gun = int(input("gün giriniz:.. "))
    if not (1 <= gun <= aylarGun[ay]):
        print("Lütfen geçerli bir ",end='')

gYil:int = yil
if ay == "ocak" or ay == "şubat":
    gYil = yil - 1

ySon2:int = int(gYil % 100) # K
yIlk2:int = int(gYil / 100) # J


#   ( q  +    ⌊(13(    m      + 1))/5⌋ +   K   +    ⌊  k  /4⌋ +    ⌊  J  /4⌋ -  2    J  ) (mod 7)
H = (gun + int((13*(aylar[ay] + 1))/5) + ySon2 + int(ySon2/4) + int(yIlk2/4) - (2*yIlk2)) % 7
#time.sleep(1)

haftaGun = {0:"Cumartesi",1:"Pazar",2:"Pazartesi",3:"Salı",4:"Çarşamba",5:"Perşembe",6:"Cuma"}

print(f"Tarihinizin Günü: {haftaGun[H]}")


# from datetime import date
#
# haftaGun = {0:"Pazartesi",1:"Salı",2:"Çarşamba",3:"Perşembe",4:"Cuma",5:"Cumartesi",6:"Pazar"}
# print(f"Tarihinizin Günü: {haftaGun[date(int(input("Yıl giriniz... ")),int(input("Ay  giriniz... ")),int(input("Gün giriniz... "))).weekday()]}")
