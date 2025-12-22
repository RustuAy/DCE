# Dutch House Prices Dataset - Proje Özeti

## 🎯 Proje Hedefi
Hollanda'daki ev fiyatlarını etkileyen faktörleri analiz etmek ve veri bilimi teknikleriyle içgörüler elde etmek.

## 📊 Kullanılan Veri Seti
- **Kaynak:** Kaggle - Dutch House Prices Dataset
- **Konum:** `C:\Users\User\.cache\kagglehub\datasets\bryan2k19\dutch-house-prices-dataset\versions\1\raw_data.csv`
- **Boyut:** 5,555 ev x 16 özellik

## 🛠️ Kullanılan Toolkit
**DataScienceToolkit** - `C:\Users\User\DataScienceToolkit`
- Veri temizleme template'leri
- EDA (Exploratory Data Analysis) şablonları
- Görselleştirme araçları

## 📈 Yapılan Analizler

### 1. Veri Temizleme
✅ Fiyat kolonu temizlendi (€ sembolü kaldırıldı, sayısal formata çevrildi)  
✅ Alan kolonları temizlendi (m² sembolü kaldırıldı)  
✅ Oda sayısı ve kat bilgisi metinden çıkarıldı  
✅ Eksik değerler dolduruldu (median/mode stratejisi)  
✅ Duplicate kayıtlar kaldırıldı  

### 2. Feature Engineering
Yeni kolonlar oluşturuldu:
- `Price_Clean` - Temizlenmiş fiyat değeri
- `Lot_Size` - Arsa alanı (m²)
- `Living_Space` - Yaşam alanı (m²)
- `Build_Year` - Yapım yılı
- `Total_Rooms` - Toplam oda sayısı
- `Bedrooms` - Yatak odası sayısı
- `Number_of_Floors` - Kat sayısı

### 3. İstatistiksel Analiz
✅ Temel istatistikler (ortalama, medyan, std, min, max)  
✅ Şehir bazlı analiz  
✅ Energy label analizi  
✅ Korelasyon analizi  
✅ Eksik değer analizi  

### 4. Görselleştirme
4 adet kapsamlı görsel oluşturuldu:
1. **Fiyat Analizi** - Histogram, box plot, şehir karşılaştırması
2. **Korelasyon Matrisi** - Değişkenler arası ilişkiler
3. **Energy Label Analizi** - Enerji etiketi dağılımı ve fiyat ilişkisi
4. **Yapım Yılı Analizi** - Yıl dağılımı ve fiyat ilişkisi

## 🔑 Ana Bulgular

### Fiyat Karakteristikleri
- **Ortalama:** €558,299
- **Medyan:** €468,500
- **Aralık:** €149,000 - €4,700,000

### En Önemli Fiyat Belirleyicileri
1. 🏠 **Yaşam Alanı** (r=0.726) - En güçlü korelasyon
2. 🚪 **Toplam Oda Sayısı** (r=0.467) - Orta güçlü ilişki
3. 📐 **Arsa Alanı** (r=0.338) - Zayıf ilişki
4. 🛏️ **Yatak Odası** (r=0.319) - Zayıf ilişki

### Şaşırtıcı Bulgular
❗ **Yapım yılı** fiyatı neredeyse etkilemiyor (r=-0.036)  
❗ **Kat sayısı** önemsiz (r=0.008)  
✅ **Energy label** yüksek = daha pahalı evler  

## 📁 Çıktı Dosyaları

```
DCE/
├── 4-DutchHousePrices_Quick.py         # Ana analiz scripti
├── data/
│   └── dutch_house_prices_cleaned.csv  # Temizlenmiş veri (5,555x23)
└── reports/
    ├── 1_price_analysis.png            # Fiyat görselleştirmeleri
    ├── 2_correlation_matrix.png        # Korelasyon matrisi
    ├── 3_energy_label_analysis.png     # Energy label analizi
    ├── 4_build_year_analysis.png       # Yapım yılı analizi
    ├── DUTCH_HOUSE_PRICES_REPORT.md    # Detaylı rapor
    └── SUMMARY.md                       # Bu dosya
```

## 🎓 Öğrenilen Teknikler

### Python Kütüphaneleri
- `pandas` - Veri manipülasyonu
- `numpy` - Sayısal hesaplamalar
- `matplotlib` - Görselleştirme
- `seaborn` - İstatistiksel görselleştirme

### Veri Bilimi Teknikleri
- Veri temizleme ve preprocessing
- Feature engineering
- Exploratory Data Analysis (EDA)
- Korelasyon analizi
- İstatistiksel görselleştirme
- Aykırı değer (outlier) tespiti

### DataScienceToolkit Kullanımı
- Template-based analiz
- Standardize edilmiş veri temizleme
- Profesyonel raporlama

## 💡 İş Değeri

### Potansiyel Kullanım Alanları
1. **Gayrimenkul Değerleme** - Ev fiyatı tahmin modelleri için temel
2. **Yatırım Analizi** - Hangi faktörlere yatırım yapmalı?
3. **Pazar Segmentasyonu** - Farklı şehir profilleri
4. **Enerji Politikaları** - Energy label'ın ekonomik etkisi

### Sonraki Adımlar
- 🔮 Makine öğrenmesi modeli geliştirme (fiyat tahmini)
- 🗺️ Coğrafi analiz (harita görselleştirmesi)
- 📊 Dashboard oluşturma (Streamlit/Plotly)
- 🔄 Zaman serisi analizi (fiyat trendleri)

## ⏱️ Proje Süresi
**Toplam:** ~10 dakika
- Veri yükleme ve temizleme: 2 dk
- Feature engineering: 1 dk
- Analiz: 2 dk
- Görselleştirme: 3 dk
- Raporlama: 2 dk

## ✅ Başarı Metrikleri
- ✅ 5,555 ev kaydı temizlendi
- ✅ 7 yeni feature oluşturuldu
- ✅ 4 görselleştirme üretildi
- ✅ 2 detaylı rapor hazırlandı
- ✅ %100 tekrarlanabilir kod

## 🎯 Sonuç
DataScienceToolkit kullanılarak Hollanda konut piyasası başarıyla analiz edildi. 
En önemli bulgu: **Yaşam alanı fiyatın en güçlü belirleyicisidir** (r=0.726).

---

**Proje Tarihi:** 22 Aralık 2025  
**Analiz Yapan:** GitHub Copilot  
**Toolkit:** DataScienceToolkit
