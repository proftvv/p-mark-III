<div align="center">

# 🚀 P-Mark-III

### Advanced Business Intelligence & Data Collection System

[![Version](https://img.shields.io/badge/version-1.0.2-blue.svg)](https://github.com/proftvv/p-mark-III)
[![Phase](https://img.shields.io/badge/phase-P--1.2/1.3-green.svg)](https://github.com/proftvv/p-mark-III)
[![Update](https://img.shields.io/badge/update-Hubble-orange.svg)](https://github.com/proftvv/p-mark-III)
[![Status](https://img.shields.io/badge/status-ON_HOLD-yellow.svg)](https://github.com/proftvv/p-mark-III)
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)

**Konum bazlı işletme verisi toplama ve analiz sistemi**

[Features](#-features) • [Quick Start](#-quick-start) • [Status](#-project-status) • [Roadmap](#-roadmap) • [Documentation](#-documentation)

</div>

---

## ⚠️ PROJECT STATUS - ON HOLD

> **🔴 Proje Geçici Olarak Durduruldu (15 Aralık 2025)**
> 
> **Sebep**: Google Maps Places API kullanımı aylık ~500₺ maliyet gerektiriyor. Proje için fon ayrılana kadar geliştirme Phase 1.4'te durdurulmuştur.
>
> **Tamamlanan**: Phase 1.1, 1.2, 1.3 (Authentication & Web Framework) ✅  
> **Bekleyen**: Phase 1.4 (Google Maps API Integration) ⏸️
>
> **Mevcut Durum**: Sistem şu anda çalışır durumda. Login sistemi, dashboard ve tüm altyapı hazır. Sadece Google API entegrasyonu ve veri toplama özellikleri beklemede.

### 💰 API Maliyet & Alternatifler
- **Google Maps Places API**: ~$60/ay (~500₺)
- **Alternatif: Mapbox**: 50,000 request/ay ücretsiz ⭐ (Önerilen)
- **Alternatif: Geoapify**: 2,500 request/gün ücretsiz
- Detaylı karşılaştırma: [API-ALTERNATIVES.md](docs/API-ALTERNATIVES.md)

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

### Tamamlanan Özellikler ✅

#### 🔐 Authentication System
- Login/Logout fonksiyonları
- Session yönetimi
- Password hashing (Werkzeug/bcrypt)
- "Beni Hatırla" özelliği
- Secure cookie handling

#### 🌐 Web Framework
- Flask 3.0.0 backend
- Responsive UI (mobil uyumlu)
- Modern gradient design
- Template engine (Jinja2)
- Static file serving

#### 🎨 User Interface
- Modern login sayfası
- Dashboard arayüzü
- Alert sistemi (auto-hide)
- Error pages (404, 500)
- CSS animations

### Bekleyen Özellikler ⏸️

#### 🗺️ Konum Bazlı Arama (Phase 1.4)
- Google Maps/Places API entegrasyonu
- Yarıçap bazlı arama
- Kategori ve anahtar kelime filtreleme
- Koordinat bazlı hassas konum belirleme

#### 📊 Veri Toplama (Phase 1.5)
- Otomatik web sitesi tespiti
- Sosyal medya hesap bulma
- İletişim bilgisi çıkarma
- Rating ve review bilgileri

#### 📑 Excel Export (Phase 1.6)
- Profesyonel formatlanmış raporlar
- Otomatik genişlik ayarı
- Zaman damgalı dosya isimlendirme
- Toplu veri dışa aktarma

---

## 🚀 Quick Start

### Gereksinimler
- Python 3.8+
- Git
- Virtual environment (otomatik oluşturulur)

### Kurulum ve Çalıştırma

```bash
# 1. Repository'yi klonla
git clone https://github.com/proftvv/p-mark-III.git
cd p-mark-III

# 2. Sistemi başlat (Windows)
start.bat

# 2. Sistemi başlat (Linux/Mac)
chmod +x start.sh
./start.sh

# 3. Tarayıcıda aç
# http://127.0.0.1:5000

# 4. Giriş bilgileri
# Kullanıcı: proftvv
# Şifre: 2503
```

Script otomatik olarak:
- Virtual environment oluşturur
- Bağımlılıkları yükler
- .env dosyası oluşturur
- Flask server'ı başlatır

---

## 📊 Project Status

**Version**: 1.0.2 (Hubble)  
**Phase**: P-1.2/1.3 ✅ TAMAMLANDI  
**Status**: 🟡 ON HOLD (API maliyet nedeniyle)  
**Last Update**: 15 Aralık 2025

### ✅ Tamamlanan Fazlar

| Phase | Name | Status | Version | Details |
|-------|------|--------|---------|---------|
| 1.1 | Project Infrastructure | ✅ | 1.0.1 | Proje yapısı, version control, docs |
| 1.2 | Authentication System | ✅ | 1.0.2 | Login/logout, session, password hash |
| 1.3 | Web Framework | ✅ | 1.0.2 | Flask setup, templates, UI |

### ⏸️ Bekleyen Fazlar

| Phase | Name | Status | Blocker |
|-------|------|--------|---------|
| 1.4 | Google Maps API Integration | ⏸️ | API maliyet (~500₺/ay) |
| 1.5 | Data Collection Module | 📝 | Phase 1.4 bağımlılığı |
| 1.6 | Excel Export System | 📝 | Phase 1.5 bağımlılığı |
| 1.7 | Enhanced Web Interface | 📝 | Phase 1.6 bağımlılığı |
| 1.8 | Debug & Testing Framework | 📝 | Planlı |

**Progress**: 37.5% (3/8 phases tamamlandı)

---

## 🎯 Roadmap

### Phase 1.4: Google Maps API Integration (NEXT - ON HOLD)

**Gereksinimler**:
- Google Cloud Platform hesabı
- API Key (Places, Geocoding)
- Aylık ~500₺ bütçe

**Alternatif**: Mapbox API (50k request/ay ücretsiz)

**Implementation Steps**:
1. API key setup (30 dk)
2. Backend integration (2-3 saat)
3. Frontend search form (2 saat)
4. Testing (1 saat)

[Detaylı Phase dokümantasyonu: docs/P-1-phases.md](docs/P-1-phases.md)

### Phase 1.5: Data Collection (4-5 saat)
- Business data schema
- Data extraction functions
- Social media URL detection
- Temporary storage

### Phase 1.6: Excel Export (3-4 saat)
- openpyxl integration
- Excel template design
- Download functionality

### Phase 1.7: Enhanced UI (4-5 saat)
- Search form with autocomplete
- Results table (DataTables.js)
- Map preview
- Export button

### Phase 1.8: Testing (3-4 saat)
- Unit tests
- Integration tests
- Performance monitoring

### Phase P-2: Enhancement (Future)
- Multiple users
- Database (SQLite/PostgreSQL)
- Search history
- Admin panel

### Phase P-3: Advanced Features (Future)
- Machine learning
- Analytics dashboard
- Mobile app
- Multiple API support

---

## 📁 Proje Yapısı

```
P-Mark-III/
├── app.py                    # Ana Flask uygulaması ✅
├── start.bat                 # Windows başlatma ✅
├── start.sh                  # Linux/Mac başlatma ✅
├── requirements.txt          # Python dependencies ✅
├── .env                      # Environment variables ✅
│
├── src/
│   ├── templates/           # HTML şablonları ✅
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── 404.html
│   │   └── 500.html
│   └── static/             # Static assets ✅
│       ├── css/style.css
│       └── js/main.js
│
├── docs/                    # Dokümantasyon ✅
│   ├── P-1-phases.md       # Detaylı faz bilgileri
│   └── API-ALTERNATIVES.md # API alternatifleri
│
├── versions/               # Version control ✅
│   ├── version-control.json
│   ├── full-updates.md
│   ├── Mars-v1.0.1.md
│   └── Hubble-v1.0.2.md
│
├── debug/                  # Debug & logs ✅
│   ├── debug.log
│   └── README.md
│
└── memory.md              # AI hafıza & context ✅
```

---

## 📚 Documentation

| Doküman | Açıklama |
|---------|----------|
| [README.md](README.md) | Ana proje dökümantasyonu (bu dosya) |
| [memory.md](memory.md) | AI hafızası, proje context, yapılacaklar |
| [P-1-phases.md](docs/P-1-phases.md) | Detaylı faz dokümantasyonu, implementation steps |
| [API-ALTERNATIVES.md](docs/API-ALTERNATIVES.md) | API alternatifleri ve maliyet karşılaştırması |
| [version-control.json](versions/version-control.json) | Versiyon yönetimi |
| [Mars v1.0.1](versions/Mars-v1.0.1.md) | Phase 1.1 update dökümantasyonu |
| [Hubble v1.0.2](versions/Hubble-v1.0.2.md) | Phase 1.2/1.3 update dökümantasyonu |

---

## 🛠️ Tech Stack

### Mevcut
- **Backend**: Python 3.8+ / Flask 3.0.0
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Auth**: Session-based with Werkzeug password hashing
- **Server**: Flask development server (localhost:5000)

### Planlı (Next Phases)
- **API**: Google Maps Places API / Mapbox (alternative)
- **Export**: openpyxl / xlsx
- **Database**: SQLite / PostgreSQL (Phase P-2)
- **Cache**: Redis (Phase P-2)

---

## 📝 Developer Notes

### Projeye Devam Etmek İçin

**Herhangi bir AI veya developer bu projeyi devam ettirebilir:**

1. **memory.md**'yi oku - Tüm proje context burada
2. **docs/P-1-phases.md**'yi oku - Detaylı implementation steps
3. **docs/API-ALTERNATIVES.md**'yi oku - API seçenekleri
4. Bu README'deki roadmap'i takip et
5. Phase 1.4'ten başla

### Önemli Dosyalar
- `memory.md` - AI hafızası, yapılacaklar, hatalar
- `app.py` - Ana Flask uygulaması
- `.env` - Environment variables
- `versions/version-control.json` - Versiyon bilgisi

### Versiyon Sistemi
- `1.x.x` - Stable versions (manuel değişim)
- `x.1.x` - Major updates (P- phase değişimi)
- `x.x.1` - Bug fixes (otomatik increment)

### Update Naming
Uzay temalı isimler: Mars, Hubble, Voyager, Apollo, Galileo, Kepler, Cassini, Newton...

### Git Workflow
```bash
git add .
git commit -m "vX.X.X - UpdateName: Description"
git push origin main
```

---

## 🔐 Development Credentials

**Test Kullanıcısı**:
- **Username**: proftvv
- **Password**: 2503

> ⚠️ Yalnızca geliştirme ortamı için

---

## 💡 API Alternatifleri

### 1. Mapbox (ÖNERİLEN) ⭐
- **Maliyet**: 50,000 request/ay ücretsiz
- **Özellikler**: Geocoding, search, places
- **Uygunluk**: ⭐⭐⭐⭐⭐

### 2. Geoapify
- **Maliyet**: 2,500 request/gün ücretsiz
- **Uygunluk**: ⭐⭐⭐⭐

### 3. Google Maps
- **Maliyet**: $200 kredi (90 gün), sonra ~$60/ay
- **Özellikler**: En kapsamlı
- **Uygunluk**: Production için ideal

[Detaylı karşılaştırma ve implementation: docs/API-ALTERNATIVES.md](docs/API-ALTERNATIVES.md)

---

## 📊 Project Statistics

- **Version**: 1.0.2
- **Total Files**: 17
- **Lines of Code**: ~2,500
- **Languages**: Python, HTML, CSS, JavaScript
- **Framework**: Flask 3.0.0
- **Completion**: 37.5% (Phase P-1)

---

## 🐛 Known Issues

### Mevcut Sorunlar
*Bilinen kritik sorun yok*

### Limitasyonlar
- ⚠️ Tek kullanıcı (proftvv only)
- ⚠️ Session-based storage (database yok)
- ⚠️ API entegrasyonu yok (beklemede)
- ⚠️ Arama özelliği yok (Phase 1.4)

---

## 📞 Contact

**Developer**: proftvv  
**Email**: [ozcanyilmazcelebi2016@gmail.com](mailto:ozcanyilmazcelebi2016@gmail.com)  
**GitHub**: [@proftvv](https://github.com/proftvv)  
**Repository**: [P-Mark-III](https://github.com/proftvv/p-mark-III)

**Status**: 🟡 ON HOLD (API maliyet)  
**Last Update**: 15 Aralık 2025

---

## 📄 License
MIT License

Copyright (c) 2025 Özcan YILMAZÇELEBİ

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## 🌟 Acknowledgments

- Flask Framework
- Google Maps Platform (future)
- Mapbox (alternative)
- Open Source Community
- VS Code & GitHub Copilot

---

## 🎯 Final Notes

> **Bu proje API maliyeti nedeniyle geçici olarak bekletilmiştir.**
>
> **Tüm altyapı hazır - sadece API entegrasyonu bekleniyor.**
>
> **Devam etmek için:**
> - Phase 1.4'ü uygula (Mapbox veya Google API)
> - memory.md ve docs/ klasöründeki dokümantasyonu takip et
> - Her phase'i test et ve commit at
>
> **Alternatif**: Mapbox ile ücretsiz devam edilebilir (50k request/ay)

---

<div align="center">

**Made with ❤️ by proftvv**

**Version 1.0.2 - Hubble Update**  
*Last Updated: December 15, 2025*  
*Status: ON HOLD - Waiting for API funding*

[⬆ Back to Top](#-p-mark-iii)

</div>
