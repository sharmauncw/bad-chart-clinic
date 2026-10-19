"""FIXED: the same area chart on a full zero-based axis.

Now the decade of enrollment reads the way the numbers read: steady, with a
dip and recovery, up 3.9% overall. The annotation reports the real change
instead of implying an explosion. All data is synthetic, invented for
teaching.
"""
import matplotlib
matplotlib.use("Agg")  # headless-safe
import matplotlib.pyplot as plt
import os

HERE = os.path.dirname(os.path.abspath(__file__))

years = list(range(2016, 2027))
headcount = [10200, 10250, 10300, 10280, 10350, 10100,
             10200, 10300, 10400, 10500, 10600]  # synthetic demo data

pct_change = (headcount[-1] - headcount[0]) / headcount[0] * 100

fig, ax = plt.subplots(figsize=(9, 5))
ax.fill_between(years, headcount, 0, color="#0f766e", alpha=0.35)
ax.plot(years, headcount, color="#0f766e", linewidth=2.5, marker="o",
        markersize=4)
ax.set_ylim(0, max(headcount) * 1.1)  # <-- THE FIX: full axis from zero
ax.set_xlim(2016, 2026)
ax.set_ylabel("Total Headcount")
ax.set_title("Total Headcount, 2016-2026 (Synthetic Data)", fontsize=13)
ax.annotate(f"+{pct_change:.1f}% over the decade",
            xy=(2026, 10600), xytext=(2021.5, 11000),
            arrowprops=dict(arrowstyle="->", color="black"),
            fontsize=10, ha="center",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray"))
fig.text(0.5, 0.01, "Source: synthetic demo data", ha="center",
         fontsize=8, style="italic")
fig.savefig(os.path.join(HERE, "fixed.png"), dpi=150, bbox_inches="tight")
print("saved", os.path.join(HERE, "fixed.png"))
