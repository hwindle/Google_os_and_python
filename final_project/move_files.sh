#!/bin/bash

# convert files
./csv_to_html.py error_message.csv errors.html
./csv_to_html.py user_statistics.csv users.html

# shift files
mv errors.html /var/www/html
mv users.html /var/www/html
