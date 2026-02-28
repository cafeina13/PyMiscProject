# *************** *** map *** ***************
# ----------------------------------------------
# isimler = ["AhMeT","aYşE","oNur", "HUSeyiN"]
#
# fixed_list = list(map(str.capitalize,isimler))
#
# print(fixed_list)
#
# ----------------------------------------------
# *************** *** filter *** ***************
# ----------------------------------------------
# liste = [1,2,3,5,6,8,11, 17, 123, 101]
#
# # def tek_mi(x):
# #     return x % 2 == 1
# # filtered = list(filter(tek_mi, liste))
#
# # filtered = list(filter(lambda x: x % 2 == 0,liste))
# # filtered = list(filter(lambda x:9 < x < 100, liste))
#
# print(filtered)
#
kelimeler = ["ayna","ahmet","ana","kalem","defter","kazak","son"]
#
# a_baslayan = list(filter(lambda x: x[0] == 'a',kelimeler))
# a_baslayan = list(filter(lambda kelime: kelime.startswith('a') ,kelimeler)) # Daha tercih edilebilir kullanım
# print(a_baslayan)
#
# a_gecen = list(filter(lambda kelime: kelime.__contains__('a') ,kelimeler))
# a_gecen = list(filter(lambda kelime: 'a' in kelime ,kelimeler)) # Daha tercih edilebilir kullanım
# print(a_gecen)
#
# palndrom = list(filter(lambda kelime: ''.join(reversed(kelime)) == kelime , kelimeler))
# palndrom = list(filter(lambda kelime: kelime[::-1] == kelime , kelimeler)) # bu daha tercih ediilir
#
# print(palndrom)

# liste = [1,2, (1,2,3),True,"string","ornek", {1,2,4}]
#
# stringler = list(filter(lambda x: type(x) == type(""),liste))
# stringler = list(filter(lambda x: isinstance(x,str), liste)) # tercih bu
# boollar = list(filter(lambda x: isinstance(x,bool), liste))
#
# print(boollar)

# kisiler = [{"Ad":"Ahmet","Yas":35}, {"Ad":"Banu","Yas":22}, {"Ad":"Can", "Yas": 18}, {"Ad": "Anıl", "Yas": 28}]
#
# a_ile_baslayan = list(filter(lambda x: x["Ad"].startswith('A'),kisiler))
# buyuk_20 = list(filter(lambda kisi: kisi["Yas"] > 20,kisiler))
#
# print(a_ile_baslayan)
# print(buyuk_20)
