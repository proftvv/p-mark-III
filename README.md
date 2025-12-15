<div align="center">

# 🚀 P-Mark-III

### Advanced Business Intelligence & Data Collection System

[![Version](https://img.shields.io/badge/version-1.0.1-blue.svg)](https://github.com/proftvv/p-mark-III)
[![Phase](https://img.shields.io/badge/phase-P--1-green.svg)](https://github.com/proftvv/p-mark-III)
[![Update](https://img.shields.io/badge/update-Mars-orange.svg)](https://github.com/proftvv/p-mark-III)
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)

**Konum bazlı işletme verisi toplama ve analiz sistemi**

[Features](#-features) • [Installation](#-installation) • [Documentation](#-documentation) • [Roadmap](#-roadmap) • [Contributing](#-contributing)

</div>

---

## 📖 Proje Hakkında

P-Mark-III, işletmelerin dijital varlıklarını ve iletişim bilgilerini toplamak için geliştirilmiş web tabanlı bir veri toplama sistemidir. Belirtilen konumdan başlayarak, belirlenen yarıçap içindeki işletmelerin:

- 🌐 Web siteleri
- 📞 Telefon numaraları
- 📱 Sosyal medya hesapları (Facebook, Instagram, Twitter, LinkedIn)
- ⭐ Google değerlendirmeleri
- 📍 Konum bilgileri
- 🕐 Çalışma saatleri

gibi detaylı bilgilerini toplayarak, profesyonel Excel raporları oluşturur.

---

## ✨ Features

### 🔐 Güvenlik
- Kullanıcı kimlik doğrulama sistemi
- Oturum yönetimi
- Şifreli veri saklama

### 🗺️ Konum Bazlı Arama
- Google Maps/Places API entegrasyonu
- Yarıçap bazlı arama (özelleştirilebilir)
- Kategori ve anahtar kelime filtreleme
- Koordinat bazlı hassas konum belirleme

### 📊 Veri Toplama
- Otomatik web sitesi tespiti
- Sosyal medya hesap bulma
- İletişim bilgisi çıkarma
- Çoklu sonuç işleme
- Gerçek zamanlı veri doğrulama

### 📑 Excel Export
- Profesyonel formatlanmış raporlar
- Özelleştirilebilir kolonlar
- Otomatik genişlik ayarı
- Zaman damgalı dosya isimlendirme
- Toplu veri dışa aktarma

### 🌐 Web Interface
- Modern ve kullanıcı dostu arayüz
- Responsive tasarım (mobil uyumlu)
- Gerçek zamanlı durum göstergeleri
- Sonuç önizleme
- Hata mesajları ve uyarılar

### 🐛 Debug & Testing
- Kapsamlı log sistemi
- Test veri üreteci
- Otomatik testler
- Performans izleme
- Hata takibi

---

## 📊 Proje Durumu

**Mevcut Faz**: P-1.1 (Infrastructure) - ✅ TAMAMLANDI  
**Versiyon**: 1.0.1  
**Son Güncelleme**: Mars (15 Aralık 2025)

### ✅ Tamamlanan
- [x] Proje yapısı oluşturuldu
- [x] Versiyon kontrol sistemi
- [x] Dokümantasyon altyapısı
- [x] Debug framework
- [x] GitHub repository kurulumu

### 🔄 Devam Eden
- [ ] Kimlik doğrulama sistemi (Faz 1.2)
- [ ] Web framework kurulumu (Faz 1.3)

### 📅 Planlanan
- [ ] Google Maps API entegrasyonu (Faz 1.4)
- [ ] Veri toplama modülü (Faz 1.5)
- [ ] Excel export sistemi (Faz 1.6)
- [ ] Web arayüzü (Faz 1.7)
- [ ] Debug & test framework (Faz 1.8)

---

## 🚀 Installation

### Gereksinimler
```bash
# Python 3.8+ veya Node.js 14+
# Git
# Google Maps API Key
```

### Kurulum (Yakında)
```bash
# Repository'yi klonlayın
git clone https://github.com/proftvv/p-mark-III.git

# Proje dizinine gidin
cd p-mark-III

# Bağımlılıkları yükleyin (yakında)
# pip install -r requirements.txt
# veya
# npm install

# Uygulamayı başlatın (yakında)
# python app.py
# veya
# npm start
```

---

## 📁 Proje Yapısı

```
P-Mark-III/
├── 📂 versions/              # Versiyon kontrol ve güncelleme geçmişi
│   ├── version-control.json  # Merkezi versiyon yönetimi
│   ├── full-updates.md       # Tüm güncellemeler
│   └── Mars-v1.0.1.md       # İlk güncelleme dökümantasyonu
│
├── 📂 debug/                 # Test ve hata ayıklama
│   ├── debug.log            # Debug kayıtları
│   └── README.md            # Debug dökümantasyonu
│
├── 📂 src/                   # Kaynak kod (geliştirilecek)
│   ├── auth/                # Kimlik doğrulama modülü
│   ├── api/                 # API entegrasyonları
│   ├── data/                # Veri işleme
│   ├── export/              # Excel export
│   └── web/                 # Web arayüzü
│
├── 📂 docs/                  # Dokümantasyon
│   ├── P-1-phases.md        # P-1 fazı detayları
│   ├── API.md               # API dökümantasyonu (yakında)
│   └── SETUP.md             # Kurulum rehberi (yakında)
│
├── 📄 memory.md             # AI hafıza ve proje bağlamı
├── 📄 README.md             # Bu dosya
├── 📄 .gitignore            # Git ignore kuralları
└── 📄 LICENSE               # Lisans (yakında)
```

---

## 📚 Documentation

| Doküman | Açıklama |
|---------|----------|
| [Memory](memory.md) | Proje bağlamı ve AI hafızası |
| [P-1 Phases](docs/P-1-phases.md) | Detaylı faz dokümantasyonu |
| [Version Control](versions/version-control.json) | Versiyon yönetimi |
| [Full Updates](versions/full-updates.md) | Günceleme geçmişi |
| [Debug README](debug/README.md) | Debug ve test bilgileri |

---

## 🎯 Roadmap

### P-1: Foundation Phase (Mevcut)
- [x] Proje altyapısı
- [ ] Kimlik doğrulama
- [ ] Web framework
- [ ] Google Maps entegrasyonu
- [ ] Veri toplama
- [ ] Excel export
- [ ] Web arayüzü
- [ ] Test sistemi

### P-2: Enhancement (Planlı)
- [ ] Çoklu kullanıcı desteği
- [ ] Veritabanı entegrasyonu
- [ ] Arama geçmişi
- [ ] Gelişmiş filtreleme
- [ ] Otomatik zamanlanmış aramalar
- [ ] API rate limit yönetimi
- [ ] Performans optimizasyonu

### P-3: Advanced Features (Gelecek)
- [ ] Makine öğrenimi entegrasyonu
- [ ] Veri analizi ve görselleştirme
- [ ] Raporlama dashboard'u
- [ ] Çoklu API desteği
- [ ] Webhook entegrasyonları
- [ ] Mobil uygulama

---

## 🔢 Versiyonlama

**Format**: `v1.x.x`

| Seviye | Kural | Açıklama |
|--------|-------|----------|
| `1.x.x` | Stable | Stabil versiyonlar (manuel güncelleme) |
| `x.1.x` | Major | Büyük güncellemeler (P- fazı değişimi) |
| `x.x.1` | Minor | Hata düzeltmeleri ve hotfix (otomatik) |

**Güncelleme İsimlendirme**: Uzay temalı (Mars, James Webb, Hubble, Voyager, Apollo, vb.)

---

## 🛠️ Teknoloji Stack

### 🎯 Planlanan Teknolojiler

**Backend**:
- Python (Flask) / Node.js (Express)
- RESTful API
- Session yönetimi

**Frontend**:
- HTML5, CSS3, JavaScript (ES6+)
- Bootstrap / Tailwind CSS
- Responsive Design

**API & Services**:
- Google Maps Places API
- Google Geocoding API

**Data Processing**:
- Pandas / JavaScript Excel libraries
- openpyxl / xlsx

**Database** (P-2):
- SQLite / PostgreSQL
- Redis (Cache)

**DevOps**:
- Git & GitHub
- VS Code
- Debug & Testing tools

---

## 👥 Contributing

Projeye katkıda bulunmak isterseniz:

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request açın

---

## 🔐 Development Credentials

**Test Kullanıcısı**:
- Username: `proftvv`
- Password: `2503`

> ⚠️ Yalnızca geliştirme amaçlı kullanın

---

## 📞 Contact

**Developer**: proftvv  
**Email**: [ozcanyilmazcelebi2016@gmail.com](mailto:ozcanyilmazcelebi2016@gmail.com)  
**GitHub**: [@proftvv](https://github.com/proftvv)  
**Repository**: [P-Mark-III](https://github.com/proftvv/p-mark-III)

---

## 📄 License

Bu proje MIT lisansı altında lisanslanacaktır. Detaylar yakında eklenecektir.

---

## 🌟 Acknowledgments

- Google Maps Platform
- Open Source Community
- VS Code & GitHub Copilot

---

<div align="center">

**Made with ❤️ by proftvv**

**Version 1.0.1 - Mars Update**  
*Last Updated: December 15, 2025*

[⬆ Back to Top](#-p-mark-iii)

</div>
