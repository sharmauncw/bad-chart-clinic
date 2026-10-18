"""DELIBERATELY BAD: cherry-picked timeline.

Only 2020-2023 is shown: the pandemic dip and the rebound become a dramatic
V-shape, framed as a triumph. The full 2012-2026 series (see fixed.py) shows
a decade of flat ~58-60% with that same dip as a blip. Choosing the window
is choosing the story. See teaching-note.md and fixed.py.
All data is synthetic, invented for teaching.
"""
import matplotlib
matplotlib.use("Agg")  # headless-safe
import matplotlib.pyplot as plt
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# <-- THE SIN: only the flattering window is shown
years = [2020, 2021, 2022, 2023]
grad_rate = [54.1, 56.8, 59.4, 61.2]  # synthetic demo data

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(years, grad_rate, color="#27ae60", marker="o", markersize=9,
        linewidth=4)
ax.fill_between(years, grad_rate, 54, color="#27ae60", alpha=0.25)
ax.set_ylim(53, 62)
ax.set_xlim(2020, 2023)
ax.set_ylabel("Six-year graduation rate (%)")
ax.set_title("Graduation Rates SKYROCKET Under New Plan!",
             fontsize=14, fontweight="bold")
ax.annotate("+7.1 pts in 3 years!", xy=(2023, 61.2), xytext=(2021.2, 60.8),
            arrowprops=dict(arrowstyle="->", color="black"),
            fontsize=11, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="orange"))
fig.text(0.5, 0.01, "Source: synthetic demo data", ha="center",
         fontsize=8, style="italic")
fig.savefig(os.path.join(HERE, "bad.png"), dpi=150, bbox_inches="tight")
print("saved", os.path.join(HERE, "bad.png"))
