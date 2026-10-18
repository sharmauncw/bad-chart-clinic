# Bad Chart Clinic

A gallery of deliberately-bad charts — each paired with a fixed, honest version and a one-paragraph teaching note.

## The story

This repo is the companion to a real guest lecture: **"Data Visualization (Session 1)"**, taught on **October 14, 2026** in the **Program Evaluation** course (**EDL 586/686**) at the **Watson College of Education, UNC Wilmington**, at the invitation of **Dr. Satlaj Dighe**. The session's hands-on segment was a **"Bad Data Clinic"** activity: students diagnosed misleading charts, then repaired them. These six chart pairs are the take-home version of that activity.

All data in this repo is **synthetic demo data** — invented for teaching, not from any real institution.

## How to run

```bash
pip install -r requirements.txt
python charts/truncated-axis/bad.py    # saves charts/truncated-axis/bad.png
python charts/truncated-axis/fixed.py  # saves charts/truncated-axis/fixed.png
```

Every `bad.py` and `fixed.py` runs standalone (headless-safe via the Agg backend) and saves a PNG next to itself. Open `teaching-note.md` in each folder for the lesson.

## The six chart pairs

| # | Folder | The sin | The fix |
|---|--------|---------|---------|
| 1 | `truncated-axis` | Bar chart with y-axis starting at 77 — a 2-point gap looks like a landslide | Honest axis from 0; annotate the real 2.1-pt range |
| 2 | `rainbow-3d-pie` | Rainbow 3D pie with exploded slices — chartjunk that distorts proportions | Sorted horizontal bars in one calm color |
| 3 | `dual-axis-trap` | Dual axes with an inverted scale — two unrelated trends made to "cross" | Index both series to 100 in the base year on one axis |
| 4 | `nine-slice-pie` | Pie with 9 slices and overlapping labels — unreadable | Sorted horizontal bars; group crumbs into "Other" |
| 5 | `exaggerated-area` | Area chart with axis starting at 10,000 — flat growth looks explosive | Full axis from 0; report the actual +3.9% change |
| 6 | `cherry-picked-timeline` | Only the 2020–2023 V-shape is shown — a dip and rebound framed as a triumph | Full 2012–2026 timeline with the cherry-picked window shaded |

## The one rule of the clinic

> If the chart would change a decision, the chart must not lie. When in doubt: start bars at zero, keep one axis, sort your categories, and show the whole timeline.
