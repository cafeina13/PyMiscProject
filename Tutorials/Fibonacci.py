import time

# # İlk 100 fibonacci
#
# baslangıc = time.time()
# fibonacciList = [1, 1]  # değerleri saklamak için liste oluşturuluyor
#                         # buralar kodda hata vermemesi il 2 eleman için manuel ekleniyor
# sayac = 2 # eklenen sayısını saklanıyor ve önceden 2 değer eklendiği için 2'den başlanıyor
# while len(fibonacciList) < 100: # 100 sayı istendiği için listenin uzunluğu 100'e oluncaya kadar döngü tekrar eder
#     fibonacciList.append(fibonacciList[-1] + fibonacciList[-2]) # fibonacci kuralı uygulanır
#
# print(fibonacciList, f"\n{round(time.time() - baslangıc,10)} ")      # sayı listelenir
# print(len(fibonacciList)) # uzunluk kontrol edilir

def fibonacci(eleman_sayisi:int):
    if eleman_sayisi == 0:
        return [0]
    elif eleman_sayisi == 1:
        return [1]
    fibonacciList = [1, 1]  # değerleri saklamak için liste oluşturuluyor
                            # buralar kodda hata vermemesi il 2 eleman için manuel ekleniyor
    sayac = 2 # eklenen sayısını saklanıyor ve önceden 2 değer eklendiği için 2'den başlanıyor
    while len(fibonacciList) < eleman_sayisi: # 100 sayı istendiği için listenin uzunluğu 100'e oluncaya kadar döngü tekrar eder
        fibonacciList.append(fibonacciList[-1] + fibonacciList[-2]) # fibonacci kuralı uygulanır
    return fibonacciList

print(fibonacci(10))

def fibonacci_2(n:int,liste:list = None):
    if liste == None:
        liste = [1,1]
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n == 2:
        return liste
    elif n > 2:
        liste.append(liste[-1]+liste[-2])
        return fibonacci_2(n-1,liste)

print(fibonacci_2(10))
#ilk 100 basamaklı fibonacciyi yazdır -----------------------------------------------------------------------
# fib_List = [0,1,1] #işlem yapmayı sağlamak için liste oluşturup gerekli ilk değerler girilir
#
# sayac = 4
# while len(str(fib_List[2])) < 100:      # fibonacci listesinde bulunan [2]./3. eleman 100 basamaktan küçükken
#                                                 # önce yeni gelecek eleman için elemanlar bir geriye sırayla
#     fib_List[0] = fib_List[1]                   # 0. elemanla işimiz yok onun yerine 1. eleman atanıyor
#     fib_List[1] = fib_List[2]                   # 1. elemanı kaydettik, onun yerini 2. elemana verebiliriz
#                                                 # 2. elemanı kaydettikten sonra yeni 2. elemanı onun yerine alıcaz
#     fib_List[2] = fib_List[0] + fib_List[1]     # fibonacci kuralını uyguluyoruz [n] + [n + 1] = [n + 2]
#     sayac += 1                                  #                                [0.] + [  1.  ] = [  2.  ]
# print(f"{sayac}. sayı  | ",end='')           # Şekil Şukuli olmadan daha iyi olur ama bu seferlik görüntüye feda oldu
# print(fib_List[2],end=" |\n") # şart sağlanınca(uyuşmayınca) listenin son halini yazdırıyoruz

#ilk 100 basamaklı fibonacciyi yazdır -----------------------------------------------------------------------
# a, b = 1, 1 #işlem yapmayı sağlamak için değişkenler oluşturup gerekli ilk değerler girilir
# sayac = 2   #kaçıncı eleman bulmak için sayaç kullanılır
# while len(str(b)) < 100:      # b değişkeni 100 basamaktan küçükken
#     a, b = b, a + b           # değişken kaydırma
#     sayac += 1
# print(f"100 basamaklı ilk fibanacci sayısı dizinin {sayac}. elemanı\n{b}\nOndan bir önceki sayı\n{a}")