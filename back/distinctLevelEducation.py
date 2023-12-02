import csv

CSV_FILE = 'StudentsPerformance.csv'

levels = set()

with open(CSV_FILE, encoding="utf-8-sig") as bitumen_csv:
    bitumen_reader = csv.DictReader(bitumen_csv)
    for port in bitumen_reader:
        levels.add(port['parental level of education'])

print(levels)