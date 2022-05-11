import csv, os

with open(os.path.join("source", "input_n.csv"), newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=";", quotechar="|")
    for row in csvreader:
        print(", ".join(row))
