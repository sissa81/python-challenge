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

    # Split data by commas
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read header
    csvheader = next (csvfile)

    # Create list of candidates (including dupes) and total votes
    for row in csvreader:
        candidate_list.append(row[2])
        Total_Votes += 1
           
    # Create a sorted list of unique candidate names
    candidate_list_unique = sorted(list(set(candidate_list)))
    # print(candidate_list_unique)
    # ['Correy', 'Khan', 'Li', "O'Tooley"]

    # Count votes per candidate        
    Correy_Count = candidate_list.count("Correy")
    Khan_Count = candidate_list.count("Khan")
    Li_Count = candidate_list.count("Li")
    OTooley_Count = candidate_list.count("O'Tooley")
    
    # Calculate percentages of votes
    Correy_percent = "{:.3%}".format(Correy_Count/Total_Votes)
    Khan_percent = "{:.3%}".format(Khan_Count/Total_Votes)    
    Li_percent = "{:.3%}".format(Li_Count/Total_Votes)
    OTooley_percent = "{:.3%}".format(OTooley_Count/Total_Votes)

    # Create list of candidate percentages
    candidate_percent_list = [Correy_percent,Khan_percent,Li_percent,OTooley_percent]

    # Create list of total votes by person
    candidate_vote_list = [Correy_Count,Khan_Count,Li_Count,OTooley_Count]
    
    # Find most votes
    most_votes = max(candidate_vote_list)
    
    # Find the position of the most votes
    most_votes_index = candidate_vote_list.index(most_votes)
    
    # Find the candiate with the most votes using the index of the count of most votes
    most_votes_candidate = candidate_list_unique[most_votes_index]
    
    # Print Analysis in Terminal
    print("Election Results")
    print("-----------------------------")
    print(f"{candidate_list_unique[0]}: {candidate_percent_list[0]} ({candidate_vote_list[0]})")
    print(f"{candidate_list_unique[1]}: {candidate_percent_list[1]} ({candidate_vote_list[1]})")
    print(f"{candidate_list_unique[2]}: {candidate_percent_list[2]} ({candidate_vote_list[2]})")
    print(f"{candidate_list_unique[3]}: {candidate_percent_list[3]} ({candidate_vote_list[3]})")
    print("-----------------------------")
    print(f"Winner: {most_votes_candidate}")
    print("-----------------------------")

    # # count number of candidate
    # for candidate in candidate_list_unique:
    #     candidate_count += 1
    
    # # candidates as variables
    # for i in range(0,20):
    #     if candidate_list[i] == candidate_list_unique[3]:
    #         candidate1_votes += 1
            
    # print(candidate_list[0])
    # print(candidate_list_unique[3])
    # print(candidate1_votes)




    # print(candidate_list_unique[1])


    

        

    




    
    


# ctr = 0
# for record in my_reader:
#     if record[1] == 'A':
#         ctr += 1
# print(ctr)

    
    
   


