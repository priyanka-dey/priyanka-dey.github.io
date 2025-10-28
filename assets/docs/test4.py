import matplotlib.pyplot as plt
import numpy as np

# Data
traits = ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]

metrics_wasserstein = {
    "TRAIT": [0.84, 0.86, 0.88, 0.85, 0.87],
    "Big5Chat": [0.82, 0.84, 0.85, 0.83, 0.85],
    "CulturalPersonas (Ours)": [0.74, 0.79, 0.75, 0.76, 0.80],
}

metrics_ks = {
    "TRAIT": [0.68, 0.69, 0.70, 0.69, 0.70],
    "Big5Chat": [0.67, 0.68, 0.69, 0.67, 0.68],
    "CulturalPersonas (Ours)": [0.63, 0.66, 0.63, 0.64, 0.64],
}

# Setup
x = np.arange(len(traits))
width = 0.22

fig, ax1 = plt.subplots(figsize=(10, 4))
ax2 = ax1.twinx()

colors = {
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
for i in range(len(traits)):
    if i % 2 == 0:
        ax1.axvspan(i - 0.5, i + 0.5, color='lightgrey', alpha=0.12, zorder=0)

# Plot bars
offsets = np.linspace(-width, width, len(metrics_wasserstein))
for i, (name, values) in enumerate(metrics_wasserstein.items()):
    ax1.bar(
        x + offsets[i],
        values,
        width,
        label=name,
        color=colors[name],
        edgecolor="black",
        hatch=patterns[name],
        zorder=3,
    )

# Axes setup
ax1.set_ylabel("Wasserstein", fontsize=12, fontweight='semibold')
ax2.set_ylabel("KS Statistic", fontsize=12, fontweight='semibold')

ax1.set_ylim(0.6, 0.95)
ax2.set_ylim(0.6, 0.72)

# Remove x-axis tick labels (we'll add titles above)
ax1.set_xticks([])
ax1.tick_params(axis="x", length=0)

# Remove extra spines
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

# Tick marks and grid
ax1.tick_params(axis="y", length=4, width=1, color="black", direction="out")
ax2.tick_params(axis="y", length=4, width=1, color="black", direction="out")
ax1.yaxis.grid(True, linestyle="-", linewidth=0.5, alpha=0.3)

# Vertical separators between traits
for i in range(len(traits) - 1):
    ax1.axvline(i + 0.5, color="black", linestyle="-", linewidth=0.5, alpha=0.4, zorder=2)

# === TOP LABELS (trait names above groups) ===
for i, label in enumerate(traits):
    ax1.text(
        i,  # x position (centered over group)
        0.96,  # just above the top limit
        label,
        ha="center",
        va="bottom",
        fontsize=12,
        fontweight="bold",
        transform=ax1.get_xaxis_transform(),
    )

# Legend: centered below plot
llm_handles = [
    plt.Rectangle((0, 0), 1, 1, color=colors[k], hatch=patterns[k], edgecolor="black")
    for k in metrics_wasserstein.keys()
]
legend = ax1.legend(
    llm_handles,
    list(metrics_wasserstein.keys()),
    title="LLM Benchmarks:",
    loc="upper center",
    bbox_to_anchor=(0.5, -0.25),
    ncol=3,
    frameon=False,
    fontsize=11,
    title_fontsize=11,
)

plt.tight_layout()
plt.subplots_adjust(bottom=0.3, top=0.85)
plt.savefig("plot_traits_toplabels.png", dpi=300, bbox_inches="tight")
plt.show()
