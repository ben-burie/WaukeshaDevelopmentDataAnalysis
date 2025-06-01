import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import textwrap

df_change = pd.read_csv("Land Cover Code Analysis\waukesha_landcover_change_2003_2023.csv")

# Load nlcd class names
classes = []
for classType in df_change["Class"]:
    classes.append(classType)

# Load 2003 data
data_2003 = []
for value in df_change["Acres_2003"]:
    data_2003.append(value)

# Load 2023 data
data_2023 = []
for value in df_change["Acres_2023"]:
    data_2023.append(value)

# Set up graph size properties
bar_width = 0.35
x = np.arange(len(classes))

# Create bars
plt.bar(x - bar_width/2, data_2003, width=bar_width, color="blue", label="2003")
plt.bar(x + bar_width/2, data_2023, width=bar_width, color="red", label="2023")

# Add labels
wrapped_labels = ['\n'.join(textwrap.wrap(label, 11)) for label in classes]
plt.xlabel("NLCD Land Class")
plt.ylabel("Acres")
plt.title("Acres Divided by Land Code (2003-2023)")
plt.xticks(x, wrapped_labels)
plt.xticks(fontsize=8)
plt.legend()
plt.show()