metin = str.strip(input("bir metin giriniz:.. ").upper())
sozluk = {}
for m in metin:
    if m.isalnum():
        sozluk[m] = sozluk.get(m,0) + 1
for mm in sozluk:
    print(f" <--| {mm} Karakterinden {sozluk.get(mm)} tane içeriyor |-->")