import csv


import os
csvfile=os.path.join("budget_data.csv")

with open(csvfile, 'r') as datafile:


    csvreader = csv.reader(datafile, delimiter=',')

    csv_header = next(csvreader)

    count = 0
    for row in csvreader:
        count+=1
        print("Totalmonths:", count)

        


