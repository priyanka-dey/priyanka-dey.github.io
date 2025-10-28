import matplotlib.pyplot as plt
import numpy as np

# Data
countries = ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]

metrics_wasserstein = {
    "BFI": [0.65, 0.58, 0.60, 0.56, 0.82],
    "IPIP-120": [0.63, 0.56, 0.58, 0.55, 0.71],
    "IPIP-300": [0.62, 0.55, 0.57, 0.54, 0.70],
    "TRAIT": [0.69, 0.67, 0.73, 0.78, 0.92],
    "Big5Chat": [0.64, 0.67, 0.69, 0.75, 0.91],
    "CulturalPersonas (Ours)": [0.56, 0.50, 0.47, 0.48, 0.68],
}

metrics_ks = {
    "BFI": [0.33, 0.25, 0.38, 0.29, 0.34],
    "IPIP-120": [0.31, 0.33, 0.36, 0.33, 0.36],
    "IPIP-300": [0.30, 0.42, 0.35, 0.32, 0.37],
    "TRAIT": [0.36, 0.37, 0.39, 0.35, 0.42],
    "Big5Chat": [0.32, 0.34, 0.37, 0.43, 0.39],
    "CulturalPersonas (Ours)": [0.28, 0.31, 0.30, 0.24, 0.33],
}

# Plot setup
x = np.arange(len(countries))
width = 0.12

fig, ax1 = plt.subplots(figsize=(12, 4))
ax2 = ax1.twinx()

colors = {
    "BFI": "#d73027",
    "IPIP-120": "#3182bd",
    "IPIP-300": "#31a354",
    "TRAIT": "#9467bd",
    "Big5Chat": "#ff7f0e",
    "CulturalPersonas (Ours)": "#5bc0de",
}

patterns = {
    "TRAIT": "//",
    "Big5Chat": "\\\\",
    "CulturalPersonas (Ours)": "//",
}

# Light grey shading for alternating traits
for i in range(len(countries)):
    if i % 2 == 0:
        ax1.axvspan(i - 0.5, i + 0.5, color="lightgrey", alpha=0.15, zorder=0)

# Offsets for bars
offsets = np.linspace(-width * 2.5, width * 2.5, len(metrics_wasserstein))

# Draw bars
for i, (name, values) in enumerate(metrics_wasserstein.items()):
    ax1.bar(
        x + offsets[i],
        values,
        width,
        label=name,
        color=colors[name],
        edgecolor="black",
        hatch=patterns.get(name, ""),
        zorder=3,
    )

# === Move X-axis labels to top ===
ax1.xaxis.set_label_position("top")
ax1.xaxis.tick_top()
ax1.set_xlabel("Personality Traits", fontsize=13, fontweight="bold", labelpad=12)

ax1.set_xticks(x)
ax1.set_xticklabels(countries, fontsize=13, fontweight="bold")

# Y axes labels
ax1.set_ylabel("Wasserstein", fontsize=13)
ax2.set_ylabel("KS Statistic", fontsize=13)

# Axis limits
ax1.set_ylim(0.2, 1.0)
ax2.set_ylim(0.1, 0.5)

# Clean up spines (no border box)
for spine in ["top", "right"]:
    ax2.spines[spine].set_visible(False)
ax1.spines["right"].set_visible(False)  # keep top visible since we use it for labels

# Tick marks
ax1.tick_params(axis="y", which="major", length=4, width=1, color="black", direction="out")
ax2.tick_params(axis="y", which="major", length=4, width=1, color="black", direction="out")
ax1.tick_params(axis="x", length=0)

# Vertical separators between traits
for i in range(len(countries) - 1):
    ax1.axvline(i + 0.5, color="black", linestyle="-", linewidth=0.5, alpha=0.5, zorder=2)

# Light horizontal gridlines
ax1.yaxis.grid(True, linestyle="-", linewidth=0.5, alpha=0.3)
ax2.yaxis.grid(False)

# Legends
psych_handles = [plt.Rectangle((0, 0), 1, 1, color=colors[k]) for k in ["IPIP-120", "IPIP-300", "BFI"]]
llm_handles = [plt.Rectangle((0, 0), 1, 1, color=colors[k], hatch=patterns.get(k, "")) for k in ["TRAIT", "Big5Chat", "CulturalPersonas (Ours)"]]

legend1 = ax1.legend(
    psych_handles,
    ["IPIP-120", "IPIP-300", "BFI"],
    title="Psychometric Tests :",
    loc="lower left",
    bbox_to_anchor=(0.05, -0.35),
    ncol=3,
    frameon=False,
)
legend2 = ax1.legend(
    llm_handles,
    ["TRAIT", "Big5Chat", "CulturalPersonas (Ours)"],
    title="LLM Benchmarks :",
    loc="lower right",
    bbox_to_anchor=(1.0, -0.35),
    ncol=3,
    frameon=False,
)
ax1.add_artist(legend1)

plt.tight_layout()
plt.subplots_adjust(bottom=0.3, top=0.85)
plt.savefig("plot4_topxlabel.png", dpi=300, bbox_inches="tight")
plt.show()
