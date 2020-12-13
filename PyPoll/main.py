import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources','election_data.csv')

# Save the output file path
output_file = os.path.join("analysis.txt")

# Path to output
output_file =os.path.join("analysis.txt")

# Read data
with open(csvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

# Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

# Create a Python script that analyzes the records:
    counter=0
    sum=0
    poll_data=[]

# The total number of votes included in the dataset
    for row in csvreader:
        counter=counter+1
        poll_data.append(row[1])

# A complete list of candidates who received votes
# I know I need to iterate through the names in the Candidate column (Index 2) and 
# count each occurrence of each unique name. Do I need to use if/elif/else? 
# JUST REALIZED -- The names are listed on the Homework instructions, so I could use 
# those names as a starting off point. I was looking through my classmates examples
# and not seeing their code on where they found the names. All the while the names
# are already given.

    candidates = []
    Khan = int()
    Correy = int()
    Li = int()
    OTooley = int()
    for x in csvreader:
        candidate.append(x[2])
        if x[2] == "Khan":
            Khan += 1
        if x[2] == "Correy":
            Correy += 1
        if x[2] == "Li":
            Li += 1
        if x[2] == "O'Tooley":
            OTooley += 1

    

# The percentage of votes each candidate won


print(counter)
print(candidates)

# #export to text file
with open(output_file, "w", newline='') as datafile:
    datafile.write("Election Results\n")
    datafile.write("-------------------\n")
    datafile.write(f'Total Votes:{counter}\n')
    datafile.write("-------------------\n")
    
   