# API Alternatives for P-Mark-III

**Date**: 2025-12-15  
**Status**: Research Document  
**Purpose**: Google Maps API alternatifleri ve karşılaştırma

---

## 🔴 Problem

Google Maps Places API kullanımı aylık yaklaşık **500₺** (~$60) maliyete sahip. Bu maliyet nedeniyle proje Phase 1.4'te durduruldu.

---

## 💰 Cost Comparison

| API Provider | Free Tier | Cost After Free | Features | Rating |
|--------------|-----------|-----------------|----------|--------|
| **Google Maps** | $200/90 gün | $17/1000 req | En kapsamlı | ⭐⭐⭐⭐⭐ |
| **Mapbox** | 50k req/ay | $5/1000 req | İyi | ⭐⭐⭐⭐⭐ |
| **Geoapify** | 2500 req/gün | €0.001/req | İyi | ⭐⭐⭐⭐ |
| **OpenStreetMap** | Unlimited | Free | Sınırlı | ⭐⭐⭐ |
| **Bing Maps** | 125k trans/year | $0.50/1000 | Kapsamlı | ⭐⭐⭐⭐ |
| **Here Maps** | 250k trans/mo | Varies | Kapsamlı | ⭐⭐⭐⭐ |

---

## 1. Mapbox (ÖNERİLEN)

### ✅ Avantajlar
- **50,000 request/ay ücretsiz**
- Geocoding, search, places API
- İyi dokümantasyon
- Python SDK mevcut
- Hızlı ve güvenilir

### ❌ Dezavantajlar
- Google kadar detaylı değil
- Sosyal medya bilgileri sınırlı

### 💻 Implementation

```python
# requirements.txt
mapbox==0.18.1

# .env
MAPBOX_ACCESS_TOKEN=your_token_here

# src/api/mapbox_client.py
from mapbox import Geocoder

class MapboxClient:
    def __init__(self, token):
        self.geocoder = Geocoder(access_token=token)
    
    def search_places(self, query, location, radius):
        response = self.geocoder.forward(
            query,
            proximity=location,
            limit=20
        )
        return response.geojson()
```

### 📊 Maliyet Analizi
- İlk 50k request: **Ücretsiz**
- 50k-200k: $5/1000 request
- **Aylık ortalama**: $0-25 (kullanıma göre)

---

## 2. Geoapify

### ✅ Avantajlar
- **2500 request/gün ücretsiz** (75k/ay)
- Places API, geocoding
- Kolay entegrasyon
- Güzel dokümantasyon

### ❌ Dezavantajlar
- Günlük limit (aylık değil)
- Küçük veritabanı

### 💻 Implementation

```python
import requests

class GeoapifyClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.geoapify.com/v2/places"
    
    def search_places(self, category, location, radius):
        params = {
            'categories': category,
            'filter': f'circle:{location[1]},{location[0]},{radius}',
            'apiKey': self.api_key
        }
        response = requests.get(self.base_url, params=params)
        return response.json()
```

---

## 3. OpenStreetMap Nominatim

### ✅ Avantajlar
- **Tamamen ücretsiz**
- Açık kaynak
- Global kapsama

### ❌ Dezavantajlar
- **1 request/second limit** (çok yavaş)
- Business details eksik
- Sosyal medya bilgileri yok
- Rate limiting çok sıkı

### 💻 Implementation

```python
from geopy.geocoders import Nominatim

class OSMClient:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="p-mark-iii")
    
    def geocode(self, address):
        return self.geolocator.geocode(address)
```

### ⚠️ Not
Hobi projeler için uygun, production için değil.

---

## 4. Bing Maps

### ✅ Avantajlar
- **125,000 transaction/year ücretsiz**
- Microsoft desteği
- Kapsamlı özellikler
- İyi dokümantasyon

### ❌ Dezavantajlar
- Yıllık limit (aylık değil)
- Python SDK kısıtlı

### 💻 Implementation

```python
import requests

class BingMapsClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://dev.virtualearth.net/REST/v1/"
    
    def search(self, query, location):
        url = f"{self.base_url}Locations"
        params = {
            'query': query,
            'userLocation': f"{location[0]},{location[1]}",
            'key': self.api_key
        }
        response = requests.get(url, params=params)
        return response.json()
```

---

## 5. Here Maps

### ✅ Avantajlar
- **250,000 transaction/month ücretsiz**
- Çok kapsamlı
- Enterprise kalite
- İyi routing

### ❌ Dezavantajlar
- Kompleks dokümantasyon
- Setup zor

---

## 📝 Recommendation

### Phase 1.4 için (Test)
**Mapbox** kullan:
- 50k request/ay ücretsiz
- Kolay entegrasyon
- Python SDK var
- Güvenilir

### Production için (Gelecek)
**Google Maps**'e geç:
- En kapsamlı data
- En iyi business info
- Sosyal medya bilgileri

### Geçiş Stratejisi
```python
# src/api/api_factory.py
class APIFactory:
    @staticmethod
    def get_client(api_type):
        if api_type == 'mapbox':
            return MapboxClient(os.getenv('MAPBOX_TOKEN'))
        elif api_type == 'google':
            return GoogleMapsClient(os.getenv('GOOGLE_API_KEY'))
        elif api_type == 'geoapify':
            return GeoapifyClient(os.getenv('GEOAPIFY_KEY'))
```

---

## 🎯 Action Plan

### Immediate (Test Phase)
1. Mapbox hesabı aç
2. Access token al (ücretsiz)
3. Phase 1.4'ü Mapbox ile implement et
4. 50k request/ay içinde test et

### Future (Production)
1. Kullanıcı sayısı arttıkça
2. Fon hazır olunca
3. Google Maps'e geç
4. Daha detaylı data

---

## 💡 Hybrid Approach

### Best of Both Worlds
```python
class HybridAPIClient:
    def __init__(self):
        self.mapbox = MapboxClient()
        self.google = GoogleMapsClient()
    
    def search(self, query, location):
        # Start with free Mapbox
        results = self.mapbox.search(query, location)
        
        # If insufficient, use Google for details
        if needs_more_details(results):
            enhanced = self.google.get_details(results)
            return enhanced
        
        return results
```

**Avantaj**: Maliyeti minimize ederken kaliteyi maksimize et

---

## 📊 Cost Projection

### Scenario 1: Mapbox Only
- **Cost**: $0/month (50k request içinde)
- **Use case**: Test, small scale

### Scenario 2: Hybrid (Mapbox + Google)
- **Mapbox**: $0 (basic search)
- **Google**: ~$100/month (details only)
- **Use case**: Medium scale

### Scenario 3: Google Only
- **Cost**: ~$500/month (full usage)
- **Use case**: Production, high quality

---

## 🔧 Implementation Priority

1. **Mapbox** - Hemen implement et (free)
2. Test ve geliştir
3. Kullanıcı feedback'i al
4. Gerekirse Google'a geç

---

## 📞 Support

Sorular için:
- Mapbox Docs: https://docs.mapbox.com/
- Geoapify Docs: https://apidocs.geoapify.com/
- Google Maps Docs: https://developers.google.com/maps

---

**Last Updated**: 2025-12-15
