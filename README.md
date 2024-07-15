# python-challenge
Module 3 Challenge
PyBank 

This Python script analyzes financial data from a CSV file (budget_data.csv). It calculates the following metrics:

Total number of months included in the dataset
Net total amount of "Profit/Losses" over the entire period
Average of the changes in "Profit/Losses" over the entire period
Greatest increase in profits (date and amount) over the entire period
Greatest decrease in losses (date and amount) over the entire period

I used the below relative path for the CSV file:
csvpath = os.path.join(r"C:\Users\nirav\Desktop\Data Analytics Bootcamp 06.20.2024\Bootcamp_Khushboo\UTOR-VIRT-DATA-PT-06-2024-U-LOLC\03-Python\3\Activities\PyBank\Resources", "budget_data.csv")

The below code was not working for me for CSV path
csvpath = os.path.join('Resources', 'budget_data.csv')

Output:

PyBank_Final_Results.txt: Text file generated by main.py containing the financial analysis results.


This Python script (main.py) analyzes election data from a CSV file (election_data.csv). It calculates the following metrics:

Total number of votes cast
Number of votes and percentage of total votes each candidate received
Winner of the election based on popular vote

I used the below relative path for the CSV file:
csvpath = os.path.join(r"C:\Users\nirav\Desktop\Data Analytics Bootcamp 06.20.2024\Bootcamp_Khushboo\UTOR-VIRT-DATA-PT-06-2024-U-LOLC\03-Python\3\Activities\PyPoll\Resources", "election_data.csv")

The below code was not working for me for CSV path
csvpath = os.path.join('Resources', 'election_data.csv')

Output:

PyPoll_FinalResults.txt: Text file generated by main.py containing the election analysis results, including total votes, votes per candidate, percentages, and the winner.