import csv

array = []
with open("table.csv", "r") as f:
    reader = csv.reader(f, delimiter = ';')
    for row in reader:
        array.append(row)

array[0].append('my_col')
for i in range(1,len(array)-1):
    array[i].append(True)

with open("new_col.csv", "w") as f:
    writer = csv.writer(f, delimiter = ';')
    writer.writerows(array)
