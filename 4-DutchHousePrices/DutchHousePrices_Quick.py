"""
Dutch House Prices - Hızlı Analiz Scripti
DataScienceToolkit kullanılarak hazırlanmıştır.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Veri setini yükle
print("=" * 80)
print("DUTCH HOUSE PRICES ANALİZİ BAŞLATILDI")
print("=" * 80)

data_path = r'C:\Users\User\.cache\kagglehub\datasets\bryan2k19\dutch-house-prices-dataset\versions\1\raw_data.csv'
df = pd.read_csv(data_path)

print(f"\n✓ Veri başarıyla yüklendi!")
print(f"Boyut: {df.shape[0]:,} satır x {df.shape[1]} kolon")
print(f"\nKolonlar: {', '.join(df.columns.tolist())}")

# ═══════════════════════════════════════════════════════════════════════════════
# 1. VERİ TEMİZLEME
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "─" * 80)
print("1. VERİ TEMİZLEME")
print("─" * 80)

# Fiyat kolonunu temizle
print("\nFiyat kolonunu temizleme...")
df['Price_Clean'] = df['Price'].astype(str).str.replace('€', '').str.replace('.', '').str.replace(',', '').str.strip()
df['Price_Clean'] = pd.to_numeric(df['Price_Clean'], errors='coerce')

# Alan kolonlarını temizle
print("Alan kolonlarını temizleme...")
df['Lot_Size'] = df['Lot size (m2)'].astype(str).str.replace('m²', '').str.replace('.', '').str.replace(',', '').str.strip()
df['Lot_Size'] = pd.to_numeric(df['Lot_Size'], errors='coerce')

df['Living_Space'] = df['Living space size (m2)'].astype(str).str.replace('m²', '').str.replace('.', '').str.replace(',', '').str.strip()
df['Living_Space'] = pd.to_numeric(df['Living_Space'], errors='coerce')

# Build year'ı sayısal yap
df['Build_Year'] = pd.to_numeric(df['Build year'], errors='coerce')

# Oda sayısını çıkar
df['Total_Rooms'] = df['Rooms'].astype(str).str.extract(r'(\d+)')[0].astype(float)
df['Bedrooms'] = df['Rooms'].astype(str).str.extract(r'\((\d+)')[0].astype(float)

# Kat sayısını çıkar
df['Number_of_Floors'] = df['Floors'].astype(str).str.extract(r'(\d+)')[0].astype(float)

print("✓ Veri temizleme tamamlandı!")

# ═══════════════════════════════════════════════════════════════════════════════
# 2. TEMEL İSTATİSTİKLER
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "─" * 80)
print("2. TEMEL İSTATİSTİKLER")
print("─" * 80)

print("\nFiyat İstatistikleri:")
print(f"  • Ortalama Fiyat: €{df['Price_Clean'].mean():,.0f}")
print(f"  • Medyan Fiyat: €{df['Price_Clean'].median():,.0f}")
print(f"  • Min Fiyat: €{df['Price_Clean'].min():,.0f}")
print(f"  • Max Fiyat: €{df['Price_Clean'].max():,.0f}")
print(f"  • Standart Sapma: €{df['Price_Clean'].std():,.0f}")

print("\nYaşam Alanı İstatistikleri:")
print(f"  • Ortalama: {df['Living_Space'].mean():.1f} m²")
print(f"  • Medyan: {df['Living_Space'].median():.1f} m²")
print(f"  • Min: {df['Living_Space'].min():.1f} m²")
print(f"  • Max: {df['Living_Space'].max():.1f} m²")

print("\nArsa Alanı İstatistikleri:")
print(f"  • Ortalama: {df['Lot_Size'].mean():.1f} m²")
print(f"  • Medyan: {df['Lot_Size'].median():.1f} m²")

print("\nYapım Yılı İstatistikleri:")
print(f"  • Ortalama: {df['Build_Year'].mean():.0f}")
print(f"  • En Eski: {df['Build_Year'].min():.0f}")
print(f"  • En Yeni: {df['Build_Year'].max():.0f}")

print("\nOda İstatistikleri:")
print(f"  • Ortalama Toplam Oda: {df['Total_Rooms'].mean():.1f}")
print(f"  • Ortalama Yatak Odası: {df['Bedrooms'].mean():.1f}")
print(f"  • Ortalama Kat Sayısı: {df['Number_of_Floors'].mean():.1f}")

# ═══════════════════════════════════════════════════════════════════════════════
# 3. EKSİK DEĞER ANALİZİ
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "─" * 80)
print("3. EKSİK DEĞER ANALİZİ")
print("─" * 80)

missing_data = pd.DataFrame({
    'Kolon': df.columns,
    'Eksik_Değer': df.isnull().sum().values,
    'Eksik_Yüzde': (df.isnull().sum().values / len(df) * 100).round(2)
})
missing_data = missing_data[missing_data['Eksik_Değer'] > 0].sort_values('Eksik_Yüzde', ascending=False)

if len(missing_data) > 0:
    print("\nEksik Değer Raporu:")
    print(missing_data.to_string(index=False))
else:
    print("\n✓ Eksik değer bulunamadı!")

# ═══════════════════════════════════════════════════════════════════════════════
# 4. ŞEHİR ANALİZİ
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "─" * 80)
print("4. ŞEHİR ANALİZİ")
print("─" * 80)

city_stats = df.groupby('City').agg({
    'Price_Clean': ['count', 'mean', 'median'],
    'Living_Space': 'mean'
}).round(0)

city_stats.columns = ['Ev_Sayısı', 'Ort_Fiyat', 'Medyan_Fiyat', 'Ort_Alan']
city_stats = city_stats.sort_values('Ort_Fiyat', ascending=False).head(10)

print("\nEn Pahalı 10 Şehir:")
print(city_stats.to_string())

# ═══════════════════════════════════════════════════════════════════════════════
# 5. ENERGY LABEL ANALİZİ
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "─" * 80)
print("5. ENERGY LABEL ANALİZİ")
print("─" * 80)

if 'Energy label' in df.columns:
    energy_stats = df.groupby('Energy label')['Price_Clean'].agg(['count', 'mean', 'median']).round(0)
    energy_stats.columns = ['Ev_Sayısı', 'Ort_Fiyat', 'Medyan_Fiyat']
    energy_stats = energy_stats.sort_values('Ort_Fiyat', ascending=False)
    
    print("\nEnergy Label'a Göre Fiyat Analizi:")
    print(energy_stats.to_string())

# ═══════════════════════════════════════════════════════════════════════════════
# 6. KORELASYON ANALİZİ
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "─" * 80)
print("6. KORELASYON ANALİZİ")
print("─" * 80)

numerical_cols = ['Price_Clean', 'Lot_Size', 'Living_Space', 'Build_Year', 
                 'Total_Rooms', 'Bedrooms', 'Number_of_Floors']
corr_df = df[numerical_cols].corr()

print("\nFiyat ile Diğer Değişkenler Arasındaki Korelasyon:")
price_corr = corr_df['Price_Clean'].sort_values(ascending=False)
for col, corr in price_corr.items():
    if col != 'Price_Clean':
        print(f"  • {col}: {corr:.3f}")

# ═══════════════════════════════════════════════════════════════════════════════
# 7. GÖRSELLEŞTİRME
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "─" * 80)
print("7. GÖRSELLEŞTİRMELER OLUŞTURULUYOR")
print("─" * 80)

# reports klasörünü oluştur
import os
os.makedirs('reports', exist_ok=True)

# Şekil 1: Fiyat Dağılımı ve Analizi
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Dutch House Prices - Kapsamlı Fiyat Analizi', fontsize=16, fontweight='bold')

# 1.1: Fiyat Histogram
axes[0, 0].hist(df['Price_Clean'].dropna(), bins=50, edgecolor='black', alpha=0.7, color='skyblue')
axes[0, 0].axvline(df['Price_Clean'].mean(), color='red', linestyle='--', linewidth=2, 
                   label=f'Ortalama: €{df["Price_Clean"].mean():,.0f}')
axes[0, 0].axvline(df['Price_Clean'].median(), color='green', linestyle='--', linewidth=2, 
                   label=f'Medyan: €{df["Price_Clean"].median():,.0f}')
axes[0, 0].set_xlabel('Fiyat (€)', fontsize=11)
axes[0, 0].set_ylabel('Frekans', fontsize=11)
axes[0, 0].set_title('Fiyat Dağılımı Histogramı', fontsize=12, fontweight='bold')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# 1.2: Fiyat Box Plot
bp = axes[0, 1].boxplot(df['Price_Clean'].dropna(), patch_artist=True)
bp['boxes'][0].set_facecolor('lightblue')
bp['boxes'][0].set_alpha(0.7)
axes[0, 1].set_ylabel('Fiyat (€)', fontsize=11)
axes[0, 1].set_title('Fiyat Box Plot (Aykırı Değer Analizi)', fontsize=12, fontweight='bold')
axes[0, 1].set_xticklabels(['Fiyat'])
axes[0, 1].grid(True, alpha=0.3)

# 1.3: En Pahalı 15 Şehir
city_prices = df.groupby('City')['Price_Clean'].mean().sort_values(ascending=False).head(15)
colors = plt.cm.viridis(np.linspace(0, 1, len(city_prices)))
axes[1, 0].barh(range(len(city_prices)), city_prices.values, color=colors)
axes[1, 0].set_yticks(range(len(city_prices)))
axes[1, 0].set_yticklabels(city_prices.index, fontsize=9)
axes[1, 0].set_xlabel('Ortalama Fiyat (€)', fontsize=11)
axes[1, 0].set_title('En Pahalı 15 Şehir', fontsize=12, fontweight='bold')
axes[1, 0].invert_yaxis()
axes[1, 0].grid(True, alpha=0.3, axis='x')

# 1.4: Yaşam Alanı vs Fiyat
valid_data = df[['Living_Space', 'Price_Clean']].dropna()
scatter = axes[1, 1].scatter(valid_data['Living_Space'], valid_data['Price_Clean'], 
                            alpha=0.5, c=valid_data['Price_Clean'], cmap='YlOrRd', s=30)
axes[1, 1].set_xlabel('Yaşam Alanı (m²)', fontsize=11)
axes[1, 1].set_ylabel('Fiyat (€)', fontsize=11)
axes[1, 1].set_title('Yaşam Alanı vs Fiyat İlişkisi', fontsize=12, fontweight='bold')
corr = valid_data['Living_Space'].corr(valid_data['Price_Clean'])
axes[1, 1].text(0.05, 0.95, f'Korelasyon: {corr:.3f}', 
               transform=axes[1, 1].transAxes, verticalalignment='top',
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8), fontsize=10)
plt.colorbar(scatter, ax=axes[1, 1], label='Fiyat (€)')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('reports/1_price_analysis.png', dpi=300, bbox_inches='tight')
print("✓ Şekil 1 kaydedildi: reports/1_price_analysis.png")
plt.close()

# Şekil 2: Korelasyon Matrisi
fig, ax = plt.subplots(figsize=(12, 10))
mask = np.triu(np.ones_like(corr_df, dtype=bool))
sns.heatmap(corr_df, annot=True, fmt='.2f', cmap='coolwarm', center=0, 
           square=True, linewidths=1, cbar_kws={"shrink": 0.8}, mask=mask, ax=ax)
ax.set_title('Korelasyon Matrisi (Sayısal Değişkenler)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('reports/2_correlation_matrix.png', dpi=300, bbox_inches='tight')
print("✓ Şekil 2 kaydedildi: reports/2_correlation_matrix.png")
plt.close()

# Şekil 3: Energy Label Analizi
if 'Energy label' in df.columns and df['Energy label'].notna().sum() > 0:
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # 3.1: Energy Label Dağılımı
    energy_counts = df['Energy label'].value_counts().sort_index()
    colors = plt.cm.RdYlGn_r(np.linspace(0, 1, len(energy_counts)))
    axes[0].bar(energy_counts.index, energy_counts.values, color=colors, edgecolor='black', alpha=0.8)
    axes[0].set_xlabel('Energy Label', fontsize=11)
    axes[0].set_ylabel('Ev Sayısı', fontsize=11)
    axes[0].set_title('Energy Label Dağılımı', fontsize=12, fontweight='bold')
    axes[0].grid(True, alpha=0.3, axis='y')
    
    # 3.2: Energy Label vs Fiyat
    energy_price = df.groupby('Energy label')['Price_Clean'].mean().sort_values(ascending=False)
    colors2 = plt.cm.viridis(np.linspace(0, 1, len(energy_price)))
    axes[1].bar(energy_price.index, energy_price.values, color=colors2, edgecolor='black', alpha=0.8)
    axes[1].set_xlabel('Energy Label', fontsize=11)
    axes[1].set_ylabel('Ortalama Fiyat (€)', fontsize=11)
    axes[1].set_title('Energy Label vs Ortalama Fiyat', fontsize=12, fontweight='bold')
    axes[1].grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('reports/3_energy_label_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Şekil 3 kaydedildi: reports/3_energy_label_analysis.png")
    plt.close()

# Şekil 4: Build Year vs Price
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# 4.1: Build Year Dağılımı
axes[0].hist(df['Build_Year'].dropna(), bins=30, edgecolor='black', alpha=0.7, color='coral')
axes[0].set_xlabel('Yapım Yılı', fontsize=11)
axes[0].set_ylabel('Ev Sayısı', fontsize=11)
axes[0].set_title('Yapım Yılı Dağılımı', fontsize=12, fontweight='bold')
axes[0].grid(True, alpha=0.3)

# 4.2: Build Year vs Price
valid_data2 = df[['Build_Year', 'Price_Clean']].dropna()
scatter2 = axes[1].scatter(valid_data2['Build_Year'], valid_data2['Price_Clean'], 
                          alpha=0.5, c=valid_data2['Price_Clean'], cmap='plasma', s=30)
axes[1].set_xlabel('Yapım Yılı', fontsize=11)
axes[1].set_ylabel('Fiyat (€)', fontsize=11)
axes[1].set_title('Yapım Yılı vs Fiyat İlişkisi', fontsize=12, fontweight='bold')
corr2 = valid_data2['Build_Year'].corr(valid_data2['Price_Clean'])
axes[1].text(0.05, 0.95, f'Korelasyon: {corr2:.3f}', 
            transform=axes[1].transAxes, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8), fontsize=10)
plt.colorbar(scatter2, ax=axes[1], label='Fiyat (€)')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('reports/4_build_year_analysis.png', dpi=300, bbox_inches='tight')
print("✓ Şekil 4 kaydedildi: reports/4_build_year_analysis.png")
plt.close()

# ═══════════════════════════════════════════════════════════════════════════════
# 8. TEMİZLENMİŞ VERİYİ KAYDET
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "─" * 80)
print("8. TEMİZLENMİŞ VERİYİ KAYDETME")
print("─" * 80)

os.makedirs('data', exist_ok=True)
output_file = 'data/dutch_house_prices_cleaned.csv'
df.to_csv(output_file, index=False)
print(f"✓ Temizlenmiş veri kaydedildi: {output_file}")

# ═══════════════════════════════════════════════════════════════════════════════
# 9. ÖZET RAPOR
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "═" * 80)
print("ÖZET RAPOR")
print("═" * 80)

print(f"""
📊 VERİ SETİ BİLGİLERİ:
  • Toplam Ev Sayısı: {len(df):,}
  • Toplam Şehir Sayısı: {df['City'].nunique()}
  • Veri Boyutu: {df.shape[0]} satır x {df.shape[1]} kolon

💰 FİYAT İSTATİSTİKLERİ:
  • Ortalama: €{df['Price_Clean'].mean():,.0f}
  • Medyan: €{df['Price_Clean'].median():,.0f}
  • Min: €{df['Price_Clean'].min():,.0f}
  • Max: €{df['Price_Clean'].max():,.0f}

🏠 EV ÖZELLİKLERİ:
  • Ortalama Yaşam Alanı: {df['Living_Space'].mean():.1f} m²
  • Ortalama Arsa Alanı: {df['Lot_Size'].mean():.1f} m²
  • Ortalama Oda Sayısı: {df['Total_Rooms'].mean():.1f}
  • Ortalama Yatak Odası: {df['Bedrooms'].mean():.1f}
  • Ortalama Kat Sayısı: {df['Number_of_Floors'].mean():.1f}

📅 YAPIM YILI:
  • Ortalama: {df['Build_Year'].mean():.0f}
  • En Eski: {df['Build_Year'].min():.0f}
  • En Yeni: {df['Build_Year'].max():.0f}

✅ OLUŞTURULAN DOSYALAR:
  ├── data/dutch_house_prices_cleaned.csv
  ├── reports/1_price_analysis.png
  ├── reports/2_correlation_matrix.png
  ├── reports/3_energy_label_analysis.png
  └── reports/4_build_year_analysis.png
""")

print("═" * 80)
print("ANALİZ TAMAMLANDI! 🎉")
print("═" * 80)
