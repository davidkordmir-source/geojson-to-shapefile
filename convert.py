import geopandas as gpd
import os

# بارگذاری فایل GeoJSON
gdf = gpd.read_file('oiix.geojson')

# ایجاد دایرکتوری برای Shapefile‌ها
os.makedirs('shapefiles', exist_ok=True)

# تبدیل به Shapefile
gdf.to_file('shapefiles/oiix.shp', driver='ESRI Shapefile')

print('✅ Shapefile با موفقیت ایجاد شد!')
print('📁 فایل‌های زیر ایجاد شدند:')
print('  - oiix.shp')
print('  - oiix.shx')
print('  - oiix.dbf')
print('  - oiix.prj')
