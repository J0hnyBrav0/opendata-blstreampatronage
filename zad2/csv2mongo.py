import csv
import json
import getopt
import sys

from pymongo import MongoClient
from pprint import pprint




def csv_to_mongodb_import(filename,collection_handler):
	with open(filename, 'rU') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			row['Longitude'] = float(row['Longitude'])
			row['Latitude'] = float(row['Latitude'])
			collection_handler.insert(row)


def main(argv):
	input_file = ''
	client = MongoClient()
	db = client['testdb']
	collection_handler = db.posts

	try:
		opts, args = getopt.getopt(argv, "hi:o:l", ["ifile="])
	except getopt.GetoptError:
		print 'csv2json.py -i <inputfile.csv> lolo'
		sys.exit(2)
	else:
		for opt, arg in opts:
		    if opt == '-h':
			print '!!! Only localhost mongoDB supported !!!'
			print 'csv2mongo.py -i <inputfile.csv> //will import csv to mongodb'
			print 'csv2mongo.py -l //will list collection'

			sys.exit()
		    elif opt in ("-i", "--ifile"):
			if arg.endswith('.csv'):
			    input_file = arg
			    csv_to_mongodb_import(input_file,collection_handler)
			else:
			    print 'csv2mongo.py -i <inputfile.csv>'
			    sys.exit()
		    elif opt in ("-l", "--listCollection"):
			for post in collection_handler.find():
				pprint (post)		
		

if __name__ == '__main__':
    main(sys.argv[1:])