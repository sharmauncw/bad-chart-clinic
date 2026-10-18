"""FIXED: sorted horizontal bars, crumbs grouped into "Other".

With this many categories, bars beat pie: every value shares a baseline and
nothing overlaps. The four smallest slices are grouped so the chart stays
scannable. All data is synthetic, invented for teaching.
"""
import matplotlib
matplotlib.use("Agg")  # headless-safe
import matplotlib.pyplot as plt
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# smallest slices grouped for readability
categories = ["Grants", "Tuition", "Housing", "Dining", "Fees", "Other"]
amounts = [22, 18, 15, 12, 9, 8 + 6 + 5 + 5]  # synthetic demo data

order = sorted(range(len(amounts)), key=lambda i: amounts[i])
categories = [categories[i] for i in order]
amounts = [amounts[i] for i in order]

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(categories, amounts, color="#0f766e")
ax.set_xlabel("Share of revenue (%)")
ax.set_title("Revenue by Source (Synthetic Data)", fontsize=13)
for bar, val in zip(bars, amounts):
    ax.text(val + 0.4, bar.get_y() + bar.get_height() / 2,
            f"{val}%", va="center", fontsize=10)
ax.set_xlim(0, max(amounts) * 1.18)
fig.text(0.5, 0.01, "Source: synthetic demo data", ha="center",
         fontsize=8, style="italic")
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fixed.png"), dpi=150, bbox_inches="tight")
print("saved", os.path.join(HERE, "fixed.png"))
