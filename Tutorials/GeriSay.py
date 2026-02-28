import time
baslangicZamani = time.time()
tab = '\t'
print()
for i in range(5):
    print(f"\r{tab*100}\rİşlem ilerlemesi: {i*20}% tamamlandı... |{i * '_'}{ (7-i) * ' '}|",end='')

    if i == 3:
        time.sleep(2)
    if i == 4:
        time.sleep(5)
    time.sleep(1)

print(f"\r{tab*100}\rİşlem ilerlemesi: 90% tamamlandı... |_____  |",end='')
time.sleep(6)

print(f"\r{tab*100}\rİşlem ilerlemesi: 95% tamamlandı... |______ |",end='')
time.sleep(8)
print(f"\rİşlem ilerlemesi: İşlem tamamlandı! |_______|\n{int(time.time() - baslangicZamani)} saniye sürdü")