import os
import csv

# Path to the CSV file
csvpath = os.path.join(r"C:\Users\nirav\Desktop\Data Analytics Bootcamp 06.20.2024\Bootcamp_Khushboo\UTOR-VIRT-DATA-PT-06-2024-U-LOLC\03-Python\3\Activities\PyBank\Resources", "budget_data.csv")

# Initialize variables for calculations
total_months = 0
net_profit_loss = 0
greatest_increase = float('-inf')
greatest_increase_month = ""
greatest_decrease = float('inf')
greatest_decrease_month = ""
previous_month_profit = 0
total_change_profits = 0

# Read the CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    csv_header = next(csvreader)
    
    # Loop through rows in the CSV
    for row in csvreader:
        # Extract month and profit/loss from the row
        month = row[0]
        profit_loss = int(row[1])
        
        # Calculate total months
        total_months += 1
        
        # Calculate net total amount of "Profit/Losses" over the entire period
        net_profit_loss += profit_loss
        
        # Calculate change in profit/loss from previous month to current month
        if total_months > 1:  # skip calculation for the first month
            change = profit_loss - previous_month_profit
            total_change_profits += change
            
            # Determine greatest increase in profits (date and amount)
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = month
            
            # Determine greatest decrease in losses (date and amount)
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = month
        
        # Store current month profit/loss for next iteration
        previous_month_profit = profit_loss

# Calculate the average of the changes in "Profit/Losses" over the entire period
average_change = total_change_profits / (total_months - 1)


# Specify the output file path
output_file = os.path.join(r"C:\Users\nirav\Desktop\Data Analytics Bootcamp 06.20.2024\Bootcamp_Khushboo\UTOR-VIRT-DATA-PT-06-2024-U-LOLC\03-Python\2\Activities\12-Stu_CensusZip\Resources", "PyBank_Final_Results.txt")

# Write Financial Analysis to the text file
with open(output_file, 'w', encoding='utf-8') as txt:
    txt.write("Financial Analysis\n")
    txt.write("----------------------------\n")
    txt.write(f"Total Months: {total_months}\n")
    txt.write(f"Total: ${net_profit_loss}\n")
    txt.write(f"Average Change: ${average_change:.2f}\n")
    txt.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txt.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

# Print Financial Analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")