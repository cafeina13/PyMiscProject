import string
import time

print("yazdırmak istediğiniz yazıyı giriniz:..|> ",end='')
yazi = input()
yazilacak_yazi = yazi if yazi != '' else "Rei Ayanami"

prtintables = ' ' + string.punctuation + string.digits + "qwertyuıopğüasdfghjklşizxcvbnmöç" + "QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ"
temp = 'Watashi wa '

a = 0
while a < len(yazilacak_yazi):
    for i in prtintables:
        print("\r" + temp+i, end='')
        time.sleep(1/120)
        if yazilacak_yazi[a] == i:
            temp += i
            break
    a += 1
print("\n")
print(temp)