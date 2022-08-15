# The data we need to retrieve.
# 1. The total number of votes coasters
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Declare a new list for candidate options
candidate_options = []

# Declare a dictionary for each candidate's votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1

        # Assign the variable to the current row's candidate
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
           
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # Determine the percenage of votes for each candidate by looping through the counts.
    # Interate through the candidates list.
    for candidate_name in candidate_options:

        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of votes.
        voter_percentage = float(votes) / float(total_votes) * 100

        # Print the candidate name, vote count, and percentage of votes.
        print(f"{candidate_name}: {voter_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (voter_percentage > winning_percentage):

            # If true then set winning_count equal to votes and winning_percentage to voter_percentage
            winning_count = votes
            winning_percentage = voter_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)