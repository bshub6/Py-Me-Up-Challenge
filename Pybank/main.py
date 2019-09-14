#Import libraries
import os
import csv

#open and read csv
budget_data = os.path.join("Resources","budget_data.csv")

#total month needs to be set to zero
total_month = 0
total_pl = 0
value = 0
change = []
dates = []
profits = []

#Read budget_data.csv file
with open (budget_data) as file :
   csv_file = csv.reader(file, delimiter = ",")
    #Reading header row
   csv_header = next(csv_file)
    
    #Creating for loop for calculations
   for row in csv_file:
        dates.append(row[0])
        change.append(int(row[1]) - value)
        profits.append(row[1])
        total_pl = total_pl + int(row[1])
        value = int(row[1])
        total_month += 1
       
    #Find the max and min revenue and associated dates   
   greatest_increase = max(change)
   greatest_index = change.index(greatest_increase)
   greatest_date = dates[greatest_index]
        
   greatest_decrease = min(change)
   worst_index = change.index(greatest_decrease)
   worst_date = dates[worst_index]
        
   avg_change = (sum(change)-change[0])/(len(change)-1)
        
        #Output Displayed
   print("Financial Analysis")
   print("------------------")
   print(f"Total Months: {str(total_month)}")
   print(f"Total: ${str(total_pl)}")
   print(f"Average Change: ${str(round(avg_change,2))}")
   print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
   print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

  #Copy to textfile
with open("Financial_analysis.text" , 'w+') as text:
     text.write("Financial Analysis\n"
                  "------------------\n" 
                  f"Total Months: {str(total_month)}\n"
                  f"Total: ${str(total_pl)}\n"
                  f"Average Change: ${str(round(avg_change,2))}\n" 
                  f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})\n" 
                  f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")  