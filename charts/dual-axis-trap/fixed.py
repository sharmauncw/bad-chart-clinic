"""FIXED: both series indexed to 100 in the base year, one axis.

Indexing removes the unit mismatch (headcount vs. percent) that the dual
axes exploited. Now the reader sees the honest story: applications grew
~20% while the admit rate fell ~23% — related, but no manufactured crossing.
All data is synthetic, invented for teaching.
"""
import matplotlib
matplotlib.use("Agg")  # headless-safe
import matplotlib.pyplot as plt
import os

HERE = os.path.dirname(os.path.abspath(__file__))

years = list(range(2018, 2027))
applications = [12400, 12800, 11900, 13100, 13800, 14200, 14700, 15100, 14900]
admit_rate = [62, 61, 64, 59, 57, 55, 52, 50, 48]  # synthetic demo data

apps_idx = [a / applications[0] * 100 for a in applications]
rate_idx = [r / admit_rate[0] * 100 for r in admit_rate]

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(years, apps_idx, marker="o", linewidth=2.5, label="Applications")
ax.plot(years, rate_idx, marker="s", linewidth=2.5, label="Admit rate")
ax.axhline(100, color="gray", linestyle="--", linewidth=1)
ax.set_ylabel("Index (2018 = 100)")
ax.set_xlabel("Year")
ax.set_title("Applications and Admit Rate, Indexed to 2018 (Synthetic Data)",
             fontsize=13)
ax.legend()
ax.annotate("Base year = 100", xy=(2018, 100), xytext=(2019.5, 112),
            arrowprops=dict(arrowstyle="->", color="gray"), fontsize=9,
            color="gray")
fig.text(0.5, 0.01, "Source: synthetic demo data", ha="center",
         fontsize=8, style="italic")
fig.savefig(os.path.join(HERE, "fixed.png"), dpi=150, bbox_inches="tight")
print("saved", os.path.join(HERE, "fixed.png"))
