import os

import csv



csvpath = os.path.join('Resources', 'election_data.csv')

csvpath_out = os.path.join('Resources', 'election_data.txt')



with open(csvpath, newline=',') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader, None)



    total_votes = 0

    candidates = []

    votes = []



    for row in csvreader:

        total_votes += 1

        if row[2] in candidates:

            votes[candidates.index(row[2])] += 1

        else:

            candidates.append(row[2])

            votes.append(1)



with open(csvpath_out, 'w', newline='') as txtfile:



    txtfile.write('Election Results' + '\n')

    txtfile.write('-------------------------' + '\n')

    txtfile.write('Total Votes: ' + str(total_votes) + '\n')

    txtfile.write('-------------------------' + '\n')



    for y in range(len(candidates)):



        txtfile.write(candidates[y] + ': ' + str(format(votes[y] / total_votes * 100, '.3f')) + '% (' + str(votes[y]) + ')\n')



    txtfile.write('-------------------------' + '\n')

    txtfile.write('Winner: ' + candidates[votes.index(max(votes))] + '\n')

    txtfile.write('-------------------------')



