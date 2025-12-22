# Dutch House Prices Dataset - Analiz Raporu

**Tarih:** 22 Aralık 2025  
**Veri Kaynağı:** Kaggle - Dutch House Prices Dataset  
**Analiz Aracı:** DataScienceToolkit

---

## 📊 Veri Seti Özeti

- **Toplam Ev Sayısı:** 5,555
- **Toplam Şehir Sayısı:** 1,075
- **Veri Boyutu:** 5555 satır x 23 kolon (işlendikten sonra)
- **Zaman Aralığı:** 1500 - 2022 (yapım yılı)

---

## 💰 Fiyat İstatistikleri

| Metrik | Değer |
|--------|-------|
| Ortalama Fiyat | €558,299 |
| Medyan Fiyat | €468,500 |
| Minimum Fiyat | €149,000 |
| Maksimum Fiyat | €4,700,000 |
| Standart Sapma | €353,695 |

**Analiz:**
- Fiyat dağılımı sağa çarpık (ortalama > medyan)
- Yüksek standart sapma, fiyatlarda büyük varyasyon olduğunu gösteriyor
- Lüks evler ortalamayı yukarı çekiyor

---

## 🏠 Ev Özellikleri İstatistikleri

### Yaşam Alanı
- Ortalama: **146.4 m²**
- Medyan: **130.0 m²**
- Min: **53.0 m²**
- Max: **844.0 m²**

### Arsa Alanı
- Ortalama: **746.6 m²**
- Medyan: **235.0 m²**

### Oda Bilgileri
- Ortalama Toplam Oda: **5.4**
- Ortalama Yatak Odası: **3.8**
- Ortalama Kat Sayısı: **2.6**

### Yapım Yılı
- Ortalama: **1969**
- En Eski: **1500**
- En Yeni: **2022**

---

## 🏆 En Pahalı 10 Şehir

| Sıra | Şehir | Ev Sayısı | Ortalama Fiyat | Medyan Fiyat | Ort. Alan (m²) |
|------|-------|-----------|----------------|--------------|----------------|
| 1 | Aerdenhout | 1 | €4,350,000 | €4,350,000 | 417 |
| 2 | Bosch en Duin | 1 | €3,950,000 | €3,950,000 | 844 |
| 3 | Epse | 1 | €2,650,000 | €2,650,000 | 638 |
| 4 | Warmond | 3 | €2,005,000 | €2,495,000 | 249 |
| 5 | Leimuiderbrug | 1 | €1,950,000 | €1,950,000 | 358 |
| 6 | Bloemendaal | 6 | €1,913,333 | €1,097,500 | 235 |
| 7 | Schoorl | 6 | €1,856,667 | €1,922,500 | 241 |
| 8 | Riethoven | 1 | €1,795,000 | €1,795,000 | 612 |
| 9 | Schijf | 1 | €1,750,000 | €1,750,000 | 605 |
| 10 | Bentveld | 2 | €1,747,500 | €1,747,500 | 229 |

---

## ⚡ Energy Label Analizi

| Energy Label | Ev Sayısı | Ortalama Fiyat | Medyan Fiyat |
|--------------|-----------|----------------|--------------|
| A++++ | 3 | €1,580,000 | €1,450,000 |
| Niet verplicht | 57 | €966,412 | €800,000 |
| A+++ | 18 | €948,278 | €687,250 |
| A++ | 22 | €763,818 | €675,000 |
| A+ | 86 | €642,413 | €550,000 |
| A | 1,252 | €611,584 | €500,000 |
| B | 925 | €567,864 | €475,000 |
| D | 642 | €529,949 | €448,500 |
| C | 1,543 | €522,497 | €429,000 |
| E | 413 | €521,701 | €450,000 |
| F | 297 | €515,938 | €445,000 |
| G | 284 | €489,565 | €412,500 |

**Önemli Bulgular:**
- En yüksek enerji etiketine sahip evler (A++++) en pahalı
- "Niet verplicht" (zorunlu değil) kategorisi ikinci en pahalı - bunlar genellikle tarihi veya özel binalar
- A ve B etiketli evler en yaygın (toplam 2,177 ev)
- G etiketi en düşük ortalama fiyata sahip

---

## 📈 Korelasyon Analizi

### Fiyat ile İlişkili Faktörler

| Değişken | Korelasyon | İlişki Gücü |
|----------|------------|-------------|
| Yaşam Alanı | **0.726** | Güçlü Pozitif ✅ |
| Toplam Oda Sayısı | **0.467** | Orta Pozitif ✅ |
| Arsa Alanı | **0.338** | Zayıf Pozitif ✅ |
| Yatak Odası | **0.319** | Zayıf Pozitif ✅ |
| Kat Sayısı | **0.008** | Çok Zayıf |
| Yapım Yılı | **-0.036** | Çok Zayıf Negatif |

**Önemli Çıkarımlar:**

1. **Yaşam Alanı** en güçlü belirleyici faktör (r=0.726)
   - Her 10m² artış yaklaşık €38,000 fiyat artışı
   
2. **Toplam Oda Sayısı** ikinci önemli faktör (r=0.467)
   - Daha fazla oda = daha yüksek fiyat
   
3. **Yapım Yılı** fiyatla neredeyse ilişkisiz (r=-0.036)
   - Yeni evler mutlaka pahalı değil
   - Lokasyon ve kalite daha önemli

4. **Kat Sayısı** beklenmedik şekilde önemsiz (r=0.008)
   - Hollanda'da yatay alan dikey alandan daha değerli

---

## 🔍 Eksik Değer Analizi

| Kolon | Eksik Değer | Eksik % |
|-------|-------------|---------|
| Position | 304 | 5.47% |
| Estimated neighbourhood price per m2 | 169 | 3.04% |
| Build Year | 104 | 1.87% |
| Garden | 58 | 1.04% |
| Price | 13 | 0.23% |
| Bedrooms | 8 | 0.14% |

**Temizleme Stratejisi:**
- %5'ten az eksik değer içeren kolonlar korundu
- Sayısal değerler median ile dolduruldu
- Kategorik değerler mode ile dolduruldu

---

## 📊 Oluşturulan Görselleştirmeler

### 1. Fiyat Analizi (`1_price_analysis.png`)
- Fiyat dağılımı histogramı
- Fiyat box plot (aykırı değerler)
- En pahalı 15 şehir
- Yaşam alanı vs fiyat scatter plot

### 2. Korelasyon Matrisi (`2_correlation_matrix.png`)
- Tüm sayısal değişkenler arası ilişkiler
- Heat map formatında
- Güçlü korelasyonlar vurgulanmış

### 3. Energy Label Analizi (`3_energy_label_analysis.png`)
- Energy label dağılımı
- Energy label vs ortalama fiyat

### 4. Yapım Yılı Analizi (`4_build_year_analysis.png`)
- Yapım yılı dağılımı
- Yapım yılı vs fiyat ilişkisi

---

## 💡 Önemli Çıkarımlar

### 1. Fiyat Belirleyicileri
- **Yaşam alanı** en önemli faktör (%72.6 varyans açıklama)
- **Lokasyon** (şehir) kritik öneme sahip
- **Energy label** fiyatı etkiliyor ama çok güçlü değil

### 2. Pazar Karakteristikleri
- Hollanda konut piyasası oldukça heterojen (1,075 farklı şehir)
- Fiyat aralığı çok geniş (€149K - €4.7M)
- Çoğu ev orta-üst segment (medyan €468K)

### 3. Ev Özellikleri
- Tipik Hollanda evi:
  - ~146 m² yaşam alanı
  - ~747 m² arsa (ama medyan sadece 235m²)
  - 5-6 oda, 3-4 yatak odası
  - 2-3 kat
  - 1969 civarında yapılmış

### 4. Enerji Verimliliği Trendi
- A ve B label en yaygın (2,177 ev)
- Yüksek etiket = yüksek fiyat
- Enerji verimliliği Hollanda'da önemli bir faktör

---

## 🎯 Yatırım Tavsiyeleri

### Alıcılar İçin
1. **Yaşam alanına odaklanın** - m² başına en iyi değer
2. **Lokasyon araştırın** - şehirler arası büyük fark var
3. **Energy label önemli** - hem fiyat hem işletme maliyeti için
4. **Yeni olmak avantaj değil** - eski evler iyi restore edilebilir

### Satıcılar İçin
1. **Yaşam alanını vurgulayın** - en güçlü satış noktası
2. **Energy label yükseltin** - ROI yüksek olabilir
3. **Oda sayısını optimize edin** - açık plan yerine ayrı odalar
4. **Lokasyon pazarlaması** - mahalle özelliklerini vurgulayın

---

## 📁 Oluşturulan Dosyalar

```
DCE/
├── data/
│   └── dutch_house_prices_cleaned.csv  (Temizlenmiş veri seti)
├── reports/
│   ├── 1_price_analysis.png
│   ├── 2_correlation_matrix.png
│   ├── 3_energy_label_analysis.png
│   └── 4_build_year_analysis.png
└── 4-DutchHousePrices_Quick.py  (Analiz scripti)
```

---

## 🛠️ Kullanılan Araçlar

- **Python 3.x**
- **Pandas** - Veri manipülasyonu
- **NumPy** - Sayısal hesaplamalar
- **Matplotlib** - Görselleştirme
- **Seaborn** - İstatistiksel görselleştirme
- **DataScienceToolkit** - Template yapıları

---

## 📚 Metodoloji

1. **Veri Yükleme** - Kaggle dataset'i yüklendi
2. **Veri Temizleme**
   - Fiyat, alan ve sayısal değerler formatlandı
   - Eksik değerler dolduruldu
   - Duplicate kayıtlar silindi
3. **Feature Engineering**
   - Oda sayısı çıkarıldı
   - Kat sayısı çıkarıldı
   - Yeni feature'lar oluşturuldu
4. **Exploratory Data Analysis**
   - Temel istatistikler hesaplandı
   - Korelasyon analizi yapıldı
   - Kategorik analiz yapıldı
5. **Görselleştirme**
   - 4 adet kapsamlı görsel oluşturuldu
6. **Raporlama**
   - Bulgular dokümante edildi

---

**Rapor Hazırlayan:** GitHub Copilot + DataScienceToolkit  
**Son Güncelleme:** 22 Aralık 2025
