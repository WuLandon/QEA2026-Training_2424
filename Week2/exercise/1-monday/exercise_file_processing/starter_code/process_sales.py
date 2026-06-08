"""
Week 2 Exercise — CSV processing with context managers.

TODO:
1. Read starter_code/data/sales.csv using csv.DictReader and with open(...).
2. Compute rows count, grand total (sum of units * unit_price), average line revenue.
3. Find SKU with max line revenue (tie: first in file).
4. Write output/summary.txt using with open(..., "w", encoding="utf-8").
"""

from __future__ import annotations

import csv
from pathlib import Path


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    sales_path = base_dir / "data" / "sales.csv"
    output_dir = base_dir / "output"
    output_path = output_dir / "summary.txt"

    total_rows = 0
    grand_total = 0.0
    max_rev = -1.0
    max_sku = ""

    with open(sales_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            try:
                units = int(row["units"])
                unit_price = float(row["unit_price"])
                sku = row["sku"]
            except (KeyError, TypeError, ValueError):
                continue

            revenue = units * unit_price

            total_rows += 1
            grand_total += revenue

            if revenue > max_rev:
                max_rev = revenue
                max_sku = sku

    avg_line_rev = grand_total / total_rows if total_rows else 0.0

    output_dir.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"rows={total_rows}\n")
        f.write(f"grand_total={grand_total:.2f}\n")
        f.write(f"average_line_revenue={avg_line_rev:.2f}\n")
        f.write(f"top_sku={max_sku}\n")
        f.write(f"top_line_revenue={max_rev:.2f}\n")


if __name__ == "__main__":
    main()
