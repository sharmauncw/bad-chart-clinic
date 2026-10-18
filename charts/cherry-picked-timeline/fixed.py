"""FIXED: the full 2012-2026 timeline.

The "skyrocket" is revealed as a recovery from a dip back to a long-run
plateau. The cherry-picked window is shaded — not hidden — so the reader can
see exactly what the bad version cropped out. All data is synthetic,
invented for teaching.
"""
import matplotlib
matplotlib.use("Agg")  # headless-safe
import matplotlib.pyplot as plt
import os

HERE = os.path.dirname(os.path.abspath(__file__))

years = list(range(2012, 2027))
grad_rate = [58.2, 58.9, 59.1, 58.4, 59.6, 59.0, 58.7, 59.3, 54.1,
             56.8, 59.4, 61.2, 60.8, 60.1, 59.9]  # synthetic demo data

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(years, grad_rate, color="#0f766e", marker="o", linewidth=2.5)
ax.axvspan(2020, 2023, color="orange", alpha=0.15)  # <-- the cropped window
ax.text(2021.5, 62.3, "window shown in\nthe 'bad' version", ha="center",
        fontsize=9, style="italic",
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray"))
ax.set_ylim(52, 64)
ax.set_ylabel("Six-year graduation rate (%)")
ax.set_title("Six-Year Graduation Rate, 2012-2026 (Synthetic Data)",
             fontsize=13)
ax.annotate("2020 dip", xy=(2020, 54.1), xytext=(2016.5, 55.5),
            arrowprops=dict(arrowstyle="->", color="black"), fontsize=9)
fig.text(0.5, 0.01, "Source: synthetic demo data", ha="center",
         fontsize=8, style="italic")
fig.savefig(os.path.join(HERE, "fixed.png"), dpi=150, bbox_inches="tight")
print("saved", os.path.join(HERE, "fixed.png"))
