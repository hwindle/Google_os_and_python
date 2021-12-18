#!/usr/bin/env python3

import sys, operator
import re, csv

def create_dictionaries():
    """
        File IO for sys log file.
        Outputs info dict of users,
        errors dict and freq of errors. Unsorted.
    """
    per_user = {}
    error = {}
    info_pattern = r'ticky: INFO'
    error_pattern = r'ERROR ([\w ]*) \('

    try:
        with open(sys.argv[1], 'r') as f_open:
            lines = f_open.readlines()
            for line in lines:
                # search for info or error
                if re.search(info_pattern, line) != None:
                    # Info line
                    user = re.find(r'\([\w*]\)$', line.strip())
                    #per_user[user] =+ 1
                    print(user)
                # if info or error, log username, info count, error count
                # if only error, log error msg and count to errors dict.
    except:
        print('File {} cannot be opened', sys.argv[1])
        sys.exit(1)


def user_csv_generator(per_user):
    pass

def error_csv_generator(error):
    pass


if __name__ == '__main__':
    try:
        if sys.argv[1] != None:
            create_dictionaries()
            #user_dict, error_dict = create_dictionaries()
            #user_csv_generator(user_dict)
            #error_csv_generator(error_dict)
        else:
            print('Pass in an arguement for the log file')
    except:
        sys.exit('Please provide a file argument')
