import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvfile)
    
    data = list(csvreader)
    row_count = len(data)
    
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", row_count)
    
    date = []
    revenue = []
    revenue_change = []
    total = 0   
    
    for row in data:
        total += int(row[1])
        date.append(row[0])
        revenue.append(int(row[1]))

    print("Total Revenue: $", total) 
     
        
    for i in range(1,len(revenue)):
        revenue_change.append(revenue[i] - revenue[i-1])
        avg_rev_change = sum(revenue_change)/len(revenue_change)
        
        max_rev_change = max(revenue_change)
        max_rev_change_date = str(date[revenue_change.index(max(revenue_change))+1])
    
        min_rev_change = min(revenue_change)
        min_rev_change_date = str(date[revenue_change.index(min(revenue_change))+1])
        
    print("Avereage Change: $", round(avg_rev_change,2))        
    print("Greatest Increase in Profits:", max_rev_change_date, "($",  max_rev_change,")")
    print("Greatest Dncrease in losses:", min_rev_change_date, "($", min_rev_change,")")
    

    
output_path = os.path.join(".", "Financial Analysis.txt")
file = open("Financial Analysis.txt","w")

file.write("Financial Analysis" + "\n")
file.write("-----------------------------------" + "\n")
file.write("Total Months: " + repr(row_count) + "\n")
file.write("Total Revenue: $" + repr(total) + "\n")
file.write("Avereage Change: $" + repr(round(avg_rev_change,2)) + "\n")
file.write("Greatest Increase in Profits:" + str(max_rev_change_date) + "($" + repr(max_rev_change) + ")" + "\n")
file.write("Greatest Dncrease in losses:" + str(min_rev_change_date) + "($" + repr(min_rev_change) + ")" + "\n")
    
file.close()
    