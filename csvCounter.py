#!/usr/bin/python

import sys, getopt, time, os, glob, csv

from os import listdir
from os.path import isfile, join


files = glob.glob(sys.argv[1], recursive=True)
print (files)
for f in files:
	print("====={}=====".format(f))
	with open(f, 'rt', encoding='utf-8') as csvfile:
		myReader = csv.reader(csvfile, delimiter=',', quotechar='"')
		firstRow = next(myReader)
		ncols=len(firstRow) # Read first line and count columns
		cols = [0] * ncols
		csvfile.seek(0)   
		rows = 0
		for row in myReader:
			colNo = 0
			rows += 1
			for col in row : 
				if not (not col or col.isspace()) : 
					cols[colNo] += 1
				colNo += 1
		print('\t'.join([str(x) for x in firstRow]))
		print('\t'.join([str(x) for x in cols]))
		print("Number of records\t{}".format(rows))
		print("")

