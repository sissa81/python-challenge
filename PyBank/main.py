# Modules
import os
import csv

# Starting count for profits and months
total_profits = 0
number_months = 0

# Create new list
profits_list = []
change_profits_list = []

# Path to collect budget data
budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    # Account for header row
    csvheader = next (csvfile)
          
    # Loop to total profits / months 
    for row in csvreader:
        profits_list.append(int(row[1]))
        total_profits += int(row[1])
        number_months += 1

    # Loop to calculate change in profits
    for i in range(1, 86):
        change = profits_list[i] - profits_list[i-1]
        change_profits_list.append(change)

    # Variables to calcuate average change in profits          
    Total_change = sum(change_profits_list)
    Number_Change = len(change_profits_list)
    Average_change = "${:,.2f}".format(Total_change/Number_Change)
    
    
    print(Average_change)

    







    # Print Analysis
    # print(f"Financial Analysis\n-----------------------------\nTotal Months: {number_months}\nTotal: ${total_profits}")


