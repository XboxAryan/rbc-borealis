"""Post-survey correlation and subgroup analysis.

Run from repo root:
    python3 cnib/data/analyze_survey.py

Source: cnib/data/post-survey-responses.csv (33 of 55 learners, anonymous).
Schema: cnib/data/post-survey-schema.csv.

Stdlib only — no pandas/numpy/scipy. Kept intentionally flat so the team can
read the analysis linearly alongside the numbers.
"""

import csv
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

CSV_PATH = Path(__file__).parent / "post-survey-responses.csv"

CONF = {"Not at all confident": 0, "Somewhat confident": 1,
        "Very confident": 2, "Extremely confident": 3}
LEC = {"Not very effective": 0, "Somewhat effective": 1, "Very effective": 2}
LAB = {"Not effective at all": 0, "Not very effective": 1,
       "Somewhat effective": 2, "Very effective": 3}
HW = {"Not at all": 0, "Not really": 1, "Somewhat": 2, "Yes, definitely": 3}
PRAC = {"Never": 0, "Rarely": 1, "Several times a week": 2, "Daily": 3}


def load():
    with open(CSV_PATH, newline="", encoding="utf-8", errors="replace") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [r for r in reader if any(c.strip() for c in r)]

    def find(substr):
        for i, h in enumerate(header):
            if substr.lower() in h.lower():
                return i
        raise KeyError(substr)

    idx = {
        "id": find("ID"),
        "completed": find("entire 6 week"),
        "conf": find("more confident"),
        "lec": find("morning lectures"),
        "lab": find("afternoon labs"),
        "hw": find("homework assignments"),
        "prac": find("practice using"),
    }

    def m(mapping, v):
        return mapping.get(v.strip() if v else "", None)

    data = []
    for r in rows:
        data.append({
            "id": r[idx["id"]].strip(),
            "completed": r[idx["completed"]].strip(),
            "conf": m(CONF, r[idx["conf"]]),
            "lec": m(LEC, r[idx["lec"]]),
            "lab": m(LAB, r[idx["lab"]]),
            "hw": m(HW, r[idx["hw"]]),
            "prac": m(PRAC, r[idx["prac"]]),
        })
    return data


def pearson(xs, ys):
    pairs = [(x, y) for x, y in zip(xs, ys) if x is not None and y is not None]
    if len(pairs) < 3:
        return None, 0
    xs, ys = zip(*pairs)
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = sum((x - mx) ** 2 for x in xs) ** 0.5
    dy = sum((y - my) ** 2 for y in ys) ** 0.5
    if dx == 0 or dy == 0:
        return None, n
    return num / (dx * dy), n


def spearman(xs, ys):
    pairs = [(x, y) for x, y in zip(xs, ys) if x is not None and y is not None]
    if len(pairs) < 3:
        return None, 0
    xs, ys = zip(*pairs)

    def rank(vs):
        s = sorted(enumerate(vs), key=lambda t: t[1])
        ranks = [0.0] * len(vs)
        i = 0
        while i < len(s):
            j = i
            while j + 1 < len(s) and s[j + 1][1] == s[i][1]:
                j += 1
            avg = (i + j) / 2 + 1
            for k in range(i, j + 1):
                ranks[s[k][0]] = avg
            i = j + 1
        return ranks

    return pearson(rank(xs), rank(ys))


def section(title):
    print(f"\n--- {title} ---")


def main():
    data = load()
    print(f"N={len(data)}  "
          f"completed_yes={sum(1 for d in data if d['completed']=='Yes')}  "
          f"completed_no={sum(1 for d in data if d['completed']=='No')}")

    section("Spearman rho across ordinal columns")
    cols = [("conf", "Confidence"), ("lec", "Lectures"),
            ("lab", "Labs"), ("hw", "Homework"), ("prac", "Practice")]
    for (a, la), (b, lb) in combinations(cols, 2):
        rho, n = spearman([d[a] for d in data], [d[b] for d in data])
        rstr = f"{rho:+.3f}" if rho is not None else "  n/a"
        print(f"  {la:12s} ~ {lb:12s}  rho={rstr}  n={n}")

    section("Confidence by completion")
    for c in ["Yes", "No"]:
        sub = [d["conf"] for d in data
               if d["completed"] == c and d["conf"] is not None]
        print(f"  completed={c}  mean_conf={sum(sub)/len(sub):.2f}  n={len(sub)}")

    section("Practice by completion")
    for c in ["Yes", "No"]:
        sub = [d["prac"] for d in data
               if d["completed"] == c and d["prac"] is not None]
        print(f"  completed={c}  mean_prac={sum(sub)/len(sub):.2f}  n={len(sub)}")

    section("Practice x Homework crosstab")
    hw_cols = ["Not at all", "Not really", "Somewhat", "Yes, definitely"]
    xtab = defaultdict(Counter)
    for d in data:
        if d["prac"] is not None and d["hw"] is not None:
            pl = next(k for k, v in PRAC.items() if v == d["prac"])
            hl = next(k for k, v in HW.items() if v == d["hw"])
            xtab[pl][hl] += 1
    print(f"  {'Practice':<22} " + " ".join(f"{c[:8]:>9}" for c in hw_cols) + "   total")
    for pl in ["Daily", "Several times a week", "Rarely", "Never"]:
        row = xtab.get(pl, Counter())
        print(f"  {pl:<22} "
              + " ".join(f"{row[c]:>9d}" for c in hw_cols)
              + f"   {sum(row.values())}")

    section("Bottom-raters overlap")
    bl = {d["id"] for d in data if d["lab"] is not None and d["lab"] <= 1}
    bh = {d["id"] for d in data if d["hw"] is not None and d["hw"] <= 1}
    ble = {d["id"] for d in data if d["lec"] is not None and d["lec"] <= 0}
    print(f"  bottom labs ({len(bl)}): {sorted(bl, key=int)}")
    print(f"  bottom hw   ({len(bh)}): {sorted(bh, key=int)}")
    print(f"  bottom lec  ({len(ble)}): {sorted(ble, key=int)}")
    print(f"  labs∩hw: {sorted(bl & bh, key=int)}  "
          f"labs∩lec: {sorted(bl & ble, key=int)}  "
          f"hw∩lec: {sorted(bh & ble, key=int)}")
    print(f"  all three: {sorted(bl & bh & ble, key=int)}")

    section("Risk subgroup intersections")
    lowconf = {d["id"] for d in data
               if d["conf"] is not None and d["conf"] <= 1}
    lowprac = {d["id"] for d in data
               if d["prac"] is not None and d["prac"] <= 1}
    noncomp = {d["id"] for d in data if d["completed"] == "No"}
    print(f"  lowConf n={len(lowconf)}: {sorted(lowconf, key=int)}")
    print(f"  lowPrac n={len(lowprac)}: {sorted(lowprac, key=int)}")
    print(f"  noncomp n={len(noncomp)}: {sorted(noncomp, key=int)}")
    print(f"  lowConf ∩ noncomp: {sorted(lowconf & noncomp, key=int)}")
    print(f"  lowPrac ∩ noncomp: {sorted(lowprac & noncomp, key=int)}")
    print(f"  lowConf ∩ lowPrac: {sorted(lowconf & lowprac, key=int)}")
    print(f"  all three:         {sorted(lowconf & lowprac & noncomp, key=int)}")

    section("Confidence distribution by Practice bucket")
    for pv in [3, 2, 1, 0]:
        label = next(k for k, v in PRAC.items() if v == pv)
        sub = [d["conf"] for d in data
               if d["prac"] == pv and d["conf"] is not None]
        if sub:
            print(f"  practice={label:<22} mean_conf={sum(sub)/len(sub):.2f} "
                  f"n={len(sub)}  dist={dict(Counter(sub))}")

    section("2x2: completion x practice")
    def cell(cond):
        return sum(1 for d in data if cond(d))
    yes_ade = cell(lambda d: d["completed"] == "Yes"
                   and d["prac"] is not None and d["prac"] >= 2)
    yes_low = cell(lambda d: d["completed"] == "Yes"
                   and d["prac"] is not None and d["prac"] <= 1)
    no_ade = cell(lambda d: d["completed"] == "No"
                  and d["prac"] is not None and d["prac"] >= 2)
    no_low = cell(lambda d: d["completed"] == "No"
                  and d["prac"] is not None and d["prac"] <= 1)
    print("               lowPrac  adequatePrac")
    print(f"  completed=Yes:   {yes_low:3d}       {yes_ade:3d}")
    print(f"  completed=No:    {no_low:3d}       {no_ade:3d}")
    if all([yes_ade, yes_low, no_ade, no_low]):
        odds = (yes_ade * no_low) / (yes_low * no_ade)
        print(f"  odds ratio (adequate vs low practice -> completion): {odds:.2f}")


if __name__ == "__main__":
    main()
