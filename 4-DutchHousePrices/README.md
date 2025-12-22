# Dutch House Prices Analysis 🏠

Hollanda konut piyasası üzerine kapsamlı veri analizi projesi. DataScienceToolkit kullanılarak hazırlanmıştır.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Latest-green)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Latest-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📋 İçindekiler
- [Proje Hakkında](#proje-hakkında)
- [Veri Seti](#veri-seti)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Analiz Sonuçları](#analiz-sonuçları)
- [Dosya Yapısı](#dosya-yapısı)
- [Teknolojiler](#teknolojiler)

## 🎯 Proje Hakkında

Bu proje, Hollanda'daki 5,555 ev satış kaydını analiz ederek ev fiyatlarını etkileyen faktörleri belirlemeyi amaçlamaktadır. 

### Ana Hedefler:
- Fiyat belirleyici faktörleri tespit etmek
- Şehir bazlı fiyat analizi yapmak
- Energy label'ın fiyata etkisini incelemek
- Temiz ve kullanılabilir veri seti oluşturmak

## 📊 Veri Seti

**Kaynak:** [Kaggle - Dutch House Prices Dataset](https://www.kaggle.com/datasets/bryan2k19/dutch-house-prices-dataset)

### Özellikler:
- **Kayıt Sayısı:** 5,555 ev
- **Şehir Sayısı:** 1,075
- **Zaman Aralığı:** 1500-2022 (yapım yılı)
- **Orijinal Kolonlar:** 16
- **İşlenmiş Kolonlar:** 23

### Ana Değişkenler:
- Address, City, Price
- Lot size, Living space size
- Build year, Build type
- House type, Roof
- Rooms, Toilet, Floors
- Energy label, Position, Garden

## 🚀 Kurulum

### Gereksinimler
```bash
python >= 3.7
pandas
numpy
matplotlib
seaborn
```

### Kurulum Adımları

1. **Repository'yi klonlayın**
```bash
git clone https://github.com/RustuAy/DCE.git
cd DCE
```

2. **Gerekli paketleri yükleyin**
```bash
pip install pandas numpy matplotlib seaborn
```

3. **Veri setini indirin**
- [Kaggle'dan indirin](https://www.kaggle.com/datasets/bryan2k19/dutch-house-prices-dataset)
- Veya kagglehub kullanın:
```bash
pip install kagglehub
```

## 💻 Kullanım

### Hızlı Başlangıç

```bash
python 4-DutchHousePrices_Quick.py
```

### Script İçeriği

Script otomatik olarak şu adımları gerçekleştirir:

1. **Veri Yükleme** - Kaggle veri setini okur
2. **Veri Temizleme** - Fiyat, alan, oda bilgilerini temizler
3. **Feature Engineering** - Yeni özellikler çıkarır
4. **İstatistiksel Analiz** - Temel istatistikler hesaplar
5. **Görselleştirme** - 4 adet detaylı grafik oluşturur
6. **Raporlama** - Sonuçları kaydeder

### Çıktılar

Script çalıştıktan sonra şu dosyalar oluşturulur:

```
reports/
├── 1_price_analysis.png            # Fiyat analizi görselleri
├── 2_correlation_matrix.png        # Korelasyon matrisi
├── 3_energy_label_analysis.png     # Energy label analizi
├── 4_build_year_analysis.png       # Yapım yılı analizi
├── DUTCH_HOUSE_PRICES_REPORT.md    # Detaylı analiz raporu
└── SUMMARY.md                       # Özet rapor

data/
└── dutch_house_prices_cleaned.csv  # Temizlenmiş veri seti
```

## 📈 Analiz Sonuçları

### 💰 Fiyat İstatistikleri
- **Ortalama Fiyat:** €558,299
- **Medyan Fiyat:** €468,500
- **Fiyat Aralığı:** €149,000 - €4,700,000

### 🏆 En Önemli Bulgular

1. **Yaşam Alanı** en güçlü fiyat belirleyicisi (korelasyon: 0.726)
2. **Yapım yılı** fiyatı etkilemiyor (korelasyon: -0.036)
3. **Energy label** yükseldikçe fiyat artıyor
4. **Şehirler arası** büyük fiyat farkları var

### 📊 Korelasyon Sıralaması
1. Yaşam Alanı: 0.726 ⭐⭐⭐
2. Toplam Oda Sayısı: 0.467 ⭐⭐
3. Arsa Alanı: 0.338 ⭐
4. Yatak Odası: 0.319 ⭐
5. Kat Sayısı: 0.008
6. Yapım Yılı: -0.036

### 🏆 En Pahalı 5 Şehir
1. Aerdenhout - €4,350,000
2. Bosch en Duin - €3,950,000
3. Epse - €2,650,000
4. Warmond - €2,005,000
5. Leimuiderbrug - €1,950,000

## 📁 Dosya Yapısı

```
DCE/
│
├── 4-DutchHousePrices_Quick.py     # Ana analiz scripti
├── 4-DutchHousePrices.py           # Detaylı analiz scripti (logging ile)
│
├── data/
│   ├── titanic.csv
│   └── dutch_house_prices_cleaned.csv  # Temizlenmiş veri
│
├── reports/
│   ├── 1_price_analysis.png
│   ├── 2_correlation_matrix.png
│   ├── 3_energy_label_analysis.png
│   ├── 4_build_year_analysis.png
│   ├── DUTCH_HOUSE_PRICES_REPORT.md
│   ├── SUMMARY.md
│   └── README.md
│
├── 1-Example.ipynb
├── 2-AirplaneCrashes.ipynb
├── 3-Titanic.ipynb
└── DA5_Titanic_Interview_Guide.md
```

## 🛠️ Teknolojiler

### Python Kütüphaneleri
- **pandas** - Veri manipülasyonu ve analizi
- **numpy** - Sayısal hesaplamalar
- **matplotlib** - Temel görselleştirme
- **seaborn** - İstatistiksel görselleştirme

### DataScienceToolkit
Proje, `C:\Users\User\DataScienceToolkit` altındaki şablonlar kullanılarak geliştirilmiştir:
- Veri temizleme template'leri
- EDA (Exploratory Data Analysis) şablonları
- Görselleştirme standartları

## 📊 Örnek Görselleştirmeler

### Fiyat Dağılımı
Script, fiyat dağılımını histogram ve box plot ile görselleştirir.

### Korelasyon Matrisi
Tüm sayısal değişkenler arasındaki ilişkileri heat map olarak gösterir.

### Energy Label Analizi
Energy label'ların dağılımını ve fiyatla ilişkisini analiz eder.

### Şehir Karşılaştırması
En pahalı 15 şehri bar chart ile gösterir.

## 🎓 Kullanım Senaryoları

### 1. Gayrimenkul Değerleme
```python
# Bir evin tahmini fiyatını hesaplama
living_space = 150  # m²
estimated_price = living_space * avg_price_per_sqm
```

### 2. Yatırım Analizi
En yüksek ROI için hangi özelliklere yatırım yapmalı?
- Yaşam alanını artırmak (en yüksek etki)
- Energy label yükseltmek
- Oda sayısını optimize etmek

### 3. Pazar Araştırması
Hangi şehirlerde fiyatlar daha uygun?

## 🔮 Gelecek Geliştirmeler

- [ ] Makine öğrenmesi modeli (fiyat tahmini)
- [ ] Coğrafi görselleştirme (harita)
- [ ] Interaktif dashboard (Streamlit/Plotly)
- [ ] Zaman serisi analizi
- [ ] Mahalle bazlı detay analiz

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen pull request göndermeden önce:

1. Fork'layın
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Push edin (`git push origin feature/AmazingFeature`)
5. Pull Request açın

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## 👨‍💻 Geliştirici

**RustuAy** - [GitHub](https://github.com/RustuAy)

## 🙏 Teşekkürler

- Kaggle - Veri seti için
- DataScienceToolkit - Template'ler için
- Python Community - Harika kütüphaneler için

## 📧 İletişim

Sorularınız için:
- GitHub Issues: [Issues sayfası](https://github.com/RustuAy/DCE/issues)
- Email: [İletişim bilgisi]

---

⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!

**Son Güncelleme:** 22 Aralık 2025
