# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Specify the file to write to
output_path = os.path.join("Resources", "output", "output.csv")

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources','budget_data.csv')

# save the output file path
output_file = os.path.join("output.txt")

# open the output file
# with open(output_file, "w", newline='') as datafile:
#     writer = csv.writer(datafile)

#     writer.writerow(["Total Months"])

#Read data
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

   
    counter=0
    sum=0
    list_one=[]
    

 # Read each row of data after the header
    for row in csvreader:
        counter=counter+1
        list_one.append(row [1])
        sum+=int(row[1])
        
    print(counter)
    print(list_one)
    print(sum)
    print(sum/counter)

    length_list=len(list_one)


    list_two=[]
    max_increase=0
    max_decrease=0

    for m in range(1, length_list):
        difference=(int(list_one[m])-int(list_one[m-1]))
        list_two.append(difference)
        if difference > max_increase: 
            max_increase=difference

    print(max_increase)
            
   for m in range(1, length_list):
        difference=(int(list_one[m])-int(list_one[m-1]))
        list_two.append(difference)
        if difference < max_decrease: 
            max_increase=difference


