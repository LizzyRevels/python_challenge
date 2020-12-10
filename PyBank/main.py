import os
import csv

# Specify the file to write to
output_path = os.path.join("Resources", "output", "output.txt")

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources','budget_data.csv')

# Save the output file path
output_file = os.path.join("output.txt")

# open the output file
# with open(output_file, "w", newline='') as datafile:
#     writer = csv.writer(datafile)

#     writer.writerow(["Total Months"])

#Read data
with open(csvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

 # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

# Create a Python script that analyzes the records:
    counter=0
    sum=0
    list_one=[]
    
 # Read each row of data after the header
    for row in csvreader:
        
        # The total number of months included in the dataset
        counter=counter+1
        list_one.append(row[1])

        # The net total amount of "Profit/Losses" over the entire period
        sum+=int(row[1])

        # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        # length = len(numbers)
        # total = 0.0
        # for number in numbers:
        #     total += number
        #     answer = total / length
        #     return total / length
        
        def average(list_one):
            length_list=len(list_one)
        
            for m in range(1, length_list):
                difference=(int(list_one[m])-int(list_one[m-1]))
        
        print(average(list_one))
            

    print(counter)
    print(list_one)
    print(sum)
    # print(sum/counter)

    # The greatest increase in profits (date and amount) over the entire period
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

    # The greatest decrease in losses (date and amount) over the entire period       
    for m in range(1, length_list):
        difference=(int(list_one[m])-int(list_one[m-1]))
        list_two.append(difference)
        if difference < max_decrease: 
            max_decrease=difference

    print(max_decrease)


