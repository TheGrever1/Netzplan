import csv, os

with open(os.path.join("source", "input_n.csv"), newline="") as csvfile:
    inputnachfolger = csv.reader(csvfile, delimiter=";", quotechar="|")
    for row in inputnachfolger:
        print(", ".join(row))

print()
print()

with open(os.path.join("source", "input_v.csv"), newline="") as csvfile:
    inputvorgaenger = csv.reader(csvfile, delimiter=";", quotechar="|")
    for row in inputvorgaenger:
        print(", ".join(row))
