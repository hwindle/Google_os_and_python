#!/usr/bin/env python3

import sys, operator
import re, csv


def get_data():
    # gets the data from the 1st argument passed in. Returns all lines.
    try:
        with open(sys.argv[1], 'r') as f_open:
            lines = f_open.readlines()
            return lines
    except:
        print('File {} cannot be opened', sys.argv[1])
        sys.exit(1)


def info_processing(file_contents):
    """
        Input: all lines from the log file.
        Outputs info dict of users in a sorted fashion.
    """
    per_user = {}
    info_pattern = r'ticky: INFO'

    for line in file_contents:
        # search for info or error
        if re.search(info_pattern, line) != None:
            # Info line
            user = re.find(r'\([\w*]\)$', line.strip())
            #per_user[user] =+ 1
            print(user)


def error_processing(file_contents):
    """
        Input: all lines from the log file.
        Outputs error dict of most common error messages with most common first.
    """
    error = {}
    error_pattern = r'ERROR ([\w ]*) \('
    for line in file_contents:
        if re.search(error_pattern, line) != None:
            error_text = re.find(error_pattern, line.strip())
            print(error_text)

def user_csv_generator(per_user):
    pass

def error_csv_generator(error):
    pass


if __name__ == '__main__':
    try:
        if sys.argv[1] != None:
            file_contents = get_data()
            #per_user = info_processing(file_contents)
            #error = error_processing(file_contents)
            #user_csv_generator(per_user)
            #error_csv_generator(error)
        else:
            print('Pass in an arguement for the log file')
    except:
        sys.exit('Please provide a file argument')
