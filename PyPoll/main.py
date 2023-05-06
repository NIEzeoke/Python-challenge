import os

import csv

file_input= os.path.join(".","Resources","election_data.csv")
file_output= os.path.join(".","analysis","election_analysis.txt")

#Variables
total_votes=0
candidates=[]
num_votes=[]
pct_votes=[]



#Start loop to read file
with open(file_input) as csv_data:
    reader = csv.reader(csv_data)

    header=next(reader)

    #first 
    first_row=next(reader)
    

    for row in reader:
        #Update total votes
        total_votes+=1

        #Set conditional: If the candidate name is not in the list, add their name and a vote in their name.
        #  If it is in candidate list only add a vote in their name
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index]+= 1

    #Add to pct_votes list
    for votes in num_votes:
        percentage = (votes/total_votes) *100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        pct_votes.append(percentage)
    
    # Find the winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

    #print findings
    print("Election Results")
print("-----------------------")
print("Total Votes: " + str(total_votes))
print("-----------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(pct_votes[i])} ({str(num_votes[i])})")
print("-----------------------")
print(f"Winner: {winning_candidate}")
print("-----------------------")

# Exporting to .txt file
output = open(file_output, "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(pct_votes[i])} ({str(num_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))