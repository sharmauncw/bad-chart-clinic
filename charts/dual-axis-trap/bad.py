"""DELIBERATELY BAD: dual axes with an inverted scale.

Applications (left axis) and admit rate (right axis) are plotted together,
but the right axis is INVERTED (65 at the bottom, 45 at the top), so the two
lines cross dramatically and look causally linked — "applications soar as
standards collapse!" In reality the axes were chosen to manufacture the
crossing. See teaching-note.md and fixed.py.
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

fig, ax1 = plt.subplots(figsize=(9, 5))
ax1.plot(years, applications, color="tab:blue", marker="o", linewidth=3,
         label="Applications")
ax1.set_ylabel("Applications", color="tab:blue", fontsize=11)
ax1.set_ylim(11500, 15500)
ax1.tick_params(axis="y", labelcolor="tab:blue")

ax2 = ax1.twinx()
ax2.plot(years, admit_rate, color="tab:red", marker="s", linewidth=3,
         label="Admit rate")
ax2.set_ylabel("Admit rate (%)", color="tab:red", fontsize=11)
ax2.set_ylim(65, 45)  # <-- THE SIN: inverted second axis
ax2.tick_params(axis="y", labelcolor="tab:red")

ax1.set_xlabel("Year")
ax1.set_title("Applications SOAR as Standards COLLAPSE!",
              fontsize=14, fontweight="bold")
fig.text(0.5, 0.01, "Source: synthetic demo data", ha="center",
         fontsize=8, style="italic")
fig.savefig(os.path.join(HERE, "bad.png"), dpi=150, bbox_inches="tight")
print("saved", os.path.join(HERE, "bad.png"))
