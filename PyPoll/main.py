# Import os module
import os

# CSV file
import csv

# Reading CSV file
csv_path = os.path.join('PyPoll', 'Resources', 'election_data.csv')

with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    print(csv_reader)

    csv_header = next(csv_reader)

# Setting lists for candidates, number of votes and percentage of votes
    candidates = []
    number_votes = []
    percentage_votes = []
# Setting counter for the total number of votes
    total_votes = 0
    for row in csv_reader:
        total_votes += 1
# Check if the candidate is part of the list, if not add his/her name along with a vote  
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_index = candidates.index(row[2])
            number_votes.append(1)
       
# If candidate exists than just add a vote to his/her name
        else:
            candidate_index = candidates.index(row[2])
            number_votes[candidate_index] += 1
# Calculate percentage then add it to the percentage votes list
    for votes in number_votes:
        percentage = (votes / total_votes)
        percentage = "{:.3%}".format(percentage)
        percentage_votes.append(percentage)

    winner = max(number_votes)
    winner_index = number_votes.index(winner)
    winning_candidate = candidates[winner_index]
    
# Find the winner
    print("Election Results")
    print("--------------")
    print(f"Total Votes: {total_votes}")
    print("--------------")

    for i in range(len(candidates)):
        print(f"{candidates[i]}: {percentage_votes[i]} ({number_votes[i]})")
    print("---------------")
    print(f"Winner: {winning_candidate}")
    print("---------------")

output = os.path.join("PyPoll", "output.txt")

with open(output, "w") as file:
    line1 = "Election Results\n"
    line2 = "---------------------\n"
    line3 = f"Total Votes: {total_votes}\n"
    line4 = "----------------------\n"
    file.writelines([line1, line2, line3, line4])

    for i in range(len(candidates)):
        file.write(f"{candidates[i]}: {percentage_votes[i]} ({number_votes[i]})\n")

    line5 = "-----------------------\n"
    line6 = f"Winner: {winning_candidate}\n"
    line7 = "------------------------\n"
    file.writelines([line5, line6, line7])


