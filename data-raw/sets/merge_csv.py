#!/usr/bin/env python3
import csv, glob, os

# ——— CONFIGURATION ———
input_dir   = "."            # where your 1970.csv … 2025.csv live
output_file = "merged.csv"   # name of the merged result
# ————————————————————

# 1) Gather and sort the list of CSV files
csv_files = sorted(glob.glob(os.path.join(input_dir, "*.csv")))

# 2) Build the superset of all headers (preserve first-seen order)
superset = []
for path in csv_files:
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        try:
            hdr = next(reader)
        except StopIteration:
            continue
        for col in hdr:
            if col not in superset:
                superset.append(col)

# 3) Write merged.csv with the combined header
with open(output_file, "w", newline="", encoding="utf-8") as out_f:
    writer = csv.DictWriter(out_f, fieldnames=superset)
    writer.writeheader()

    # 4) For each file: read rows as dicts and dump them
    for path in csv_files:
        with open(path, newline="", encoding="utf-8") as in_f:
            reader = csv.DictReader(in_f)
            for row in reader:
                # missing keys → blank fields
                writer.writerow(row)

print(f"Merged {len(csv_files)} files into {output_file}")
