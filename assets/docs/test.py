import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap

# -----------------------------
# Data
# -----------------------------
countries = ["BR", "IN", "US", "JP", "SA", "ZA"]

TRAIT = np.array([
    [0.65, 0.67, 0.64, 0.80, 0.66],
    [0.68, 0.75, 0.62, 0.61, 0.65],
    [0.70, 0.74, 0.80, 0.76, 0.75],
    [0.69, 0.71, 0.73, 0.68, 0.66],
    [0.68, 0.70, 0.72, 0.73, 0.66],
    [0.67, 0.66, 0.71, 0.68, 0.66],
])

Big5Chat = np.array([
    [0.74, 0.78, 0.65, 0.63, 0.67],
    [0.66, 0.70, 0.68, 0.66, 0.66],
    [0.72, 0.70, 0.68, 0.72, 0.74],
    [0.69, 0.72, 0.71, 0.73, 0.64],
    [0.71, 0.73, 0.75, 0.68, 0.64],
    [0.69, 0.71, 0.73, 0.68, 0.68],
])

CulturalPersonas = np.array([
    [0.74, 0.75, 0.78, 0.72, 0.73],
    [0.73, 0.72, 0.72, 0.71, 0.70],
    [0.78, 0.74, 0.73, 0.78, 0.78],
    [0.78, 0.72, 0.74, 0.70, 0.68],
    [0.70, 0.72, 0.70, 0.71, 0.68],
    [0.70, 0.71, 0.73, 0.72, 0.73],
])

# -----------------------------
# Compute Δ values
# -----------------------------
delta_trait = CulturalPersonas.mean(axis=1) - TRAIT.mean(axis=1)
delta_big5 = CulturalPersonas.mean(axis=1) - Big5Chat.mean(axis=1)

data = pd.DataFrame(
    [delta_trait, delta_big5],
    index=["Δ CulturalPersonas–TRAIT", "Δ CulturalPersonas–Big5Chat"],
    columns=countries
)

# -----------------------------
# Custom gray → green colormap
# -----------------------------
gray_to_green = LinearSegmentedColormap.from_list(
    "gray_to_green", ["#E0E0E0", "#B7E1B0", "#4DAF4A"]
)

# -----------------------------
# Plot
# -----------------------------
plt.figure(figsize=(8, 2.5))
sns.heatmap(
    data,
    annot=True,
    cmap=gray_to_green,
    linewidths=0.4,
    alpha=0.9,
    fmt=".2f",
    cbar_kws={'label': 'Δ Lexical Diversity (TTR)'},
)

plt.title("Increase in Lexical Diversity (Type-Token Ratio)", fontsize=12, pad=10)
plt.xlabel("Country", fontsize=10)
plt.ylabel("")
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.savefig("test.png", dpi=200)

