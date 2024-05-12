import csv

file = open('Breast_Cancer.csv')
print(type(file))
csvreader = csv.reader(file)
header = []
header = next(csvreader)


rows = []
i = 0

for row in csvreader:
    rows.append(row)
    if (i > 20):
        break
    i += 1

print(type(rows[0][3]))