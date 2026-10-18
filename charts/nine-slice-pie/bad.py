"""DELIBERATELY BAD: pie chart with 9 slices.

Nine slices means five of them are slivers, the labels collide into an
unreadable heap, and the reader can't compare anything smaller than the top
two. See teaching-note.md and fixed.py.
All data is synthetic, invented for teaching.
"""
import matplotlib
matplotlib.use("Agg")  # headless-safe
import matplotlib.pyplot as plt
import os

HERE = os.path.dirname(os.path.abspath(__file__))

categories = ["Grants", "Tuition", "Housing", "Dining", "Fees",
              "Bookstore", "Parking", "Events", "Other"]
amounts = [22, 18, 15, 12, 9, 8, 6, 5, 5]  # synthetic demo data

fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(amounts, labels=categories, autopct="%1.0f%%",  # <-- THE SIN: 9 slices
       colors=plt.cm.tab20.colors, textprops={"fontsize": 8},
       wedgeprops={"edgecolor": "white"})
ax.set_title("Where Does the Money Go? (Good Luck Reading This)",
             fontsize=13, fontweight="bold")
fig.text(0.5, 0.01, "Source: synthetic demo data", ha="center",
         fontsize=8, style="italic")
fig.savefig(os.path.join(HERE, "bad.png"), dpi=150, bbox_inches="tight")
print("saved", os.path.join(HERE, "bad.png"))
