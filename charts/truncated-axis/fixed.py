"""FIXED: the same data with an honest axis.

Bars start at zero, the palette is calm, the title describes instead of
shouts, and an annotation reports what the data actually says: the spread
across colleges is 2.1 percentage points.
All data is synthetic, invented for teaching.
"""
import matplotlib
matplotlib.use("Agg")  # headless-safe
import matplotlib.pyplot as plt
import os

HERE = os.path.dirname(os.path.abspath(__file__))

colleges = ["Arts", "Business", "Education", "Nursing", "Sciences"]
retention = [78.2, 79.1, 78.8, 80.3, 79.5]  # synthetic demo data

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(colleges, retention, color="#0f766e")
ax.set_ylim(0, 100)  # <-- THE FIX: bars start at zero
ax.set_ylabel("First-year retention rate (%)")
ax.set_title("First-Year Retention by College (Synthetic Data)", fontsize=13)
for bar, val in zip(bars, retention):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1.2,
            f"{val}%", ha="center", fontsize=10)
ax.annotate("Spread across colleges: 2.1 pts",
            xy=(3, 80.3), xytext=(1.2, 92),
            arrowprops=dict(arrowstyle="->", color="black"),
            fontsize=10, ha="center",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray"))
fig.text(0.5, 0.01, "Source: synthetic demo data", ha="center",
         fontsize=8, style="italic")
fig.savefig(os.path.join(HERE, "fixed.png"), dpi=150, bbox_inches="tight")
print("saved", os.path.join(HERE, "fixed.png"))
