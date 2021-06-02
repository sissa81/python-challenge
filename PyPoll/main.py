# Modules
import os
import csv

# Creating starting point for total votes & candidates
Total_Votes = 0
candidate_count = 0

# Create list for Candidate Rows
candidate_list = []
candidate1_votes = []


# Path to collect budget data
votes_csv = os.path.join("Resources", "election_data.csv")

# Read in the csv file
with open(votes_csv) as csvfile:

    # split data by commas
    csvreader = csv.reader(csvfile, delimiter=",")

    # read header
    csvheader = next (csvfile)

    # create list of candidates (including dupes) and total votes
    for row in csvreader:
        candidate_list.append(row[2])
        Total_Votes += 1
           
    # create list of unique candidate names
    candidate_list_unique = list(set(candidate_list))

    # count number of candidate
    for candidate in candidate_list_unique:
        candidate_count += 1
    
    # candidates as variables
    for i in range(0,20):
        if candidate_list[i] == candidate_list_unique[3]:
            candidate1_votes += 1
            
    print(candidate_list[0])
    print(candidate_list_unique[3])
    print(candidate1_votes)




    # print(candidate_list_unique[1])


    

        

    




    
    


# ctr = 0
# for record in my_reader:
#     if record[1] == 'A':
#         ctr += 1
# print(ctr)

    
    
   


