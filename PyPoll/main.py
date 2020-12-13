import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources','election_data.csv')

# Save the output file path
output_file = os.path.join("analysis.txt")

# Path to output
output_file =os.path.join("analysis.txt")

#Read data
with open(csvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

 # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

# Create a Python script that analyzes the records:
    counter=0
    sum=0
    candidates=[]
    poll_data=[]

# The total number of months included in the dataset
    for row in csvreader:
        counter=counter+1
        poll_data.append(row[1])

# A complete list of candidates who received votes
    candidates=[]
    for row in csvreader:
        Candidate.add(row[1])


print(counter)
print(candidates)