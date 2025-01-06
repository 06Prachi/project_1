from operator import itemgetter

# Data
party_names = [
    "Party A", "Party B", "Party A", "Party C", "Party B", "Party C",
    "Party A", "Party B", "Party C", "Party A"
]
candidate_names = [
    "Candidate 1", "Candidate 2", "Candidate 3", "Candidate 4",
    "Candidate 5", "Candidate 6", "Candidate 7", "Candidate 8",
    "Candidate 9", "Candidate 10"
]
votes_received = [1200, 1150, 1400, 1300, 1500, 1450, 1600, 1580, 1700, 1650]

# Step 1: Group data by constituency
constituencies = []
for i in range(0, len(party_names), 2):  # Assuming 2 candidates per constituency
    constituency_data = [
        {
            "party": party_names[i],
            "candidate": candidate_names[i],
            "votes": votes_received[i]
        },
        {
            "party": party_names[i + 1],
            "candidate": candidate_names[i + 1],
            "votes": votes_received[i + 1]
        }
    ]
    constituencies.append(constituency_data)

# Step 2: Calculate total votes for each party
party_votes = {}
for constituency in constituencies:
    for candidate in constituency:
        party_votes[candidate["party"]] = (
            party_votes.get(candidate["party"], 0) + candidate["votes"]
        )

# Step 3: Identify the winning party in each constituency
winning_parties = []
for constituency in constituencies:
    winner = max(constituency, key=itemgetter("votes"))
    winning_parties.append(winner["party"])

# Step 4: Determine the overall election winner
overall_winner = max(party_votes.items(), key=itemgetter(1))[0]

# Step 5: Calculate vote share percentage
total_votes = sum(votes_received)
vote_shares = {
    party: (votes / total_votes) * 100 for party, votes in party_votes.items()
}

# Step 6: Identify constituencies with close contests (margin < 12%)
close_contests = []
for i, constituency in enumerate(constituencies):
    sorted_candidates = sorted(constituency, key=itemgetter("votes"), reverse=True)
    margin = sorted_candidates[0]["votes"] - sorted_candidates[1]["votes"]
    margin_percent = (margin / sorted_candidates[0]["votes"]) * 100
    if margin_percent < 12:
        close_contests.append({
            "Constituency": i + 1,
            "Winner": sorted_candidates[0],
            "Margin (%)": margin_percent
        })

# Display results
print("Total Votes for Each Party:", party_votes)
print("Winning Party in Each Constituency:", winning_parties)
print("Overall Election Winner:", overall_winner)
print("Vote Share Percentage:")
for party, share in vote_shares.items():
    print(f"  {party}: {share:.2f}%")
print("Close Contests (Constituency, Winner, Margin):")
for contest in close_contests:
    print(f"  Constituency {contest['Constituency']}: {contest['Winner']} with {contest['Margin (%)']:.2f}% margin")