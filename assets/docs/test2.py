import matplotlib.pyplot as plt
import numpy as np

# Data for the plot (approximate values from the image)
countries = ['Brazil', 'India', 'Japan', 'USA', 'Saudi Arabia', 'South Africa']

# Psychometric Tests (Wasserstein - left y-axis)
ipip_120 = [0.72, 0.68, 0.69, 0.70, 0.72, 0.69]
ipip_300 = [0.69, 0.68, 0.73, 0.71, 0.71, 0.67]
bfi = [0.69, 0.68, 0.65, 0.67, 0.69, 0.71]

# LLM Benchmarks
# TRAIT and Big5Chat (Wasserstein - left y-axis)
trait = [0.78, 0.83, 0.85, 0.75, 0.76, 0.79]
big5chat = [0.75, 0.79, 0.82, 0.83, 0.76, 0.84]

# CulturalPersonas (KS Statistic - right y-axis)
cultural_personas = [0.24, 0.25, 0.23, 0.24, 0.22, 0.22]

# Set up the figure with subplots
fig, axes = plt.subplots(1, 6, figsize=(16, 4), sharey='row')
fig.subplots_adjust(wspace=0.3)

# Bar width and positions
bar_width = 0.13
x = np.arange(1)

# Colors
colors = {
    'IPIP-120': '#5B8DB8',
    'IPIP-300': '#6BAB6F',
    'BFI': '#C85756',
    'TRAIT': '#8B5BA8',
    'Big5Chat': '#E87D3E',
    'CulturalPersonas': '#50B5B5'
}

# Hatching patterns
hatches = {
    'TRAIT': '///',
    'Big5Chat': '///',
    'CulturalPersonas': None
}

for idx, (ax, country) in enumerate(zip(axes, countries)):
    # Create twin axis for KS Statistic
    ax2 = ax.twinx()
    
    # Plot psychometric tests
    positions = [x[0] - 2*bar_width, x[0] - bar_width, x[0]]
    ax.bar(positions[0], bfi[idx], bar_width, color=colors['BFI'], label='BFI')
    ax.bar(positions[1], ipip_120[idx], bar_width, color=colors['IPIP-120'], label='IPIP-120')
    ax.bar(positions[2], ipip_300[idx], bar_width, color=colors['IPIP-300'], label='IPIP-300')
    
    # Plot LLM benchmarks
    positions_llm = [x[0] + bar_width, x[0] + 2*bar_width, x[0] + 3*bar_width]
    ax.bar(positions_llm[0], trait[idx], bar_width, color=colors['TRAIT'], 
           hatch=hatches['TRAIT'], edgecolor='black', linewidth=0.5, label='TRAIT')
    ax.bar(positions_llm[1], big5chat[idx], bar_width, color=colors['Big5Chat'], 
           hatch=hatches['Big5Chat'], edgecolor='black', linewidth=0.5, label='Big5Chat')
    ax2.bar(positions_llm[2], cultural_personas[idx], bar_width, color=colors['CulturalPersonas'], 
            label='CulturalPersonas (Ours)')
    
    # Formatting
    ax.set_xlim(-0.35, 0.55)
    ax.set_ylim(0.4, 0.9)
    ax2.set_ylim(0.10, 0.40)
    
    ax.set_xticks([])
    ax.set_title(country, fontsize=13, fontweight='bold', pad=10)
    
    # Only show y-axis labels on leftmost and rightmost plots
    if idx == 0:
        ax.set_ylabel('Wasserstein', fontsize=11)
        ax.tick_params(axis='y', labelsize=9)
    else:
        ax.set_yticklabels([])
    
    if idx == 5:
        ax2.set_ylabel('KS Statistic', fontsize=11)
        ax2.tick_params(axis='y', labelsize=9)
    else:
        ax2.set_yticklabels([])
    
    # Grid
    ax.grid(axis='y', alpha=0.3, linestyle='-', linewidth=0.5)
    ax.set_axisbelow(True)

# Add left side labels
fig.text(0.02, 0.85, '1: Diverging\n    Dists.', fontsize=10, fontweight='bold', 
         color='#C85756', ha='left', va='top')
fig.text(0.02, 0.20, '0: Identical\n    Dists.', fontsize=10, fontweight='bold', 
         color='#6BAB6F', ha='left', va='bottom')

# Add vertical arrow
arrow = plt.annotate('', xy=(0.015, 0.25), xytext=(0.015, 0.80),
                     xycoords='figure fraction', textcoords='figure fraction',
                     arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))

# Create custom legend
legend_elements = [
    plt.Rectangle((0, 0), 1, 1, fc=colors['IPIP-120'], label='IPIP-120'),
    plt.Rectangle((0, 0), 1, 1, fc=colors['IPIP-300'], label='IPIP-300'),
    plt.Rectangle((0, 0), 1, 1, fc=colors['BFI'], label='BFI'),
    plt.Rectangle((0, 0), 1, 1, fc=colors['TRAIT'], hatch='///', 
                  edgecolor='black', linewidth=0.5, label='TRAIT'),
    plt.Rectangle((0, 0), 1, 1, fc=colors['Big5Chat'], hatch='///', 
                  edgecolor='black', linewidth=0.5, label='Big5Chat'),
    plt.Rectangle((0, 0), 1, 1, fc=colors['CulturalPersonas'], label='CulturalPersonas (Ours)')
]

# Position legend at the bottom
fig.legend(handles=legend_elements, 
          loc='lower center', 
          bbox_to_anchor=(0.5, -0.08),
          ncol=6,
          frameon=False,
          fontsize=10,
          columnspacing=1.5)

# Add section labels above legend
fig.text(0.28, -0.02, 'Psychometric Tests:', fontsize=10, fontweight='bold', 
         ha='right', va='center', transform=fig.transFigure)
fig.text(0.72, -0.02, 'LLM Benchmarks:', fontsize=10, fontweight='bold', 
         ha='right', va='center', transform=fig.transFigure)

plt.tight_layout(rect=[0.04, 0.05, 1, 1])
plt.savefig("test.png", dpi=200)
