import csv
from collections import Counter
import os

with open('election_data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)

    total_votes = 0
    candidates = []

    for row in csv_reader:

        total_votes += 1

        candidates.append(row['Candidate'])

    candidate_votes = Counter(candidates)

    percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

    winner = max(candidate_votes, key=candidate_votes.get)

    print("Election Results")
    print("----------------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------------")
    for candidate, votes in candidate_votes.items():
            print(f"{candidate}: {percentages[candidate]:.3f}% ({votes})")
    print("----------------------------------")
    print(f"Winner: {winner}")
    print("----------------------------------")
