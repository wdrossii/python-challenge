# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
date_beginning = 0
date_old = 0
date_new = 0
amt_beginning = 0 #DR_ watch this, need to pass beginning amount into this variable on first iteration, amt_new = amt_beginning before the loop begins but after the first values are read
amt_old = 0
amt_new = 0
month_old = str
month_new = str

# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    for row in reader:
        print(row)

    # Track the total and net change
    #DR_datebase = date data in row 1 and will not change
    date_beginning = #value at current position
    
    #DR_dateold = date data in row 1 and will refresh each iteration
    #DR_datenew = date data in row 2 and will refresh each iteration
    date_new = date_beginning

    #DR_dateold will be replaced by datenew at the end of each iteration
    date_old = date_new
    
        #DR_ Data must be sorted in order to get interim change
        #DR_ net change would be one figure to the next, right?
        #DR_ total change would be for the entire column?
        #DR_ need variables for date

    # Process each row of data
    for row in reader:
        #DR_amt_base = amount data in row 1 and will not change
        #DR_amt_old = amount data in row 1 and will refresh each iteration
        #DR_amt_new = amount data in row 2 and will refresh each iteration
        #DR_amt_old will be replaced with amtnew at the end of each iteration
        # Track the total
            #DR_this will be written to the file

        # Track the net change
        #DR_daily_change = amt_new - amt_old
        #DR_overall_change = amt_new + amt_base


        # Calculate the greatest increase in profits (month and amount)
        #DR_greatest_increase_overall = maximum of amt_new and amt_base for each iteration
        #DR_greatest_increase_month will require validating the month data from the date with an if statement, if month_new = month_old and amt_new > amt_base, update greatest_increase_overall 
        # DR_ELSE update greatest_increase_month - will need a variable for the beginning/base of each month
        
        # Calculate the greatest decrease in losses (month and amount)
        #DR_same as for greatest increase but less than rather than increases.



# Calculate the average net change across the months
    #DR_average(daily_change)

# Generate the output summary
    #DR_???

# Print the output
    #DR_print to file

# Write the results to a text file
#with open(file_to_output, "w") as txt_file:
#    txt_file.write(output)
