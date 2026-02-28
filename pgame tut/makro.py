import pyautogui
import keyboard
import time

# --- AYARLAR ---
AC_KAPAT_TUSU = 'f6'  # Burayı 'p', 'f10' veya 'caps lock' gibi değiştirebilirsin
BEKLEME_SURESI = 32    # Tıklamalar arası saniye
# ----------------

aktif = False
son_tiklama_zamani = 0

print("--- OTOMATİK TIKLAYICI ---")
print("Durum: KAPALI")
print(f"Açmak veya Kapatmak için '{AC_KAPAT_TUSU.upper()}' tuşuna bas.")
print("Tamamen çıkmak için 'ESC' tuşuna bas.")

def tikla_ve_islem_yap():
    """Shift + 2x Sağ Tık işlemini gerçekleştirir."""
    pyautogui.keyDown('shift')
    pyautogui.click(button='right', clicks=3, interval=0.3)
    pyautogui.keyUp('shift')
    print(f"[{time.strftime('%H:%M:%S')}] İşlem yapıldı.")

try:
    while True:
        # Açma/Kapatma tuşuna basıldı mı kontrol et
        if keyboard.is_pressed(AC_KAPAT_TUSU):
            aktif = not aktif  # Durumu tersine çevir (True ise False yap)
            durum_metni = "AKTİF" if aktif else "KAPALI"
            print(f"Program Durumu: {durum_metni}")
            time.sleep(1)  # Tuşa basıldığında birden fazla algılamasın diye kısa bekleme

        # Eğer program aktifse ve süresi geldiyse tıkla
        if aktif:
            su_an = time.time()
            if su_an - son_tiklama_zamani >= BEKLEME_SURESI:
                tikla_ve_islem_yap()
                son_tiklama_zamani = su_an
        
        # Tamamen çıkış için ESC kontrolü
        if keyboard.is_pressed('esc'):
            print("Programdan çıkılıyor...")
            break

        # İşlemciyi yormamak için çok kısa bir bekleme
        time.sleep(0.08)

except Exception as e:
    print(f"Bir hata oluştu: {e}")
finally:
    pyautogui.keyUp('shift') # Güvenlik için shift'i bırak