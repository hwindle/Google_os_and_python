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
        user_list = re.findall(r'\([a-zA-Z ]*\)$', line.strip())
        # append user key to dict.
        for u in user_list:
            user_clean = u[1:-1] # take () off
        if user_clean not in per_user:
            per_user[user_clean] = {'INFO': 0, 'ERROR': 0} # initialise inner dict.
        # increment info and error
        if re.search(info_pattern, line) != None:
            # Info line
            per_user[user_clean]['INFO'] = per_user[user_clean]['INFO'] + 1
        else:
            per_user[user_clean]['ERROR'] = per_user[user_clean]['ERROR'] + 1
    # sort the dictionary by user a-z, returns list of tuples for each dict row.
    return sorted(per_user.items(), key = operator.itemgetter(0))


def error_processing(file_contents):
    """
        Input: all lines from the log file.
        Outputs error dict of most common error messages with most common first.
    """
    error = {}
    error_pattern = r'ERROR ([\w ]*) \('
    for line in file_contents:
        if re.search(error_pattern, line) != None:
            error_text = re.findall(error_pattern, line.strip())
            print(error_text)
    return error

def user_csv_generator(per_user):
    pass

def error_csv_generator(error):
    pass


if __name__ == '__main__':
    if sys.argv[1] != None:
        file_contents = get_data()
        #per_user = info_processing(file_contents)
        error = error_processing(file_contents)
        print(error)
    try:
        pass
            #
            #user_csv_generator(per_user)
            #error_csv_generator(error)

    except:
        pass
        #sys.exit('Please provide a file argument')
