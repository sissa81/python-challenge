# Modules
import os
import csv

# Path to collect budget data
budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next (csvfile)
    # print(f"Header: {csvheader}")

    value = len(list(csvreader))
    print(f"Financial Analysis")
    print(f"-----------------------------")
    print(f"Total Months: {value}")

    
    # for row in csvreader:
    # print(row)
        
# with open(csvpath, "r") as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))
