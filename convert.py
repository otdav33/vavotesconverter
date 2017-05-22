import csv
import sys

"""
This program will convert a file from historical.elections.virginia.gov to one usable in the database and put in on stdout.
"""


try:
	inputfile = open(sys.argv[1])
except:
	print("You must give an input file as the argument.")
	sys.exit(0)

reader = csv.reader(inputfile)
l = list(reader) #two-level list read from CSV
writer = csv.writer(sys.stdout)
for i in range(len(l[0]))[3:]: #iterate through candidates
	name = l[0][i]
	try:
		party = l[1][i]
	except:
		party = ""
	c = [name, party]
	for r in l[2:]: #iterate through counties
		#add a new output row of candidate name, party, county, votes
		writer.writerow(c + [r[0], r[i]])
