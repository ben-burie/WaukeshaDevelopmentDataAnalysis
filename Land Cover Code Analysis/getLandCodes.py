import rasterio
import numpy as np
import pandas as pd

# NLCD classes
nlcd_classes = {
    11: "Open Water",
    21: "Developed, Open Space",
    22: "Developed, Low Intensity",
    23: "Developed, Medium Intensity",
    24: "Developed, High Intensity",
    31: "Barren Land",
    41: "Deciduous Forest",
    42: "Evergreen Forest",
    43: "Mixed Forest",
    52: "Shrub/Scrub",
    71: "Grassland/Herbaceous",
    81: "Pasture/Hay",
    82: "Cultivated Crops",
    90: "Woody Wetlands",
    95: "Emergent Herbaceous Wetlands"
}

# Open raster file
with rasterio.open("Land Cover Code Analysis\waukesha_land_cover_2023.tif") as src:
    print("File opened.")
    raster = src.read(1) # first row
    pixel_size = src.res[0] * src.res[1] # width*height
    crs_units = src.crs.linear_units

# Remove pixels with no data
raster = raster[raster != src.nodata]

# Count each land cover class
unique, counts = np.unique(raster, return_counts=True)
landcover_counts = dict(zip(unique, counts))
print("Land cover classes counted.")

# Convert to area
def pixel_area(count):
    sq_meters = count * pixel_size
    hectares = sq_meters / 10_000
    acres = sq_meters * 0.000247105
    return hectares, acres

# Summary table
rows = []
for code, count in landcover_counts.items():
    hectares, acres = pixel_area(count)
    rows.append({
        "Code": code,
        "Class": nlcd_classes.get(code, "Unknown"),
        "Pixels": count,
        "Hectares": round(hectares, 2),
        "Acres": round(acres, 2)
    })
print("Table generated.")

# Final DataFrame
df = pd.DataFrame(rows)
df = df.sort_values(by="Pixels", ascending=False)
print(df)

# Save to CSV
df.to_csv("waukesha_summary_table_2023.csv", index=False)
print("Data saved.")