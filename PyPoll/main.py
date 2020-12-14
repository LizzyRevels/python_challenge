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
        

# A complete list of candidates who received votes
    # print(vote_counts)
    Khan_votes = vote_counts.count("Khan")
    tota_votes = len(vote_counts)
    Khan_percent = (Khan_votes/tota_votes) * 100
    print(Khan_percent) 
    print(Khan_votes)
    candidates = set(vote_counts)
    print(candidates)

    # Khan = int()
    # Correy = int()
    # Li = int()
    # OTooley = int()
    # for x in csvreader:
    #     candidates.append(x[2])
    #     if x[2] == "Khan":
    #         Khan += 1
    #     if x[2] == "Correy":
    #         Correy += 1
    #     if x[2] == "Li":
    #         Li += 1
    #     if x[2] == "O'Tooley":
    #         OTooley += 1
        

# The percentage of votes each candidate won

    # candidates_set = (set(candidates))
    # Khan_percent = float(Khan/counter) * 100
    # Correy_percent = float(Correy/counter) 
    # Li_percent = float(Li/counter) * 100
    # OTooley_percent = float(OTooley/counter) * 100

    print(counter)
    

# export to text file
with open(output_file, "w", newline='') as textfile:
    textfile.write("Election Results\n")
    textfile.write("-------------------\n")
    textfile.write(f'Total Votes:{counter}\n')
    textfile.write("-------------------\n")
    # textfile.write(f'Khan:{Khan_percent}\n')
    # textfile.write(f'Correy:{Correy_percent}\n')
    # textfile.write(f'Li:{Li_percent}\n')
    # textfile.write(f'OTooley:{OTooley_percent}\n')
    # textfile.write(f'Winner':{x})
   