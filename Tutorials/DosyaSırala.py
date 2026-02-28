import os

os.chdir("C:/Users/ZERO/Downloads")
#mkdir("*!*/OLUŞTURULACAK!klasör") #                                              #
#makedirs("istenilen/kadar/yol/girilebilir") #her girilen oluşturulacak           #
#rmdir("*!*/İçiBoşSilinecekDosya") #*!*gerekiyorsa Silinmedem önceside olur       #
# #removedirs("istenilen/kadar/yol/girilebilir") #her girilen Silinecek           #
# os.mkdir("Deneme123") #içinde bulunan yere deneme123 klasörü oluşur             #
# os.makedirs("Deneme123/asdfasddas/vcxzxcv/hasır") #dizine uygun klasörler oluşur#
# os.rmdir("Deneme123/asdfasddas/vcxzxcv/hasır")#sadece 'hasır' silinecek!boşsa   #
# os.removedirs("Deneme123/asdfasddas/vcxzxcv") #hepsinin içi boşsa hepsi silinir #
#                                                                                 #
#remove #her türlü dosyayı siler, klasör silemez                                  #
# os.mkdir("silinecek") #silinecek adında klasör oluşur                           #
# for i in os.listdir("silinecek"):#silinecek adlı klasördeki tüm dosyaları gezer #
#    os.remove("silinecek/" + i)  #gezdikçe siler                                 #
# os.remove("silinecek") #silinecek adlı klasör silinir                           #
#---------------------------------------------------------------------------------#
# # os.rename("silinecek","silindi") #dosya adı değiştirme                        #
# os.mkdir("Taşınacak")                                                           #
# os.rename("Taşınacak","Sağlam klasör/Taşındı") #ad değiştirme ile taşıma        #
#---------------------------------------------------------------------------------#
# stats # dosya detayları !datetime.timestamp ! zaman ile ilgili veriiler için    #
# os.walk("Path") # ağaç şeklinde verilen pathdeki herşeyi sıralar                #
#---------------------------------------------------------------------------------#
# os.path.join("bir","iki","üç","dört") # içine aldığı stringleri / ile brleştirir#
#---------------------------------------------------------------------------------#
# os.path.isdir / os.path.isfile # verilen adrestekinin tipine göre bool döndürür #
# os.path.splitext # verilen adresteki uçtakinin yolunu ve uzantısını ayrırır     #
#---------------------------------------------------------------------------------#
"---------------------------------------------------------------------------------"
#---------------------------------------------------------------------------------#
#---------Proje: İçinde farklı dosyalar bulunan bir klasördeki dosyaları----------#
#-------------------------uzantısına göre klasörlere ayır-------------------------#

liste = list()

for i in os.listdir():
    if os.path.isdir(i):
        dirKlasor = "Klasorler"
        if not os.path.exists(dirKlasor):
            os.mkdir(dirKlasor)
        os.rename(i, os.path.join(dirKlasor,i))
    elif os.path.isfile(i):
        klasor = os.path.splitext(i)[1].replace(".","")
        if klasor == '':
            liste.append(i)
            continue
        if not os.path.exists(klasor):
            os.mkdir(f"{klasor}")
        os.rename(i,os.path.join(klasor,i))

if len(liste) != 0:
        print(liste,sep=' - ')
        print("Uzantısız dosyalar")



































