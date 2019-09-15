<<<<<<< HEAD
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
duplicateVotes = []

with open (file_path,'r') as csvfile:
    csvdata = csv.reader(csvfile, delimiter = ',')
    
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
print('Total Votes:  + str(nVotes)')
print('-----------------------------------------------')
for k,v in candidates.items():
    print(k + ': ' + str(round((100*v/nVotes),2)) + '% (' + str(v) +')')
    print('-------------------------------------------')
    print('Winner:' + winner')
    print('-------------------------------------------')
    #Print to text file
=======
#create a Python script that analyzes the votes 

#Import libraries
import os
import csv
import sys

#open and read csv file
file_path = os.path.join("Resources", "election_data.csv")

#Variables to envoke
voters = []
candidates = {}
nVotes = 0
duplicateVotes = []

with open (file_path,'r') as csvfile:
    csvdata = csv.reader(csvfile, delimiter = ',')
    
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
print('Total Votes:  + str(nVotes)')
print('-----------------------------------------------')
for k,v in candidates.items():
    print(k + ': ' + str(round((100*v/nVotes),2)) + '% (' + str(v) +')')
    print('-------------------------------------------')
    print('Winner:' + winner')
    print('-------------------------------------------')
    #Print to text file
>>>>>>> e94cab48d942374b1e808ec8855411882489498a
