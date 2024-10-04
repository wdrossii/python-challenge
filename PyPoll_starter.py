# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
#DR_this is the count of the ballot_id - do I need to check for duplicates?

# Define lists and dictionaries to track candidate names and vote counts
#DR_separate varable for each county/candidate combination (similar to a pivot table in excel) to accumulate and hold the count of votes for each combination
ca_stoc = 0
ca_dege = 0
ca_doan = 0
co_arap = 0
co_denv = 0
co_jeff = 0

# Winning Candidate and Winning Count Tracker

#DR_maximum of ca_ variables is winner.

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

        # Skip the header row
    header = next(reader)
    record = {reader}
    ballotid = (record[:7])
    County = (record[8:18]) #DR_ records show counties have lengths of 6, 7, and 8 - don't know how to flex it.
    Candidate = (record[19:])

    # Loop through each row of the dataset and process it
    for row in reader:
        if Candidate == "Charles Casper Stockham":
            ca_stoc = ca_stoc + 1
        elif Candidate == "Diana DeGette":
            ca_dege = ca_dege + 1
        elif Candidate == "Raymond Anthony Doane":
            ca_doan = ca_doan + 1
        else:
            break  #DR_ add candiate - either log the errors or give user opportunity to add value to Candidate variable
    row = row + 1
        
        #DR_Evaluate and count each combination accumulating it in it's variable

        # Print a loading indicator (for large datasets)
        #DR_print(". ", end="")
        #DR_???

        # Increment the total vote count for each row
        #DR_ move row by row

        # Get the candidate's name from the row
        #DR_    name is a new variable to be used to validate if name exists - should probably show up earlier in the routine

        # If the candidate is not already in the candidate list, add them

        #DR_    check if name variable exists or not. add variable if not.

        # Add a vote to the candidate's count
        #DR_   ca_stoc
        #DR_   ca_dege
        #DR_   ca_doan

# Open a text file to save the output
    with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
        print(ca_dege)
        print(ca_doan)
        print(ca_stoc)
        print(co_arap + co_denv + co_jeff)  #command of sum of the ca_* variables

    # Write the total vote count to the text file
    #DR_    write to text file

    # Loop through the candidates to determine vote percentages and identify the winner
    #DR_    ?Percentages of what, candidate/total, votes counted/total?

        # Get the vote count and calculate the percentage
    #DR_    ?Percentages of what, candidate/total, votes counted/total?

        # Update the winning candidate if this one has more votes
    #DR_    Print leader to terminal - is this good enough?

        # Print and save each candidate's vote count and percentage
    #DR_    ?Percentages of what, candidate/total, votes counted/total? -- print to file

    # Generate and print the winning candidate summary
    #DR_    ?Percentages of what, candidate/total, votes counted/total? -- print only winning candiated information to terminal

    # Save the winning candidate summary to the text file