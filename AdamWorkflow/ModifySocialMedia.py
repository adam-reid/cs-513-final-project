#!/usr/bin/python3
# @begin ModifySocialMedia @desc This modifies the social media column.
# @in file:PostOpenRefine.csv
# @out file:PostOpenRefineNew.csv

import csv
import os

# @begin process @desc Checks the 3rd and 4th columns to resolve Twitter and Facebook URLS.
# @in file:PostOpenRefine.csv
# @out file:PostOpenRefineNew.csv
with open('PostOpenRefine.csv') as infile, open('PostOpenRefineNew.csv','w', newline='') as outfile:
    writer = csv.writer(outfile)
    for row in csv.reader(infile):
        output_row = row
        
        if(row[4].startswith('twitter.com')):
            #print(row[4])
            output_row[4] = 'https://www.' + row[4]
        if(row[4].startswith('@')):
            #print(row[4][1:])
            output_row[4] = 'https://www.twitter.com/' + row[4][1:]
        if(row[4].startswith('www.twitter.com')):
            #print(row[4])
            output_row[4] = 'https://' + row[4]
        if(row[3].startswith('facebook.com') | row[3].startswith('Facebook.com')):
            output_row[3] = 'https://www.' + row[3]
        if(row[3].startswith('@')):
            #print(row[4][1:])
            output_row[3] = 'https://www.facebook.com/' + row[3][1:]
        if(row[3].startswith('www.')):
            #print(row[4][1:])
            output_row[3] = 'https://' + row[3]
        
        writer.writerow(output_row)
# @end process

# @end ModifySocialMedia
