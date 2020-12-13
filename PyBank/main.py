import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources','budget_data.csv')

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
    profit_loss=[]
    # avg_change=[]
    
 # Read each row of data after the header
    for row in csvreader:
        
        # The total number of months included in the dataset
        counter=counter+1
        profit_loss.append(row[1])

        # The net total amount of "Profit/Losses" over the entire period
        sum+=int(row[1])

        # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        # for r in range(len(profit_loss)-1):
        #     avg_change.append(profit_loss)[r+1]-profit_loss[r]
            

    print(counter)
    print(profit_loss)
    print(sum)
    # print(avg_change)
   

    # The greatest increase in profits (date and amount) over the entire period
    length_list=len(profit_loss)
    list_two=[]
    max_increase=0
    max_decrease=0

    for m in range(1, length_list):
        difference=(int(profit_loss[m])-int(profit_loss[m-1]))
        list_two.append(difference)
        if difference > max_increase: 
            max_increase=difference

    print(max_increase)

    # The greatest decrease in losses (date and amount) over the entire period       
    for m in range(1, length_list):
        difference=(int(profit_loss[m])-int(profit_loss[m-1]))
        list_two.append(difference)
        if difference < max_decrease: 
            max_decrease=difference

    print(max_decrease)


# #export to text file
with open(output_file, "w", newline='') as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("-------------------\n")
    datafile.write(f'Greatest Decrease in Profits:{max_decrease}\n')
    datafile.write(f'Greatest Increase in Profits:{max_increase}\n')
    datafile.write(f'Total Months:{counter}\n')
    datafile.write(f'profit_loss:{profit_loss}\n')
    datafile.write(f'Total:{sum}\n')