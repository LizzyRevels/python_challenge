import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources','election_data.csv')

# Save the output file path
output_file = os.path.join("analysis.txt")

# Read data
with open(csvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

# Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

# Create a Python script that analyzes the records:
    counter=0
    vote_counts=[]
    

# The total number of votes included in the dataset
    for row in csvreader:
        counter=counter+1
        vote_counts.append(row[2])

    total_votes = len(vote_counts)   
    print(counter)
    candidates = set(vote_counts)
    print(candidates)

# A complete list of candidates who received votes
    Khan_votes = vote_counts.count("Khan")
    Khan_percent = (Khan_votes/total_votes) * 100
    print(Khan_percent) 
    print(Khan_votes)
    
    Correy_votes = vote_counts.count("Correy")
    Correy_percent = (Correy_votes/total_votes) * 100
    print(Correy_percent) 
    print(Correy_votes)

    Li_votes = vote_counts.count("Li")
    Li_percent = (Li_votes/total_votes) * 100
    print(Li_percent) 
    print(Li_votes)

    OTooley_votes = vote_counts.count("O'Tooley")
    OTooley_percent = (OTooley_votes/total_votes) * 100
    print(OTooley_percent) 
    print(OTooley_votes)  
    
    # The winner of the election based on popular vote.
    max_votes=max({Khan_votes} , {Correy_votes} , {Li_percent} , {OTooley_votes})
    print(max_votes)

# export to text file
with open(output_file, "w", newline='') as textfile:
    textfile.write("Election Results\n")
    textfile.write("-------------------\n")
    textfile.write(f'Total Votes: {counter}\n')
    textfile.write("-------------------\n")
    textfile.write(f'Khan: {round(Khan_percent)}% {Khan_votes}\n')
    textfile.write(f'Correy: {round(Correy_percent)}% {Correy_votes}\n')
    textfile.write(f'Li: {round(Li_percent)}% {Li_votes}\n')
    textfile.write(f'O\'Tooley: {round(OTooley_percent)}% {OTooley_votes}\n')
    textfile.write("-------------------\n")
    textfile.write(f'Winner: Khan')
    # textfile.write(f'Winner':{x})
   