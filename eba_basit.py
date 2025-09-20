from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
import pandas as pd
import time

# Ayarlar
EXCEL_PATH = 'liste.xlsx'
OUTPUT_PATH = 'liste_eba_sifre.xlsx'

def main():
    # Excel dosyasını oku
    try:
        # Önce sheet adlarını kontrol et
        xl = pd.ExcelFile('liste.xlsx')
        print(f"📋 Bulunan sheet adları: {xl.sheet_names}")
        
        # İlk sheet'i kullan
        sheet_name = xl.sheet_names[0]
        print(f"📊 Kullanılacak sheet: '{sheet_name}'")
        
        df = pd.read_excel('liste.xlsx', sheet_name=sheet_name, header=0)
        print(f"✅ Excel dosyası okundu")
        print(f"📊 Sütunlar: {list(df.columns)}")
        print(f"📈 Toplam öğrenci: {len(df)}")
        
        # Şifre sütunu yoksa ekle
        if 'Şifre' not in df.columns:
            df['Şifre'] = ''
            print("➕ 'Şifre' sütunu eklendi")
            
    except Exception as e:
        print(f"❌ Excel dosyası okuma hatası: {e}")
        return
    
    # Firefox tarayıcısını başlat
    print("🌐 Tarayıcı başlatılıyor...")
    service = Service('geckodriver.exe')
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    
    try:
        # EBA öğretmen şifre sayfasına git
        print("🔗 EBA öğretmen şifre sayfasına gidiliyor...")
        driver.get('https://eba.gov.tr/ogretmensifre')
        
        print("\n⚠️  ÖNEMLİ:")
        print("1. Lütfen EBA'ya öğretmen hesabınızla giriş yapın")
        print("2. Öğretmen şifre sayfasına gidin")
        print("3. Hazır olduğunuzda Enter'a basın")
        input("\nHazır olduğunuzda Enter'a basın...")
        
        for idx, row in df.iterrows():
            tc_no = str(row.iloc[0]).strip()
            name = str(row.iloc[1]).strip()
            surname = str(row.iloc[2]).strip()
            
            if not tc_no or tc_no == 'nan':
                continue
                
            print(f"\n📋 {idx + 1}. Öğrenci: {name} {surname} (TC: {tc_no})")
            
            try:
                # TC alanını bul ve temizle (HTML'den gelen doğru seçici)
                tc_input = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='studentTckn']"))
                )
                tc_input.clear()
                tc_input.send_keys(tc_no)
                print("✅ TC numarası girildi")
                
                # Öğrenci bilgilerini getir butonuna tıkla
                get_btn = driver.find_element(By.CSS_SELECTOR, "button.btn.standart-btn")
                get_btn.click()
                print("✅ Öğrenci bilgileri getirildi")
                
                # Kısa bekleme - sayfa yüklenmesi için
                time.sleep(2)
                
                # Tek kullanımlık şifre oluştur butonunu bul ve tıkla
                create_password_btn = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Tek Kullanımlık Giriş Şifresi Oluştur')]"))
                )
                create_password_btn.click()
                print("✅ Tek kullanımlık şifre oluştur butonuna tıklandı")
                
                # Şifrenin oluşmasını bekle ve al
                password_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "code#user-pass"))
                )
                password = password_element.text
                print(f"🔑 Şifre alındı: {password}")
                
                # Şifreyi DataFrame'e kaydet
                df.loc[idx, 'Şifre'] = password
                
                # Yeni işlem butonuna tıkla (bir sonraki öğrenci için)
                if idx < len(df) - 1:  # Son öğrenci değilse
                    new_process_btn = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-info")
                    new_process_btn.click()
                    print("✅ Yeni işlem butonuna tıklandı")
                    time.sleep(1)
                
                time.sleep(2)  # Kısa bekleme
                
            except Exception as e:
                print(f"❌ Hata: {e}")
                continue
                
            time.sleep(1)  # Sonraki öğrenci için kısa bekleme
        
        # Dosyayı kaydet
        df.to_excel(OUTPUT_PATH, sheet_name=sheet_name, index=False)
        print(f"\n🎉 Tamamlandı! Dosya kaydedildi: {OUTPUT_PATH}")
        
    finally:
        input("\nİşlem tamamlandı. Tarayıcıyı kapatmak için Enter'a basın...")
        driver.quit()

if __name__ == "__main__":
    main()