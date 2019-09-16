#create a Python script that analyzes the votes 

#Import libraries

import os
import csv

#Create the path to file

file_path = os.path.join("Resources", "election_data.csv")

#Set Variables

all_candidates = []
vote_count = []

with open(file_path,'r') as csvfile:
    csvdata = csv.reader(csvfile, delimiter = ',')
    
    header = next(csvdata, None)
    
    #Creating If Else statment in for loop
    for row in csvdata:
        if row[2] not in all_candidates:
            all_candidates.append(row[2])
            vote_count.append(1)
        else:
            whatindex = all_candidates.index(row[2])
            vote_count[whatindex] += 1
            
  #Calculating the total vote and percentage counts          

    total_votes = sum(vote_count)

    votepercentage = [round(vote_count[i]/total_votes*100,4) for i in range(0,len(vote_count))]

    print("--------------------")
    print("| Election Results |")
    print("--------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------")
    
    for i in range(0,len(all_candidates)):
        print(f"Candidate: {all_candidates[i]} with {vote_count[i]} votes ({votepercentage[i]}%)")

    print("--------------------")
    print(f"The winner is: {all_candidates[vote_count.index(max(vote_count))]}")
    
    #Display and write results to text

    with open("Election Results.txt", "w") as text_file:
        print("--------------------", file=text_file)
        print("Election Results", file=text_file)
        print("--------------------", file=text_file)
        print(f"Total Votes: {total_votes}", file=text_file)
        print("--------------------", file=text_file)
        for i in range(0,len(all_candidates)):
            print(f"Candidate: {all_candidates[i]} with {vote_count[i]} votes ({votepercentage[i]}%)", file=text_file)
        print("--------------------", file=text_file)
        print(f"The winner is: {all_candidates[vote_count.index(max(vote_count))]}", file=text_file)

