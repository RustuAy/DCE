# DA-5 ile Titanic: Staj Mülakatleri İçin Uygulamalı Eğitim Rehberi 💼📊

_**Not:** Bu doküman aday perspektifiyle yazılmıştır — cevaplar "Ben …" şeklinde örnek ifadeler içerir. Amaç: hem pratik bir çalışma rehberi hem de staj mülakatlarında sıkça sorulan sorulara hazır; uygulanabilir cevaplar ve küçük uygulama adımları içermek._

---

## Özet (Ne elde edeceğim)
Ben bu rehberle Titanic veri setini kullanarak DA-5 (Define, Acquire, Assess, Analyze, Act) çerçevesine göre adım adım ilerleyeceğim. Her adımda:
- Ne yapacağımı kısa açıklama şeklinde okurum ✅
- Uygulama (kod) adımı yaparım ✅
- Mülakatta gelebilecek soru örnekleri ve kendi cümlelerimle kısa cevaplar hazırlarım ✅
- Kısa ödev veya alıştırma verilir, başarı ölçütü belirtilir ✅

---

## DA-5 adımları kısa (başlıklar)
1. Define — Problemi tanımlama
2. Acquire — Veri edinme ve doğrulama
3. Assess — Veri kalitesi ve hazırlık
4. Analyze — Keşifsel Veri Analizi ve Basit Modeller
5. Act — Sonuçları sunma ve aksiyon önerileri

---

## 1) DEFINE — Problemi tanımlama 🎯
Ne yaparım (özet):
- Hedefi net olarak cümleleştiririm: "Bu projede hedefim `Survived` sütununu kullanarak yolcuların kurtulma olasılığını anlamak/öngörmek." 
- Amaçları (başarı ölçütlerini) belirlerim: doğruluk, basit yorumlanabilirlik, ya da etkileyici bir görselleştirme gibi.

Kısa Uygulama - Not: Bu hücre sadece düşünme adımıdır (kod yok):
- Yazılacak not:
  - Hedef: "Kısa ve anlaşılır model ile yolcunun hayatta kalıp kalmayacağını %X doğrulukla tahmin etmek." 
  - KPI: **Accuracy** (doğruluk — modelin tüm tahminler içinde doğru yaptığı tahminlerin oranı) > %75 (örnek), fakat açıkla ki bu hedef dataset'e göre değişebilir.

Mülakat soruları ve örnek cevaplar:
- Soru: "Problem tanımını nasıl yaparsınız?" 
  - Cevap (örnek): "Önce hedef değişkeni ve başarının nasıl ölçüleceğini netleştiririm. Bu projede hedefimiz `Survived`. Başarıyı **accuracy** (doğruluk — doğru tahmin oranı), **F1** (F1 skoru — precision ve recall'un harmonik ortalaması; dengesiz sınıflarda anlamlıdır) veya **AUC** (ROC eğrisi altındaki alan — modelin sınıfları ayırt etme yeteneğini gösterir) ile ölçerim ve başta basit hedefler belirlerim (örn. accuracy > %70)."
- Soru: "Bu projede hangi paydaşlar olacak, hangi iş kararları etkilenebilir?"
  - Cevap: "Paydaş örneğin eğitim amaçlı veya yarışma amaçlı olabilir; müşteri içinse sonuçlar tahsis edilen kaynaklara (koltuk rezervasyonu, kurtarma planları gibi) ışık tutabilir."

Alıştırma:
- Kendin için hedef ve KPI yaz: 1-2 cümleyle.
- Değerlendirme: Hedef ve KPI net ve ölçülebilir mi?

---

## 2) ACQUIRE — Veri edinme & doğrulama 📂
Ne yaparım (özet):
- CSV dosyasını güvenli ve tekrar edilebilir şekilde notebook'a yüklerim.
- Dosyanın mevcut lokasyonunu doğrular, kopyalama tercihini kararlaştırırım (proje içerisindeki `data/` önerilir).

Kısa Kod (Notebook hücresi - çalıştırılabilir):
```python
# 1) Kütüphaneler
from pathlib import Path
import pandas as pd

# 2) Dosya yolu (örnek)
data_path = Path(r"C:\Users\User\Desktop\Dataset\titanic.csv")

# 3) Var mı kontrol et
if not data_path.exists():
    raise FileNotFoundError(f"Dosya yok: {data_path}")

# 4) Oku
df = pd.read_csv(data_path)
print('Okundu:', df.shape)
```

Mülakat soruları ve örnek cevaplar:
- Soru: "Veriyi nasıl alırsınız ve doğrularsınız?"
  - Cevap: "Dosya yolunu kontrol ederim, dosyayı `pandas.read_csv` ile okurum, satır/sütun sayısını ve ilk 5 satırı doğrularım. Kopyala-yapıştır yerine proje içi `data/` kullanmayı tercih ederim; böylece çalışma tekrar edilebilir olur." 

Alıştırma:
- Yukarıdaki kodu çalıştır ve `df.shape`, `df.head()` çıktısını kopyala.
- Değerlendirme: Dosyayı bulup okuyabiliyor musun?

---

## 3) ASSESS — Veri kalitesi & hazırlık 🧹
Ne yaparım (özet):
- `df.info()`, `df.isnull().sum()` ile veri eksikliklerini görürüm.
- Eksik değer stratejileri seçerim (drop? impute? özel değer?).
- Kategorik değişkenleri inceleyip dönüşüm planı yaparım.

Kısa Kod (Notebook hücresi - çalıştırılabilir):
```python
# Temel kontroller
print(df.info())
print('\nEksikler:\n', df.isnull().sum())

# Örnek small fix: Age için median ile doldurma (örnek adım)
df['Age_filled'] = df['Age'].fillna(df['Age'].median())

# Kısa kontrol
print('Age eksik kalır mı?', df['Age_filled'].isnull().any())
```

Mülakat soruları ve örnek cevaplar:
- Soru: "Eksik verilerle nasıl uğraşırsınız?" 
  - Cevap: "Eksik verinin dağılımını gözlemler, mekanizmasını anlamaya çalışırım (MCAR/MAR/MNAR). Hızlı bir prototip için numeric'leri median/mean ile doldururum, kategoriklerde 'Unknown' veya en sık kategoriyle doldurma uygundur. Büyük oranda eksik bir sütun varsa (örn. Cabin) o sütunu düşünebilirim veya farklı bir feature engineering yaparım." 
- Soru: "Neden median yerine mean kullanmayız?"
  - Cevap: "Ortalama uç değerlere daha hassastır; median daha dayanıklıdır, özellikle age gibi skewed dağılımlarda." 

Alıştırma:
- `Age` için median ve mean değerlerini hesapla; arada fark varsa not et. `Age` eksiklerini median ile doldur.
- Değerlendirme: Eksiklikler azaldı mı? (örn. `df.isnull().sum()` tekrar çalıştır)

---

## 4) ANALYZE — Keşifsel analiz & basit modelleme 📈
Ne yaparım (özet):
- Sınıflayıcı olarak basit bir model (örn. Logistic Regression) kurarım; pipeline ile eksik doldurma + encoding + model.
- Ayrıca pivot/tablo ve basit görselleştirmeler yaparım (ör: hayatta kalma oranı sınıfa göre).

Kısa Kod (Notebook hücresi - çalıştırılabilir) — EDA:
```python
# Basit pivot
print(df.groupby('Pclass')['Survived'].mean())

# Cinsiyete göre hayatta kalma
print(df.groupby('Sex')['Survived'].mean())
```

Kısa Kod — Basit model (sklearn ile):
```python
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Base features
features = ['Pclass', 'Sex', 'Age_filled', 'Fare']
X = df[features]
y = df['Survived']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Transformer
numeric_feats = ['Age_filled','Fare']
cat_feats = ['Pclass','Sex']
pre = ColumnTransformer([
    ('num', SimpleImputer(strategy='median'), numeric_feats),
    ('cat', OneHotEncoder(handle_unknown='ignore'), cat_feats)
])

pipe = make_pipeline(pre, LogisticRegression(max_iter=1000))
pipe.fit(X_train, y_train)
print('Test accuracy:', accuracy_score(y_test, pipe.predict(X_test)))
```

Mülakat soruları ve örnek cevaplar:
- Soru: "Model performansını nasıl değerlendirirsiniz?"
  - Cevap: "İlk olarak **accuracy** (doğruluk), **precision** (kesinlik — pozitif tahminlerin kaçının doğru olduğunu gösterir), **recall** (duyarlılık — gerçek pozitiflerin kaçının yakalandığını gösterir) ve **AUC** (ROC eğrisi altındaki alan) değerlerini kontrol ederim; dengesiz sınıf varsa accuracy yanıltıcı olabilir. Ayrıca basit bir baseline (örn. random veya most-frequent) ile karşılaştırırım." 
- Soru: "Feature seçimi nasıl yaparsınız?"
  - Cevap: "Öncelikle domain bilgisi, ardından korelasyon ve model bazlı önem sıralaması ile seçerim; fazla feature varsa regularizasyon veya seçme yöntemleri kullanırım." 

Alıştırma:
- Yukarıdaki pipeline'ı çalıştır. Test doğruluğunu raporla.
- Değerlendirme: Model baseline'in üzerinde mi?

---

## 5) ACT — Sonuçları sunma & aksiyon önerileri 📣
Ne yaparım (özet):
- Sonuçları açık, kısa ve görselleştirilmiş bir rapor halinde sunarım (ör: Jupyter -> PDF/HTML veya PowerPoint'te birkaç slide).
- Öneriler ve limitasyonlar bölümünü eklerim (ör: veri bias, eksik veriler, model belirsizliği).

Sunum kontrol listesi (örnek):
- 2-3 slayt: Problem, veri + temel bulgular, öneriler
- Bir cümlede sonuç: "Pclass ve Sex en belirleyici iki özellik" gibi
- Limitasyonlar: "Cabin sütunu çok eksik, bu feature güvenilir değil"

Mülakat soruları ve örnek cevaplar:
- Soru: "Sonuçları nasıl sunarsınız?"
  - Cevap: "Kısa, görsel ve aksiyon odaklı sunarım: 1) problem tanımı, 2) önemli bulgular, 3) öneriler (ve riskler).

Alıştırma:
- Basit bir görselleştirme oluştur (örn. Pclass vs Survived bar chart). Sunum slaytları için 3 kısa madde yaz.

---

## Ek Bölüm: Mülakatta Teknik ve Davranışsal Sorulara Kısa Notlar
- Teknik örnekler: "Veri eksikliği ile nasıl başa çıkarsın?", "Model overfitting'i nasıl anlarsın?" — cevaplarda önce ANALİZ akışını (DA-5) belirtirim, sonra kısa teknik çözümü söylerim.
- Davranışsal: "Takım içinde zor karar aldığın bir örnek?" — STAR (Situation, Task, Action, Result) formatını kullanırım.

---

## Hızlı Cheat-sheet (Kopyala-yapıştır için küçük kod parçaları)
- Dosya okuma:
```python
from pathlib import Path
import pandas as pd
df = pd.read_csv(Path(r"C:\Users\User\Desktop\Dataset\titanic.csv"))
```
- Eksik kontrol:
```python
print(df.info())
print(df.isnull().sum())
```
- Median ile doldurma:
```python
df['Age'] = df['Age'].fillna(df['Age'].median())
```

---

## Son Söz
"Bu rehberi takip ederek hem pratik bir proje yapmış olacağım, hem de staj mülakatlarında sıkça sorulan soruları cevaplarken DA-5 yapı taşı gibi kullanabileceğim kısa, mantıklı argümanlara sahip olacağım.

---
