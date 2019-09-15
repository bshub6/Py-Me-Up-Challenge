#create a Python script that analyzes the votes 

#Import libraries
import os
import csv


#open and read csv file
file_path = os.path.join("Resources", "election_data.csv")

#Variables to envoke
voters = []
candidates = {}
nVotes = 0
duplicateVotes = 0

with open (file_path,'r') as csvfile:
    csvdata = csv.reader(csvfile, delimiter = ',')
    
    #No header
    next(csvdata, 'None')
    
    #Creating If Else statment in for loop
    for row in csvdata:
        if row[2] not in candidates.keys():
            candidates[row[2]] = 1
        else: 
            candidates[row[2]] += 1
        nVotes += 1
        
#calculate the winner of election
winner = max(candidates, key=candidates.get)

#Display elections results in terminal
print('Election Results')
print('----------------------------------------------')
print('Total Votes:'  + str(nVotes)')
print('-----------------------------------------------')
for k,v in candidates.items():
    print(k + ': ' + str(round((100*v/nVotes),2)) + '% (' + str(v) +')')
    print('-------------------------------------------')
    print('Winner:' + str(winner)')
    print('-------------------------------------------')
    #Print to text file
