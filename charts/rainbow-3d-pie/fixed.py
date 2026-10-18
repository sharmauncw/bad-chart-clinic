"""FIXED: the same shares as sorted horizontal bars.

One calm color, longest bar on top, values labeled at the bar ends. Every
slice is now comparable by length against a common baseline — no perspective
tricks, no rainbow. All data is synthetic, invented for teaching.
"""
import matplotlib
matplotlib.use("Agg")  # headless-safe
import matplotlib.pyplot as plt
import os

HERE = os.path.dirname(os.path.abspath(__file__))

programs = ["Data Science", "Cybersecurity", "Psychology",
            "Biology", "Business", "English"]
shares = [28, 22, 18, 14, 10, 8]  # synthetic demo data

order = sorted(range(len(shares)), key=lambda i: shares[i])
programs = [programs[i] for i in order]
shares = [shares[i] for i in order]

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(programs, shares, color="#0f766e")
ax.set_xlabel("Share of enrollment (%)")
ax.set_title("Enrollment Share by Program (Synthetic Data)", fontsize=13)
for bar, val in zip(bars, shares):
    ax.text(val + 0.4, bar.get_y() + bar.get_height() / 2,
            f"{val}%", va="center", fontsize=10)
ax.set_xlim(0, max(shares) * 1.15)
fig.text(0.5, 0.01, "Source: synthetic demo data", ha="center",
         fontsize=8, style="italic")
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fixed.png"), dpi=150, bbox_inches="tight")
print("saved", os.path.join(HERE, "fixed.png"))
