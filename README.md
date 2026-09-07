# GeoJSON به Shapefile تبدیل

## درباره
این repository شامل تبدیل داده‌های GeoJSON برای OIIX (تهران ACC/FIR) به فرمت Shapefile است.

## فایل‌ها
- `oiix.geojson` - داده‌های اصلی GeoJSON
- `convert.py` - اسکریپت تبدیل
- `shapefiles/` - فایل‌های Shapefile خروجی

## نحوه استفاده

### نیاز‌مندی‌ها
```bash
pip install geopandas fiona shapely pyproj
```

### اجرا
```bash
python convert.py
```

## Shapefile خروجی
فایل‌های زیر تولید می‌شوند:
- `oiix.shp` - داده‌های هندسی
- `oiix.shx` - شاخص داده‌های هندسی
- `oiix.dbf` - جدول خصوصیات
- `oiix.prj` - اطلاعات سیستم مختصات

## مختصات
- **عرض جغرافیایی**: 35.689° شمالی
- **طول جغرافیایی**: 51.318° شرقی
- **کشور**: ایران
- **کد ICAO**: OIIX
