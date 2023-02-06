# Election Audit

### Purpose
The purpose of this election analysis audit was the take a csv file with over a million pieces of data, process the information by writing scripts containing for loops and if statements, and return the results in an easily readable text file.

### Resources
- Data Source: election_results.csv
- Software: Python 3.7, Visual Studio Code

## Results
The analysis of the election show that:
- There were 369,711 votes cast in the election.

- The counties were:
  - Jefferson
  - Denver
  - Arapahoe
 
- The county results were:
  - Jefferson represented 10.5% of the votes, with 38,855 votes.
  - Denver represented 82.8% of the votes, with 306,055 votes.
  - Arapahoe represented 6.7% of the votes, with 24,801 votes.
 
- Largest County Turnout:
  - Denver, who accounted for 82.8% of the precinct's votes, with 306,055 votes.

- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane

- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.

- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 votes.

When printed as a text file the results will look like the following:
![Election_Results_Image](https://user-images.githubusercontent.com/109091887/185178775-307c094f-8869-4ebc-a9cc-8a00996256a0.PNG)

## Summary
The election commission will be pleased to know that the script that was written for this election audit can be easily adapted to future elections. A few key factors should be noted though. It is important to format any future election csv files the same as this election so that the script will be able to read and produce accurate results. When assigning the variable candidate_name, we use the index of the column. `candidate_name = row[2]` Since the candidates' names are in the third column, which corresponds to the index 2, we know the code is correctly assigning the variable. That being said, it would be possible to modify the code to account for columns being in different positions by changing the index of the list to match the corresponding column. 

Two other modifications that should be made are specifying the name of the election csv file. For instance, when writing the code to load the file from a path, we used:
`file_to_load = os.path.join("election_results.csv")`
If the new election results file is given the same name, this will result in the code reading this election's results, and not the results of the future election you are auditing. This will also be the case when saving our results to a text file. The following code is use to create a variable to save the file to a path: `file_to_save = os.path.join("analysis", "election_analysis.txt")`
If 'election_analysis.txt' is used again, when the code is run it will print over the results from the original election audit. It is best practice to use unique file names.
