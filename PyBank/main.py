# Modules
import os
import csv

# Starting count for and months
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
          
    # Loop to append to profits list and to total profits / months 
    for row in csvreader:
        profits_list.append(int(row[1]))
        TotalProfits = "${:,.2f}".format(sum(profits_list))
        number_months += 1

    # Loop to calculate change in profits
    for i in range(1, 86):
        change = profits_list[i] - profits_list[i-1]
        change_profits_list.append(change)

    # Variables to calcuate average change in profits          
    Total_change = sum(change_profits_list)
    Number_Change = len(change_profits_list)
    Average_change = "${:,.2f}".format(Total_change/Number_Change)
    
    # Find the max and min in the change list
    max_change = "${:,.2f}".format(max(change_profits_list))   
    min_change = "${:,.2f}".format(min(change_profits_list))   




    







    # Print Analysis
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {number_months}")
print(f"Total: {TotalProfits}")
print(f"Average Change: {Average_change}")
print(f"Greatest Increase in Profits: {max_change}")
print(f"Greatest Increase in Profits: {min_change}")