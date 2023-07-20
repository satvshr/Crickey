import csv
import time


def read_csv_file(csv_file_path):
    all_rows = []
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            all_rows.append(row)

    return all_rows

while(1):
    rowList = read_csv_file('liveScores.csv')
    # print(rowList)

    for row in rowList:
        if len(row) == 3:
            print(row[0],'\t', row[1])
        else:
            print(row[0], '\t\t',row[1])

    print('\n'+rowList[0][2])
    time.sleep(30)