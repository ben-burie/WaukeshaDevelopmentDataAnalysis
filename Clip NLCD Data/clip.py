import geopandas as gpd
import rasterio
from rasterio.mask import mask

# Waukesha County Shapefile
gdf = gpd.read_file("cb_2018_us_county_500k.shp")
gdf = gdf[gdf["NAME"] == "Waukesha"]
print("File read.")

# Reproject map to match shapefile
with rasterio.open("Annual_NLCD_LndCov_2023_CU_C1V0.tif") as src:
    print("Shapefile opened.")
    gdf = gdf.to_crs(src.crs)

    gdf = gdf[gdf.geometry.notnull()]
    out_image, out_transform = mask(src, gdf.geometry, crop=True)
    out_meta = src.meta.copy()
    print("Outimage generated.")

# Update metadata
out_meta.update({
    "driver": "GTiff",
    "height": out_image.shape[1],
    "width": out_image.shape[2],
    "transform": out_transform
})
print("Metadata updated.")

# Save clipped raster
with rasterio.open("waukesha_land_cover_2023.tif", "w", **out_meta) as dest:
    dest.write(out_image)
    print("Output file created.")