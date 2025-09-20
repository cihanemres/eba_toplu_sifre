# 🔐 EBA Öğrenci Şifre Otomasyonu

EBA (Eğitim Bilişim Ağı) platformunda öğrenciler için tek kullanımlık şifreler oluşturan otomatik Python scripti.

## 📋 Özellikler

- ✅ Excel dosyasından öğrenci TC numaralarını okuma
- ✅ EBA öğretmen paneline otomatik giriş
- ✅ Tek kullanımlık şifre oluşturma
- ✅ Şifreleri Excel dosyasına kaydetme
- ✅ Dinamik sheet adı desteği
- ✅ Hata yönetimi ve detaylı konsol çıktıları

## 🚀 Kurulum

### Gereksinimler

1. **Python 3.8+**
2. **Firefox Tarayıcısı**
3. **geckodriver.exe** (proje klasöründe mevcut)

### Kütüphane Kurulumu

```bash
pip install -r requirements.txt
```

### Manuel Kurulum

```bash
pip install selenium pandas openpyxl
```

## 📁 Dosya Yapısı

```
eba/
├── eba_basit.py              # Ana script (basit versiyon)
├── requirements.txt          # Gerekli kütüphaneler
├── geckodriver.exe          # Firefox WebDriver
├── liste.xlsx               # Giriş Excel dosyası
├── liste_eba_sifre.xlsx     # Çıkış Excel dosyası (otomatik oluşur)
└── README.md               # Bu dosya
```

## 📊 Excel Dosya Formatı

### Giriş Dosyası (`liste.xlsx`)
| TC Kimlik No | Ad | Soyad |
|-------------|----|----|
| 12345678901 | Ahmet | YILMAZ |
| 98765432109 | Ayşe | KAYA |

### Çıkış Dosyası (`liste_eba_sifre.xlsx`)
| TC Kimlik No | Ad | Soyad | Şifre |
|-------------|----|----|-------|
| 12345678901 | Ahmet | YILMAZ | A1B2C3 |
| 98765432109 | Ayşe | KAYA | X9Y8Z7 |

## 🎯 Kullanım

### 1. Basit Versiyon (Önerilen)

```bash
python eba_basit.py
```

### 2. Tam Özellikli Versiyon

```bash
python "from selenium import webdriver.py"
```

## 📝 Kullanım Adımları

1. **Excel Hazırlığı**: `liste.xlsx` dosyasını TC, Ad, Soyad sütunları ile hazırlayın
2. **Script Çalıştırma**: Yukarıdaki komutlardan birini çalıştırın
3. **EBA Girişi**: Açılan tarayıcıda EBA öğretmen hesabınızla giriş yapın
4. **Otomatik İşlem**: Script otomatik olarak:
   - Her öğrenci için TC numarasını girer
   - Öğrenci bilgilerini getirir
   - Tek kullanımlık şifre oluşturur
   - Şifreyi Excel'e kaydeder
5. **Sonuç**: `liste_eba_sifre.xlsx` dosyası oluşturulur

## ⚠️ Önemli Notlar

- **EBA Girişi**: Script çalıştıktan sonra manuel olarak EBA'ya giriş yapmanız gerekir
- **İnternet Bağlantısı**: Stabil internet bağlantısı gereklidir
- **Tarayıcı**: Firefox tarayıcısı kullanılır
- **Hız**: Her öğrenci için yaklaşık 5-10 saniye sürer

## 🔧 Sorun Giderme

### Yaygın Hatalar

1. **geckodriver.exe bulunamadı**
   - `geckodriver.exe` dosyasının proje klasöründe olduğundan emin olun

2. **Excel dosyası bulunamadı**
   - `liste.xlsx` dosyasının proje klasöründe olduğundan emin olun

3. **Element bulunamadı**
   - EBA sayfasının tamamen yüklendiğinden emin olun
   - İnternet bağlantınızı kontrol edin

4. **InvalidSessionIdException**
   - Tarayıcıyı kapatıp scripti yeniden çalıştırın

## 🛠️ Geliştirme

### Kod Yapısı

- **Excel İşlemleri**: pandas ile Excel okuma/yazma
- **Web Otomasyonu**: Selenium WebDriver ile Firefox kontrolü
- **Hata Yönetimi**: try-except blokları ile güvenli çalışma
- **Dinamik Selektörler**: CSS ve XPath selektörleri

### Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Commit yapın (`git commit -am 'Yeni özellik eklendi'`)
4. Push yapın (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje eğitim amaçlı geliştirilmiştir. Kullanım sorumluluğu kullanıcıya aittir.

## 📞 İletişim

Sorularınız için GitHub Issues kullanabilirsiniz.

---

**⚡ Hızlı Başlangıç:**
```bash
git clone <repo-url>
cd eba
pip install -r requirements.txt
python eba_basit.py
```

🎉 **Başarılı kullanımlar!**


### programı python olarak kullanamayacaklar için exe dosyası linki: https://drive.google.com/file/d/1u6RWVcSB6u7Ao5tsIN9EyL_5Qs6Zs071/view?usp=sharing
virüs var olarak algılayacaktır program kendi üretimim
