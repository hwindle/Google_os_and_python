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
    error_text = ''
    error_clean = ''
    error_pattern = r'ERROR ([\w ]*) \('
    for line in file_contents:
        error_text = re.findall(error_pattern, line.strip())
        for one_error in error_text:
            error_clean = one_error.strip()
        if error_clean not in error:
            error[error_clean] = 1 # initialise dictionary key
        else:
            error[error_clean] = error[error_clean] + 1 #  increment
    del error['']
    return sorted(error.items(), key = operator.itemgetter(1), reverse = True)

def user_csv_generator(per_user):
    filename = 'user_statistics.csv'
    headers = ['User', 'INFO', 'ERROR']
    with open(filename, 'w', newline = '\n') as f:
        user_writer = csv.writer(f, delimiter = ',')
        user_writer.writerow(headers)
        for row in per_user:
            row_list = []
            row_list.append(row[0])
            row_list.append(row[1]['INFO'])
            row_list.append(row[1]['ERROR'])
            user_writer.writerow(row_list)


def error_csv_generator(error):
    filename = 'error_message.csv'
    headers = ['Error', 'Count']
    with open(filename, 'w', newline = '\n') as f:
        error_writer = csv.writer(f, delimiter = ',')
        error_writer.writerow(headers)
        for row in error:
            error_writer.writerow(row)


if __name__ == '__main__':
    if sys.argv[1] != None:
        file_contents = get_data()
        per_user = info_processing(file_contents)
        error = error_processing(file_contents)
        user_csv_generator(per_user)
        error_csv_generator(error)
        print('Success!')
    else:
        sys.exit('Please provide a file argument')
