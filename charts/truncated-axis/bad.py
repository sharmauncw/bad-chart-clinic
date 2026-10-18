"""DELIBERATELY BAD: bar chart with a truncated y-axis.

The differences between colleges are tiny (~2 points on a 0-100 scale), but
because the axis starts at 77 instead of 0, Nursing looks like it towers over
everyone else. See teaching-note.md and fixed.py.
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
bars = ax.bar(
    colleges, retention,
    color=["#e74c3c", "#e67e22", "#f1c40f", "#2ecc71", "#3498db"],
    edgecolor="black",
)
ax.set_ylim(77, 81)  # <-- THE SIN: truncated axis exaggerates tiny gaps
ax.set_ylabel("Retention rate (%)")
ax.set_title("Nursing CRUSHES Other Colleges in Retention!",
             fontsize=14, fontweight="bold")
for bar, val in zip(bars, retention):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05,
            f"{val}%", ha="center", fontsize=10, fontweight="bold")
fig.text(0.5, 0.01, "Source: synthetic demo data", ha="center",
         fontsize=8, style="italic")
fig.savefig(os.path.join(HERE, "bad.png"), dpi=150, bbox_inches="tight")
print("saved", os.path.join(HERE, "bad.png"))
