# Modules
import os
import csv

# Create starting point for total months
Total_Months = 0

# Create new list
months_list = []
profits_list = []
change_profits_list = []

# Path to collect budget data
budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    # Account for header row
    csvheader = next (csvfile)
          
    # Loop to append to profits / months list and to total profits / months 
    for row in csvreader:
        profits_list.append(int(row[1]))
        Total_Profits = "${:,.2f}".format(sum(profits_list))
        months_list.append(row[0])
        Total_Months += 1
      
    # Loop to calculate change in profits
    for i in range(1, 86):
        change = profits_list[i] - profits_list[i-1]
        change_profits_list.append(change)

    # Variables to calcuate average change in profits          
    Total_change = sum(change_profits_list)
    Number_Change = len(change_profits_list)
    Average_change = "${:,.2f}".format(Total_change/Number_Change)
    
    # Find the max and min in the change list, one unformatted for index purposes
    max_change = "${:,.2f}".format(max(change_profits_list))   
    min_change = "${:,.2f}".format(min(change_profits_list))   

    max_change_for_index = max(change_profits_list)
    min_change_for_index = min(change_profits_list)

    # Find the max and min position of max and min changes
    max_index = change_profits_list.index(max_change_for_index)
    min_index = change_profits_list.index(min_change_for_index)
    
    # Find the max and min months
    max_month = months_list[max_index]
    min_month = months_list[min_index]
    
    


    # Print Analysis
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: {Total_Profits}")
print(f"Average Change: {Average_change}")
print(f"Greatest Increase in Profits: {max_month} {max_change}")
print(f"Greatest Increase in Profits: {min_month} {min_change}")