import pandas as pd
import matplotlib.pyplot as plt

df_2003 = pd.read_csv("Land Cover Code Analysis\waukesha_summary_table_2003.csv")
df_2023 = pd.read_csv("Land Cover Code Analysis\waukesha_summary_table_2023.csv")

developed_codes = [21, 22, 23, 24]
developed_acres_2003 = 0
developed_acres_2023 = 0

# Total up developed acres
def total_developed_acres(dataset, total):
    for index, row in dataset.iterrows():
        if (row["Code"] in developed_codes):
            acres = row["Acres"]
            total += acres
    return total

developed_acres_2003 = total_developed_acres(df_2003, developed_acres_2003)
developed_acres_2023 = total_developed_acres(df_2023, developed_acres_2023)

print("2003:", developed_acres_2003)
print("2023:", developed_acres_2023)
print("Difference:", developed_acres_2023 - developed_acres_2003)