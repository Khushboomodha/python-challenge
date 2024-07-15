import os
import csv
from collections import Counter

# Path to the CSV file
csvpath = os.path.join(r"C:\Users\nirav\Desktop\Data Analytics Bootcamp 06.20.2024\Bootcamp_Khushboo\UTOR-VIRT-DATA-PT-06-2024-U-LOLC\03-Python\3\Activities\PyPoll\Resources", "election_data.csv")

# Initialize variables to store data
votes = []
candidates = []

# Read the CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    csv_header = next(csvreader)
    
    # Loop through rows in the CSV
    for row in csvreader:
        # Append vote and candidate data
        votes.append(row[0])
        candidates.append(row[2])

# Calculate total number of votes
total_votes = len(votes)

# Count votes for each candidate using Counter from collections
candidate_count = Counter(candidates)

# Sort candidates by the number of votes received
sorted_candidates = sorted(candidate_count.items(), key=lambda x: x[1], reverse=True)

# Extract candidate names and vote counts from sorted list
candidate_names = [candidate[0] for candidate in sorted_candidates]
vote_counts = [candidate[1] for candidate in sorted_candidates]

# Calculate percentage of votes for each candidate
vote_percentages = [(votes / total_votes) * 100 for votes in vote_counts]

# Extract top three candidates (assuming there are at least three candidates)
first_place = candidate_names[0]
second_place = candidate_names[1]
third_place = candidate_names[2]

first_votes = vote_counts[0]
second_votes = vote_counts[1]
third_votes = vote_counts[2]

first_percent = vote_percentages[0]
second_percent = vote_percentages[1]
third_percent = vote_percentages[2]

# Determine the winner (candidate with the most votes)
winner = candidate_names[0]

# Print Election Results to console
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{first_place}: {first_percent:.3f}% ({first_votes})")
print(f"{second_place}: {second_percent:.3f}% ({second_votes})")
print(f"{third_place}: {third_percent:.3f}% ({third_votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Specify the output file path
export_path = os.path.join(r"C:\Users\nirav\Desktop\Data Analytics Bootcamp 06.20.2024\Bootcamp_Khushboo\UTOR-VIRT-DATA-PT-06-2024-U-LOLC\03-Python\3\Activities\PyPoll\Resources", "PyPoll_FinalResults.txt")

# Write Election Results to the text file
with open(export_path, 'w', newline='') as txt:
    txt.write("Election Results\n")
    txt.write("-------------------------\n")
    txt.write(f"Total Votes: {total_votes}\n")
    txt.write("-------------------------\n")
    txt.write(f"{first_place}: {first_percent:.3f}% ({first_votes})\n")
    txt.write(f"{second_place}: {second_percent:.3f}% ({second_votes})\n")
    txt.write(f"{third_place}: {third_percent:.3f}% ({third_votes})\n")
    txt.write("-------------------------\n")
    txt.write(f"Winner: {winner}\n")