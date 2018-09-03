import os
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvfile)
    
    voter_id = []
    #county = []
    #candidate = []
    khan = 0
    correy = 0
    li = 0
    tooley = 0
    
    
    for row in csvreader:
        
        voter_id.append(row[0])
        total = len(voter_id)

        if row[2] == 'Khan':
            khan += 1
        elif row[2] == "Correy":
            correy += 1
        elif row[2] == "Li":
            li += 1
        elif row[2] == "O'Tooley":
            tooley += 1            
    
    print("Election Results")
    print("-----------------------------------")
    print("Total Votes:", total)
    print("-----------------------------------")
    
    khan_percent = round(khan/total*100, 4)
    correy_percent = round(correy/total*100, 4)
    li_percent = round(li/total*100, 4)
    tooley_percent = round(tooley/total*100, 4)
    
    percent = [khan_percent,correy_percent,li_percent,tooley_percent]
    name = ["Khan","Correy","Li","O'Tooley"]
    
    winner = name[percent.index(max(percent))]
    
    print("Khan:", khan_percent,"%","(",khan,")")
    print("Correy:", correy_percent,"%","(",correy,")")
    print("Li:", li_percent,"%","(",li,")")
    print("O'Tooley:", tooley_percent,"%","(",tooley,")")
    print("-----------------------------------")
    print("Winner:", winner)
    print("-----------------------------------")
    
    
output_path = os.path.join(".", "Election Results.txt")

with open(output_path, 'w') as text_file:
    print(f"Election Results", file = text_file)
    print(f"-----------------------------------", file = text_file)
    print(f"Total Votes: {total}", file = text_file)
    print(f"-----------------------------------", file = text_file)
    print(f"Khan: {khan_percent}% ({khan})", file = text_file)
    print(f"Correy: {correy_percent}% ({correy})", file = text_file)
    print(f"Li: {li_percent}% ({li})", file = text_file)
    print(f"O'Tooley: {tooley_percent}% ({tooley})", file = text_file)
    print(f"-----------------------------------", file = text_file)
    print(f"Winner: {winner}", file = text_file)
    print(f"-----------------------------------", file = text_file)    
