import pandas as pd

df_2003 = pd.read_csv("Land Cover Code Analysis\waukesha_summary_table_2003.csv")
df_2023 = pd.read_csv("Land Cover Code Analysis\waukesha_summary_table_2023.csv")

df_2003 = df_2003.rename(columns={
    "Hectares": "Hectares_2003",
    "Acres": "Acres_2003"
})

df_2023 = df_2023.rename(columns ={
    "Hectares": "Hectares_2023",
    "Acres": "Acres_2023"
})

# Merge the tables
merged = pd.merge(df_2003[["Code", "Class", "Hectares_2003", "Acres_2003"]],
                  df_2023[["Code", "Hectares_2023", "Acres_2023"]],
                  on="Code", how="outer")

# Calculate change
merged["Acres_Change"] = merged["Acres_2023"] - merged["Acres_2003"]
merged["Hectares_Change"] = merged["Hectares_2023"] - merged["Hectares_2003"]

# Sort
merged = merged.sort_values(by="Acres_Change", key=lambda x: abs(x), ascending=False)

merged.to_csv("waukesha_landcover_change_2003_2023.csv", index=False)