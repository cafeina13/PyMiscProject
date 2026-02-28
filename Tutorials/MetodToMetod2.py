def kisi_sec(kisi:str):
    def takim_sec(takim:str):
        return f"{kisi}, {takim} taraftarı"
    return takim_sec


m1 = kisi_sec("Umay")
m2 = kisi_sec("Kayra")

print(m1("Fenerbahçe"))
print(m2("Galatasaray"))

print(kisi_sec("Elif")("Beşiktaş"))