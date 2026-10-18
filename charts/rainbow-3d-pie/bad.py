"""DELIBERATELY BAD: rainbow 3D pie with exploded slices.

A rainbow palette, a fake-3D base layer, and exploded slices all conspire to
make the biggest slice look even bigger (the front-bottom wedge is visually
inflated by the perspective trick) while the small slices become unreadable
slivers. See teaching-note.md and fixed.py.
All data is synthetic, invented for teaching.
"""
import matplotlib
matplotlib.use("Agg")  # headless-safe
import matplotlib.pyplot as plt
import numpy as np
import os

HERE = os.path.dirname(os.path.abspath(__file__))

programs = ["Data Science", "Cybersecurity", "Psychology",
            "Biology", "Business", "English"]
shares = [28, 22, 18, 14, 10, 8]  # synthetic demo data


def darken(rgba, factor=0.45):
    r, g, b, a = rgba
    return (r * factor, g * factor, b * factor, a)


rainbow = plt.cm.rainbow(np.linspace(0, 1, len(shares)))  # <-- garish palette

fig, ax = plt.subplots(figsize=(8, 6))
# "3D" base: the same pie in darkened shades, shifted down for fake depth
base, _ = ax.pie(shares, colors=[darken(c) for c in rainbow],
                 startangle=90, counterclock=False)
for wedge in base:
    cx, cy = wedge.center
    wedge.set_center((cx, cy - 0.22))
# top layer: exploded, with shouty percentage labels
ax.pie(shares, colors=rainbow, startangle=90, counterclock=False,
       explode=[0.07] * len(shares), autopct="%1.0f%%", pctdistance=0.8,
       textprops={"fontsize": 10, "weight": "bold"})
ax.set_ylim(-1.5, 1.35)
ax.set_title("Data Science DOMINATES Enrollment!", fontsize=14, fontweight="bold")
ax.legend(programs, loc="center left", bbox_to_anchor=(1, 0.5), fontsize=9)
fig.text(0.5, 0.01, "Source: synthetic demo data", ha="center",
         fontsize=8, style="italic")
fig.savefig(os.path.join(HERE, "bad.png"), dpi=150, bbox_inches="tight")
print("saved", os.path.join(HERE, "bad.png"))
