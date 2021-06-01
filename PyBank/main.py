# Modules
import os
import csv

# starting count for profits and months
total_profits = 0
number_months = 0
change_profits = 0
# Path to collect budget data
budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    # Account for header row
    csvheader = next (csvfile)
          
    # Loop to total profits and months
    for row in csvreader:
        total_profits += int(row[1])
        number_months += 1

        print(change_profits)
    # Print Analysis
    # print(f"Financial Analysis\n-----------------------------\nTotal Months: {number_months}\nTotal: {total_profits}")



    
        
# average = (total_profits) / (value)
# print (average)

    # Calc average
            

        
# with open(csvpath, "r") as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


