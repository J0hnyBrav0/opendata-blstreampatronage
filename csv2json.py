__author__ = 'michaljankowski'


import sys
import csv
import json
import getopt


def main(argv):
    input_file = ''
    output_file = ''

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print 'csv2json.py -i <inputfile.csv> -o <outputfile.json>'
        sys.exit(2)
    else:
        for opt, arg in opts:
            if opt == '-h':
                print 'csv2json.py -i <inputfile.csv> -o <outputfile.json>'
                sys.exit()
            elif opt in ("-i", "--ifile"):
                if arg.endswith('.csv'):
                    input_file = arg
                else:
                    print 'csv2json.py -i <inputfile.csv> -o <outputfile.json>'
                    sys.exit()
            elif opt in ("-o", "--ofile"):
                output_file = arg
        dictionary = import_from_file(input_file)
        dict_2_json_file(output_file, dictionary)


def import_from_file(input_file):
    """
    Function will open file, and construct list of dictionaries.
    Each dictionary refers to each row of a csv file
    :param input_file: file in csv format # file object or string path?
    :return: array of dictionaries
    """
    list_of_dicts = []
    floats = ('Longitude', 'Latitude')
    tmp_dict = {}
    try:
        csv_file = open(input_file, 'rU')
    except IOError:
        print "Error:", sys.exc_info()[0]
        sys.exit()
    else:
        reader = csv.reader(csv_file)
        keys = reader.next()
        for values in reader:
            tuples = zip(keys, values)
            for key, value in tuples:
                if key in floats:
                    try:
                        tmp_dict[key] = float(value)
                    except ValueError:
                        print "Error:", sys.exc_info()[0]
                        tmp_dict[key] = value
                else:
                    tmp_dict[key] = value
                list_of_dicts.append(tmp_dict)
        csv_file.close()
    return list_of_dicts


def dict_2_json_file(output_file, data):
    """
    Function will open/create output file and write json dictionary in in.
    :param output_file: file to save json
    :param data: dictionary which will be convert to json file
    :return: none
    """
    try:
        handler = open(output_file, 'w')
    except IOError:
        print "Error:", sys.exc_info()[0]
        sys.exit()
    else:
        json.dump(data, handler)
        handler.close()

if __name__ == '__main__':
    main(sys.argv[1:])
