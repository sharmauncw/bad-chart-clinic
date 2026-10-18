"""DELIBERATELY BAD: area chart with the y-axis starting at 10,000.

Headcount drifts from ~10,200 to ~10,600 over a decade — a 3.9% change — but
with the axis starting at 10,000, the filled area balloons upward and the
growth looks explosive. Area charts are extra vulnerable to this because the
filled region reads as "amount", and truncating the axis inflates that
amount. See teaching-note.md and fixed.py.
All data is synthetic, invented for teaching.
"""
import matplotlib
matplotlib.use("Agg")  # headless-safe
import matplotlib.pyplot as plt
import os

HERE = os.path.dirname(os.path.abspath(__file__))

years = list(range(2016, 2027))
headcount = [10200, 10250, 10300, 10280, 10350, 10100,
             10200, 10300, 10400, 10500, 10600]  # synthetic demo data

fig, ax = plt.subplots(figsize=(9, 5))
ax.fill_between(years, headcount, 10000, color="#e74c3c", alpha=0.85)
ax.plot(years, headcount, color="#7b241c", linewidth=2)
ax.set_ylim(10000, 10700)  # <-- THE SIN: axis starts at 10,000
ax.set_xlim(2016, 2026)
ax.set_ylabel("Total headcount")
ax.set_title("Enrollment EXPLODES to Record Highs!", fontsize=14,
             fontweight="bold")
fig.text(0.5, 0.01, "Source: synthetic demo data", ha="center",
         fontsize=8, style="italic")
fig.savefig(os.path.join(HERE, "bad.png"), dpi=150, bbox_inches="tight")
print("saved", os.path.join(HERE, "bad.png"))
