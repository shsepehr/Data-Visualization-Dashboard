
"""

@author: Sepehr
"""



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ------------------------------
# 1️⃣ Load CSV dataset
# ------------------------------
csv_file = "sample_data.csv"  # Input File name
df = pd.read_csv(csv_file)

# ------------------------------
# 2️⃣ Create output folder
# ------------------------------
output_folder = "plots"
os.makedirs(output_folder, exist_ok=True)

# ------------------------------
# 3️⃣ Identify numeric columns
# ------------------------------
numeric_cols = df.select_dtypes(include="number").columns

if len(numeric_cols) == 0:
    print("No numeric columns found in CSV.")
else:
    # ------------------------------
    # 4️⃣ Generate histograms for each numeric column
    # ------------------------------
    for col in numeric_cols:
        plt.figure(figsize=(6,4))
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        
        # ------------------------------
        # 5️⃣ Save each plot as PNG
        # ------------------------------
        file_path = os.path.join(output_folder, f"{col}_hist.png")
        plt.savefig(file_path)
        plt.close()  # Close figure to free memory
        print(f"Saved plot: {file_path}")

print(f"All plots saved in folder '{output_folder}'")
