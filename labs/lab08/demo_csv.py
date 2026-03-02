import csv

f = open("labs/lab08/data/students.csv", "r", newline="")
reader = csv.reader(f)

content = []
for row in reader:
    content.append(row)

f.close()
print(content)