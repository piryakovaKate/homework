import csv

array = []
with open("table.csv", "r") as f:
    reader = csv.reader(f, delimiter = ';')
    for row in reader:
        array.append(row)


mid_point = len(array)//2
array = array[0:mid_point] + [[-200, -200, -200, -200]] + array[mid_point:]

with open('middle_row.csv', 'w') as f:
    writer = csv.writer(f, delimiter = ';')
    writer.writerows(array)
