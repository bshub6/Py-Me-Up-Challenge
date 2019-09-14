
#Import libaries
import os
import csv

#open and read csv
file_path = os.path.join("Resources","budget_data.csv")

#total month needs to be set to zero
totalMonths = 0
totalRev = 0
pastRev= 0
highestIncRev= 0
lowestDecRev = 99999999999

#create lists for revenue change
revChange = []

#Read budget_data.csv file
with open (file_path,'r') as csvfile:
   csvdata = csv.reader(csvfile, delimiter = ',')
   
#print (csv_file)
next(csvdata, None)

   
#Creating for loop for variables and count calculations
for row in csvdata:
        totalMonths = totalMonths + 1
        #count total revenue
        totalRev = totalRev + (int(row[1]))
        #create variable to count revenue change
        monthlyrevChange = int(row[1]) - pastRev
        pastRev = int(row[1])
        #add change to new list
        revChange.append(monthlyrevChange) 
        avgrevChange = round(sum(revChange)/totalMonths)
        
        #Find the greatest increase and decrease in Revenue
        if (monthlyrevChange > highestIncRev):
             highestIncMonth = row[0]
             highestIncRev = monthlyrevChange
             
if (monthlyrevChange < lowestDecRev):
               lowestDecMonth = row[0]
               lowestDecRev = monthlyrevChange
               
                
#Print the Financial Analysis Results with f strings to format
print("Financial Analysis")
print("------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${totalRev}")
print(f"Average Revenue Change: ${avgrevChange}")
print(f"Greatest Increase in Revenue: {highestIncMonth} (${highestIncRev})")
print(f"Greatest Decrease in Revenue: {lowestDecMonth} (${lowestDecRev})")

   
#write output file to export results into text file
with open("Financial_Analysis.txt", "w") as file:
     file.write("Financial Analysis")
     file.write("------------------")  
     file.write(f"Total Months: {totalMonths}")
     file.write(f"Average Revenue Change: ${avgrevChange}") 
     file.write(f"Greatest Increase in Revenue: {highestIncMonth} (${highestIncRev})") 
     file.write(f"Greatest Decrease in Revenue: {lowestDecMonth} (${lowestDecRev})")  
     
     #close the file written to
     file.close    
   
