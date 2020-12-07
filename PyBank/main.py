# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Specify the file to write to
output_path = os.path.join("Resources", "output", "results.csv")

csvpath = os.path.join('Resources','budget_data.csv')


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

def list_information(simple_list):
    print(f"The values within the list are...")
    for value in simple_list:
        print(value)
    print("The length of this list is... " + str(len(simple_list)))


