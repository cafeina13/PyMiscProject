# class Ogrenci:
#     def __init__(self,ad="NoName",soyad="NoSurname",no=-1,dogum_yeri="NoBirthPlace"):
#         self.ad = ad
#         self.soyad = soyad
#         self.no = no
#         self.dogum_yeri = dogum_yeri
#
# ogr1 = Ogrenci("Emily", "Chester", 7, "Lincoln Park")
# ogr2 = Ogrenci("Ferah", "şebo")
#
# print(ogr1.ad)
# print(ogr2)
#
# class Kitap:
#     def __init__(self,ad,yazar,sayfa):
#         self.ad = ad
#         self.yazar = yazar
#         self.sayfa = sayfa
#
#     def uzun(self):
#         return self.sayfa >= 300
#
# kitap1 = Kitap("kamera", "fero", 350)
# kitap2 = Kitap("dokuz", "sero", 250)
#
# print(kitap1.uzun())
# print(kitap2.uzun())
#
# class Hesap:
#     def __init__(self,hesap_adi, bakiye = 0):
#         self.hesap_adi = hesap_adi
#         self.bakiye = bakiye
#
#     def para_yatir(self,miktar):
#         self.bakiye += miktar
#
#     def para_cek(self,miktar):
#         if self.bakiye < miktar:
#             print(f"yetersiz, en fazla {self.bakiye}")
#         else:
#             self.bakiye -= miktar
#             print(f"çektildi: {miktar}, yeni bakiye: {self.bakiye}")
#
# berna = Hesap("Şule", 5000)
# berna.para_yatir(250)
# berna.para_cek(6000)
# berna.para_cek(5000)
#
# class Rectangle:
#     def __init__(self,width,height=None):
#         if not height:
#             self.height = width
#         else:
#             self.height = height
#         self.width = width
#
#     def area(self):
#          return self.height * self.width
#
#     def perimeter(self):
#          return 2 * (self.height + self.width)
#
# rect = Rectangle(13,7)
# rect2 = Rectangle(13)
# print(rect.area())
# print(rect.perimeter())
#
# print(rect2.area())
# print(rect2.perimeter())
#
#
# class Student:
#     total_student = 0
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#         Student.total_student += 1
#
#     def calc_avarage(self):
#         return sum(self.grades)/len(self.grades)
#
#     def display_info(self):
#         avrg_grade = Student.calc_avarage(self)
#         return avrg_grade
#
#     @classmethod
#     def get_total_students(cls):
#         return f"Toplam ogr: {cls.total_student}"
#
# std1 = Student("Maya",[78])
# std2 = Student("Riva", [98])
#
# print(std1.display_info())
# print(std2.display_info())
#
# print(Student.get_total_students())
#
#
# class Kutuphane:
#     maksimum_kitap_sayisi = 700
#
#     def __init__(self, isim):
#         self.isim = isim
#         self.kitaplar = list()
#
#     @staticmethod
#     def gecerli_kitap(kitap_adi):
#         return isinstance(kitap_adi,str) and len(kitap_adi) > 7
#
#     def kitap_ekle(self, kitap_adi):
#         if Kutuphane.maksimum_kitap_sayisi > len(self.kitaplar):
#             if Kutuphane.gecerli_kitap(kitap_adi):
#                 self.kitaplar.append(kitap_adi)
#                 print(f'"{kitap_adi}" adlı kitap eklendi')
#             else:
#                 print(f"Kitap adı {kitap_adi} geçersiz")
#         else:
#             print("Maks kitap sayısına ulaşıldı")
#
#     @classmethod
#     def maks_sayi_degis(cls,yeni_maks):
#         cls.maksimum_kitap_sayisi = yeni_maks
#         print(f"Yeni maks {cls.maksimum_kitap_sayisi}")
#
#
#
# merkez_kutuphane = Kutuphane("Merkez Şube Kütüphanesi")
# print(f"Kütüphane Adı: {merkez_kutuphane.isim}")
# print(f"Maksimum Kapasite (Başlangıç): {Kutuphane.maksimum_kitap_sayisi}")
#
# print("\n--- Geçerli Kitap Ekleme Denemeleri ---")
#
# merkez_kutuphane.kitap_ekle("Sefiller")
# merkez_kutuphane.kitap_ekle("Suç ve Ceza")
#
# print(f"\nGüncel Kitap Listesi: {merkez_kutuphane.kitaplar}")
#
# print("\n--- Kitap Geçerlilik Kontrolleri (Statik Metot) ---")
#
# print(f"'Harry Potter' geçerli mi? {Kutuphane.gecerli_kitap('Harry Potter')}") # True
#
# print(f"'Deneme' geçerli mi? {Kutuphane.gecerli_kitap('Deneme')}") # False
#
# print(f"12345678 geçerli mi? {Kutuphane.gecerli_kitap(12345678)}") # False
#
# print("\n--- Geçersiz Kitap Ekleme Denemeleri ---")
#
# merkez_kutuphane.kitap_ekle("Kısa")
#
# merkez_kutuphane.kitap_ekle(99999999)
#
#
# print("\n--- Kapasite Değişikliği ve Sınır Testi ---")
#
# Kutuphane.maks_sayi_degis(3)
#
# print(f"Yeni Maksimum Kapasite: {Kutuphane.maksimum_kitap_sayisi}")
# print(f"Mevcut Kitap Sayısı: {len(merkez_kutuphane.kitaplar)}")
#
# merkez_kutuphane.kitap_ekle("Yüzyıllık Yalnızlık")
#
# print("\n--- Sınır Aşımı Denemesi ---")
# merkez_kutuphane.kitap_ekle("Dönüşüm")
#
#
# class Student:
#     all_students = []
#
#     @staticmethod
#     def validate_student_id(student_id):
#         if not (isinstance(student_id, str) or len(student_id) != 7 or student_id.startswith("std")):
#             return False
#         return True
#
#     def __init__(self, student_id, name):
#         if not Student.validate_student_id(student_id):
#             raise ValueError(f"Geçersiz Öğrenci ID'si: {student_id}. ID 5 haneli pozitif bir sayı olmalıdır.")
#
#         self.student_id = student_id
#         self.name = name
#
#         Student.all_students.append(self)
#
#     @classmethod
#     def add_students(cls, student_id, name):
#         try:
#             new_student = cls(student_id, name)
#             print(f"Öğrenci eklendi: ID {new_student.student_id}, İsim {new_student.name}")
#             return new_student
#         except ValueError as e:
#             print(f"Öğrenci eklenemedi: {e}")
#             return None
#
#     @classmethod
#     def list_students(cls):
#         print("\n--- 👥 Kayıtlı Öğrenciler ---")
#         if not cls.all_students:
#             print("Kayıtlı öğrenci bulunmamaktadır.")
#             return
#
#         for student in cls.all_students:
#             print(f"ID: {student.student_id} | İsim: {student.name}")
#         print("----------------------------")
#
#     @classmethod
#     def remove_student(cls, student_id):
#         initial_count = len(cls.all_students)
#
#         cls.all_students = [
#             student for student in cls.all_students
#             if student.student_id != student_id
#         ]
#
#         if len(cls.all_students) < initial_count:
#             print(f"Öğrenci ID {student_id} listeden başarıyla silindi.")
#         else:
#             print(f"Öğrenci ID {student_id} bulunamadı.")
#
#     @classmethod
#     def display_students_info(cls):
#         cls.list_students()
#
#
# # 1. Başarılı Öğrenci Ekleme
# print("--- ✅ Başarılı Ekleme ---")
# ogrenci_a = Student.add_students("std1234", "Ebru Özcan")
# ogrenci_b = Student.add_students("std3333", "Furkan Yıldız")
# ogrenci_c = Student.add_students("std7899", "Gizem Aydın")
#
#
# print("\n--- ❌ Geçersiz ID Testi ---")
# # ID 5 haneli değil (4 haneli)
# ogrenci_d = Student.add_students("4000", "Halil Erdem")
# # ID sayısal değil
# ogrenci_e = Student.add_students("5000E44", "İrem Kaya")
# # ID negatif veya sıfır
# ogrenci_f = Student.add_students("std2343", "Jale Aktaş")
#
#
# print("\n--- Tüm Öğrenciler (Listeleme) ---")
# Student.list_students()
#
#
# print("\n--- Öğrenci Silme Testi ---")
#
# # 1. Var olan bir öğrenciyi silme
# Student.remove_student("std7899")
# # 2. Silme işleminden sonra listeyi kontrol etme
# Student.list_students()
# # 3. Listede olmayan bir öğrenciyi silme denemesi
# Student.remove_student(99999)
#
#
# print("\n--- 💡 ID Geçerlilik Kontrolü ---")
# print(f"ID std0002 geçerli mi? {Student.validate_student_id("std0002")}") # True
# print(f"ID 123456 (6 haneli) geçerli mi? {Student.validate_student_id("123456")}") # False
# print(f"ID 'abcde' (String) geçerli mi? {Student.validate_student_id('abcde')}") # False
#
#

class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def display(self):
        print(f"İsmi: {self.name}, Rengi: {self.color}")

class Rectangle(Shape):
    def __init__(self, name, color, width, height):
        super().__init__(name,color)
        self.width = width
        self.height = height


    def area(self):
        return self.height * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)

class Circle(Shape):
    pi = 3.14
    def __init__(self, name, color,radius):
        super().__init__(color,name)
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2

    def perimeter(self):
        return 2 * Circle.pi * self.radius

r1 = Rectangle("Dikdörtgen","Kırmızı", 7, 11)
r1.display()
print(f"{r1.name} alanı: {r1.area()}, çevresi: {r1.perimeter()}")

c1 = Circle("Daire","Yeşil", 13)
c1.display()
print(f"{c1.name} alanı: {c1.area()}, çevresi: {c1.perimeter()}")


class employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary


