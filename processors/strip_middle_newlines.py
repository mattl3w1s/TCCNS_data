import sys
import csv

writer = csv.writer(sys.stdout)

for row in csv.reader(iter(sys.stdin.readline,'')):
    row = list(row)
    for i in range(len(row)):
        if('\n' in row[i]):
            row[i] = row[i].replace('\n',' ')
    writer.writerow(row)
